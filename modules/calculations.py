import itertools
import math
import math as m
import numpy as np
from sympy import primefactors
from scipy.stats import kurtosis
import modules.plot as mp

# coprimes for modulo is supposed to be from 1..n-1 (e.g. for 13 is 1,2,3,.12)
# checking all g^p mod modulo from where g,p = 1..n-1 and adding to temporary list
# if tmp_list equals to required then we mark(add) g as primitive root
# !!!modulo argument is INTEGER!!!

def prim_roots(modulo):
    required_set = {num for num in range(1, modulo) if m.gcd(num, modulo)}
    return [g for g in range(1, modulo) if required_set == {pow(g, powers, modulo)
                                                            for powers in range(1, modulo)}]


def prim_roots2(modulo):
    required_set = {num for num in range(1, modulo) if m.gcd(num, modulo)}
    tmp_set = set()
    result_list = list()
    for g in range(1, modulo):
        for powers in range(1, modulo):
            tmp = pow(g, powers, modulo)
            tmp_set.add(tmp)
        if required_set == tmp_set:
            result_list.append(g)
            tmp_set.clear()
        else:
            tmp_set.clear()
    return result_list


def isPrime(n):
    # Corner cases
    if (n <= 1):
        return False
    if (n <= 3):
        return True

    # This is checked so that we can skip
    # middle five numbers in below loop
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6

    return True


""" Iterative Function to calculate (x^n)%p 
    in O(logy) */"""


def power(x, y, p):
    res = 1  # Initialize result

    x = x % p  # Update x if it is more
    # than or equal to p
    while (y > 0):
        # If y is odd, multiply x with result
        if (y & 1):
            res = (res * x) % p
            # y must be even now
        y = y >> 1  # y = y/2
        x = (x * x) % p

    return res


