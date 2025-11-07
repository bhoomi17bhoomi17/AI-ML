for i in range(10):
   if i == 5:
     break  
   print(i)
# Output: 0 1 2 3 4
# Continue - skip current iteration
for i in range(5):
   if i == 2:
    continue
   print(i)
# Output: 0 1 3 4