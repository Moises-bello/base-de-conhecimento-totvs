---
content_hash: 6b8360c7e78a38767054949e8b455343bf9715fee031cfc8813c8d5e24e7b09b
fetched_at: '2026-06-29T00:09:03.620674+00:00'
page_id: '381051703'
product: rm
source: tdn-rm
title: Funções Globais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=381051703
version: 112
---

(CONTEÚDO|0.\*)

## **CONTEÚDO**

1. **Visão Geral**
2. **Funções**

## **01. VISÃO GERAL**

   As fórmulas globais são aquelas apresentadas para todos os módulos do sistema, e são passíveis de uso em qualquer um deles. O objetivo deste documento é apresentar as Fórmulas Globais, com sua descrição, sintaxe, parâmetros e apresentar um breve exemplo com seu respectivo retorno.

       Conheça as fórmulas globais:

## **02. FUNÇÕES**

# ABS

---

| Função | **ABS** |
| --- | --- |
| Descrição | Retorna o valor absoluto de um número. |
| Sintaxe | ABS( NUM ) |
| Parâmetros | * NUM → Número para Operação |
| Exemplo | ABS(-17) |
| Retorno | 17 |

# ANODT

---

| Função | **ANODT** |
| --- | --- |
| Descrição | Retorna o ano de uma data. |
| Sintaxe | ANODT( ' DATA ' ) |
| Parâmetros | * DATA → Data para selecionar o ano |
| Exemplo | ANODT('24/10/2018') |
| Retorno | 2018 |

# ARRED

---

| Função | **ARRED** |
| --- | --- |
| Descrição | Arredonda um valor sem casas decimais. |
| Sintaxe | ARRED( NUM ) |
| Parâmetros | * NUM → Número para Operação |
| Exemplo | ARRED(24.73) ARRED(24.33) ARRED(24.50) |
| Retorno | 25 24 25 |

# ARREDONDA

---

| Função | **ARREDONDA** |
| --- | --- |
| Descrição | Arredonda um valor. |
| Sintaxe | ARREDONDA( NUM A, NUM B ) |
| Parâmetros | * NUM A → Número para Operação * NUM B → Quantidade de casas decimais |
| Exemplo | ARREDONDA(24.33568784,3) |
| Retorno | 24,336 |

# ARREDVALOR

---

| Função | **ARREDVALOR** |
| --- | --- |
| Descrição | Arredonda um valor Independente de Sistema. |
| Sintaxe | ARREDVALOR( NUM A, NUM B ) |
| Parâmetros | * NUM A → Número para Operação * NUM B → Fator |
| Exemplo | ARREDVALOR(24.33,1) |
| Retorno | 25 |

# ASCII

---

| Função | **ASCII** |
| --- | --- |
| Descrição | Retorna o valor que representa um determinado caractere na tabela ASCII. |
| Sintaxe | ASCII( ' CHAR ' ) |
| Parâmetros | * CHAR → Caracteres que se deseja retirar. |
| Exemplo | ASCII('o') |
| Retorno | 111 |

# ATRIBUI

---

| Função | **ATRIBUI** |
| --- | --- |
| Descrição | Atribui um valor à uma memoria. |
| Sintaxe | ATRIBUI( CHAVE , CONTEUDO) |
| Parâmetros | * CHAVE → Chave da memória * CONTEUDO → Conteúdo para atribuir |
| Exemplo | ATRIBUI('MEMORIA001','Mundo bonito') |
| Retorno | Mundo Bonito |

# COLIGADACORRENTE

---

| Função | **COLIGADACORRENTE** |
| --- | --- |
| Descrição | Retorna a coligada corrente. |
| Sintaxe | COLIGADACORRENTE( ) |
| Parâmetros | N/A |
| Exemplo | COLIGADACORRENTE() |
| Retorno | 1 |

# CONCAT

---

| Função | **CONCAT** |
| --- | --- |
| Descrição | Concatena os textos A e B |
| Sintaxe | CONCAT( ' TEXTO A ' , ' TEXTO B ' ) |
| Parâmetros | * TEXTO A → Primeiro Texto * TEXTO B → Segundo Texto |
| Exemplo | CONCAT('Mundo','Bonito') |
| Retorno | MundoBonito |

# CONCAT2

---

| Função | **CONCAT2** |
| --- | --- |
| Descrição | Concatena as strings A e B com um espaço entre elas. |
| Sintaxe | CONCAT2( ' TEXTO A ' , ' TEXTO B ' ) |
| Parâmetros | * TEXTO A → Primeiro Texto * TEXTO B → Segundo Texto |
| Exemplo | CONCAT2('Mundo','Bonito') |
| Retorno | Mundo Bonito |

