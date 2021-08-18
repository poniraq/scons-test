#include <string>

#ifdef MYLIB_DLL
#define MYLIB_EXPORT __declspec(dllexport)
#else
#define MYLIB_EXPORT
#endif

class MYLIB_EXPORT MyLibraryClass {
public:
    MyLibraryClass();
    ~MyLibraryClass() noexcept;

    std::string test_member_fun();
    static std::string test_static_fun();
};