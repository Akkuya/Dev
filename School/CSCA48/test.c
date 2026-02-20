#include <stdio.h>
#include <string.h>

typedef struct customer
{
    int id;
    char name[256];
} Customer;
void set_id(Customer *p, int id) {
    p->id = id;
}
void set_name(Customer *p, const char *name)  {
    strcpy(p->name, name);
}
void print_customer(Customer *p) {
    printf("ID: %d, \t Name: %s", p->id, p->name);
}
int main()
{
    Customer c1;
    set_id(&c1, 100);
    set_name(&c1, "Harry Potter");
    print_customer(&c1);
    return 0;
}