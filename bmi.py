#BMI = 体重 / （身高 ** 2 ）

try:
    user_weight = float(input("请输入您的体重（单位：kg）："))
    user_height = float(input("请输入您的身高（单位：m）："))
    user_BMI = user_weight / (user_height ** 2)
except ValueError:
    print("输入不合理数字")
except ZeroDivisionError:
    print("身高不能为0")
except:
    print("未知错误")
else:
    print("Your BMI is" + str(user_BMI))
    if user_BMI <= 18.5:
        print("此BMI值属于偏瘦范围")
    elif user_BMI <= 25:
        print("此BMI值属于正常范围")
    elif user_BMI <= 30:
        print("此BMI值属于偏胖范围")
    else:
        print("此BMI值属于肥胖范围")
finally:
    print("结束")

