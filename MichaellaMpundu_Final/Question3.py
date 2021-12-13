


def encryptText(text,n):
    # creatign a new list
    lst= []
    # assinging the value of n to ctr
    ctr = n
    # creatign another counter and initializing it with zero
    masterctr=0
    # looping from 0 to the length of the text string
    for i in range(len(text)):
        # creating a new list to append new columns
        col =[]
        # looping from zero to the value of sub arrays passed
        for j in range(n):
            # if the ctr is equal to the number of sub arrays  appedn text of outer loop and increae the master counter and set ctr to zero
            if(ctr==n ):
                col.append(text[i])
                ctr=0
                masterctr+=1

            # else increae the ctr and append a space in a col array

            else:
                ctr+=1
                col.append(' ')
            # lastly if masterctr is ZERO set ctr to n and set master to zero

            if (masterctr==n):
                ctr=n
                masterctr=0



        #in outer loop apend the sub columns into the another list

        lst.append(col)
    #return the main list to caller

    return lst
def decryptText(text,n):
    # creatign a new string
    lst= ''
    # assinging the value of n to ctr
    ctr = n
    # creatign another counter and initializing it with zero
    masterctr=0
    # looping from 0 to the length of the text string
    for i in text:
        # creating a new string  to append new charecters
        col =''
        # looping from zero to the value of sub arrays passed

        for j in i :
            # if the ctr is equal to the number of sub arrays  appedn text of outer loop and increae the master counter and set ctr to zero

            if(ctr==n ):
                col+=j
                ctr=0
                masterctr+=1

                # else increae the ctr and append a space in a col array

            else:
                ctr+=1
                # col+=' '
            if (masterctr==n):
                ctr=n
                masterctr=0

        #in outer loop apend the sub charecters into the another main string
        lst+=col
    #return the main string  to caller

    return lst







if __name__ == '__main__':
    # passing string to ecnryptText() function and also passing the number of sub arrays and storing the encrypted text to str variable
    str = encryptText('plain text',3)
    print(str)
    # passing str the encrypted Text function and also passing the number of sub arrays and saving it on str
    str = decryptText(str,3)
    # printing the values
    print(str)


