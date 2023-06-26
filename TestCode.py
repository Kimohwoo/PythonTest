num1 = int(input("첫번쨰 숫자를 입력하세요: "))
num2 = int(input("두번쨰 숫자를 입력하세요: "))
addNum = int(input("더할 숫자를 입력하세요: "))

result = 0

for num in range(num1, num2+1, addNum):
    result += num

print("result: %d", result) 
