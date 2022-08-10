# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    # converting positive integer N to binary

    index_string = ''
    container_index1 = []
    container_index2 = []
    binary_num = format(N, "b")

    for i in range(len(binary_num)):
        if binary_num[i] == '1':
            temp_var = i
            container_index1.append(str(temp_var))
    for i in range(len(container_index1)-1):
        e = int(container_index1[i+1]) - int(container_index1[i])
        container_index2.append(e-1)
    if len(container_index2) >= 1:
        return max(container_index2)
    else:
        return 0
    
