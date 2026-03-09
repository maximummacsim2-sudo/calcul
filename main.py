print ("1 - умножение")
print("2 - деление")
print("3 - сложение")
print("4 - вычитанние")

def umn():
    num1 = int(input("1 множетель - "))
    num2 = int(input("2 множитель - "))
    print(f" Ответ: {num1*num2}")

function = input("Что вам нкжно сделать из выше перечисленного?(Напишите число) - ")

if function == "1":
    umn()

