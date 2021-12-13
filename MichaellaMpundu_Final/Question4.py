

def recursiveSum(num):

    if(len(num)==1):
        return num
    sum =0
    for i in num:
        sum+=int(i)
    string = str(sum)
    return recursiveSum(string)


def superDigit(str,num):
    return recursiveSum(str*num)



if __name__ == '__main__':

    sum =superDigit('148',3)
    print(sum)