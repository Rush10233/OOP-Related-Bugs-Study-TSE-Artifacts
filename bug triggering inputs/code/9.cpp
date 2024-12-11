/*
Accept invalid on clang trunk
Unconfirmed
*/
#include<iostream>
template <class K,int NON=0>
struct C    
{      
    int x=0;  
    C<K>(){x=1;};    
};        
int main(){
    C<int> Cont;
    //Cont.x=1
    std::cout<<Cont.x<<std::endl;
    C<int ,100> Cont_2;
    //Cont_2.x=1
    std::cout<<Cont_2.x<<std::endl;    
}