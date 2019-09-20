import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

### Original Code - Average 10 seconds ###
# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

### Average of 0.017 seconds ###
# duplicates = []  
# names = names_1 + names_2  
# names.sort()  
# for x in range(len(names)-1):  
#     if names[x] == names[x+1]:  
#         duplicates.append(names[x])

### Average 0.0095 seconds ###
x = {}
for name in names_1:
    x[name] = True
duplicates = []
for name in names_2:
    if x.get(name):
        duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

