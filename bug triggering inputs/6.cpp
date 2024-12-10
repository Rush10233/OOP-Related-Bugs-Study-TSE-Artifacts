/*
Accept invalid on gcc trunk
Confirmed
*/
class Base
{
    virtual ~Base() = default;
};

class Derived : public Base
{
    ~Derived() override = default;
};