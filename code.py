from os import name, system
from time import sleep

# Variáveis
status = True # True > continuar | False > fechar
homens = 0
mulheres = 0

# Repetições & Condições
while status:
  print('='*30)
  print('SELETOR DE PESSOAS'.center(30))
  print('='*30)
  print('\n')
  idade = int(input('Qual idade da pessoa? ⪼ ').strip())
  sexo = input('Qual sexo da pessoa? [F/M]⪼ ')
  print('Qual cor do cabelo? ︾')
  print('='*30)
  cabelo_color = int(input(f'[1] Preto\n[2] Castanho\n[3] Loiro\n[4] Ruivo\n  ⪼ ')) 
  if sexo.strip().lower() in ['m', 'masculino']:
    # Condições ser for homem
    if cabelo_color == 2 and idade >= 18:
      homens+=1
    
  else:
    # Condições ser for mulheres
    if idade >= 25 and idade <= 30 and cabelo_color == 3:
      mulheres+=1
  print('\n')
  resp = input('Desejar adicionar mais uma pessoa? [S/N]')
  system('cls' if name == 'ns' else 'clear')
  if resp in ['n', 'nao', 'não']:
    status = False
    print('='*30)
    print('SELETOR DE PESSOAS'.center(30))
    print('='*30)
    print('\n')
    print(f'HOMENS DE +18 ANOS E CABELO CASTANHO ⪼ {homens}\n\nMULHERES ENTRE 25 E 30 COM CABELO LOIRO ⪼ {mulheres}')
    print('\n\n💻 ⪼ Fechado programa em 5s')
    sleep(5)
