from MyModule import *
import matplotlib
import matplotlib.pyplot as plt
import time
import numpy as np
from matplotlib.patches import *

# sec = input("Введите последовательность: ", ).upper() # для ручного ввода последовательности
try:
    with open('cdk8.fasta.fasta') as file:
        linelist = file.readlines()
        genes = []
        for i in linelist:
            i = i.replace('\n', '')
            if '>' in i:
                genes.append([i])
            else:
                genes[len(genes)-1].append(i)
        sec = ''.join(genes[0][1:]).upper()
        name = genes[0][0].split()[1]
        print(f'первая из {len(genes)} последовательностей {name} \nдлиной {len(sec)}bp: {sec[:10]}...{sec[-10:]}', sep='\n')

        sec = sec.replace('U', 'T')
        reverse_sec = sec[::-1]

        print('доделать - график "али", диаграммы нуклеотидов и аминокислот, '
              '\n\tотдельно функцию стартс/стопс(sec), отдельный принт ORF data(sec),'
              '\n\tрасфигачить по пакетам модули(? 8.4 лекция), volcano plot?'
              '\n\tуказать длину рамки поискать про фреймшифт последовательности, сплайсинг?')
        print()

        motifs = [
            'gggg',
            'ggcg',
            'ggcc',
            'cggg',
            'cgcg',
            'gccg',
            'gggc',
            'ccgg',
            'gcgg',
            'gcgc'
    ]

        for i in range(len(motifs)):
            motifs[i] = motifs[i].upper()

        barcode_pic(motifs, sec)
        # d= {}
        # count_content_abs(sec,d, sortby='values')


except Exception as e: print(e)
