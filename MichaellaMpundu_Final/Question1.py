# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import timeit



def sum_array(lst):
    # declaring a new variable sum and intialize it to 0
    sum = 0
    # loop through the list and add the numeric values into the sum variable
    for i in lst:
        sum+= i

    #     after the loop unds return the total sum calculated back
    return sum

def test_10():
    array = [1,2,3,4,5,6,7,8,9,0]
    # passing to sum_array() and checkign if its value is 45

    assert sum_array(array) == 45


def test_10000():
    # producing array of 10000

    array = [1,2,3,4,5,6,7,8,9,0]*100
    # passing to sum_array() and checkign if its value is 4500

    assert sum_array(array) == 4500


def test_1000000():
    # producing array of 1000000

    array = [1,2,3,4,5,6,7,8,9,0]*100000
    # passing to sum_array() and checkign if its value is 4500000

    assert sum_array(array) == 4500000


def test_1000000000():
    # producing array of 1000000000

    array = [1,2,3,4,5,6,7,8,9,0]*100000000
    # passing to sum_array() and checkign if its value is 4500000000

    assert sum_array(array) == 4500000000




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # starting timer
    start = timeit.default_timer()
    # calling the test for 10 values

    test_10()
    print("--- %s seconds1 --- \t for  10 values\t" % (timeit.default_timer() - start))
    # calling the test for 1000000000 values
    # starting timer
    start = timeit.default_timer()
    # calling the test for 10000 values
    test_10000()
    print("--- %s seconds2 ---\t for  10000 values\t" % (timeit.default_timer() - start))
    # starting timer

    start = timeit.default_timer()
    # calling the test for 10000000 values

    test_1000000()
    print("--- %s seconds3 ---\t for  10000000 values\t" % (timeit.default_timer() - start))
    # starting timer

    start = timeit.default_timer()
    # calling the test for 1000000000 values
    test_1000000000()
    print("--- %s seconds4 ---\t for  1000000000 values\t" % (timeit.default_timer()- start))
    print("Everything passed")

# --- 5.299999999999749e-06 seconds1 ---
# --- 0.00018080000000000873 seconds2 ---
# --- 0.0886033 seconds3 ---
# --- 69.1541242 seconds4 ---
# Everything passed