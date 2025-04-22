import math


#这是一行注释

name = "张三"
print("你好" + " 世界\n" + name)
print("He said \"Let\'s go!\"")
print("""三引号
可直接换行""")

print(math.sqrt(4))

print(len(name + "\n"))

print(name[0]) #从0开始

print(type(True))
print(type(None))

#逻辑判断 not 非 > and 与 > or 或

shopping_list = ["键盘"]  #列表是可变的
example_tuple = ("键盘","键帽") #元组是不可变的
shopping_list.append("键帽")
shopping_list.remove("键帽")
shopping_list[0] = "硬盘"
print(shopping_list)

prize = [799, 1000, 899, 1024]
max_prize = max(prize)
min_prize = min(prize)
sorted_prize = sorted(prize)
print(sorted_prize)

contacts = {"张三": "003", "李四": "002"}  #{key：value，key2:value2}字典的key只能是不可变参数
print(contacts)
print(contacts.keys())
print(contacts.values())
print(contacts.items())
print(str(len(contacts)))
if "张三" in contacts:
    print(contacts["张三"])

#for 变量名 in 可迭代对象:
#while 条件:

year = 2024.2025
print("""{0}
{1:.2f}""".format(name,year))
print("""{name}
{year}""".format(name=name,year=year))
print(f"""{name}
{year:.3f}""")

#def 函数名(变量，变量2)：
#   return 变量