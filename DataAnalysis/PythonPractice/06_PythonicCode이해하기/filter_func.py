# [10, 20, 30, 40, 50]에서 30보다 큰 수만 필터링하세요. 

row_list = [10, 20, 30, 40, 50]
filter_list = list(filter(lambda x: x > 30, row_list))
print(filter_list)