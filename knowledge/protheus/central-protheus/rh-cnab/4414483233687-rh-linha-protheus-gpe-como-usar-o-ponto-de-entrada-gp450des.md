---
article_id: 4414483233687
category: RH - CNAB
content_hash: 0477031e01f85426f327b34c8eced24247ce1af62101a8f02f944a1ffd37a4d7
fetched_at: '2026-06-28T22:43:39.205358+00:00'
product: protheus
section_id: 360004833653
source: central-protheus
title: RH - Linha Protheus - GPE - Como usar o ponto de entrada GP450DES
type: support-article
updated_at: '2025-06-16T18:29:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414483233687-RH-Linha-Protheus-GPE-Como-usar-o-ponto-de-entrada-GP450DES
---

Descrição:

```
Ponto de Entrada para desprezar funcionário, caso retorne .F., na geração de líquidos para o SISPAG.
```

Eventos

Este ponto de entrada esta localizado após a consistência de funcionários.

Programa Fonte

```
GPEM450.PRX
```

Sintaxe

GP450DES - Desprezar Funcionário ( [ ] ) --> lRet

Parâmetros:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Nome |  |  | Tipo |  |  | Descrição |  |  | Default |  |  | Obrigatório |  |  | Referência |  |
|  |  |  |  | Array of Record |  |  |  |  |  |  |  |  |  |  |  |  |  |

Retorno

**lRet**

(logico)* Caso o rdmake retorne falso (.F.) o funcionário posicionado será desprezado.

Observações

Exemplos

```
#INCLUDE "Protheus.CH"User Function GP450DES()Local lRet 	   := .T.//-- Condicao para considerar o funcionario, caso nao atenda a condicao, o funcionario é desconsiderado e o proximo funcionario//-- será processado.lRet:= ( nValor > 10 )                                              		Return(lRet)
```

Variáveis

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Nome |  |  | Tipo |  |  | Escopo |  |  | Pode Alterar |  |  | descrição |  |
|  |  |  |  | Array of Record |  |  | Global |  |  | Não |  |  |  |  |

![GP450DES.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17615362678039)
