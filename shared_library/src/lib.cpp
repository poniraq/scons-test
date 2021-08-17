#include "lib.h"
#include <string>

MyLibraryClass::MyLibraryClass()
{}

MyLibraryClass::~MyLibraryClass()
{}

std::string MyLibraryClass::test_member_fun()
{
    return "test_member_fun";
}

std::string MyLibraryClass::test_static_fun()
{
    return "test_static_fun";
}