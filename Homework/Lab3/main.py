
def array_cyclic_shift(array: list, shift: int):
    return array[shift::] + array[:shift:]

def rearrange_nested_lists(matrix: list[list], shift: int):
    answer = []
    for i in matrix:
        answer.append(i[shift::] + i[:shift:])
    return answer

def list_blocks_reversal(array: list, block_size: int):
    answer = []
    for i in range(0, len(array)-block_size+1, block_size):
        answer += (array[i:i+block_size:])[::-1]
    return answer + array[len(array) - (len(array) % block_size)::]

def max_subarray_sum(array: list, k: int):
    answer = list(array[0:k:])
    for i in range(len(array)+1-k):
        subarray = array[i:i+k:]
        if (sum(subarray) > sum(answer)):
            answer = subarray
    return answer

print(array_cyclic_shift([1,2,3,4,5,6], 2))
print(rearrange_nested_lists([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2))
print(list_blocks_reversal([1, 2, 3, 4, 5, 6, 7], 3))
print(max_subarray_sum([1, -2, 3, 4, -1, 2, 1, -5, 4], 3))