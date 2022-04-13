int main(){
    Number x, y, z(45), z2;
    x.display();
    y.display();
    z.display();

     Number z1(z); 
    z1.display();

    z2 = z; 
    z2.display();

    Number z3 = z; 
    z3.display();



    return 0;
}
