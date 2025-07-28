f1 = open("data.txt", "rt")
print(f1)
print(f1.readline())
print(f1.read(1))
print(f1.readline())
f1.close()

with open("/Users/eddieliu/PycharmProjects/prac_data.txt") as f2:
    # print(f2.read())
    for x in f2:
        print(x)