# CONTEMVALOR

---

| Função | **CONTEMVALOR** |
| --- | --- |
| Descrição | Procura um determinado valor em um conjunto de dados. |
| Sintaxe | CONTEMVALOR( ' CONJUNTO ' , VALOR , ' TIPO ' ) |
| Parâmetros | * CONJUNTO → Conjunto de valores separados por / * VALOR → Valor a ser procurado * TIPO → Tipo de dado a ser tratado D = Data S = String Vazio/Outros → Decimal |
| Exemplo | CONTEMVALOR( 'casa/geladeira/mesa/gato/gaiola ', 'gato', 'S') |
| Retorno | 1 |

# COTACAOMOEDA

---

| Função | **COTACAOMOEDA** |
| --- | --- |
| Descrição | Cotação de uma moeda. |
| Sintaxe | COTACAOMOEDA( ' SIMBOLO ' , 'DATA' ) |
| Parâmetros | * SIMBOLO → Símbolo da moeda * DATA→ Data da cotação |
| Exemplo | COTACAOMOEDA('US$','25/10/2018') |
| Retorno | 3,724 |

# DATANULA

---

| Função | **DATANULA** |
| --- | --- |
| Descrição | Retorna a data mínima do sistema. |
| Sintaxe | DATANULA() |
| Parâmetros | N/A |
| Exemplo | DATANULA() |
| Retorno | 01/01/2000 |

# DECANO

---

| Função | **DECANO** |
| --- | --- |
| Descrição | Subtrai um número de meses de um mês/ano e retorna o ano do resultado. |
| Sintaxe | DECANO(INTEIRO1,INTEIRO2,INTEIRO3) |
| Parâmetros | * INTEIRO1 → Mês da data inicial * INTEIRO2 → Ano da data inicial * INTEIRO3 → Quantidade de meses para subtrair da data inicial |
| Exemplo | DECANO(2,2018,26) |
| Retorno | 2015 |

# DECMES

---

| Função | **DECMES** |
| --- | --- |
| Descrição | Subtrai uma quantidade de meses ( X meses) de um mês inicial (1 a 12). |
| Sintaxe | DECMES(INTEIRO1,INTEIRO2) |
| Parâmetros | * INTEIRO1 → Mês inicial * INTEIRO2 → Quantidade de meses para diminuir do mês inicial |
| Exemplo | DECMES(11,5) |
| Retorno | 6 |

# DIADT

---

| Função | **DIADT** |
| --- | --- |
| Descrição | Retorna o dia de uma data. |
| Sintaxe | DIADT( ' DATA ' ) |
| Parâmetros | * DATA → Data para selecionar o dia |
| Exemplo | DIADT('24/10/2018') |
| Retorno | 24 |

# DIASEMANA

---

| Função | **DIASEMANA** |
| --- | --- |
| Descrição | Retorna o dia da semana de uma data. (1= Domingo | 2= Segunda | 3= Terça | 4=Quarta | 5=Quinta | 6=Sexta | 7= Sábado) |
| Sintaxe | DIASEMANA( ' DATA ' ) |
| Parâmetros | * DATA → Data para selecionar o dia da semana |
| Exemplo | DIASEMANA('24/10/2018') |
| Retorno | 4 |

# ESCREVELOG

---

| Função | **ESCREVELOG** |
| --- | --- |
| Descrição | Escreve Log |
| Sintaxe | ESCREVELOG( ' TEXTO ' ) |
| Parâmetros | * TEXTO → Texto a ser inserido no Log. |
| Exemplo | ESCREVELOG(' Log Adicionado') |
| Retorno | Log Adicionado |

# EXECSQL

---

| Função | **EXECSQL** |
| --- | --- |
| Descrição | Executa uma Consulta SQL. |
| Sintaxe | EXECSQL( ' CÓDIGO ' ) |
| Parâmetros | * CÓDIGO → Código da Consulta SQL. |
| Exemplo | EXECSQL('CON001' ) |
| Retorno | Será o retorno (Se tiver) da Consulta SQL 'CON001'. |

# FALSO

---

| Função | **FALSO** |
| --- | --- |
| Descrição | Retorna 0. |
| Sintaxe | FALSO( ) |
| Parâmetros | N/A |
| Exemplo | FALSO() |
| Retorno | 0 |

# FOR

---

| Função | **FOR** |
| --- | --- |
| Descrição | Executa uma fórmula. |
| Sintaxe | FOR( ' CÓDIGO ' ) |
| Parâmetros | * CÓDIGO → Código da fórmula. |
| Exemplo | FOR('FOR001' ) |
| Retorno | Será o retorno da fórmula 'FOR001'. |

