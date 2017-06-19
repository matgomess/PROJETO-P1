import sys
import random
TODO_FILE = 'todo.txt'
ARCHIVE_FILE = 'done.txt'
RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"
YELLOW = "\033[0;33m"
ADICIONAR = 'a'
REMOVER = 'r'
FAZER = 'f'
PRIORIZAR = 'p'
LISTAR = 'l'
def printCores(texto, cor) :
  print(cor + texto + RESET)
def adicionar(descricao, extras):
  # não é possível adicionar uma atividade que não possui descrição. 
  if descricao  == '' :
    print("Informe uma descrição para o seu projeto")
    return False
  data = ''
  hora = ''
  pri = ''
  cont = ''
  proj = ''
  for i in extras:
    if dataValida(i):
      data = i
    elif horaValida(i):
      hora = i
    elif prioridadeValida(i):
      pri = i
    elif contextoValido(i):
      cont = i
    elif projetoValido(i):
      proj = i
  novaAtividade = data+" "+hora+" "+pri+" "+descricao+" "+cont+" "+proj 
  # Escreve no TODO_FILE. 
  try: 
    fp = open(TODO_FILE, 'a')
    fp.write(novaAtividade + "\n")
    fp.close()
  except IOError as err:
    print("Não foi possível escrever para o arquivo " + TODO_FILE)
    print(err)
    return False
  return True
# Valida a prioridade.
def prioridadeValida(prioridade):
  pris = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
  if len(prioridade) == 3 and prioridade[0] == "(" and prioridade[2] == ")" and prioridade[1] in pris:
    return True
  return False
def horaValida2(horaMin) :
  if len(horaMin) != 6 or not soDigitos(horaMin[0:2]+horaMin[3:5]):
    return False
  else:
    hora = horaMin[0]+horaMin[1]
    minut = horaMin[3]+horaMin[4]
    if hora < '00' or hora > '23':
        return False
    if minut < '00' or minut > '59':
        return False
    return True
def horaValida(horaMin) :
  if len(horaMin) != 4 or not soDigitos(horaMin):
    return False
  else:
    hora = horaMin[0]+horaMin[1]
    minut = horaMin[2]+horaMin[3]
    if hora < '00' or hora > '23':
        return False
    if minut < '00' or minut > '59':
        return False
    return True
def dataValida(data) :
  mes = {}
  mes['01'] = ['31']
  mes['02'] = ['29']
  mes['03'] = ['31']
  mes['04'] = ['30']
  mes['05'] = ['31']
  mes['06'] = ['30']
  mes['07'] = ['31']
  mes['08'] = ['31']
  mes['09'] = ['30']
  mes['10'] = ['31']
  mes['11'] = ['30']
  mes['12'] = ['31']
  if len(data) != 8 or not soDigitos(data):
    return False
  else:
    dia = data[0]+data[1]
    mesd = data[2]+data[3]
    ano = data[4]+data[5]+data[6]+data[7]
    if dia < "01" or dia > mes[mesd][0]:
      return False
    elif mesd < "01" or mesd > "12":
      return False
    elif ano < "0001":
      return False
  return True
def dataValida2(data) :
  mes = {}
  mes['01'] = ['31']
  mes['02'] = ['29']
  mes['03'] = ['31']
  mes['04'] = ['30']
  mes['05'] = ['31']
  mes['06'] = ['30']
  mes['07'] = ['31']
  mes['08'] = ['31']
  mes['09'] = ['30']
  mes['10'] = ['31']
  mes['11'] = ['30']
  mes['12'] = ['31']
  if len(data) != 10 or not soDigitos(data[:2]+data[3:5]+data[6:]):
    return False
  else:
    dia = data[0]+data[1]
    mesd = data[3]+data[4]
    ano = data[6]+data[7]+data[8]+data[9]
    if dia < "01" or dia > mes[mesd][0]:
      return False
    elif mesd < "01" or mesd > "12":
      return False
    elif ano < "0001":
      return False
  return True
