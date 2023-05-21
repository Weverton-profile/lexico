import string

palavras_reservadas = ['program', 'if', 'then', 'else', 'while', 'do', 'until', 'repeat', 'int', 'double', 'char', 'case', 'switch', 'end', 'procedure', 'function', 'for', 'begin']

def geral():
    buffer = ''
    comentario = False
    estado = 0
    mensagem = ''
    linha_erro = 0
    with open('teste.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
    
    for linha in linhas:
        if estado != -1:
            i = 0
            linha_erro += 1
            while i < len(linha):
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
                        elif token == ' ' or token == '\n':
                            pass
                        else:
                            mensagem = f'Erro linha {linha_erro}, caractere não reconhecido "{token}".'
                            estado = -1
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
                            print(f'<IDENTIFICADOR, {buffer}>')
                            buffer = ''
                            estado = 0
                            i -= 1
                    elif estado == 3:
                        if token in string.ascii_lowercase or token in [str(x) for x in range(0, 9)]:
                            buffer += token
                            estado = 2
                        else:
                            mensagem = f'Erro linha {linha_erro}, você tem "{buffer}". "{buffer[-1]}" não pode finalizar um identificador.'
                            estado = -1
                    elif estado == 4:
                        if token in string.ascii_lowercase:
                            buffer += token
                            estado = 2
                        else:
                            mensagem = f'Erro linha {linha_erro}, você tem "{buffer}". "{buffer[-1]}" não pode finalizar um identificador.'
                            estado = -1
                    elif estado == 2:
                        if (token in [str(x) for x in range(0, 9)] or 
                            token in string.ascii_lowercase):
                            buffer += token
                            estado = 2
                            if i + 1 == len(linha):
                                if buffer in palavras_reservadas:
                                    print(f'<PALAVRA_RESERVADA, {buffer}>')
                                else:
                                    print(f'<IDENTIFICADOR, {buffer}>')
                                buffer = ''
                        elif token == "$":
                            buffer += token
                            estado = 4
                        else:
                            if buffer in palavras_reservadas:
                                print(f'<PALAVRA_RESERVADA, {buffer}>')
                            else:
                                print(f'<IDENTIFICADOR, {buffer}>')
                            buffer = ''
                            estado = 0
                            i -= 1
                    elif estado == 5:
                        if token == "@":
                            estado = 6
                        else:
                            print(f'<SIMBOLO_ESPECIAL, {buffer}>')
                            buffer = ''
                            estado = 0
                            i -= 1
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
                            print(f'<SIMBOLO_ESPECIAL, {buffer}>')
                            buffer = ''
                            estado = 0
                            i -= 1
                    elif estado == 11:
                        if token in [str(x) for x in range(0, 9)]:
                            buffer += token
                            estado = 12
                        else:
                            print(f'<SIMBOLO_ESPECIAL, {buffer}>')
                            buffer = ''
                            estado = 0
                            i -= 1
                    elif estado == 12:
                        if token in [str(x) for x in range(0, 9)]:
                            buffer += token
                            estado = 12
                        elif token == ",":
                            buffer += token
                            estado = 13
                        else:
                            print(f'<DIGITO, {buffer}>')
                            buffer = ''
                            estado = 0
                            i -= 1
                    elif estado == 13:
                        if token in [str(x) for x in range(0, 9)]:
                            buffer += token
                            estado = 14
                        else:
                            mensagem = f'Erro linha {linha_erro}, você tem "{buffer}". "{buffer[-1]}" não pode finalizar um dígito.'
                            estado = -1
                    elif estado == 14:
                        if token in [str(x) for x in range(0, 9)]:
                            buffer += token
                            estado = 14
                            if i + 1 == len(linha):
                                print(f'<DIGITO, {buffer}>')
                        else:
                            print(f'<DIGITO, {buffer}>')
                            buffer = ''
                            estado = 0
                            i -= 1
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
                            print(f'<SIMBOLO_ESPECIAL, {buffer}>')
                            buffer = ''
                            estado = 0
                            i -= 1
                    elif estado == 17:
                        if token == "=":
                            buffer += token
                            print(f'<SIMBOLO_ESPECIAL, {buffer}>')
                            buffer = ''
                            estado = 0
                        else:
                            print(f'<SIMBOLO_ESPECIAL, {buffer}>')
                            buffer = ''
                            estado = 0
                            i -= 1
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
                
                i += 1
        else:
            print(mensagem)
            break