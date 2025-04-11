# 문자열을 인자로 받아 단어 수를 반환하는 count_words 함수를 작성하세요.   

def count_words(sentence):
    cnt = len(sentence.split(' '))
    print("단어 수:", cnt)
    
count_words('단어 개수 셉니다 !') #4개