# Valida que o string do projeto está no formato correto. 
def projetoValido(proj):
  if len(proj) >= 2 and proj[0] == "+":
    return True
  return False
# Valida que o string do contexto está no formato correto. 
def contextoValido(cont):
  if len(cont) >= 2 and cont[0] == "@":
    return True
  return False

def soDigitos(numero) :
  if type(numero) != str :
    return False
  for x in numero :
    if x < '0' or x > '9' :
      return False
  return True 
def organizar(linhas):
  # Linhas será uma lista do texto em .readlines()
  itens = []
  for l in linhas:
    data = '' 
    hora = ''
    prioridade = ''
    desc = ''
    contexto = ''
    projeto = ''
    l = l.strip() # remove espaços em branco e quebras de linha do começo e do fim
    tokens = l.split() # quebra o string em palavras 
    for l in tokens:   
      if dataValida(l) and data == '':
         data = l
      elif horaValida(l) and hora == '':
         hora = l
      elif prioridadeValida(l) and prioridade == '':
         prioridade = l
      elif contextoValido(l) and contexto == '':
         contexto = l
      elif projetoValido(l) and projeto == '':
         projeto = l
      else:
        if l != " ":
           desc += l+" "
    itens.append((desc,(data, hora, prioridade, contexto, projeto)))
  return itens
def organizar2(linhas):
  # Linhas será uma lista do texto em .readlines()
  itens = []
  for l in linhas:
    data = '' 
    hora = ''
    prioridade = ''
    desc = ''
    contexto = ''
    projeto = ''
    desc2 = ''
    l = l.strip() # remove espaços em branco e quebras de linha do começo e do fim
    tokens = l.split() # quebra o string em palavras
    for l in tokens:
      if dataValida(tokens[0]) or horaValida(tokens[0]) or prioridadeValida(tokens[0]):
        if dataValida(l) and data == '':
          data = l[0]+l[1]+"/"+l[2]+l[3]+"/"+l[4]+l[5]+l[6]+l[7]
        elif horaValida(l) and hora == '':
          hora = l[0]+l[1]+"h"+l[2]+l[3]+"m"
        elif prioridadeValida(l) and prioridade == '':
          prioridade = l
        elif contextoValido(l):
          if contexto == '':
            contexto = l
          else:
            desc2 += l
        elif projetoValido(l):
          if projeto == '':
            projeto = l
          else:
            desc2 += l 
        else:
          if l != " ":
            desc += l+" "
      else:
        desc += l+" "
    itens.append(((data, hora, prioridade), desc, (contexto, projeto)))   
  return itens
def listar(texto): 
  prio = ["A", "B", "C", "D", "a","b", "c", "d"]
  cores = [RED, BLUE, CYAN, GREEN, YELLOW]
  try:
    agenda = open(TODO_FILE, "r")
    texto = agenda.readlines()
  except:
    agenda = open(TODO_FILE, "a+")
    texto = agenda.readlines()
  agenda.close()
  itens = organizar2(texto)
  itens = ordenarPorDataHora(itens)
  itens = ordenarPorPrioridade(itens)
  cores = [BLUE, CYAN, GREEN, YELLOW, REVERSE]
  cores1 = [BLUE, CYAN]
  cor = random.choice(cores)
  i = 1
  for x in itens:
    if prioridadeValida(x[0][2]) and (x[0][2] == "(a)" or x[0][2] == "(A)"):
      stringnum = str(i)
      tuples = " ".join(x[0])+" "
      tuplesf = x[1]+" "+" ".join(x[2])
      mostrar = stringnum+" "+tuples+tuplesf
      printCores(mostrar, RED+BOLD)
      i += 1
    elif prioridadeValida(x[0][2]) and (x[0][2] == "(b)" or x[0][2] == "(B)"):
        stringnum = str(i)
        tuples = " ".join(x[0])+" "
        tuplesf = x[1]+" "+" ".join(x[2])
        mostrar = stringnum+" "+tuples+tuplesf
        printCores(mostrar, BLUE)
        i += 1
    elif prioridadeValida(x[0][2]) and (x[0][2] == "(c)" or x[0][2] == "(C)"):
        stringnum = str(i)
        tuples = " ".join(x[0])+" "
        tuplesf = x[1]+" "+" ".join(x[2])
        mostrar = stringnum+" "+tuples+tuplesf
        printCores(mostrar, YELLOW)
        i += 1
    elif prioridadeValida(x[0][2]) and (x[0][2] == "(d)" or x[0][2] == "(D)"):
        stringnum = str(i)
        tuples = " ".join(x[0])+" "
        tuplesf = x[1]+" "+" ".join(x[2])
        mostrar = stringnum+" "+tuples+tuplesf
        printCores(mostrar, GREEN)
        i += 1  
    else:
      print(i," ".join(x[0])," ",x[1]," ".join(x[2]))
      i += 1 
  return itens
