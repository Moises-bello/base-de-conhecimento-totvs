---
article_id: 360018467392
category: Contabilidade Gerencial - Visão Gerencial
content_hash: 7877eda8b8f138308fd8a36a776f17069ec1eddf7a2a454dd13340153da9de27
fetched_at: '2026-06-28T22:40:50.665985+00:00'
product: protheus
section_id: 1500001548642
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB: Qual e a funcionalidade
  da função MovClass?'
type: support-article
updated_at: '2022-07-18T18:39:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018467392-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Qual-e-a-funcionalidade-da-fun%C3%A7%C3%A3o-MovClass
---

A função LerVal()é uma função específica para o processo de Contabilização TXT para os ambientes SIGACON - Contabilidade e SIGACTB - Contabilidade Gerencial.   
  
Esta função retorna um conteúdo no formato numérico, de acordo com as posições informadas na linha de movimento do arquivo TXT em processamento. Este conteúdo sempre será retornado considernado-se duas (2) casas decimais.

Programa Fonte:

```
MATXFUNC.PRW
```

Sintaxe:

LerVal() - Retorna conteúdo numérico ( nPosIni (x)nCaracteres (y) ) --> nValor

Retorno:

**nValor**(numerico)

* Valor com duas casas decimais.

Observações

Esta função utiliza a variável xBuffer (escopo Private) disponível em tempo de processamento da rotina de Contabilização TXT. O conteúdo da variável xBuffer é do tipo string, sendo que seu tamanho depende da parametrização da rotina de contabilização TXT, o qual deve avaliar o tamanho da linha do arquivo TXT + duas posições. As posições adicionadas ao tamanho da linha são referentes ao CRLF formado pela combinação de chr(10) + chr(13).

Exemplos

1o. Estrutura da linha do arquivo TXT analisado:LLLTDDDDDDDDDDDDDDDDDDDDCCCCCCCCCCCCCCCCCCCCVVVVVVVVVVVVVVVVVVVVHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHAonde:LLL - Código do lançamento padrão : 001 - 003 (03)T - Tipo do lançamento contábil (DC) : 004 - 004 (01)DDD - Conta à debito do lançamento contábil : 005 - 024 (20)CCC - Conta à crédito do lançamento contábil : 025 - 044 (20)VVV - Valor do lançamento contábil : 045 - 064 (20)HHH - Histótico do lançamento contabil : 065 - 104 (40)2o. O tamanho de linha a ser configurado para correta leitura deste arquivo será 106 (última posição de informação (104) + 2 caracteres de final de linha.3o. Uso do LerVal(x,y):A. LerVal(45,20) --> retornará o valor do lançamento contábil no formato 18,2 (20 posições).

Parâmetros:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Nome |  |  | Tipo |  |  | Descrição |  |  | Default |  |  | Obrigatório |  |  | Referência |  |
|  | nPosIni (x) |  |  | Numérico |  |  | Posição inicial da informação da linha do arquivo |  |  |  |  |  | X |  |  |  |  |
|  | nCaracteres (y) |  |  | Numérico |  |  | Quantidade de caracteres que compõe a informação a ser avaliada a partir da posição inicial (inclusive). |  |  |  |  |  | X |  |  |  |  |
