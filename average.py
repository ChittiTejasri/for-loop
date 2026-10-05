n=int(input("Enter a natural numbers:"))
sum=0
for i in range(1,n+1,1):
    sum=sum+i
average = sum/n

print("Average of first", n, "natural numbers =",average)
print(f"Average of first {n} naturan numbers = {average}")