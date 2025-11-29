"""CSCA08: Fall 2025 -- Assignment 3: Social Media Data Analyst

Starter code.

This code is provided solely for the personal and private use of
students taking the CSC108/CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2025 Jacqueline Smith, David Liu, Dominik Luszczynski,
and Anya Tafliovich

"""

from typing import TextIO
from copy import deepcopy

from constants import (
    UserData,
    AccountData,
    DOB,
    NUM_POSTS,
    NUM_COMMENTS,
    ACCOUNT_CREATED,
    FOLLOWERS,
    FOLLOWING,
    NUM_MUTUALS,
    BOT_GROUPS,
    SEP,
    USERNAME_COL,
    DOB_COL,
    NUM_POSTS_COL,
    NUM_COMMENTS_COL,
    ACCOUNT_CREATED_COL,
    FOLLOWER_COL,
    FOLLOWING_COL,
    HCLP,
    HCLM,
    HCNA,
    HFLF,
    P_HCLM_COMMENT,
    P_HCLM_MUTUALS,
    P_HCLP_COMMENT,
    P_HCLP_POSTS,
    P_HCNA_COMMENT,
    HFLF_FACTOR,
)

SAMPLE_DATA = {
    "username1": {
        DOB: "1973-01-06",
        NUM_POSTS: 3,
        NUM_COMMENTS: 8,
        ACCOUNT_CREATED: "2023-01-01",
        FOLLOWERS: ["username2"],
        FOLLOWING: ["username2", "username4"],
        BOT_GROUPS: [],
    },
    "username2": {
        DOB: "1973-01-06",
        NUM_POSTS: 5,
        NUM_COMMENTS: 5,
        ACCOUNT_CREATED: "2025-01-01",
        FOLLOWERS: ["username1", "username3"],
        FOLLOWING: [
            "username1",
            "username3",
        ],
        BOT_GROUPS: [],
    },
    "username3": {
        DOB: "1973-01-06",
        NUM_POSTS: 0,
        NUM_COMMENTS: 11,
        ACCOUNT_CREATED: "2025-01-01",
        FOLLOWERS: ['username2'],
        FOLLOWING: ["username2", "username4", "username5"],
        BOT_GROUPS: [],
    },
    "username4": {
        DOB: "1973-01-06",
        NUM_POSTS: 10,
        NUM_COMMENTS: 1,
        ACCOUNT_CREATED: "2023-01-01",
        FOLLOWERS: ["username1",
                    "username3",
                    "username5"],
        FOLLOWING: [],
        BOT_GROUPS: [],
    },
    "username5": {
        DOB: "1973-01-06",
        NUM_POSTS: 2,
        NUM_COMMENTS: 10,
        ACCOUNT_CREATED: "2023-01-01",
        FOLLOWERS: ["username3"],
        FOLLOWING: ["username4"],
        BOT_GROUPS: [],
    },
}

SAMPLE_DATA_WITH_NUM_MUTUALS = {
    "username1": {
        DOB: "1973-01-06",
        NUM_POSTS: 3,
        NUM_COMMENTS: 8,
        ACCOUNT_CREATED: "2023-01-01",
        FOLLOWERS: ["username2"],
        FOLLOWING: ["username2", "username4"],
        BOT_GROUPS: [],
        NUM_MUTUALS: 1
    },
    "username2": {
        DOB: "1973-01-06",
        NUM_POSTS: 5,
        NUM_COMMENTS: 5,
        ACCOUNT_CREATED: "2025-01-01",
        FOLLOWERS: ["username1", "username3"],
        FOLLOWING: [
            "username1",
            "username3",
        ],
        BOT_GROUPS: [],
        NUM_MUTUALS: 2,
    },
    "username3": {
        DOB: "1973-01-06",
        NUM_POSTS: 0,
        NUM_COMMENTS: 11,
        ACCOUNT_CREATED: "2025-01-01",
        FOLLOWERS: ['username2'],
        FOLLOWING: ["username2", "username4", "username5"],
        BOT_GROUPS: [],
        NUM_MUTUALS: 1
    },
    "username4": {
        DOB: "1973-01-06",
        NUM_POSTS: 10,
        NUM_COMMENTS: 1,
        ACCOUNT_CREATED: "2023-01-01",
        FOLLOWERS: ["username1", "username3", "username5"],
        FOLLOWING: [],
        BOT_GROUPS: [],
        NUM_MUTUALS: 0
    },
    "username5": {
        DOB: "1973-01-06",
        NUM_POSTS: 2,
        NUM_COMMENTS: 10,
        ACCOUNT_CREATED: "2023-01-01",
        FOLLOWERS: ["username3"],
        FOLLOWING: ["username4"],
        BOT_GROUPS: [],
        NUM_MUTUALS: 0
    },
}

