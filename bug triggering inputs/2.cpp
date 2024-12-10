/*
Reject valid on clang trunk
Unconfirmed
*/
struct Base {
protected:
    ~Base() = default;  
};

struct Derived : Base{
};

int main(){
    Derived d{};
}