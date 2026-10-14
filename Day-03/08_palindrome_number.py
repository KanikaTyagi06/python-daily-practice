n=int(input())
original_num=n
reverse=0
digit=0
while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n=n//10
if reverse==original_num:
    print("Yes")
else:
    print("No")