def findPrimitive(n):
    s = set()

    # Check if n is prime or not
    if (isPrime(n) == False):
        return -1

    # Find value of Euler Totient function
    # of n. Since n is a prime number, the
    # value of Euler Totient function is n-1
    # as there are n-1 relatively prime numbers.
    phi = n - 1

    # Find prime factors of phi and store in a set
    s = primefactors(phi)

    # Check for every number from 2 to phi
    for r in range(2, phi + 1):

        # Iterate through all prime factors of phi.
        # and check if we found a power with value 1
        flag = False
        for it in s:

            # Check if r^((phi)/primefactors)
            # mod n is 1 or not
            if (power(r, phi // it, n) == 1):
                flag = True
                break

        # If there was no power with value 1.
        if flag == False:
            return r

            # If no primitive root found
    return -1


# phi = n*(1-1/a)*(1-1/b)*(1-1/c)..
# num_compries Euler's totient function
# All coprimes of n are put in comprime_list
def coprimes(n):
    coprime_list = list()
    prime_fact = primefactors(n)
    arr = [(1 - 1 / el) for el in prime_fact]
    num_coprimes = int(np.prod(arr) * n)

    for el in range(1, n):
        if m.gcd(el, n) == 1:
            coprime_list.append(el)

    return num_coprimes, coprime_list


# gettng rmax from correlation list
# if abs_flag = True then absolute values
def getMax(aList: list, start, end, abs_flag=False):
    rmax_indx_list = list()

    if abs_flag == True:
        abs_list = [abs(x) for x in aList]
        rmax = max(abs_list[start:end])
        for i in range(0, len(aList)):
            if abs(aList[i]) == rmax:
                rmax_indx_list.append(i)
    else:
        rmax = max(aList[start:end])
        for i in range(0, len(aList)):
            if aList[i] == rmax:
                rmax_indx_list.append(i)

    return rmax, rmax_indx_list





def getPair(list_with_count_of_sigs: list):
    pair_list = []
    for pair in itertools.combinations(list_with_count_of_sigs, 2):
        # print(pair)
        pair_list.append(pair)
    return pair_list


# getting Average(mean) of the list
# abs_flag==false then AVG for all value(included positive and negative sign)(?????? ???????? ????????????????)
# abs_flag==true AVG for absolute values(???? ????????????)
def getAVG(aList, start, end, abs_flag=False):
    if abs_flag == True:
        abs_list = [abs(x) for x in aList]
        return np.mean(abs_list[start:end])
    return np.mean(aList[start:end])


# getting Dispersion(varience) of the list
# abs_flag==false then VAR for all value(included positive and negative sign)
# abs_flag==true VAR for absolute values(???? ????????????)
def getVAR(aList, start, end, abs_flag=False):
    if abs_flag == True:
        abs_list = [abs(x) for x in aList]
        return np.var(abs_list[start:end])
    return np.var(aList[start:end])


# getting Standert Deviation(std) of the list
# abs_flag==false then STD for all value(included positive and negative sign)
# abs_flag==true STD for absolute values(???? ????????????)
def getSTD(aList, start, end, abs_flag=False):
    if abs_flag == True:
        abs_list = [abs(x) for x in aList]
        return np.std(abs_list[start:end])
    return np.std(aList[start:end])

def getKurtosis(aList, start, end, abs_flag=False):
    if abs_flag == True:
        abs_list = [abs(x) for x in aList]
        return kurtosis(abs_list)

    return kurtosis(aList)


# Calculate stats for each corel_list in ansamble
# abs_flag==false then statistics for all value(included positive and negative sign)
# abs_flag==true statistics for absolute values(???? ????????????)
# List of num var for consists combination of signals
# start,end - starting and ending index of correlation functions(
# slice of correlation function
#  e.g corel_func =[-4 0 -4 .. -2]
#  so in cross correlation you have to count 1st (0 pos in list) and last (len(list)) elements
#  in order to calculate correct statistics
#  but in auto correlation first and last elements' value are same as signals length so it's no need to use it
#  start = 1 end = len(signal)-1)
def printFullStat(ensamble_of_correl_lists: list, start, end, abs_flag=False, list_of_num=None):
    avg_list = list()
    var_list = list()
    std_list = list()
    x_list = list()
    kurtosis_list = list()
    p = 0
    i = 0
    if abs_flag == True:
        print("=====ABSOLUTE=====")
        if list_of_num:
            print("%-10s %-10s %-10s %-10s %-10s %-10s" % ("#\t", "X\t", "AVG\t", "VAR\t", "STD\t", "KURTOSIS\t"))
        else:
            print("%-10s %-10s %-10s %-10s %-10s" % ("X\t", "AVG\t", "VAR\t", "STD\t", "KURTOSIS\t"))
    else:
        print("=======ALL=======")
        if list_of_num:
            print("%-10s %-10s %-10s %-10s %-10s %-10s" % ("#\t", "X\t", "AVG\t", "VAR\t", "STD\t", "KURTOSIS\t"))
        else:
            print("%-10s %-10s %-10s %-10s %-10s" % ("X\t", "AVG\t", "VAR\t", "STD\t", "KURTOSIS\t"))

    for item in ensamble_of_correl_lists:

        p = len(item)
        X = getMax(item, start, end, abs_flag)
        AVG = getAVG(item, start, end, abs_flag)
        VAR = getVAR(item, start, end, abs_flag)
        STD = getSTD(item, start, end, abs_flag)
        KURTOSIS = getKurtosis(item,start,end,abs_flag)
        x_list.append(X[0])
        avg_list.append(AVG)
        var_list.append(VAR)
        std_list.append(STD)
        kurtosis_list.append(KURTOSIS)

        if list_of_num:
            print("{0}\t\t {1:5f}\t {2:5f}\t {3:5f}\t {4:5f}\t {5:5f}\t".format(list_of_num[i], X[0] / math.sqrt(p),
                                                                         AVG / math.sqrt(p), VAR / math.sqrt(p),
                                                                         STD / math.sqrt(p), KURTOSIS   ))
            i += 1
        else:
            print("{0:5f}\t {1:5f}\t {2:5f}\t {3:5f}\t {4:5f}\t ".format(X[0] / math.sqrt(p), AVG / math.sqrt(p),
                                                                         (VAR) / math.sqrt(p), STD / math.sqrt(p), KURTOSIS  ))

    print("____________________________"*2)
    print("X = {0:5f}\tAVG = {1:5f}\tVAR = {2:5f}\tSTD = {3:5f}\tKURTOSIS = {4:5f}".format(np.mean(x_list) / math.sqrt(p),
                                                                            np.mean(avg_list) / math.sqrt(p),
                                                                            np.mean(var_list) / math.sqrt(p),
                                                                            np.mean(std_list) / math.sqrt(p),
                                                                            np.mean(kurtosis_list) / math.sqrt(p)))
    print("____________________________"*2,"\n")