# FRAC

---

| Função | **FRAC** |
| --- | --- |
| Descrição | Retorna a parte fracionada de um valor. |
| Sintaxe | FRAC( NUM ) |
| Parâmetros | * NUM → Número para Operação |
| Exemplo | FRAC(24.73) |
| Retorno | 0,73 |

# HOJE

---

| Função | **HOJE** |
| --- | --- |
| Descrição | Retorna a data de hoje. |
| Sintaxe | HOJE() |
| Parâmetros | N/A |
| Exemplo | HOJE() |
| Retorno | 24/10/2018 |

# INCANO

---

| Função | **INCANO** |
| --- | --- |
| Descrição | Adiciona um número de meses a um mês/ano e retorna o ano do resultado. |
| Sintaxe | INCANO(INTEIRO1,INTEIRO2,INTEIRO3) |
| Parâmetros | * INTEIRO1 → Mês da data inicial * INTEIRO2 → Ano da data inicial * INTEIRO3 → Quantidade de meses para adicionar na data inicial |
| Exemplo | INCANO(2,2018,26) |
| Retorno | 2019 |

# INCMES

---

| Função | **INCMES** |
| --- | --- |
| Descrição | Adiciona uma quantidade de meses ( X meses) à um mês inicial (1 a 12). |
| Sintaxe | INCMES(INTEIRO1,INTEIRO2) |
| Parâmetros | * INTEIRO1 → Mês inicial * INTEIRO2 → Quantidade de meses para adicionar ao mês inicial |
| Exemplo | INCMES(2,19) |
| Retorno | 9 |

# INTTOSTRFORMAT

---

| Função | **INTTOSTRFORMAT** |
| --- | --- |
| Descrição | Converte um valor inteiro para string (texto) preenchendo com zeros. |
| Sintaxe | INTTOSTRFORMAT( INTEIRO , ZEROS ) |
| Parâmetros | * INTEIRO → Valor a ser convertido. * ZEROS→ Quantidade de Zeros. |
| Exemplo | INTTOSTRFORMAT(27,5) |
| Retorno | 00027 |

# MAX

---

| Função | **MAX** |
| --- | --- |
| Descrição | Retorna o maior número. |
| Sintaxe | MAX( NUM A , NUM B ) |
| Parâmetros | * NUM A → Número para comparação * NUM B → Número para comparação |
| Exemplo | MAX(17,12) |
| Retorno | 17' |

# MEMORIA

---

| Função | **MEMORIA** |
| --- | --- |
| Descrição | Retorna o valor de uma memória. |
| Sintaxe | MEMORIA( CHAVE ) |
| Parâmetros | * CHAVE → Chave da memória |
| Exemplo | MEMORIA('MEMORIA001') |
| Retorno | Mundo Bonito |

# MESDT

---

| Função | **MESDT** |
| --- | --- |
| Descrição | Retorna o mês de uma data. |
| Sintaxe | MESDT( ' DATA ' ) |
| Parâmetros | * DATA → Data para selecionar o mês |
| Exemplo | MESDT('24/10/2018') |
| Retorno | 10 |

# MIN

---

| Função | **MIN** |
| --- | --- |
| Descrição | Retorna o menor número. |
| Sintaxe | MIN( NUM A , NUM B ) |
| Parâmetros | * NUM A → Número para comparação * NUM B → Número para comparação |
| Exemplo | MIN(17,12) |
| Retorno | 12 |

# MTDATA

---

| Função | **MTDATA** |
| --- | --- |
| Descrição | Monta uma data a partir de um dia, mês e ano. |
| Sintaxe | MTDATA(INTEIRO1,INTEIRO2,INTEIRO3) |
| Parâmetros | * INTEIRO1 → Dia da data * INTEIRO2 → Mês da data * INTEIRO3 → Ano da data |
| Exemplo | MTDATA(17,11,1989) |
| Retorno | 17/11/1989 |

# PAR

---

| Função | **PAR** |
| --- | --- |
| Descrição | Retorna o que foi armazenado na propriedade de parâmetros genéricos de fórmula. |
| Sintaxe | PAR( ) |
| Parâmetros | N/A |
| Exemplo | PAR() |
| Retorno | Conteúdo do parâmetro armazenado |

# PARMQRY

---

| Função | **PARMQRY** |
| --- | --- |
| Descrição | Retorna o conteúdo de um campo. Utilizada no Gerador de Relatórios (RMGerador.dll). |
| Sintaxe | PARMQRY( ' CAMPO ' ) |
| Parâmetros | * CAMPO → Nome do Campo |
| Exemplo | PARMQRY('CODUSUARIO') |
| Retorno | IgorMC |

