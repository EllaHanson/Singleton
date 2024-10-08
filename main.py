import sys

if (len(sys.argv) == 2):
    file_name = sys.argv[1]
else:
    exit()
    #print("error!! enter template -> 'python3 main.py [filename]'")

A = []
with open(file_name, 'r') as file:
    for x in file:
        A.append(int(x))

def single(A: list[int]):
    if len(A) == 1:
        return A[0]
    start = 0
    end = len(A) - 1
    mid_index = end // 2
    mid_value = A[mid_index]
    left_mid = A[mid_index-1]
    right_mid = A[mid_index+1]

    if left_mid != mid_value and right_mid != mid_value:
        return mid_value
    
    if mid_value == right_mid:
        right_list = A[mid_index:]
        left_list = A[:mid_index]

    else:
        right_list = A[mid_index+1:]
        left_list = A[:mid_index+1]

    if len(right_list) % 2 == 1:
        return single(right_list)
    else:
        return single(left_list)
    

print(single(A))
#single(A)





