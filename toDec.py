import time
#function to return value of a character 0-9 as the same value, A-F as
def value(num):
    if num>= '0' and num <= '9':
        return chr(ord(num) - ord('0'))
    else : 
        return chr(ord(num) - ord('A')+10) 

#function to reverse string
def strev(str):
    length = len(str)
    for i in range(int(length/2)):
        temp = str[i]
        str[i] = str[length -i -1]
        str[len-i-1] = temp

#function to find number of digits required to convert decimal numbers to inputted base
def fromDectoBase(base,inputnumber):
        res=""
        index = 0
        while(inputnumber>0):
            res+=value(inputnumber%base)
            inputnumber=int(inputnumber/base)

        #reverse the result
        res=res[::-1]

        return len(res)

def graphBase(base):
    out =[]
    x=[]
    inp = [1, 10, 100, 1000, 5000, 10000, 50000, 100000, 500000, 100000 ]
    for i in inp:
        start_time = time.time()
        out.append(fromDectoBase(base,i))
        x = time.time() -start_time
    return [out,x]
    
print(graphBase(2))

    









