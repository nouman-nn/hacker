marks = dict()

count  = int(input())
for students in range(count):
    name,mark1,mark2,mark3 = input().split()
    marks[name] = [float(mark1),float(mark2),float(mark3)]
query = input()
print(query)
mark = marks.get(str(name))
print(mark)
#print(mark)
#print(sum(mark)/3)
avg = round(sum(mark)/3,2)
#print("{:.2f}".format(avg))