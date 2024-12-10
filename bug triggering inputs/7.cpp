/*
Reject valid on clang 17.0.1
Already fixed on clang 18.1.0
*/
template <bool V> struct A {
  template <class T> struct B { B(T) requires V; };
};

A<true>::B x(0);