SAMPLE_DATA_FULL = {
    "username1": {
        DOB: "1973-01-06",
        NUM_POSTS: 3,
        NUM_COMMENTS: 8,
        ACCOUNT_CREATED: "2023-01-01",
        FOLLOWERS: ["username2"],
        FOLLOWING: ["username2", "username4"],
        BOT_GROUPS: [],
        NUM_MUTUALS: 1
    },
    "username2": {
        DOB: "1973-01-06",
        NUM_POSTS: 5,
        NUM_COMMENTS: 5,
        ACCOUNT_CREATED: "2025-01-01",
        FOLLOWERS: ["username1", "username3"],
        FOLLOWING: [
            "username1",
            "username3",
        ],
        BOT_GROUPS: [],
        NUM_MUTUALS: 2,
    },
    "username3": {
        DOB: "1973-01-06",
        NUM_POSTS: 0,
        NUM_COMMENTS: 11,
        ACCOUNT_CREATED: "2025-01-01",
        FOLLOWERS: ['username2'],
        FOLLOWING: ["username2", "username4", "username5"],
        BOT_GROUPS: ['highCommentsNewAccount',
                     'highFollowingLowFollowers',
                     'highCommentsLowPosts'],
        NUM_MUTUALS: 1
    },
    "username4": {
        DOB: "1973-01-06",
        NUM_POSTS: 10,
        NUM_COMMENTS: 1,
        ACCOUNT_CREATED: "2023-01-01",
        FOLLOWERS: ["username1", "username3", "username5"],
        FOLLOWING: [],
        BOT_GROUPS: [],
        NUM_MUTUALS: 0
    },
    "username5": {
        DOB: "1973-01-06",
        NUM_POSTS: 2,
        NUM_COMMENTS: 10,
        ACCOUNT_CREATED: "2023-01-01",
        FOLLOWERS: ["username3"],
        FOLLOWING: ["username4"],
        BOT_GROUPS: ['highCommentsLowMutuals'],
        NUM_MUTUALS: 0
    },
}

SAMPLE_DATA_ABUSING = {
    "username4": {
        DOB: "1973-01-06",
        NUM_POSTS: 10,
        NUM_COMMENTS: 1,
        ACCOUNT_CREATED: "2023-01-01",
        FOLLOWERS: ["username1", "username3", "username5"],
        FOLLOWING: [],
        BOT_GROUPS: [],
        NUM_MUTUALS: 0
    },
    "username5": {
        DOB: "1973-01-06",
        NUM_POSTS: 2,
        NUM_COMMENTS: 10,
        ACCOUNT_CREATED: "2023-01-01",
        FOLLOWERS: ["username3"],
        FOLLOWING: ["username4"],
        BOT_GROUPS: ['highCommentsLowMutuals'],
        NUM_MUTUALS: 0
    }
}

# We provide the header and docstring for this function to get you
# started and to demonstrate that there are no docstring examples in
# functions that read from files.


def create_users_dictionary(users_file: TextIO) -> UserData:
    """Return a dictionary (no duplicates) created from
    the file users_file in the form of the UserData:

    {
        username: {
            DOB : dob,
            NUM_POSTS: num_posts,
            NUM_COMMENTS: num_comments,
            ACCOUNT_CREATED: account_created,
            FOLLOWERS: [],
            FOLLOWING: [],
            BOT_GROUPS: []
        }
        ...
    }

    Precondition: users_file is open for reading
                  users_file is in the format described in the handout

    """
    users_file.readline()

    user_data = {}
    for line in users_file:
        parts = line.strip().split(SEP)
        username = parts[USERNAME_COL]
        dob = parts[DOB_COL]
        num_posts = int(parts[NUM_POSTS_COL])
        num_comments = int(parts[NUM_COMMENTS_COL])
        account_created = parts[ACCOUNT_CREATED_COL]

        user_data[username] = {
            DOB: dob,
            NUM_POSTS: num_posts,
            NUM_COMMENTS: num_comments,
            ACCOUNT_CREATED: account_created,
            FOLLOWERS: [],
            FOLLOWING: [],
            BOT_GROUPS: [],
        }
    return user_data

# We provide the header and part of a docstring for this function to
# get you started and to demonstrate the use of function deepcopy in
# examples that modify input data.


