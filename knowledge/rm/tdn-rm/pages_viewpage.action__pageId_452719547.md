---
content_hash: 14ec158bbdcf0b41f63eb0b72622bdcff237e69ad659fb5e302eb14eb4ec1bf4
fetched_at: '2026-06-29T00:10:08.613454+00:00'
page_id: '452719547'
product: rm
source: tdn-rm
title: Fórmulas / Funções - I
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719547
version: 4
---

**Função I**   
Retorna número de filhos para salário família.  
   
**Função IDADE**  
Retorna a idade do funcionário no primeiro dia do mês de competência.  
IDADE (MTDATA (1, MÊS, ANO)).  
   
**Exemplo**  
IDADE (HOJE)   
/\* onde a variável HOJE é a data que será comparada com a data de nascimento do funcionário\*/   
   
**Função INCANO**  
Soma ao mês o número de meses e retorna o ano correspondente.  
INCANO (MÊS, ANO, NÚMERO DE MESES)  
   
**Exemplo**  
INCANO (10, 2013, 5) = 2014  
A função somará 5 ao mês de outubro de 2013, retornando 2014.  
   
   
   
**Função INCDEP**  
Retorna "1" se o dependente estiver com a determinada incidência marcada e "0" em caso contrário.  
INCDEP (Número do Dependente, Número da incidência)  
   
**Observação**  
A variável INCDEP busca somente as incidências na pasta dependentes | incidências | outras incidências no cadastro dos funcionários. É importante identificar os Códigos criados para os tipos de Outras Incidências em uma tabela dinâmica específica - Código INT37 (Administração Pessoal lCadastros Globais | Tabelas Dinâmicas).   
   
**Exemplo**  
A empresa precisa conhecer quantos são os dependentes do tipo Filho Válido e do sexo feminino para comprar presentes de Natal.  
Na tabela dinâmica INT37, o item 2 refere-se a Presentes de Natal:  
É necessário criar uma sentença SQL para identificar todos os dependentes do tipo Filho Válido e do sexo Feminino dos funcionários da coligada 1  
   
Sentença SQL Código H0005:  
   
SELECT CODCOLIGADA, CHAPA, NOME, NRODEPEND, SEXO, GRAUPARENTESCO FROM PFDEPEND  
WHERE GRAUPARENTESCO=1 AND SEXO = 'F' AND CODCOLIGADA = 1  
   
Fórmula:  
   
DECL (CONT, PR2); /\* CONT conta dependentes, PR2 parâmetro 2 de INCDEP \*/  
SETVAR (PR2,2); /\* Incidência 2 na pasta Administração Pessoal l Funcionário l Anexo l Folha de pagamento l Dependente \*/  
SE EXECSQL('H0005') = VERDADE   
ENTAO  
REPITA    
SE INCDEP (RESULTSQL ('H0005', 'NRODEPEND'), PR2) = 1 /\* Resultado da coluna NRPDEPEND e Valor da PR2) \*/   
ENTAO SETVAR (CONT, CONT+1)   
FIMSE   
ATE PROXREGSQL('H0005') = FALSO    
FIMSE;  
             CONT  
   
   
**Função INCMES**  
Soma ao mês informado o número de meses e retorna o mês correspondente.  
             INCMES (MÊS, NÚMERO DE MESES)  
   
**Exemplo**  
INCMES (10, 20) = 6  
   
**Função INIPERAQUIS**  
Esta fórmula retorna a data de início do último período aquisitivo em aberto. Confira os dados cadastrais em Funcionário| | período aquisitivo   
INIPERAQUIS ('D'), onde 'D' é o retorno da data.  
   
   
**Exemplo**  
 INIPERAQUIS('D') retorna 04/10/2010  
INIPERAQUIS('D') +364 retorna 03/10/2011  
   
Se o ano for bissexto:   
INIPERAQUIS('D') retorna 04/10/2012  
INIPERAQUIS('D') +365 retorna 03/10/2013  
   
   
**Função INT**  
Retorna parte inteira de um valor.  
INT (VALOR)  
   
**Exemplo**  
INT (50.3)  
Retornará 50.  
   
   
   
**Função IRRFDC**  
Retorna IRRF descontado. Retorno Valor   
IRRFDESC  
   
   
**Função INFEMP**  
Retorna informações do empréstimo pendentes, ou seja, que tem o Saldo Devedor maior que 0(zero)

INFEMP (Valor, String)

Onde:

**Valor**: É o identificador do empréstimo. Durante o cálculo da rescisão o sistema verifica todos os empréstimos pendentes do funcionário e atribui para os mesmos números sequenciais.

**String:** É a informação que desejamos saber do empréstimo.   
Os campos possíveis para preenchimento são:  
CODIGO  
CODIGOEVENTO  
DTEMPRESTIMO  
INICIODESCONTO  
NROPARCELAS  
NROPARCPAGAS  
PERIODICIDADE  
VALORORIGINAL  
TIPOEMPRESTIMO  
SALDODEVEDOR

Ainda para facilitar a criação da fórmula pode-se utilizar :

 -1= Total de Empréstimo pendente: InfEmp ( -1', '')

 -2= Total do saldo devedor dos empréstimos pendentes: InfEmp ( -2', '')

Ordem default do empréstimo = Quando desejar que retorne qualquer valor da tabela de empréstimo.

**Observação**: O campo String só deve ser preenchido quando o campo **Valor** for preenchido com a 'Ordem defaut do empréstimo'. Caso contrário preencher com vazio ' '.

**Exemplos:**  
O funcionário tem três empréstimo, sendo que o primeiro tem Saldo Devedor 0,00 (zero), o segundo tem Saldo Devedor R$500,00 e o terceiro Saldo Devedor R$700,00.   
Ao preencher com 1(um) neste campo, é considerado os dados do segundo empréstimo. Se preencher 2(dois) é considerado o terceiro empréstimo.  
    
  
O funcionário tem os seguintes empréstimos cadastrados:  
**CODIGO      CODIGOEVENTO        NROPARCPAGAS       SALDODEVEDOR**  
001                         0060                                    5                                      R$0,00  
002                         0061                                   10                                     R$500,00  
003                         0062                                    2                                      R$700,00  
   
Para a fórmula INFEMP (1, NROPARCPAGAS) retorna 10. O nº de parcelas do primeiro empréstimo com Saldo Devedor maior que 0(zero)  
   
   
**Função INTTOSTRFORMAT**   
Converte um valor inteiro para string (texto) preenchendo com zeros.  
INTTOSTRFORMAT (VALOR, VALOR)  
Onde:  
**Valor1** = Informe o número que será convertido.  
**Valor2**= quantos zeros serão acrescentado no número que será convertido.

**Exemplo:**  
INTTOSTRFORMAT(9,5) =000009