def ordenarPorDataHora(lista):
  i = 0
  try:
    while i < len(lista)-1:
      while lista[i][0][1] == '' and lista[i+1][0][1] != '':
        lista[i], lista[i+1] = lista[i+1], lista[i]
        i = 0
      i += 1
  except:
      ''
  x = 0
  while x < len(lista) - 1:
    try:
      while ((int(lista[x][0][1][0]+lista[x][0][1][1])*3600)+(int(lista[x][0][1][3]+lista[x][0][1][4])*60)) > ((int(lista[x+1][0][1][0]+lista[x+1][0][1][1])*3600)+(int(lista[x+1][0][1][3]+lista[x+1][0][1][4])*60)):
        lista[x], lista[x+1] = lista[x+1], lista[x]
        x = 0
      x += 1 
    except:
      x = 1000000000000000000000    
  i = 0
  try:
    while i < len(lista)-1:
      while lista[i][0][0] == '' and lista[i+1][0][0] != '':
        lista[i], lista[i+1] = lista[i+1], lista[i]
        i = 0
      i += 1
  except:
     ''
  x = 0
  while x < len(lista) - 1:
     try:
       while ((int(lista[x][0][0][6]+lista[x][0][0][7]+lista[x][0][0][8]+lista[x][0][0][9])*365) + (int(lista[x][0][0][3]+lista[x][0][0][4])*30) + (int(lista[x][0][0][0]+lista[x][0][0][1]))) > ((int(lista[x+1][0][0][6]+lista[x+1][0][0][7]+lista[x+1][0][0][8]+lista[x+1][0][0][9])*365) + (int(lista[x+1][0][0][3]+lista[x+1][0][0][4])*30) + (int(lista[x+1][0][0][0]+lista[x+1][0][0][1]))):
         lista[x], lista[x+1] = lista[x+1], lista[x]
         x = 0
       x += 1
     except:
       x = 100000000000000000000
  return lista
def ordenarPorPrioridade(lista):
  dic = {}
  dic["A"] = 26
  dic["B"] = 25
  dic["C"] = 24
  dic["D"] = 23
  dic["E"] = 22
  dic["F"] = 21
  dic["G"] = 20
  dic["H"] = 19
  dic["I"] = 18
  dic["J"] = 17
  dic["K"] = 16
  dic["L"] = 15
  dic["M"] = 14
  dic["N"] = 13
  dic["O"] = 12
  dic["P"] = 11
  dic["Q"] = 10
  dic["R"] = 9
  dic["S"] = 8
  dic["T"] = 7
  dic["U"] = 6
  dic["V"] = 5
  dic["X"] = 4
  dic["W"] = 3
  dic["Y"] = 2
  dic["Z"] = 1
  i = 0
  try:
    while i < len(lista)-1:
      while lista[i][0][2] == '' and lista[i+1][0][2] != '':
        lista[i], lista[i+1] = lista[i+1], lista[i]
        i = 0
      i += 1
      if lista[i][0][2] == '' and lista[i+1][0][2] == '':
        i += 1
  except:
    ""    
  i = 0
  while i < len(lista)-1:
    try:
      while dic[lista[i][0][2][1].upper()] < dic[lista[i+1][0][2][1].upper()]:
        lista[i], lista[i+1] = lista[i+1], lista[i]
        i = 0
      i += 1
    except:
      i = 10000000000000000000
  return lista
