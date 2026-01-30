import json

tagsUUID = {
    "MzamLshWg_Eb0cR6aCl7q": "Assignment",
    "onvsp4qCPJ37v1EFUPygH": "Notes",
    "EM_IMPORTANT": "Important",
    "EM_URGENT": "Urgent",
}

projects = {
    "finXv6Dg84Uev1I8SmoH6": "Calculus",
    "cea1n3TKIpGBeP-3OJ8mP": "Linear Algebra",
    "5cqnShK3x0Abx1clhs2Ba": "Co-op",
    "7IkqK75wtIPNyBSbV1n20": "Business",
    "wFIp8qfy46fRDzCCTGCt2": "Computer Science",
    "fNMVNFkfhEP0sCqkyklzE": "Gym App",
    "INBOX_PROJECT": "Miscellaneous"
}

seen = set()

def load_super_productivity_tasks(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        x = json.load(file)
    
    tasks = []
    
    for index, (id, task) in enumerate(x["data"]["task"]["entities"].items()):
        
        if task["id"] in seen:
            continue
        seen.add(task["id"])

        tags = []

        for tag in task['tagIds']:
            tags.append(tagsUUID[tag])
        
        projectId = projects[task['projectId']]

        task_info = {
            'title': task["title"],
            'tags': tags,
            'project': projectId
        }
        tasks.append(task_info)
    
    return tasks

if __name__ == "__main__":
    file_path = 'data.json'
    tasks = load_super_productivity_tasks(file_path)
    for task in tasks:
        print(f"Title: {task['title']}, Project: {task['project']}, Tags: {', '.join(task['tags'])}")