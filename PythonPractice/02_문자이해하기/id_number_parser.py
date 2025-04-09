#주민등록번호 "901212-1234567"에서 생년월일을 추출하세요. 

birth="901212-1234567"
year=birth[:2]
month=birth[4:6]
day=birth[7:9]
print(f"19{year}년 {month}월 {day}일")