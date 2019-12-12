#    _ _ _      _____                 _     
#   | (_) |    / ____|               | |    
#   | |_| |_  | |  __ _ __ __ _ _ __ | |__  
#   | | | __| | | |_ | '__/ _` | '_ \| '_ \ 
#   | | | |_  | |__| | | | (_| | |_) | | | |
#   |_|_|\__|  \_____|_|  \__,_| .__/|_| |_|
#                              | |          
#                              |_|          
#############################################
#                                           #
#		Made by Boitata             #
#	   github.com/boitatabrazil         #
#                                           #
#############################################
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import networkx as nx
from itertools import count
from networkx.drawing.nx_agraph import graphviz_layout
import os
import nltk
nltk.download('punkt')

files = os.listdir()
print('\n\n')
for i in files:
    print(i)

filename = input('\n\nDigite o nome do arquivo do livro\t')
dicname = input('Digite o nome do arquivo do dicionario de personagens\t')

window = int(input('\nDigite o tamanho da janela\t'))
overlap = int(input('Digite o tamanho do overlap\t'))

limiar = int(input('Digite o valor do limiar para aumentar a borda\t'))

saida = input('Digite o nome do arquivo de saida\t')


f = open(filename, 'r')

string = f.read()

tokens =  nltk.word_tokenize(string)

dic = pd.read_csv(dicname,delimiter=';')

dicc = dic.Dic.values

for i in range(0,len(dicc)):
    dicc[i] = dicc[i].split()

for i in range(0,len(tokens)):
    for j in range(0,len(dicc)):
        if tokens[i] in dicc[j]:
            tokens[i] = dic.Name[j]
            break

matrix = np.zeros((len(dic),len(dic)),float)

def lim(x,w,l):
    x = x+w
    if x > l:
        return l
    return x

i=0
while(i<len(tokens)):
    conec = []
    for j in range(0,len(dic)):
        if dic.Name[j] in tokens[i:lim(i,window,len(tokens))]:
            if dic.Name[j] not in conec:
                conec.append([dic.Name[j],j])
    for k in conec:
        for l in conec:
            if k!=l:
                matrix[k[1]][l[1]] = matrix[k[1]][l[1]] + 1
    i = i + window - overlap
    print(conec)

c = []
for i in matrix:
    c.append(i.sum())


G = nx.Graph()
j=0
for i in dic.Name:
    if c[j] != 0:
        G.add_node(i,conec=c[j])
    j = j+1
for i in range(0,len(matrix)):
    for j in range(i,len(matrix)):
        if matrix[i][j] != 0:
            G.add_edge(dic.Name[i],dic.Name[j], weight=matrix[i][j])
            
elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] > limiar]
esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] <= limiar]

groups = set(nx.get_node_attributes(G,'conec').values())
mapping = dict(zip(sorted(groups),count()))
nodes = G.nodes()
colors = [mapping[G.node[n]['conec']] for n in nodes]

from networkx.drawing.nx_agraph import graphviz_layout
pos = graphviz_layout(G)
plt.axis('off')
nx.draw_networkx_nodes(G,pos,nodelist=nodes, node_color=colors,cmap=plt.cm.Wistia, alpha = 1,node_size=1000)  # draws nodes
#nx.draw_networkx_edges(G,pos,edge_color='b',alpha = 0.6)  # draws edges

nx.draw_networkx_edges(G, pos, edgelist=elarge, width=3, edge_color='b',alpha = 0.6)
nx.draw_networkx_edges(G, pos, edgelist=esmall, alpha=0.6, edge_color='b')


#nx.draw_networkx_edge_labels(G,pos,edge_labels = nx.get_edge_attributes(G,'weight')) # edge lables
nx.draw_networkx_labels(G,pos,font_size=18) # node lables

fig = plt.gcf()
fig.set_size_inches(25, 20)
fig.savefig(saida, dpi=100)


print('DONE')
