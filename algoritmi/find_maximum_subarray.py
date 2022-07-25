def find_max_crossing_subarray(A, low, mid, high):
    left_sum = -100000000
    sum = 0
    max_left = 0
    max_right = 0
    for i in range(mid, low - 1, -1):
        sum = sum + A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    right_sum = -10000000
    sum = 0
    for j in range(mid + 1, high + 1):
        sum = sum + A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    return (max_left, max_right, left_sum + right_sum)

def find_maximum_subarray(A, low, high):
    if high == low:
        return (low, high, A[low])
    else:
        mid = (high + low) // 2
        (left_low, left_high, left_sum) = find_maximum_subarray(A, low, mid)
        (right_low, right_high, right_sum) = find_maximum_subarray(A, mid + 1, high)
        (cross_low, cross_high, cross_sum) = find_max_crossing_subarray(A, low, mid, high)
        if (left_sum >= right_sum) and (right_sum >= cross_sum):
            return (left_low, left_high, left_sum)
        elif (right_sum >= left_sum) and (right_sum >= cross_sum):
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)

if __name__ == '__main__':
    A = [1,2,3,4,5,6,7,8,9,10]
    print(find_maximum_subarray(A,2,8))
