import matplotlib
import matplotlib.pyplot as plt
import time
import numpy as np
from matplotlib.patches import *
from matplotlib.ticker import PercentFormatter



d_ak = {
    # 'M' - START, '_' - STOP
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "TGT": "C", "TGC": "C",
    "GAT": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "TTT": "F", "TTC": "F",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    "CAT": "H", "CAC": "H",
    "ATA": "I", "ATT": "I", "ATC": "I",
    "AAA": "K", "AAG": "K",
    "TTA": "L", "TTG": "L", "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    "ATG": "M",
    "AAT": "N", "AAC": "N",
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAA": "Q", "CAG": "Q",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S", "AGT": "S", "AGC": "S",
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "TGG": "W",
    "TAT": "Y", "TAC": "Y",
    "TAA": "_", "TAG": "_", "TGA": "_"
}


def translate(sec, shift=0):
    '''
    Транслирует последовательность нуклеотидов ДНК в верхнем регистре в аминокислотную последовательность
    zip(*[iter(sec)] * 3) - разбивает последовательность на триплеты
    d_ak[(''.join(i))] - заменяет триплеты на соотвествующий символ аминокислоты из словаря d_ak
    :param sec: Транслируемая последовательность
    :param shift: Сдвиг рамки считывания, по умолчанию 0, можно сдвинуть на 1 или 2 (shift=1 или shift=2)
    '''
    sec = sec[shift:]
    return ''.join([d_ak[(''.join(i))] for i in zip(*[iter(sec)] * 3)])


def codon_search(sec, codon='M'):
    codons0 = ['+0:']
    codons1 = ['+1:']
    codons2 = ['+2:']
    t0 = translate(sec, shift=0)
    t1 = translate(sec, shift=1)
    t2 = translate(sec, shift=2)
    for i, x  in enumerate(t0):
        if x == codon:
            codons0.append(i+1)
    for i, x in enumerate(t1):
        if x == codon:
            codons1.append(i+1)
    for i, x in enumerate(t2):
        if x == codon:
            codons2.append(i+1)
    return [codons0, codons1, codons2]


def orf(shift=0,):
    orf_list = []
    for i in starts[shift][1:]:
        for j in stops[shift][1:]:
            if i < j:
                orf_list.append([i,j])
    return orf_list


def ORF_find(starts, stops, frames0= [], frames1= [], frames2= []):
    frames0.append('+0 orfs:')
    frames0.append(orf(0))
    frames1.append('+1 orfs:')
    frames1.append(orf(1))
    frames2.append('+2 orfs:')
    frames2.append(orf(2))
    return [frames0, frames1, frames2]


def find_motif_noncross(motif, sec):
    search_index = 0
    res = []
    while search_index != -1:
        search_index = sec.find(motif, search_index)
        #res.append(search_index)
        res.append([search_index,(search_index + len(motif) - 1)])
        if search_index != -1:
            search_index += len(motif)
    return res[:-1]


def find_motif(motif, sec):
    search_index = 0
    res = []
    while search_index != -1:
        search_index = sec.find(motif, search_index)
        #res.append(search_index)
        res.append([search_index,(search_index + len(motif) - 1)])
        if search_index != -1:
            search_index += 1
    return res[:-1]


# def find_motifs(motifs, sec):
#     search_index = 0
#     res = []
#     while search_index != -1:
#         for motif in motifs:
#             search_index = sec.find(motif, search_index)
#             res.append([search_index,(search_index + len(motif))])
#             if search_index != -1:
#                 search_index += 1
#     return res[:-1]

def find_motifs(motifs, sec):
    search_index = 0
    res1 = []
    res2 = []
    for motif in motifs:
        res1.append(find_motif(motif, sec))
    for reslists in res1:
        for ranges in reslists:
            for i in range(ranges[0], ranges[1]+1):
                res2.append(i)
    return list(set(res2))


def test_time(func):
    def wraper(*args, **kwargs):
        st = time.time()
        result = func(*args, **kwargs)
        et = time.time()
        dt = et - st
        print(f"time: {dt} sek")
        return result

    return wraper


def barcode_pic(motifs, sec):
    mots = find_motifs(motifs, sec)
    #print(f'отображение мотивов {motifs} на последовательности длиной {len(sec)}')
    barcode = [1]
    for i in range(len(sec)):
        if i in mots:
            barcode.append(5)
        else:
            barcode.append(3)
    barcode.append(8)


    code = np.array(barcode)

    pixel_per_bar = 4
    dpi = 100

    fig = plt.figure(figsize=(len(code) * pixel_per_bar / dpi, 0.5), dpi=dpi)
    ax = fig.add_axes([0, 0, 1, 1])  # span the whole figure
    ax.set_axis_off()
    ax.imshow(code.reshape(1, -1), cmap='binary', aspect='auto',
              interpolation='nearest')
    plt.show()


def count_content_abs(sec, d, sortby='keys'):
    for i in set(sec):
        d[i] = sec.count(i)
    if sortby=='keys':
        d = dict(sorted(d.items()))
    if sortby=='values':
        d = dict(sorted(d.items(), key=lambda x: d[x[0]], reverse=True))

    y = list(d.values())
    x = list(d.keys())


    fig = plt.figure(figsize=(6, 4))
    ax = fig.add_subplot()
    ax.bar(x, y, zorder=3, edgecolor='black')
    ax.grid(zorder=0)
    ax.set_ylabel('Count')
    fig.suptitle(f'')
    plt.show()
    return d


def count_content_perc(sec, d, sortby='keys'):
    for i in set(sec):
        d[i] = round(sec.count(i) / len(sec) * 100, 2)
    if sortby=='keys':
        d = dict(sorted(d.items()))
    if sortby=='values':
        d = dict(sorted(d.items(), key=lambda x: d[x[0]], reverse=True))

    y = list(d.values())
    x = list(d.keys())

    fig = plt.figure(figsize=(6, 4))
    ax = fig.add_subplot()
    ax.bar(x, y, zorder=3, edgecolor='black')
    ax.grid(zorder=0)
    #ax.set_ylabel('%')
    fig.suptitle(f'')
    ax.yaxis.set_major_formatter(PercentFormatter(xmax=100))
    plt.show()
    return d