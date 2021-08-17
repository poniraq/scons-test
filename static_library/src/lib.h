#include <string>

class MyLibraryClass {
public:
    MyLibraryClass();
    ~MyLibraryClass() noexcept;

    std::string test_member_fun();
    static std::string test_static_fun();
};