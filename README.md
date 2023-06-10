🇧🇷 PT - BR

# Documentação do Código

Este código implementa um analisador léxico simples para reconhecimento de tokens em um arquivo de entrada. Ele identifica identificadores, palavras reservadas, dígitos e símbolos especiais.

## Função `geral(arquivo)`

Esta função recebe como entrada o nome de um arquivo e realiza a análise léxica do seu conteúdo.

### Parâmetros

- `arquivo` (str): O nome do arquivo a ser analisado.

### Variáveis

- `token` (str): Variável que armazena o token atual durante a análise.
- `comentario` (bool): Variável de controle que indica se o analisador está dentro de um comentário.
- `estado` (int): Variável que representa o estado atual do analisador léxico.
- `mensagem` (str): Variável para armazenar mensagens de erro, caso ocorram.
- `linha_erro` (int): Variável que registra o número da linha atual durante a análise.

### Comportamento

A função `geral` inicializa as variáveis necessárias para controlar o token atual, o estado, o controle de comentário, a mensagem de erro e o número da linha.

O código abre o arquivo especificado em modo de leitura (`'r'`) e lê todas as linhas do arquivo.

É feita uma iteração sobre cada linha do arquivo. Para cada caractere na linha, o analisador léxico verifica seu tipo e determina o próximo estado de acordo com a lógica de reconhecimento de tokens.

Durante a análise, diferentes tipos de tokens são identificados, como identificadores, palavras reservadas, dígitos e símbolos especiais.

Caso ocorra algum erro durante a análise, uma mensagem de erro é gerada, indicando a linha e o caractere que causaram o erro.

Após a análise de cada linha, o analisador léxico imprime os tokens identificados.

## Tokens Reconhecidos

O analisador léxico é capaz de reconhecer os seguintes tipos de tokens:

- Identificadores: Sequências de letras maiúsculas ou minúsculas, números, sublinhados (_) ou cifrão ($). Exemplo: `<IDENTIFICADOR, nome_variavel>`
- Palavras reservadas: Conjunto de palavras reservadas da linguagem. Exemplo: `<PALAVRA_RESERVADA, if>`
- Dígitos: Sequências de números. Exemplo: `<DIGITO, 123>`
- Símbolos especiais: Caracteres especiais, como ponto e vírgula (;), vírgula (,), ponto (.), parênteses (), chaves {}, sinal de igual (=), entre outros. Exemplo: `<SIMBOLO_ESPECIAL, ;>`

<hr>
🇺🇸 EN

# Code Documentation

This code implements a simple lexical analyzer for token recognition in an input file. It identifies identifiers, reserved words, digits, and special symbols.

## Function  `geral(arquivo)`

This function takes the name of a file as input and performs the lexical analysis of its content.

### Parameters

- `arquivo` (str): The name of the file to be analyzed.

### Variables

- `token` (str): Variable that stores the current token during analysis.
- `comentario` (bool): Control variable that indicates whether the analyzer is inside a comment.
- `estado` (int): Variable that represents the current state of the lexical analyzer.
- `mensagem` (str): Variable to store error messages, if any.
- `linha_erro` (int): Variable that records the current line number during analysis.

### behaviour

The geral function initializes the necessary variables to control the current token, the state, the comment control, the error message, and the line number.

The code opens the specified file in read mode ('r') and reads all lines of the file.

An iteration is performed over each line of the file. For each character in the line, the lexical analyzer checks its type and determines the next state according to the token recognition logic.

During the analysis, different types of tokens are identified, such as identifiers, reserved words, digits, and special symbols.

If an error occurs during the analysis, an error message is generated, indicating the line and the character that caused the error.

After analyzing each line, the lexical analyzer prints the identified tokens.

## Recognized Tokens

The lexical analyzer is capable of recognizing the following types of tokens:

- Identificadores: Sequences of uppercase or lowercase letters, numbers, underscores (_), or dollar signs ($). Example: `<IDENTIFICADOR, nome_variavel>`
- Palavras reservadas: Set of reserved words in the language. Example: `<PALAVRA_RESERVADA, if>`
- Dígitos: Sequences of numbers. Example: `<DIGITO, 123>`
- Símbolos especiais: Special characters such as semicolon (;), comma (,), dot (.), parentheses (), curly braces {}, equal sign (=), among others. Example: `<SIMBOLO_ESPECIAL, ;>`
