import string

palavras_reservadas = ['program', 'if', 'then', 'else', 'while', 'do', 'until', 'repeat', 'int', 'double', 'char', 'case', 'switch', 'end', 'procedure', 'function', 'for', 'begin']

def geral(arquivo):
    token = ''
    comentario = False
    estado = 0
    mensagem = ''
    linha_erro = 0
    with open(arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
    
    for linha in linhas:
        if estado != -1:
            i = 0
            linha_erro += 1
            if '\n' not in linha:
              linha += '\n'
            while i < len(linha):
                caractere = linha[i]
                if comentario == False:
                    if estado == 0:
                        if (caractere in string.ascii_lowercase or 
                            caractere in string.ascii_uppercase):
                            token += caractere
                            estado = 1
                        elif caractere == "-":
                            token += caractere
                            estado = 11
                        elif caractere in [str(x) for x in range(0, 9)]:
                            token += caractere
                            estado = 12
                        elif caractere in [';', ',', '.', '(', ')', '{', '}', '=']:
                            print(f'<SIMBOLO_ESPECIAL, {caractere}>')
                            estado = 0
                        elif caractere == "<":
                            token += caractere
                            estado = 16
                        elif caractere in ['>', ':', '*', '+']:
                            token += caractere
                            estado = 17
                        elif caractere == "@":
                            token += caractere
                            estado = 5
                        elif caractere == "/":
                            token += caractere
                            estado = 7
                        elif caractere == '\t' or caractere == ' ' or caractere == '\n':
                            pass
                        else:
                            mensagem = f'Erro linha {linha_erro}, caractere não reconhecido "{caractere}".'
                            estado = -1
                    elif estado == 1:
                        if (caractere in [str(x) for x in range(0, 9)] or 
                            caractere in string.ascii_lowercase):
                            token += caractere
                            estado = 2
                        elif caractere == "_":
                            token += caractere
                            estado = 3
                        elif caractere == "$":
                            token += caractere
                            estado = 4
                        else:
                            print(f'<IDENTIFICADOR, {token}>')
                            token = ''
                            estado = 0
                            i -= 1
                    elif estado == 3:
                        if caractere in string.ascii_lowercase or caractere in [str(x) for x in range(0, 9)]:
                            token += caractere
                            estado = 2
                        else:
                            mensagem = f'Erro linha {linha_erro}, você tem "{token}". "{token[-1]}" não pode finalizar um identificador.'
                            estado = -1
                    elif estado == 4:
                        if caractere in string.ascii_lowercase:
                            token += caractere
                            estado = 2
                        else:
                            mensagem = f'Erro linha {linha_erro}, você tem "{token}". "{token[-1]}" não pode finalizar um identificador.'
                            estado = -1
                    elif estado == 2:
                        if (caractere in [str(x) for x in range(0, 9)] or 
                            caractere in string.ascii_lowercase):
                            token += caractere
                            estado = 2
                            if i + 1 == len(linha):
                                if token in palavras_reservadas:
                                    print(f'<PALAVRA_RESERVADA, {token}>')
                                else:
                                    print(f'<IDENTIFICADOR, {token}>')
                                token = ''
                        elif caractere == "$":
                            token += caractere
                            estado = 4
                        else:
                            if token in palavras_reservadas:
                                print(f'<PALAVRA_RESERVADA, {token}>')
                            else:
                                print(f'<IDENTIFICADOR, {token}>')
                            token = ''
                            estado = 0
                            i -= 1
                    elif estado == 5:
                        if caractere == "@":
                            estado = 6
                        else:
                            print(f'<SIMBOLO_ESPECIAL, {token}>')
                            token = ''
                            estado = 0
                            i -= 1
                    elif estado == 6:
                        token = ''
                        if caractere == '\n':
                            estado = 0
                    elif estado == 7:
                        if caractere == "/":
                            token += caractere
                            comentario = True
                            token = ''
                            estado = 8
                        elif caractere == "*":
                            token += caractere
                            comentario = True
                            token = ''
                            estado = 22
                        else:
                            print(f'<SIMBOLO_ESPECIAL, {token}>')
                            token = ''
                            estado = 0
                            i -= 1
                    elif estado == 11:
                        if caractere in [str(x) for x in range(0, 9)]:
                            token += caractere
                            estado = 12
                        else:
                            print(f'<SIMBOLO_ESPECIAL, {token}>')
                            token = ''
                            estado = 0
                            i -= 1
                    elif estado == 12:
                        if caractere in [str(x) for x in range(0, 9)]:
                            token += caractere
                            estado = 12
                        elif caractere == ",":
                            token += caractere
                            estado = 13
                        else:
                            print(f'<DIGITO, {token}>')
                            token = ''
                            estado = 0
                            i -= 1
                    elif estado == 13:
                        if caractere in [str(x) for x in range(0, 9)]:
                            token += caractere
                            estado = 14
                        else:
                            mensagem = f'Erro linha {linha_erro}, você tem "{token}". "{token[-1]}" não pode finalizar um dígito.'
                            estado = -1
                    elif estado == 14:
                        if caractere in [str(x) for x in range(0, 9)]:
                            token += caractere
                            estado = 14
                            if i + 1 == len(linha):
                                print(f'<DIGITO, {token}>')
                        else:
                            print(f'<DIGITO, {token}>')
                            token = ''
                            estado = 0
                            i -= 1
                    elif estado == 16:
                        if caractere == "=":
                            token += caractere
                            print(f'<SIMBOLO_ESPECIAL, {token}>')
                            token = ''
                            estado = 0
                        elif caractere == ">":
                            token += caractere
                            print(f'<SIMBOLO_ESPECIAL, {token}>')
                            token = ''
                            estado = 0
                        else:
                            print(f'<SIMBOLO_ESPECIAL, {token}>')
                            token = ''
                            estado = 0
                            i -= 1
                    elif estado == 17:
                        if caractere == "=":
                            token += caractere
                            print(f'<SIMBOLO_ESPECIAL, {token}>')
                            token = ''
                            estado = 0
                        else:
                            print(f'<SIMBOLO_ESPECIAL, {token}>')
                            token = ''
                            estado = 0
                            i -= 1
                else:
                    if estado == 8:
                        if caractere == "/":
                            estado = 9
                    elif estado == 9:
                        if caractere == "/":
                            comentario = False
                            estado = 0
                    elif estado == 22:
                        if caractere == "*":
                            estado = 23
                    elif estado == 23:
                        if caractere == "/":
                            comentario = False
                            estado = 0
                i += 1
        else:
            break
    if mensagem != '':
      print(mensagem)

geral("teste.txt")