def add_num_mutual_connections(users_dict: UserData) -> None:
    """Modify the dictionary users_dict by adding the number of
    mutual relationships each user has using the NUM_MUTUALS key.

    Note a mutual relationship occurs when two users follow each
    other.

    >>> sample_data_copy = deepcopy(SAMPLE_DATA)
    >>> add_num_mutual_connections(sample_data_copy)
    >>> sample_data_copy['username1'][NUM_MUTUALS] == 1
    True
    >>> sample_data_copy['username2'][NUM_MUTUALS] == 2
    True
    """
    for user in users_dict:
        mutual_count = 0
        followers = users_dict[user][FOLLOWERS]
        following = users_dict[user][FOLLOWING]
        for follower in followers:
            if follower in following:
                mutual_count += 1
        users_dict[user][NUM_MUTUALS] = mutual_count


def add_followers(users_dict: UserData, followers_file: TextIO) -> None:
    """Modify users_dict by adding followers and following
    information from followers_file.

    Precondition: followers_file is open for reading
                  followers_file is in the format described in the handout
    """
    followers_file.readline()

    for line in followers_file:
        parts = line.strip().split(SEP)
        follower = parts[FOLLOWER_COL]
        following = parts[FOLLOWING_COL]

        if follower in users_dict:
            users_dict[follower][FOLLOWING].append(following)
        if following in users_dict:
            users_dict[following][FOLLOWERS].append(follower)


def get_quantile(data: list[int], p: float) -> int:
    """Return the p-th quantile of the list data.

    The p-th quantile is defined as the first value at the index i
    which such that (i+1)/len(sorted_data) > p.
    If p > 1 or p < 0, return -1.

    Precondition: len(data) > 0

    >>> get_quantile([5, 2, 1, 3, 4], 0.5)
    3
    >>> get_quantile([10, 20, 30, 40], 0.25)
    20
    >>> get_quantile([7, 8, 9], 0.67)
    9
    """
    sorted_data = sorted(data)
    if p < 0 or p > 1:
        return -1

    for i in range(len(sorted_data)):
        quantile = (i + 1) / len(sorted_data)
        if quantile > p:
            return sorted_data[i]
    return sorted_data[-1]


def get_user_quantiles(users_dict: UserData) -> tuple[int, int, int, int, int]:
    """Helper function that gives the quantiles for all bot
    identification categories, using the data in users_dict.

    >>> sample_data_copy = deepcopy(SAMPLE_DATA_FULL)
    >>> get_user_quantiles(sample_data_copy)
    (11, 0, 11, 0, 10)
    """
    comments_list = []
    posts_list = []
    mutuals_list = []

    for user in users_dict:
        comments_list.append(users_dict[user][NUM_COMMENTS])
        posts_list.append(users_dict[user][NUM_POSTS])
        mutuals_list.append(users_dict[user][NUM_MUTUALS])

    comment_quantile_hclp = get_quantile(comments_list, P_HCLP_COMMENT)
    post_quantile_hclp = get_quantile(posts_list, P_HCLP_POSTS)
    comment_quantile_hclm = get_quantile(comments_list, P_HCLM_COMMENT)
    mutuals_quantile_hclm = get_quantile(mutuals_list, P_HCLM_MUTUALS)
    comment_quantile_hcna = get_quantile(comments_list, P_HCNA_COMMENT)

    quantiles = []
    quantiles.append(comment_quantile_hclp)
    quantiles.append(post_quantile_hclp)
    quantiles.append(comment_quantile_hclm)
    quantiles.append(mutuals_quantile_hclm)
    quantiles.append(comment_quantile_hcna)

    return tuple(quantiles)


def add_bot_candidate_groups(users_dict: UserData) -> None:
    """Mutates users_dict by adding bot candidate groups
    to each user's BOT_GROUPS list based on the criteria
    described in the handout.
    """
    user_quant = get_user_quantiles(users_dict)

    for user in users_dict:
        num_comments = users_dict[user][NUM_COMMENTS]
        num_posts = users_dict[user][NUM_POSTS]
        num_mutuals = users_dict[user][NUM_MUTUALS]
        acc_created = users_dict[user][ACCOUNT_CREATED]

        if (num_comments >= user_quant[0] and num_posts <= user_quant[1]):
            users_dict[user][BOT_GROUPS].append(HCLP)

        if (num_comments >= user_quant[2] and num_mutuals <= user_quant[3]):
            users_dict[user][BOT_GROUPS].append(HCLM)

        if (num_comments >= user_quant[4] and acc_created >= "2023-01-01"):
            users_dict[user][BOT_GROUPS].append(HCNA)

        followers_count = len(users_dict[user][FOLLOWERS])
        following_count = len(users_dict[user][FOLLOWING])
        if following_count >= HFLF_FACTOR * followers_count:
            users_dict[user][BOT_GROUPS].append(HFLF)


