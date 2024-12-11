/*
Reject valid on clang trunk
Unconfirmed
*/
struct A { int i; };
struct B:A { int j; };
struct C:B { int k; static_assert((int(B::*))&C::k, ""); };