def fazer(chave):
  chaves = int(chave)
  dic = {}
  agenda = open(TODO_FILE, "r")
  texto = agenda.readlines()
  agenda.close()
  itens = organizar2(texto)
  itens = ordenarPorDataHora(itens)
  itens = ordenarPorPrioridade(itens)
  i = 1
  for x in itens:
    dic[i] = x
    i += 1
  txt2 = open(ARCHIVE_FILE, "a")
  txt = open(TODO_FILE, "w")
  fazer = dic[chaves]
  del dic[chaves]
  for x in dic:
    linha2 = dic[x][0][0]+" "+dic[x][0][1]+" "+dic[x][0][2]+" "+dic[x][1]+dic[x][2][0]+" "+dic[x][2][1]
    lista2 = linha2.split()
    data = ''
    hora = ''
    prioridade = ''
    cont = ''
    proj = ''
    desc = ''
    desc2 = ''
    for y in lista2:
      if dataValida2(y) and data == '':
        data = y[0]+y[1]+y[3]+y[4]+y[6]+y[7]+y[8]+y[9]
      elif horaValida2(y) and hora == '':
        hora = y[0]+y[1]+y[3]+y[4]
      elif prioridadeValida(y) and prioridade == '':
        prioridade = y
      elif contextoValido(y):
        if cont == '':
          cont = y
        else:
          desc2 += y
      elif projetoValido(y):
        if proj == '':
          proj = y
        else:
          desc2 += y
      else:
        desc += y+" "
    if desc != '':
      txt.write(data+" "+hora+" "+prioridade+" "+desc+" "+cont+" "+proj+"\n")
  linha = fazer[0][0]+" "+fazer[0][1]+" "+fazer[0][2]+" "+fazer[1]+fazer[2][0]+" "+fazer[2][1]
  lista = linha.split()
  data = ''
  hora = ''
  prioridade = ''
  cont = ''
  proj = ''
  desc = ''
  desc2 = ''
  for i in lista:
    if dataValida2(i) and data == '':
      data = i[0]+i[1]+i[3]+i[4]+i[6]+i[7]+i[8]+i[9]
    elif horaValida2(i) and hora == '':
      hora = i[0]+i[1]+i[3]+i[4]
    elif prioridadeValida(i) and prioridade == '':
      prioridade = i
    elif contextoValido(i):
      if cont == '':
        cont = i
      else:
        desc2 += i
    elif projetoValido(i):
      if proj == '':
        proj = i
      else:
        desc2 += i
    else:
      desc += i+" "
  if desc != '':
    txt2.write(data+" "+hora+" "+prioridade+" "+desc+" "+cont+" "+proj+"\n")
  txt.close()
  txt2.close()
  listar(TODO_FILE)
  return 
def remover(chave):
  chaves = int(chave)
  dic = {}
  agenda = open(TODO_FILE, "r")
  texto = agenda.readlines()
  agenda.close()
  itens = organizar2(texto)
  itens = ordenarPorDataHora(itens)
  itens = ordenarPorPrioridade(itens)
  index = 1
  for x in itens:
    dic[index] = x
    index += 1
  try:
    del dic[chaves]
  except:
    print("chave inexistente")
    pass  
  txt = open(TODO_FILE, "w")
  for x in dic:
    linha = dic[x][0][0]+" "+dic[x][0][1]+" "+dic[x][0][2]+" "+dic[x][1]+dic[x][2][0]+" "+dic[x][2][1]
    lista = linha.split()
    data = ''
    hora = ''
    prioridade = ''
    cont = ''
    proj = ''
    desc = ''
    for y in lista:
      if dataValida2(y) and data == '':
        data = y[0]+y[1]+y[3]+y[4]+y[6]+y[7]+y[8]+y[9]
      elif horaValida2(y) and hora == '':
        hora = y[0]+y[1]+y[3]+y[4]
      elif prioridadeValida(y) and prioridade == '':
        prioridade = y
      elif contextoValido(y) and cont == '':
        cont = y
      elif projetoValido(y) and proj == '':
        proj = y
      else:
        desc += y+" "
    if desc != '':
      txt.write(data+" "+hora+" "+prioridade+" "+desc+" "+cont+" "+proj+"\n")
  return
