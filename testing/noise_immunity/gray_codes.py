def generate_gray(n):
    if (n<=0):
        return ['0']
    if (n==1):
        return ['0','1']
    # call recursion
    rec_ans = generate_gray(n-1)

    main_ans = []

    # Add 0 to first half
    for i in range(len(rec_ans)):
        sym = rec_ans[i]
        main_ans.append("0" + sym)
    # Add 1 to second half(mirrored)
    for i in range(len(rec_ans)-1, -1, -1):
        sym = rec_ans[i]
        main_ans.append("1" + sym)
    
    return main_ans

def convert_bin_to_gray(n):
    pad = len(n)
    n = int(str(n), 2)
    n ^= (n >> 1)

    
    return format(n, "0{0}b".format(pad))
  
def convert_gray_to_bin(n):
    n = int(str(n),2)
    mask = n
    while n!=0:
        mask = mask >> 1
        n ^= mask
    return bin(n)[:2]


if __name__=="__main__":
    gray_code = generate_gray(2)
    print(gray_code)
    print(convert_bin_to_gray('010'))
