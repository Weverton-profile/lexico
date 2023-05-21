import string

palavras_reservadas = ['program', 'if', 'then', 'else', 'while', 'do', 'until', 'repeat', 'int', 'double', 'char', 'case', 'switch', 'end', 'procedure', 'function', 'for', 'begin']

def geral():
  tokens = []
  buffer = ''
  comentario = False
  estado = 0
  with open('teste.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
  for linha in linhas:
    for i in range(len(linha)):
      token = linha[i]
      if comentario == False:
        if estado == 0:
          if (token in string.ascii_lowercase or 
              token in string.ascii_uppercase):
            buffer += token
            estado = 1
          elif token == "-":
            buffer += token
            estado = 11
          elif token in [str(x) for x in range(0, 9)]:
            buffer += token
            estado = 12
          elif token in [';', ',', '.', '(', ')', '{', '}', '=']:
            print(f'<SIMBOLO_ESPECIAL, {token}>')
            estado = 0
          elif token == "<":
            buffer += token
            estado = 16
          elif token in ['>', ':', '*', '+']:
            buffer += token
            estado = 17
          elif token == "@":
            buffer += token
            estado = 5
          elif token == "/":
            buffer += token
            estado = 7
          else:
            if token == ' ' or token == '\n':
              continue
            else:
              print(f'Erro, caractere não reconhecido: "{token}".')
              break
        elif estado == 1:
          if (token in [str(x) for x in range(0, 9)] or 
              token in string.ascii_lowercase):
              buffer += token
              estado = 2
          elif token == "_":
            buffer += token
            estado = 3
          elif token == "$":
            buffer += token
            estado = 4
          else:
            if token == ' ' or token == '\n':
              print(f'<IDENTIFICADOR, {buffer}>')
              buffer = ''
              estado = 0
            else:
              print(f'Erro, ocorrencia de um caractere inesperado: "{token}".')
              break
        elif estado == 3:
          if token in string.ascii_lowercase or token in [str(x) for x in range(0, 9)]:
            buffer += token
            estado = 2
          elif token == ' ' or token == '\n':
            print(f'Erro, você tem "{buffer}", "{buffer[-1]}" não pode finalizar um identificador, complete com o que é esperado.')
            break
          else:
            print(f'Erro, ocorrencia de um caractere inesperado: "{token}".')
            break
        elif estado == 4:
          if  token in string.ascii_lowercase:
            buffer += token
            estado = 2
          elif token == ' ' or token == '\n':
            print(f'Erro, você tem "{buffer}", "{buffer[-1]}" não pode finalizar um identificador, complete com o que é esperado.')
            break
          else:
            print(f'Erro, ocorrencia de um caractere inesperado: "{token}".')
            break
        elif estado == 2:
          if (token in [str(x) for x in range(0, 9)] or 
              token in string.ascii_lowercase):
            buffer += token
            estado = 2
          elif token == "$":
            buffer += token
            estado = 4
          else:
            if token == ' ' or token == '\n':
              if buffer in palavras_reservadas:
                print(f'<PALAVRA_RESERVADA, {buffer}>')
              else:
                print(f'<IDENTIFICADOR, {buffer}>')
              buffer = ''
              estado = 0
            else:
              print(f'Erro, ocorrencia de um caractere inesperado: "{token}".')
              break
        elif estado == 5:
          if token == "@":
            estado = 6
          else:
            if token == ' ' or token == '\n':
              print(f'<SIMBOLO_ESPECIAL, {buffer}>')
              buffer = ''
              estado = 0
            else:
              print(f'Erro, ocorrencia de um caractere inesperado: "{token}".')
              break
        elif estado == 6:
          buffer = ''
          if token == '\n':
            estado = 0
        elif estado == 7:
          if token == "/":
            buffer += token
            comentario = True
            buffer = ''
            estado = 8
          elif token == "*":
            buffer += token
            comentario = True
            buffer = ''
            estado = 22
          else:
            if token == ' ' or token == '\n':
              print(f'<SIMBOLO_ESPECIAL, {buffer}>')
              buffer = ''
              estado = 0
            else:
              print(f'Erro, ocorrencia de um caractere inesperado: "{token}".')
              break
        elif estado == 11:
          if token in [str(x) for x in range(0, 9)]:
            buffer += token
            estado = 12
          else:
            if token == ' ' or token == '\n':
              print(f'<SIMBOLO_ESPECIAL, {buffer}>')
              buffer = ''
              estado = 0
            else:
              print(f'Erro, ocorrencia de um caractere inesperado: "{token}".')
              break
        elif estado == 12:
          if token in [str(x) for x in range(0, 9)]:
            buffer += token
            estado = 12
          elif token == ",":
            buffer += token
            estado = 13
          else:
            if token == ' ' or token == '\n':
              print(f'<DIGITO, {buffer}>')
              buffer = ''
              estado = 0
            else:
              print(f'Erro, ocorrencia de um caractere inesperado: "{token}".')
              break
        elif estado == 13:
          if token in [str(x) for x in range(0, 9)]:
            buffer += token
            estado = 14
          else:
            if token == ' ' or token == '\n':
              print(f'Erro, você tem "{buffer}", "{buffer[-1]}" não pode finalizar um digito, complete com o que é esperado.')
              break
            else:
              print(f'Erro, ocorrencia de um caractere inesperado: "{token}".')
              break
        elif estado == 14:
          if token in [str(x) for x in range(0, 9)]:
            buffer += token
            estado = 14
          else:
            if token == ' ' or token == '\n':
              print(f'<DIGITO, {buffer}>')
              buffer = ''
              estado = 0
            else:
              print(f'Erro, ocorrencia de um caractere inesperado: "{token}".')
              break
        elif estado == 16:
          if token == "=":
            buffer += token
            print(f'<SIMBOLO_ESPECIAL, {buffer}>')
            buffer = ''
            estado = 0
          elif token == ">":
            buffer += token
            print(f'<SIMBOLO_ESPECIAL, {buffer}>')
            buffer = ''
            estado = 0
          else:
            if token == ' ' or token == '\n':
              print(f'<SIMBOLO_ESPECIAL, {buffer}>')
              buffer = ''
              estado = 0
            else:
              print(f'Erro, ocorrencia de um caractere inesperado: "{token}".')
              break
        elif estado == 17:
          if token == "=":
            buffer += token
            print(f'<SIMBOLO_ESPECIAL, {buffer}>')
            buffer = ''
            estado = 0
          else:
            if token == ' ' or token == '\n':
              print(f'<SIMBOLO_ESPECIAL, {buffer}>')
              buffer = ''
              estado = 0
            else:
              print(f'Erro, ocorrencia de um caractere inesperado: "{token}".')
              break
      else:
        if estado == 8:
          if token == "/":
            estado = 9
        elif estado == 9:
          if token == "/":
            comentario = False
            estado = 0
        elif estado == 22:
          if token == "*":
            estado = 23
        elif estado == 23:
          if token == "/":
            comentario = False
            estado = 0