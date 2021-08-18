#include <string>
#include <iostream>
#include "../lib/lib.h"

int main(int argc, char const *argv[])
{
    MyLibraryClass instance;
    std::cout << MyLibraryClass::test_static_fun() << std::endl;
    std::cout << instance.test_member_fun() << std::endl;
    return 0;
}
