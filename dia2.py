#Dia 2: Um programa que leia 3 valores inteiros e imprima o maior e o menor deles.
def main ():
  a,b,c = map(int, input().split())
  maior(a,b,c)
  menor(a,b,c)

def maior(a,b,c):
  if (a >= b and a >= c):
      print (f"O maior é {a}")
  elif (b >= a and b >= c):
      print (f"O maior é {b}")
  else:
      print (f"O maior é {c}")

def menor(a,b,c):
  if (a <= b and a <= c):
      print (f"O menor é {a}")
  elif (b <= a and b <= c):
      print (f"O menor é {b}")
  else:
      print (f"O menor é {c}")

main()