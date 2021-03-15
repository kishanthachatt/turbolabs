text = "My Name is Kishan Thachatt"
N = 12
l = text.split(" ")
x = ""
for i in range(len(l)-1):
  x = x +" " +l[i]
  if len(x + l[i+1]) >= N:
    print(x)
    x = ""
print(x+" "+l[-1])