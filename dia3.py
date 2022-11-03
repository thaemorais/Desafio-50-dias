#Dia 3: Um programa que receba 4 notas de um aluno, uma de cada bimestre, e calcule a média final. Imprima a média final e se o aluno foi APROVADO ou REPROVADO, considerando que a média de aprovação seja igual ou superior a seis.

def main ():
    nota1,nota2,nota3,nota4 = map(int, input().split())
    m = media(nota1,nota2,nota3,nota4)
    print(f"A média do aluno é {m:.2f}")
    aprovado(nota1,nota2,nota3,nota4)

def media(a,b,c,d):
    media = (a+b+c+d)/4
    return media

def aprovado(a,b,c,d):
    m = media(a,b,c,d)
    if m >= 6:
        print("APROVADO")
    else:
        print("REPROVADO")
    
main()