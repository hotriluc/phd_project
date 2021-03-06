import itertools

import matplotlib
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import numpy as np

# using plotly to build plot
from matplotlib import ticker
from matplotlib.ticker import FormatStrFormatter


def build_plotly(aList, graph_name="Untitled"):
    fig = go.Figure(data=go.Scatter(y=aList, name=graph_name, line=dict(color='red', width=2)))
    fig.update_layout(title=graph_name)
    fig.write_html(graph_name + '.html', auto_open=True)


# using matplotlib to build plot
def build_plot(aList, graph_name=""):
    if (len(aList) > 300):
        plt.figure(figsize=(20, 10))


    plt.plot(aList, color='red', linewidth=1, marker='o', markersize=1)
    csfont = {'fontname': 'Times New Roman',
                          'weight': 'normal',
                            'size': 10}
    plt.title(graph_name, **csfont)
    plt.grid()
    plt.show()

def build_BER(snrindB_range,ber):
    plt.plot(snrindB_range, ber, 'o-', label='practical')
    plt.yscale('log')
    # plt.axis([0, 10, 0, 0.1])
    plt.xlabel('snr(dB)')
    plt.ylabel('BER')
    plt.grid(True)
    plt.title('BPSK Modulation')
    plt.legend()
    plt.show()

def build_BER_compare(snridB_range, *args):
    fig, ax = plt.subplots()
    marker = itertools.cycle((',', '+', '.', 'o', '*'))
    name = ['КС','ХДС','АФМ-16']
    i=0
    for set in args:
        # plt.plot(snridB_range, set,label='Set '+str(i))
        ax.plot(snridB_range, set,marker=next(marker),label=name[i])
        i+=1

    plt.xlabel('snr(dB)')
    plt.ylabel('BER')
    plt.grid(True)
    plt.title('BPSK Modulation')
    plt.legend()
    ax.set_yscale('log')
    ax.set_ylim( ymax=1)
    # ax.yaxis.set_major_formatter(FormatStrFormatter('%.03f'))


    plt.show()

def build_spectrum(frequency,power_spectrum,graph_name=""):
    if (len(frequency) > 200):
        plt.figure(figsize=(20, 10))

    if (len(frequency) > 1000):
        plt.figure(figsize=(30, 10))

    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Spectrum')

    plt.plot(frequency, abs(power_spectrum),linewidth=1)
    csfont = {'fontname': 'Times New Roman',
              'weight': 'normal',
              'size': 10}
    plt.title(graph_name, **csfont)
    plt.grid()
    plt.show()

    # fig = plt.figure()
    # ax1 = fig.add_subplot(121)
    # ax2 = fig.add_subplot(122)
    # ax1.plot(frequency, abs(power_spectrum))
    # ax2.plot(frequency, abs(power_spectrum))
    #
    # scale_y = 1e2
    # ticks_y = ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x / scale_y))
    # ax2.yaxis.set_major_formatter(ticks_y)


    # plt.stem(frequency, abs(power_spectrum),use_line_collection=True)
    # plt.show()


def build_spectrum_plotly(frequency,power_spectrum,graph_name="Untitled"):

    fig = go.Figure(data=go.Scatter(x=frequency,y=abs(power_spectrum), name=graph_name, line=dict(color='red', width=2)))
    fig.update_layout(title=graph_name)
    fig.write_html(graph_name + '.html', auto_open=True)

if __name__ == "__main__":
    a = [1,2,3,4,5,6,7,8,9,10]
    cs_ber = [0.05621953125, 0.037604296875, 0.022876171875, 0.012468359375, 0.0059296875, 0.002419140625, 0.000802734375, 0.000205078125, 3.046875e-05, 3.515625e-06]
    cds_ber = [0.056342578125, 0.0375125, 0.02279765625, 0.012490625, 0.005978125, 0.002396875, 0.00077265625, 0.000187890625, 3.515625e-05, 4.6875e-06]
    afm_ber = [0.264275, 0.1391, 0.0832, 0.04625, 0.028225, 0.0176, 0.011125, 0.0074, 0.004025, 0.002025]

    build_BER_compare(a,cs_ber,cds_ber,afm_ber)