---
article_id: 360018755911
category: Contabilidade Gerencial - Visão Gerencial
content_hash: 1ecbd884db33c47818f02ea09035a7b5c9ad0dbfb72d4eaf321fbf66cc59b64c
fetched_at: '2026-06-28T22:40:50.620735+00:00'
product: protheus
section_id: 1500001548642
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB -  Qual e a funcionalidade
  da função MovCusto?
type: support-article
updated_at: '2022-03-18T12:07:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018755911-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Qual-e-a-funcionalidade-da-fun%C3%A7%C3%A3o-MovCusto
---

A função MovConta() retorna o valor do movimento de uma determinada conta contábil, de acordo com as parametrizações informadas.   
Uso recomendado para integração básica entre o Protheus e o Microsoft Excel.   
Pode ser utilizado em outros pontos do Sistema, respeitando a correta parametrização da função.

Programa Fonte:

```
CTBXFUN.PRW
```

Sintaxe:

MovConta() - Retorna valor de uma conta contábil ( cContadDataInidDataFimcMoedacTpSaldnQualSaldo [ nSint ] [ nImpAntLP ] [ dDataLP ] ) --> aMovimento[nQualSaldo]

Retorno:  **aMovimento[nQualSaldo]**(numerico)

* Ver detalhe da composição do array aMovimento

Observações

O Array aMovimento é composto das seguintes informações:

[1] Movimento Devedor  
[2] Movimento Credor  
[3] Movimento do Mes  
[4] Saldo Final

Em função do parâmetro nQualSaldo será retornada uma das possibilidades de saldos contidas no array aMovimento.

Exemplos

```
MovConta("2101",FirtDay(dDataBase),LastDay(dDataBase),"01","1",3)// Efeito: Retorna o movimento do mês para a conta contábil "2101", partindo do primeiro dia do // mês corrente, até o último dia do mês corrente, para a moeda "01", tipo de saldo "1".
```

Parâmetros:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Nome |  |  | Tipo |  |  | Descrição |  |  | Default |  |  | Obrigatório |  |  | Referência |  |
|  | cConta |  |  | Caracter |  |  | Codigo da Conta |  |  |  |  |  | X |  |  |  |  |
|  | dDataIni |  |  | Data |  |  | Data inicial para composição do valor do movimento |  |  |  |  |  | X |  |  |  |  |
|  | dDataFim |  |  | Data |  |  | Data final para composição do valor do movimento |  |  |  |  |  | X |  |  |  |  |
|  | cMoeda |  |  | Caracter |  |  | Moeda de referência para o movimento |  |  |  |  |  | X |  |  |  |  |
|  | cTpSald |  |  | Caracter |  |  | Saldo de referência para o movimento |  |  |  |  |  | X |  |  |  |  |
|  | nQualSaldo |  |  | Numérico |  |  | Retorno desejado (ver detalhe do retorno) |  |  |  |  |  | X |  |  |  |  |
|  | nSint |  |  | Numérico |  |  | Indica se a conta é sintética (1) ou analítica (0) |  |  |  |  |  |  |  |  |  |  |
|  | nImpAntLP |  |  | Numérico |  |  | Indica se considera valores anteriores a última apuração de lucros e perdas |  |  |  |  |  |  |  |  |  |  |
|  | dDataLP |  |  | Data |  |  | Data da última apuração de lucros e perdas |  |  |  |  |  |  |  |  |  |  |
