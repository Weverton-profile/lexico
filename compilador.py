import re
import string

def identificadores(entrada, estado):
    for i in range(len(entrada)):
        caractere = entrada[i]
        if estado != -1:
            if estado == 0:
                if (caractere in string.ascii_lowercase or 
                    caractere in string.ascii_uppercase):
                    estado = 1
                else:
                    estado = -1
            elif estado == 1:
                if (caractere in [str(x) for x in range(0, 9)] or 
                    caractere in string.ascii_lowercase):
                    estado = 2
                elif caractere == "_":
                    estado = 3
                elif caractere == "$":
                    estado = 4
                else:
                    estado = -1
            elif estado == 3:
                if caractere in string.ascii_lowercase or caractere in [str(x) for x in range(0, 9)]:
                    estado = 2
            elif estado == 4:
                if caractere in string.ascii_lowercase:
                    estado = 2
                else:
                    estado = -1
            elif estado == 2:
                if (caractere in [str(x) for x in range(0, 9)] or 
                    caractere in string.ascii_lowercase):
                    estado = 2
                elif caractere == "$":
                    estado = 4
                else:
                    estado = -1
        else:
            break
    if estado == 2 or estado == 1:
        return True
    else:
        return False

def comentarios(entrada, estado):
    for i in range(len(entrada)):
        caractere = entrada[i]
        if estado != -1:
            if estado == 0:
                if caractere == "@":
                    estado = 5
                elif caractere == "/":
                    estado = 7
                else:
                    estado = -1
            elif estado == 5:
                if caractere == "@":
                    estado = 6
                else:
                    estado = -1
            elif estado == 6:
                if i + 1 == len(entrada):
                    estado = 25
            elif estado == 7:
                if caractere == "/":
                    estado = 8
                elif caractere == "*":
                    estado = 22
                else:
                    estado = -1
            elif estado == 8:
                estado = 9
            elif estado == 9:
                if caractere == "/":
                    estado = 10
            elif estado == 10:
                if caractere == "/":
                    estado = 25
                else:
                    estado = 9
            elif estado == 22:
                estado = 23
            elif estado == 23:
                if caractere == "*":
                    estado = 24
                else:
                    estado = 23
            elif estado == 24:
                if caractere == "/":
                    estado = 25
                else:
                    estado = 23
        else:
            break
    if estado == 5 or estado == 25 or estado == 7:
        return True
    else:
        return False

def digitos(entrada, estado):
    for i in range(len(entrada)):
        caractere = entrada[i]
        if estado != -1:
            if estado == 0:
                if caractere == "-":
                    estado = 11
                elif caractere in [str(x) for x in range(0, 9)]:
                    estado = 12
                else:
                    estado = -1
            elif estado == 11:
                if caractere in [str(x) for x in range(0, 9)]:
                    estado = 12
                else:
                    estado = -1
            elif estado == 12:
                if caractere in [str(x) for x in range(0, 9)]:
                    estado = 12
                elif caractere == ",":
                    estado = 13
                else:
                    estado = -1
            elif estado == 13:
                if caractere in [str(x) for x in range(0, 9)]:
                    estado = 14
                else:
                    estado = -1 
            elif estado == 14:
                if caractere in [str(x) for x in range(0, 9)]:
                    estado = 14
                else:
                    estado = -1
        else:
            break     
    if estado == 11 or estado == 12 or estado == 14:
        return True
    else:
        return False

def simbolo_especial(entrada, estado, simbolos_especiais):
    for i in range(len(entrada)):
        caractere = entrada[i]
        if estado != -1:
            if estado == 0:
                if caractere in simbolos_especiais:
                    estado = 15
                elif caractere == "<":
                    estado = 16
                elif caractere == ">":
                    estado = 17
                elif caractere == "=":
                    estado = 21
                elif caractere == ":":
                    estado = 18
                elif caractere == "*":
                    estado = 19
                elif caractere == "+":
                    estado = 20
                else:
                    estado = -1
            elif estado == 16:
                if caractere == "=":
                    estado = 21
                elif caractere == ">":
                    estado = 21
                else:
                    estado = -1
            elif estado == 17:
                if caractere == "=":
                    estado = 21
                else:
                    estado = -1
            elif estado == 18:
                if caractere == "=":
                    estado = 21
                else:
                    estado = -1
            elif estado == 19:
                if caractere == "=":
                    estado = 21
                else:
                    estado = -1
            elif estado == 20:
                if caractere == "=":
                    estado = 21
                else:
                    estado = -1
        else:
            break
    if (estado == 15 or estado == 16 or estado == 17 or 
        estado == 18 or estado == 19 or estado == 20 or estado == 21):
        return True
    else:
        return False

def analisador_lexico(linhas):
    palavras_reservadas = ['program', 'if', 'then', 'else', 'while', 'do', 'until', 'repeat', 'int', 'double', 'char', 'case', 'switch', 'end', 'procedure', 'function', 'for', 'begin']
    tabela_de_simbolos = [';', ',', '.', '(', ')', '{', '}', '+', '-', '*', '<', '>', '=', ':', '/', '@', ':=', '>=', '<=', '*=', '+=', '/*', '*/', '//', '@@']

    padrao = r'//.*?\n|/\*.*?\*/|@@.*?\n|\w+|[^\w\s]+'
    tokens = re.findall(padrao, linhas, re.DOTALL)

    lexemes = []
    comentario = False
    for token in tokens:
        if comentario:
            if token.endswith('\n'):
                comentario = False
            continue
        elif token.startswith('//') or token.startswith('@@'):
            continue
        elif token.startswith('/*'):
            if '*/' not in token:
                comentario = True
            continue
        elif token.endswith('*/'):
            continue
        elif token in palavras_reservadas:
            lexemes.append(('PALAVRA_RESERVADA', token))
        elif token in tabela_de_simbolos:
            lexemes.append(('SIMBOLO', token))
        elif identificadores(token, 0):
            lexemes.append(('IDENTIFICADOR', token))
        elif comentarios(token, 0):
            lexemes.append(('COMENTARIO', token))
        elif digitos(token, 0):
            lexemes.append(('DIGITO', token))
        elif simbolo_especial(token, 0, tabela_de_simbolos):
            lexemes.append(('SIMBOLO_ESPECIAL', token))

    return lexemes

arquivo = open("padrao.txt", "r")

linhas = arquivo.read()

arquivo.close()

result = analisador_lexico(linhas)
for token, lexeme in result:
    print(f'<{token}, {lexeme}>')
