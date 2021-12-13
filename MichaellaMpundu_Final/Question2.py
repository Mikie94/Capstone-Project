

import copy

def grade(arr):
    ctr=0
    for i in arr:
        nextNum = ((i//5)+1)*5
        if(nextNum- i <3 and nextNum>=40):
            arr[ctr] = nextNum
            print(nextNum)
        ctr+=1;
    return arr
    ''''''


if __name__ == '__main__':
    gnuine = [73,67,38,33]
    edited = grade(copy.deepcopy(gnuine))

    for i in range(len(gnuine)):
        print(gnuine[i],' ->  ',edited[i])
