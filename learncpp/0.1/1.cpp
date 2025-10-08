#include <iostream>

struct X {
    X() = default;
    int i = 0;
};

int main() {
    const X x;
    std::cout << x.i;
}
