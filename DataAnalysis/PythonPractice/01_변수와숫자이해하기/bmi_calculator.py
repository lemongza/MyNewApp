#사용자로부터 체중(kg)과 키(cm)를 입력받아 BMI를 계산하세요. 

weight = float(input("체중(kg): "))
height = float(input("키(cm): "))
BMI = weight / (height * 0.01) ** 2
print("BMI: ",round(BMI,1))