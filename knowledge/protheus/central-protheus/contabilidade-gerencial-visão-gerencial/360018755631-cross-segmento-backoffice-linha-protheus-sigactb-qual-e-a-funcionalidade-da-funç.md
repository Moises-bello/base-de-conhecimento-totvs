---
article_id: 360018755631
category: Contabilidade Gerencial - Visão Gerencial
content_hash: 7739fd6babaa65b81fe3585d1da6f388685f0ca810fcb001887df4dc33545170
fetched_at: '2026-06-28T22:40:50.658817+00:00'
product: protheus
section_id: 1500001548642
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB: Qual e a funcionalidade
  da função LerStr?'
type: support-article
updated_at: '2022-06-20T20:07:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018755631-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Qual-e-a-funcionalidade-da-fun%C3%A7%C3%A3o-LerStr
---

**Dúvida**Qual e a funcionalidade da função LerStr?

**Ambiente**Protheus – Contabilidade Gerencial – A partir da versão 11.80  
  
   
**Solução**

|  |  |
| --- | --- |
| Versões: | Advanced Protheus 5.07 , Advanced Protheus 5.08 , Advanced Protheus 6.09 , Advanced Protheus 7.10 , Microsiga Protheus 8.11 , Protheus 10 |
| Compatível Países: | Todos |
| Sistemas Operacionais: | Todos |
| Compatível às Bases de Dados: | Todos |
| Nível de Acesso: | Nível 1 (Acesso Clientes) |
| Idiomas: | Espanhol , Inglês |

Descrição:

A função LerStr()é uma função específica para o processo de Contabilização TXT para os ambientes SIGACON - Contabilidade e SIGACTB - Contabilidade Gerencial.  
  
Esta função retorna um conteúdo no formato String, de acordo com as posições informadas na linha de movimento do arquivo TXT em processamento.

Programa Fonte:

```
MATXFUNC.PRW
```

Sintaxe:

LerStr() - Retorna conteúdo do formato String ( nPosIni (x)nCaracteres (y) ) --> cString

Retorno: **cString**(caracter)

* String contendo as informações referentes ao intervado x,y definido nos parâmetros

Observações

Esta função utiliza a variável xBuffer (escopo Private) disponível em tempo de processamento da rotina de Contabilização TXT. O conteúdo da variável xBuffer é do tipo string, sendo que seu tamanho depende da parametrização da rotina de contabilização TXT, o qual deve avaliar o tamanho da linha do arquivo TXT + duas posições. As posições adicionadas ao tamanho da linha são referentes ao CRLF formado pela combinação de chr(10) + chr(13).

Exemplos

1o. Estrutura da linha do arquivo TXT analisado:LLLTDDDDDDDDDDDDDDDDDDDDCCCCCCCCCCCCCCCCCCCCVVVVVVVVVVVVVVVVVVVVHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHAonde:LLL - Código do lançamento padrão : 001 - 003 (03)T - Tipo do lançamento contábil (DC) : 004 - 004 (01)DDD - Conta à debito do lançamento contábil : 005 - 024 (20)CCC - Conta à crédito do lançamento contábil : 025 - 044 (20)VVV - Valor do lançamento contábil : 045 - 064 (20)HHH - Histótico do lançamento contabil : 065 - 104 (40)2o. O tamanho de linha a ser configurado para correta leitura deste arquivo será 106 (última posição de informação (104) + 2 caracteres de final de linha.3o. Uso do LerStr(x,y):A. LerStr(04,01) --> retorna o tipo do lançamento contábil, aonde: 1- Débito, 2- Crédito, 3- Partida DobradaB. LerStr(05,20) --> retorna o código da conta contábil à debito do lançamentoC. LerStr(25,20) --> retorna o código da conta contábil à crédito do lançamentoD. LerStr(65,40) --> retorna o texto do histórico do lançamento

Parâmetros:

​

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Nome |  |  | Tipo |  |  | Descrição |  |  | Default |  |  | Obrigatório |  |  | Referência |  |
|  | nPosIni (x) |  |  | Numérico |  |  | Posição inicial da informação da linha do arquivo |  |  |  |  |  | X |  |  |  |  |
|  | nCaracteres (y) |  |  | Numérico |  |  | Quantidade de caracteres que compõe a informação a ser avaliada a partir da posição inicial (inclusive). |
