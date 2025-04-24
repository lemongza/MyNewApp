#12345초를 시간, 분, 초로 변환하세요. 
import time

sec=12345
hour = int(sec /3600)
sec= (sec%3600)
min = int(sec/60)
sec=int(sec%60)
print(f"12345초는 {hour}시간 {min}분 {sec}초입니다.")