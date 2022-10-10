def helper(arr, n, start, lsum, rsum):

    # If reached the end
    if start == n:
        return lsum == rsum

    # If divisible by 5 then add
    # to the left sum
    if arr[start] % 5 == 0:
        lsum += arr[start]

    # If divisible by 3 but not by 5
    # then add to the right sum
    elif arr[start] % 3 == 0:
        rsum += arr[start]

    # Else it can be added to any of
    # the sub-arrays
    else:

        # Try adding in both the sub-arrays
        # (one by one) and check whether
        # the condition satisfies
        return helper(arr, n, start + 1, lsum + arr[start], rsum) or helper(
            arr, n, start + 1, lsum, rsum + arr[start]
        )

    # For cases when element is multiple of 3 or 5.
    return helper(arr, n, start + 1, lsum, rsum)


# Function to start the recursive calls
def balancedSplitExists(arr):

    # Initially start, lsum and rsum
    # will all be 0
    n = len(arr)
    return helper(arr, n, 0, 0, 0)


def printString(string):
    print('["', string, '"]', sep="", end="")


test_case_number = 1


def check(expected, output):
    global test_case_number
    result = False
    if expected == output:
        result = True
    rightTick = "\u2713"
    wrongTick = "\u2717"
    if result:
        print(rightTick, "Test #", test_case_number, sep="")
    else:
        print(wrongTick, "Test #", test_case_number, ": Expected ", sep="", end="")
        printString(expected)
        print(" Your output: ", end="")
        printString(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    arr_1 = [2, 1, 2, 5]
    expected_1 = True
    output_1 = balancedSplitExists(arr_1)
    check(expected_1, output_1)

    arr_2 = [3, 6, 3, 4, 4]
    expected_2 = False
    output_2 = balancedSplitExists(arr_2)
    check(expected_2, output_2)