def priorizar(num, pricomando):

  chaves = int(num)
  dic = {}
  agenda = open(TODO_FILE, "r")
  texto = agenda.readlines()
  agenda.close()
  itens = organizar2(texto)
  itens = ordenarPorDataHora(itens)
  itens = ordenarPorPrioridade(itens)
  i = 1
  for x in itens:
    dic[i] = x
    i += 1
  txt = open(TODO_FILE, "w")
  
  for x in dic:
    if x == chaves and prioridadeValida("("+pricomando+")"):
      linha = dic[x][0][0]+" "+dic[x][0][1]+" "+dic[x][0][2]+" "+dic[x][1]+" "+dic[x][2][0]+" "+dic[x][2][1]
      lista = linha.split()
      data = ''
      hora = ''
      prioridade = ''
      cont = ''
      proj = ''
      desc = ''
      desc2 = ''
      for y in lista:
        if dataValida2(y) and data == '':
          data = y[0]+y[1]+y[3]+y[4]+y[6]+y[7]+y[8]+y[9]
        elif horaValida2(y) and hora == '':
          hora = y[0]+y[1]+y[3]+y[4]
        elif prioridadeValida(y):
          desc2 += y
        elif contextoValido(y):
          if cont == '':
            cont = y
          else:
            desc2 += y
        elif projetoValido(y):
          if proj == '':
            proj = y
          else:
            desc2 += y
        else:
          desc += y+" "
      if desc != '':
        txt.write(data+" "+hora+" "+"("+pricomando+")"+" "+desc+" "+cont+" "+proj+"\n")
    else:
      linha = dic[x][0][0]+" "+dic[x][0][1]+" "+dic[x][0][2]+" "+dic[x][1]+" "+dic[x][2][0]+" "+dic[x][2][1]
      lista = linha.split()
      
      data = ''
      hora = ''
      prioridade = ''
      cont = ''
      proj = ''
      desc = ''
      desc2 = ''
      for y in lista:
        if dataValida2(y) and data == '':
          data = y[0]+y[1]+y[3]+y[4]+y[6]+y[7]+y[8]+y[9]
        elif horaValida2(y) and hora == '':
          hora = y[0]+y[1]+y[3]+y[4]
        elif prioridadeValida(y):
          if prioridade == '':
            prioridade = y
          else:
            desc2 += y
        elif contextoValido(y):
          if cont == '':
            cont = y
          else:
            desc2 += y
        elif projetoValido(y) and proj == '':
          proj = y
        else:
          desc += y+" "
      if desc != '':
        txt.write(data+" "+hora+" "+prioridade+" "+desc+" "+cont+" "+proj+"\n")
  txt.close()  
  listar(TODO_FILE)
  return  

def processarComandos(comandos) :
  if comandos[1] == ADICIONAR:
    comandos.pop(0) # remove 'agenda.py'
    comandos.pop(0) # remove 'adicionar'
    itemParaAdicionar = organizar([" ".join(comandos)])[0]
    adicionar(itemParaAdicionar[0], itemParaAdicionar[1]) # novos itens não têm prioridade
  elif comandos[1] == LISTAR:
    
    return listar(TODO_FILE)

  elif comandos[1] == REMOVER:

    return remover(comandos[2])

  elif comandos[1] == FAZER:
    
    return fazer(comandos[2])    

  elif comandos[1] == PRIORIZAR:

    return priorizar(comandos[2], comandos[3])

  else :
    print("Comando inválido.")
  return   
  
processarComandos(sys.argv)

#Matheus Andrde Gomes
#Information Systems
#mag2@cin.ufpe.br
#P1
