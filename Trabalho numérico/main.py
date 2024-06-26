import funcoes as f
import numpy as n


#Alturas
at1 = "at1.txt"
at2 = "at2.txt"
at3 = "at3.txt"
at4 = "at4.txt"
at5 = "at5.txt"

M1 =f.SomaMedia(f.LeArquivos(at1))
D1 = f.DesvioPadrao(f.LeArquivos(at1))

M2 = f.SomaMedia(f.LeArquivos(at2)) 
D2 = f.DesvioPadrao(f.LeArquivos(at2))


M3 = f.SomaMedia(f.LeArquivos(at3))
D3 = f.DesvioPadrao(f.LeArquivos(at3))

M4 = f.SomaMedia(f.LeArquivos(at4))
D4 = f.DesvioPadrao(f.LeArquivos(at4))

M5 = f.SomaMedia(f.LeArquivos(at5))
D5 = f.DesvioPadrao(f.LeArquivos(at5))

a = (1.0, 1.1, 1.2,1.3, 1.4)
b = (M1,M2,M3,M4,M5)
c = (D1,D2,D3,D4,D5)


f.PlotarExperimental(a,b,c)

f.reducao(a,b,c)
f.Plotar(a,b,c,9.81)

Ra, Rb = f.lineaziracao()

G = f.Gravidade(Ra)

f.Plotar(a,b,c,G)


f.MostarGrafico()
