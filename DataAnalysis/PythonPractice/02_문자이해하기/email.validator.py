#입력된 이메일 주소가 유효한지 검사하세요. (조건: @와 . 포함)

email = input("이메일 주소: ")

if email.__contains__("@"):
    domain = email.split("@")[1]

    if domain.__contains__(".") :
        org = domain.split(".")[1]
        print("유효함")
    else:
        print("유효하지 않음")

else:
    print("유효하지 않음")
