# 4. Viết chương trình nhập vào các số a, b, c, sau đó kiểm tra bộ ba số a, b, c vừa nhập vào 
# là bộ ba cạnh của tam giác thường, tam giác vuông, tam giác cân, tam giác vuông cân, tam giác đều 
# hay không phải là bộ ba cạnh của tam giác.
print("Bạn hãy nhập độ dài 3 cạnh tam giác")
a = float(input("a="))
b = float(input("b="))
c = float(input("c="))
if a == b and b != c or a !=c :
    print("Tam giác trên là tam giác cân ")
elif a == b == c :
    print("Tam giác trên của bạn là tam giác đều ")
else :
    print("Tam giác trên là 1 tam giác thường ")