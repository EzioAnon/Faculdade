import numpy as n
import math
import matplotlib.pyplot as pl



def LeArquivos(at):
    
  (x, y, z, w,h) = n.loadtxt(at, dtype='float', comments='#')
    
  return(x, y, z, w,h)

def quedalivre(q):
  x = n.linspace(1.0, 1.4, 1000)
  y = ((2 * x) / q) ** (1 / 2)
  Q = [x,y]
  return Q

def ajustedereta(Px, A, B):
 q = 0
 w = 0
 e = 0
 r = 0
 i = 0
 while i < Px:
   q += A[i]
   w += A[i] *A[i]
   e += B[i]
   r += A[i] * B[i]
   i += 1
 div = ((Px * w) - (q * q))
 Ra = (((w * e) - (r * q)) / float(div))
 Rb = (((Px * r) - (q * e)) / float(div))
 return Ra, Rb
  
def SomaMedia(m):
  contador = 0
  media = 0
  while(contador < 5):
    media+= m[contador]
    contador += 1
  media= media/5
  
  return media


def DesvioPadrao(x):
 media = SomaMedia(x)
  
 desvio = ((((x[0]-media)**2)+((x[1]-media)**2)+((x[2]-media)**2)+((x[3]-media)**2)+((x[4]-media)**2))/4)
  
  
 return math.sqrt(desvio)

def reducao(a,b,c):
 DR = n.array(a + b + c)
 DR = n.array(DR.reshape(3, 5), dtype = n.float)
 DR = DR.T
 n.savetxt("dadosreduzidos.txt", DR)


def PlotarExperimental(a,b,c):
 pl.title("Tempo x Altura")
 pl.xlabel("Altura")
 pl.ylabel("Tempo de queda")
 
 pl.errorbar ( a , b , yerr = c , fmt = 'or', label = "Experimental")
 pl.plot ( a , b , 'ob')
 

def Plotar (a,b,c, q):
 Q = quedalivre(q)
 pl.plot(Q[0], Q[1], "-", label = q)
 return


def MostarGrafico():
 pl.grid(linestyle='-', linewidth=1.0)
 pl.legend(loc = 'upper left')
 pl.savefig("grafico.jpg")
 pl.show()
 return


def lineaziracao():
 a,b,erro = n.loadtxt( "dadosreduzidos.txt").transpose()
 A = n.log(a)
 B = n.log(b)
 Px = len(A) 
 assert len(B) == Px
 return  ajustedereta(Px, A, B) 

  
def Gravidade(g):#ConserterAlgumErroaqui ou em ajuste de reta
  g = math.e**g
  G = 2/(g**2)
  return G