# POTENCIA

---

| Função | **POTENCIA** |
| --- | --- |
| Descrição | Retorna a potência. |
| Sintaxe | POTENCIA( NUM A , NUM B ) |
| Parâmetros | * NUM A→ Base da potência * NUM B→ Expoente da potência |
| Exemplo | POTENCIA(2,4) |
| Retorno | 16 |

# PROXREGSQL

---

| Função | **PROXREGSQL** |
| --- | --- |
| Descrição | Avança um registro na Consulta SQL executada. |
| Sintaxe | PROXREGSQL( ' CÓDIGO ' ) |
| Parâmetros | * CÓDIGO → Código da Consulta SQL. |
| Exemplo | PROXREGSQL('CON001' ) |
| Retorno | Avança um registro na Consulta SQL 'CON001'. |

# RAIZ

---

| Função | **RAIZ** |
| --- | --- |
| Descrição | Retorna a raiz quadrada de um valor. |
| Sintaxe | RAIZ( NUM ) |
| Parâmetros | * NUM → Número para Operação |
| Exemplo | RAIZ(25) |
| Retorno | 5 |

# RESULTSQL

---

| Função | **RESULTSQL** |
| --- | --- |
| Descrição | Retorna o valor de um campo de um resultado da Consulta SQL. |
| Sintaxe | RESULTSQL( ' CÓDIGO ' , ' CAMPO ' ) |
| Parâmetros | * CÓDIGO → Código da Consulta SQL * CAMPO → Campo desejado |
| Exemplo | RESULTSQL('CON001','CODUSUARIO' ) |
| Retorno | Retorna o valor do campo CODUSUARIO do resultado da Consulta SQL 'CON001'. |

# RETIRACARACTERES

---

| Função | **RETIRACARACTERES** |
| --- | --- |
| Descrição | Retira do texto todas as ocorrências dos caracteres da string chars. |
| Sintaxe | RETIRACARACTERES( ' CHAR ' , ' TEXTO ' ) |
| Parâmetros | * CHAR → Caracteres que se deseja retirar. * TEXTO → String que é desejado retirar os caracteres |
| Exemplo | RETIRACARACTERES('o','Mundo Bonito') |
| Retorno | Mund Bnit |

# SETVAR

---

| Função | **SETVAR** |
| --- | --- |
| Descrição | Atribui um valor a uma variável. |
| Sintaxe | SETVAR( ' VAR ' , CONTEUDO) |
| Parâmetros | * VAR → Variável * CONTEUDO → Conteúdo para adicionar na variável |
| Exemplo | SETVAR('var1', 200) |
| Retorno | 200 |

# STR

---

| Função | **STR** |
| --- | --- |
| Descrição | Retorna número de acordo com máscara informada, que pode ser composta da seguinte forma: • com noves: o número será completado com espaços brancos à esquerda; • com zeros ou 'z' (minúsculo ou maiúsculo): o número será completado com zeros à esquerda. • Pode-se usar separador de decimais: '.' (ponto) ou ',' (vírgula) • No caso da máscara contiver ':' será formatado do tipo hora. |
| Sintaxe | STR( VALOR , ' MASK ' ) |
| Parâmetros | * VALOR → Valor decimal a ser formatado. * MASK → Máscara que será aplicada no valor. |
| Exemplo | STR(27, '000') STR(12,'99,99') STR(5, '00.00') STR(320, '00:00') STR(22222, '000:00') |
| Retorno | 027 12,00 05.00 05:20 370:20 |

# STRLEFT

---

| Função | **STRLEFT** |
| --- | --- |
| Descrição | Copia o lado DIREITO de um string (texto) um número de caracteres (quantidade). |
| Sintaxe | STRLEFT( ' TEXTO ' , INTEIRO ) |
| Parâmetros | * TEXTO → String para fazer a cópia iniciando pelo lado Direito * INTEIRO → Quantidade de caracteres que deseja-se copiar |
| Exemplo | STRLEFT('Mundo Bonito',10) |
| Retorno | ndo Bonito |

# STRRIGHT

---

| Função | **STRRIGHT** |
| --- | --- |
| Descrição | Copia o lado ESQUERDO de um string (texto) um número de caracteres (quantidade). |
| Sintaxe | STRRIGHT( ' TEXTO ' , INTEIRO ) |
| Parâmetros | * TEXTO → String para fazer a cópia iniciando pelo lado Esquerdo * INTEIRO → Quantidade de caracteres que deseja-se copiar |
| Exemplo | STRRIGHT('Mundo Bonito',10) |
| Retorno | Mundo Boni |

