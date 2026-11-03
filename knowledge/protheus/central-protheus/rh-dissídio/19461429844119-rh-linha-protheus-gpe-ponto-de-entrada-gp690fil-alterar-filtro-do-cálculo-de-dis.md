---
article_id: 19461429844119
category: RH - Dissídio
content_hash: fb7e853a08a88cf5a5108d8a426cbf8f1fd3c925350891b4954816fe7376446e
fetched_at: '2026-06-28T22:43:43.420905+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - Ponto de Entrada GP690FIL - Alterar filtro do cálculo
  de dissídio
type: support-article
updated_at: '2025-08-05T17:41:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19461429844119-RH-Linha-Protheus-GPE-Ponto-de-Entrada-GP690FIL-Alterar-filtro-do-c%C3%A1lculo-de-diss%C3%ADdio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19461416923927) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Ponto de Entrada GP690FIL - Alterar filtro do cálculo de dissídio.

**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - Todas as versões.  
  
**Solução**

Este ponto de entrada permite alterar filtro do cálculo de dissídio.

**Programa Fonte**  
GPEM690.PRX, GPEM020

Retorno

xRet

#### **EXEMPLO DE UTILIZAÇÃO**

Exemplo:

#INCLUDE "PROTHEUS.CH"  
User Function GP690FIL()

Local nTipo     := Paramixb[1]  
Local cFiltPad  := Paramixb[2]  
Local xRet        := Nil

//Filtro SRA (em linguagel SQL)  
If nTipo == 1  
    xRet    := "%(RA\_FILIAL BETWEEN '01' AND '99') AND RA\_SITFOLH IN(' ') %"  
//Filtro Cálculo (em linguagem AdvPL)  
ElseIf nTipo == 2  
    xRet    := "((RA\_FILIAL >= '01' .AND. RA\_FILIAL <= '99')) .AND. (RA\_SITFOLH $ (' '))"  
//Indica se irá processar o cálculo do registro ou não  
ElseIf nTipo == 3  
    xRet := .T.  
EndIf

Return xRet

/\*

No exemplo, é feito verificação da chamada do ponto de entrada:

1 - Filtro em SQL para a tabela SRA para processar os registros da filial 01 a 99 com o campo RA\_SITFOLH em branco.

2 - Filtro em AdvPl para o cálculo para processar os registros da filial 01 a 99 com o campo RA\_SITFOLH em branco.

3 - Retorno lógico indicando que irá processar todos os registros da SRA.

Obs.: após a compilação do ponto de entrada, é necessário que nas três execuções sejam retornado o conteúdo conforme formato explicado acima. Para manter a coerência do filtro, tanto o filtro em SQL quanto em AdvPL devem efetuar o mesmo filtro, com a particularidade de sintaxe de cada linguagem.

\*/

**Saiba mais:** <https://tdn.totvs.com/display/PROT/DT_PE_GP690FIL_Alterar_Filtro_Dissidio>   
[RH - Dissidio](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109132-RH-Diss%C3%ADdio)
