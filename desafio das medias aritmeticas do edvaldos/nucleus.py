#@title Desafio Evaldos Neneira  { vertical-output: true }
value, grade_list, counter = 0, [], 1             # definindo as variaveis-base

def start():
  global value, grade_list, counter               # setando elas atraves de listas e inputs
  while counter <= 4:
    value = int(input("Please, enter a 🅽🆄🅼🅱🅴🆁 from 𝟎 to 𝟏𝟎! "))
    if 0 <= value <= 10:
      grade_list.append(value); print(grade_list) # colocando o valor do input numa lista
      counter += 1
    elif value < 0 or value > 10:
      print("You haven't inserted a valid number! Please, type again. ")
      counter += 0
  make_sum()

def make_sum():                                   # funcao que faz a soma dos elementos captados do input/lista
  global grade_list
  value, int_to_str = sum(grade_list), [str(int) for int in grade_list]
  if value != 0:
    final_grade = value / 4                       # media final das notas
    if 4 <= final_grade < 6:                      # verifica a media e printa uma mensagem a respeito
      print(f"{'|'.join(int_to_str)} → {final_grade} → You need to do a retake test.")
    elif final_grade < 3.9:
      print(f"{'|'.join(int_to_str)} → {final_grade} → You are flunked, sorry, mate.")
    elif final_grade >= 6:
      print(f"{'|'.join(int_to_str)} → {final_grade} → You passed!")
  elif value == 0:
    print("You are flunked, sorry, mate.")
start()
