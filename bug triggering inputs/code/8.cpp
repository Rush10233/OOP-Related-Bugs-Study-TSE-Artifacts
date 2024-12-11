/*
Reject valid on clang 17.0.1
Already fixed on clang 18.1.0
*/
template<class T>
struct A {
  template<class U> struct B { B(U); };
};

template<class T>
void f() {
  typename A<T>::B x(0);
}

template void f<int>();