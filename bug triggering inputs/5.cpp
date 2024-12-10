/*
Accept invalid on gcc trunk
Unconfirmed
*/
template<typename T> void f() {
  struct S { void g(int n = T::unknown){}; };
}
template void f<int>();