# SUBSTR

---

| Função | **SUBSTR** |
| --- | --- |
| Descrição | Copia a partir da posição início um número de caracteres de texto. |
| Sintaxe | SUBSTR( ' TEXTO ' , INTEIRO1, INTEIRO2 ) |
| Parâmetros | * TEXTO → Texto onde é desejado selecionar uma parte para cópia * INTEIRO1 → Caracter início * INTEIRO2 → Quantidade de caracteres que você deseja selecionar. |
| Exemplo | SUBSTR('Alô Mundo', 2,5) |
| Retorno | lô mu |

# SUBTRAIDATAS

---

| Função | **SUBTRAIDATAS** |
| --- | --- |
| Descrição | Retorna a subtração entre duas datas |
| Sintaxe | SUBTRAIDATAS( DATA1 , DATA2 ) |
| Parâmetros | * DATA1 → Data inicial * DATA2 → Data para subtrair |
| Exemplo | SUBTRAIDATAS('24/10/2018','21/09/2018') |
| Retorno | 33 |

# TABCOLIG

---

| Função | **TABCOLIG** |
| --- | --- |
| Descrição | Retorna o valor de um campo da coligada. |
| Sintaxe | TABCOLIG( ' CAMPO ' ) |
| Parâmetros | * CAMPO → Nome do Campo |
| Exemplo | TABCOLIG('NOMEFANTASIA') |
| Retorno | TOTVS SA |

# TABCOLIGADA

---

| Função | **TABCOLIGADA** |
| --- | --- |
| Descrição | Retorna o valor de uma Coluna da tabela GCOLIGADA da coligada corrente que o usuário tem acesso na GPERMISS. |
| Sintaxe | TABCOLIGADA( ' CAMPO ' ) |
| Parâmetros | * CAMPO → Nome do Campo |
| Exemplo | TABCOLIGADA('Numero') |
| Retorno | 2664 |

# TAMSTR

---

| Função | **TAMSTR** |
| --- | --- |
| Descrição | Retorna o tamanho da string. |
| Sintaxe | TAMSTR( ' TEXTO ' ) |
| Parâmetros | * TEXTO → String que é desejado saber a quantidade de caracteres |
| Exemplo | TAMSTR('Mundo Bonito') |
| Retorno | 12 |

# TETO

---

| Função | **TETO** |
| --- | --- |
| Descrição | Retorna o valor truncado mais um. |
| Sintaxe | TETO( NUM ) |
| Parâmetros | * NUM → Número para Operação |
| Exemplo | TETO(24.03) |
| Retorno | 25 |

# TRUNCVALOR

---

| Função | **TRUNCVALOR** |
| --- | --- |
| Descrição | Trunca um valor com casas decimais. |
| Sintaxe | TRUNCVALOR( NUM A ) ou TRUNCVALOR( NUM A , NUM B ) |
| Parâmetros | * NUM A→ Número para Operação * NUM B→ Quantidade de casas Decimais |
| Exemplo | TRUNCVALOR(24.83) TRUNCVALOR(24.83, 1) |
| Retorno | 24 24,8 |

# ULTDIAMES

---

| Função | **ULTDIAMES** |
| --- | --- |
| Descrição | Retorna o último dia do mês de uma data. |
| Sintaxe | ULTDIAMES( ' DATA ' ) |
| Parâmetros | * DATA → Data para selecionar o último dia do mês |
| Exemplo | ULTDIAMES('24/10/2018') |
| Retorno | 31/10/2018 |

# USUARIOCORRENTE

---

| Função | **USUARIOCORRENTE** |
| --- | --- |
| Descrição | Retorna o usuário corrente. |
| Sintaxe | USUARIOCORRENTE( ) |
| Parâmetros | N/A |
| Exemplo | USUARIOCORRENTE() |
| Retorno | IgorMC |

# VAL

---

| Função | **VAL** |
| --- | --- |
| Descrição | Converte um string para valor. |
| Sintaxe | VAL( ' VALOR ' ) |
| Parâmetros | * VALOR → String para se converter em valor |
| Exemplo | VAL('12,65') |
| Retorno | 12,65 |

# VERDADE

---

| Função | **VERDADE** |
| --- | --- |
| Descrição | Retorna 1. |
| Sintaxe | VERDADE ( ) |
| Parâmetros | N/A |
| Exemplo | VERDADE() |
| Retorno | 1 |

false

**Versão:** 12.01.XX
