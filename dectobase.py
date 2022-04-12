from math import floor
import time

def main():
    dectobase(10000)

def dectobase(num):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    nums = [None] * 35
    times = [None] * 35
    arr = [None] * 2

    for x in range(2, 37):
        outs = ""
        number = num
        start_time = time.time()

        while number > 0:
            if (number % x) < 10:
                outs = str(number % x) + outs
                number = floor(number / x)
            else:
                outs = alphabet[(number % x) - 10] + outs
                number = floor(number / x)
        
        nums[x - 2] = outs
        times[x - 2] = time.time() - start_time
    
    arr[0] = nums
    arr[1] = times

if __name__ == "__main__":
    main()