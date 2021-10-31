import secrets

import modules.arr_procedures
from modules import calculations as cal


class CryptoSignal:

    def __init__(self, p):
        if p <= 0:
            raise Exception("P can't be less or equal to 0")
        self.__P = p


    def get_P(self):
        return self.__P

    def set_P(self, p):
        if p <= 0:
            raise Exception("P can't be less or equal to 0")
        self.__P = p

    def generate_random_seq(self):
        secrets_generator = secrets.SystemRandom()
        signal = list()
        for i in range(0, self.__P):
            random_number = secrets_generator.randint(0, 1)
            if random_number == 0:
                random_number = -1
                signal.append(random_number)
            else:
                signal.append(random_number)
        return signal

    def generate_def_random_seq(self, if_rmax):

        while True:
            sig = self.generate_random_seq()
            # Getting PFAK
            corel_list = modules.arr_procedures.getCorellation(sig, sig)
            rmax = cal.getMax(corel_list, 1, self.__P - 1, True)
            if rmax[0] <= if_rmax:
                return sig
                break
            # else:
            #    print("trying to generate another")

    # стоит некий счетчик и после 100 попыток если не удалось найти сигнал с заданной кореляцией
    # значение за которым отбирается увеличивается на 1
    def generateDefRandomSeq2(self, if_rmax):
        counter = 0
        while True:
            if counter >= 100:
                counter = 0
                if_rmax += 1

            sig = self.generate_random_seq()
            # Getting PFAK
            corel_list = modules.arr_procedures.getCorellation(sig, sig)
            rmax = cal.getMax(corel_list, 1, self.__P - 1, True)
            if rmax[0] <= if_rmax:
                print(if_rmax)
                return sig
                break
            else:
                counter += 1

    def generete_ensamble_of_cryptosig(self, n, if_rmax):
        tmp_list = []
        for i in range(0, n):
            tmp_list.append(self.generate_def_random_seq(if_rmax))
        return tmp_list

    # 0 ot centralnogo pika
    def genereteAnsambleOfCryptoSig_zero(self, n, ifrmax):
        tmp_list = []
        cnt = 0
        while (cnt != n):

            arr = self.generate_def_random_seq(ifrmax)
            corel_list = modules.arr_procedures.getCorellation(arr, arr)

            if (corel_list[1] == 0 and corel_list[2] == 0 and corel_list[3] == 0):
                print("FOUND")
                tmp_list.append(arr)
                cnt+=1

        return tmp_list

if __name__ == "__main__":
    p=16
    cs = CryptoSignal(p)
    # sig1 = cs.generateRandomSeq()
    # print(sig1)
    # print("AFAK",cal.getCorellation(sig1,sig1,True))

    # pfak rmax = 4 L =16
    # sig2 = cs.generateDefRandomSeq(4)
    # print(sig2)
    # print("PFAK",cal.getCorellation(sig2, sig2))

    # sig3 = cs.generateDefRandomSeq2(2)
    # print(sig3)
    # print("PFAK",cal.getCorellation(sig3, sig3))

    # generete asnsamble of signals with defined Rmax
    ansam = cs.generete_ensamble_of_cryptosig(5, 4)
    print(ansam)

    # getting all pfvks
    asnsam_pfvk_list = modules.arr_procedures.cross_corel_btwn_pairs(ansam, "PFVK")
    # calculate stat for pfaks
    cal.printFullStat(asnsam_pfvk_list, 0, p, True)
    cal.printFullStat(asnsam_pfvk_list, 0, p)

    # for sig in ansam:
    #  print(sig)
    #  pfak_list = cal.getCorellation(sig,sig)
    #   print("PFAK",pfak_list)
    #   cal.printFullStat(pfak_list,1,255,True)