def find_users_abusing_system(users_dict: UserData) -> UserData:
    """Return a list of usernames of users who are abusing
    the system by having a follower makeup of
    more than 50% bot candidates.

    Precondition: add_bot_candidate_groups has already been
                  called on users_dict.

    >>> sample_data_copy = deepcopy(SAMPLE_DATA_FULL)
    >>> find_users_abusing_system(sample_data_copy) == SAMPLE_DATA_ABUSING
    True
    """
    abusing_users = {}

    for user in users_dict:
        followers = users_dict[user][FOLLOWERS]
        if len(followers) == 0:
            continue
        bot_count = 0
        for follower in followers:
            if len(users_dict[follower][BOT_GROUPS]) > 0:
                bot_count += 1
        if bot_count / len(followers) > 0.5:
            abusing_users[user] = users_dict[user]

    return abusing_users


def find_all_bot_candidates(users_dict: UserData) -> UserData:
    """Return a dictionary of all bot candidates from users_dict.

    Precondition: add_bot_candidate_groups has already been
                  called on users_dict.

    >>> sample_data_copy = deepcopy(SAMPLE_DATA_FULL)
    >>> find_all_bot_candidates(sample_data_copy) == {'username3': sample_data_copy['username3'], 'username5': sample_data_copy['username5']}
    True
    """
    bot_candidates = {}

    for user in users_dict:
        if len(users_dict[user][BOT_GROUPS]) > 0:
            bot_candidates[user] = users_dict[user]

    return bot_candidates


def order_bot_candidates(users_dict: UserData) -> list[str]:
    """Return a list of usernames of bot candidates ordered
    in descending order by the number of bot candidate groups
    they belong to.

    Precondition: add_bot_candidate_groups has already been
                  called on users_dict.

    >>> sample_data_copy = deepcopy(SAMPLE_DATA_FULL)
    >>> order_bot_candidates(sample_data_copy)
    ['username3', 'username5']
    """

    bot_candidates = find_all_bot_candidates(users_dict)

    bot_count = []
    for name, data in bot_candidates.items():
        bot_count.append((name, len(data[BOT_GROUPS])))

    bot_count.sort(key=sort_key, reverse=True)
    ordered_usernames = []
    for bot in bot_count:
        ordered_usernames.append(bot[0])
    return ordered_usernames


def order_users_abusing_system(users_dict: UserData) -> list[str]:
    """Return a list of usernames of users abusing the system
    ordered in descending order by the number of bot followers they have.

    Precondition: add_bot_candidate_groups has already been
                  called on users_dict.
                  find_users_abusing_system has already been
                  called on users_dict.

    >>> sample_data_copy = deepcopy(SAMPLE_DATA_FULL)
    >>> order_users_abusing_system(sample_data_copy)
    ['username4', 'username5']
    """
    abusing_users = find_users_abusing_system(users_dict)

    users_count = []
    for user in abusing_users:
        bot_follower_count = 0
        followers = users_dict[user][FOLLOWERS]
        for follower in followers:
            if len(users_dict[follower][BOT_GROUPS]) > 0:
                bot_follower_count += 1
        users_count.append((user, bot_follower_count))

    users_count.sort(key=sort_key, reverse=True)
    ordered_usernames = []
    for user in users_count:
        ordered_usernames.append(user[0])

    return ordered_usernames


def sort_key(item: tuple[str, int]) -> tuple[int, str]:
    """Return a tuple that can be used as a sort key for ordering
    bot candidates or users abusing the system. Reverses item,
    First sorts by the count, then by username.

    >>> sort_key(('username3', 3))
    (3, 'username3')
    >>> sort_key(('username5', 1))
    (1, 'username5')
    """
    return (item[1], item[0])


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    '''
    Uncomment the code below when you are ready to test.

    The code below uses the small dataset. If you wish to use the
    larger dataset, please replace _small with _medium.
    '''

    # with open("users_medium.csv", "r") as f:
    #     all_users = create_users_dictionary(f)

    # with open("followers_medium.csv", "r") as f:
    #     add_followers(all_users, f)

    # add_num_mutual_connections(all_users)

    # add_bot_candidate_groups(all_users)

    # all_bot_candidates = find_all_bot_candidates(all_users)
    # users_using_bots = find_users_abusing_system(all_users)
    # bot_candidate_order = order_bot_candidates(all_users)
    # users_using_bots_order = order_users_abusing_system(all_users)

    # print("=" * 50)
    # print('Bot Candidates: ')
    # print("=" * 50)
    # print(bot_candidate_order)
    # print("=" * 50)
    # print('Users Using Bots: ')
    # print("=" * 50)
    # print(users_using_bots_order)
