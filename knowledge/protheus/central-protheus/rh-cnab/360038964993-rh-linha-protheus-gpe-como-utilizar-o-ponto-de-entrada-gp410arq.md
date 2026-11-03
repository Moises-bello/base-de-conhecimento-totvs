---
article_id: 360038964993
category: RH - CNAB
content_hash: a1d6d38b2bd5cbdafbb7ca366210f04ae2eac91a7e722f8b9c23207ea10f8f88
fetched_at: '2026-06-28T22:43:39.213380+00:00'
product: protheus
section_id: 360004833653
source: central-protheus
title: RH - Linha Protheus - GPE - Como utilizar o ponto de entrada GP410ARQ
type: support-article
updated_at: '2025-06-17T18:18:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038964993-RH-Linha-Protheus-GPE-Como-utilizar-o-ponto-de-entrada-GP410ARQ
---

**Descrição:**

```
Essa implementação tem o objetivo de permitir ao usuário escolher o local de gravação dos arquivos diretamente.
```

**Programa Fonte**

```
GPEM410.PRX
```

**Sintaxe**

GP410ARQ - Escolha do local de Gravação dos Arquivos ( [ PARAMIXB[1] ] ) --> cArqSaida

Parâmetros:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Nome |  |  | Tipo |  |  | Descrição |  |  | Default |  |  | Obrigatório |  |  | Referência |  |
|  | PARAMIXB[1] |  |  | Caracter |  |  | Contém o caminho onde o arquivo será gravado. |  |  |  |  |  |  |  |  |  |  |

Retorno

**cArqSaida**

()* Contém o caminho onde o arquivo será gravado.

**Observações:**

A pasta indicada no retorno deverá existir, caso contrário o arquivo não será criado e gravado.

**Exemplos:**

```
#INCLUDE 'PROTHEUS.CH'User Function GP410ARQ()Local aArea		:= GetArea()Local cArqSaida := PARAMIXB[1]Alert( "Passou pelo PE GP410ARQ" )cArqSaida := "C:\CNAB\teste.txt"RestArea( aArea )Return ( cArqSaida )
```

Variáveis

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Nome |  |  | Tipo |  |  | Escopo |  |  | Pode Alterar |  |  | descrição |  |
|  |  |  |  | Array of Record |  |  | Global |  |  | Não |  |  |  |  |

Exemplo montado (disponível também anexo):  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6353305874455)

Funcionamento do PE 410ARQ

![GP410ARQ.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/6354041910167)

**Saiba Mais**
