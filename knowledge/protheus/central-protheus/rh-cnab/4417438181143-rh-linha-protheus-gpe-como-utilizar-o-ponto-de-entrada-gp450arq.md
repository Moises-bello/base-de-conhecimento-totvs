---
article_id: 4417438181143
category: RH - CNAB
content_hash: b05502ba7f7a16e5de887145619295688d57512db30376845db7959cd222df02
fetched_at: '2026-06-28T22:43:39.222916+00:00'
product: protheus
section_id: 360004833653
source: central-protheus
title: RH - Linha Protheus - GPE - Como utilizar o ponto de entrada GP450ARQ
type: support-article
updated_at: '2025-06-16T15:01:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4417438181143-RH-Linha-Protheus-GPE-Como-utilizar-o-ponto-de-entrada-GP450ARQ
---

**Descrição:**Essa implementação tem o objetivo de permitir ao usuário escolher o local de gravação dos arquivos diretamente.   
 **Programa Fonte**GPEM450.PRX

**Sintaxe**

GP450ARQ - Local de Gravação dos Arquivos ( [ PARAMIXB[1] ] ) --> cArqSaida

Parâmetros:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Nome |  |  | Tipo |  |  | Descrição |  |  | Default |  |  | Obrigatório |  |  | Referência |  |
|  | PARAMIXB[1] |  |  | Caracter |  |  | Contém o caminho onde o arquivo será gravado. |  |  |  |  |  |  |  |  |  |  |

Retorno

**cArqSaida**

()* Contém o caminho onde o arquivo será gravado.

Observações

A pasta indicada no retorno deverá existir, caso contrário o arquivo não será criado e gravado.

**Exemplos:**

#INCLUDE 'PROTHEUS.CH'  
User Function GP450ARQ()  
Local aArea := GetArea()  
Local cArqSaida := PARAMIXB[1]  
Alert( "Passou pelo PE GP450ARQ" )  
cArqSaida := "C:\SISPAG\teste.txt"  
RestArea( aArea )  
Return ( cArqSaida )

**Variáveis**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Nome |  |  | Tipo |  |  | Escopo |  |  | Pode Alterar |  |  | descrição |  |
|  |  |  |  | Array of Record |  |  | Global |  |  | Não |  |  |  |  |

![GP450ARQ.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/18132803838487)

**Saiba Mais:**  
[RH - Linha Protheus - GPE - Passo a passo para geração do Arquivo CNAB (GPEM080)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8420406092951-RH-Linha-Protheus-GPE-Passo-a-passo-para-gera%C3%A7%C3%A3o-do-Arquivo-CNAB-GPEM080-)

[Artigos - CNAB](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833653-RH-CNAB)
