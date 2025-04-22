f = open("./data.txt", "r", encoding="utf-8")
content = f.read()
print(content)
f.close()

with open("./data.txt", "r", encoding="utf-8") as f:
    print(f.readline())
    print(f.readline())

with open("./data.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        print(line)

with open("./data2.txt", "w", encoding="utf-8") as f:
    f.write("一\n")
    f.write("二\n")
    f.write("三\n")
    f.write("四\n")

with open("./data2.txt", "a", encoding="utf-8") as f:
    f.write("五\n")
    f.write("六\n")