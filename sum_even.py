var_int = 8888
a = var_int // 10             
b = var_int % 10              
c = a % 10                     
a = a // 10                     
d = a % 10                   
e = a // 10
b = ((b % 2)+1)%2*b
c = ((c % 2)+1)%2*c
d = ((d % 2)+1)%2*d
e = ((e % 2)+1)%2*e
sum_even = b+c+d+e
print(sum_even)