x = [1,2,3,10,6]
for i in range(len(x)):
  if sum(x[:i]) == sum(x[i+1:len(x)]):
    print(i+1)
    break