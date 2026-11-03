---
article_id: 8057464093079
category: ADVPL - Ponto de Entrada
content_hash: 8260034bdda29614e06971cf038d251a7e096669c8e7bada48f7ed0da1d29a11
fetched_at: '2026-06-28T22:40:12.948894+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN  - Ponto de entrada -
  menu/ Browser- F050ROT
type: support-article
updated_at: '2025-05-30T20:09:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8057464093079-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Ponto-de-entrada-menu-Browser-F050ROT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32485869835927) Tempo aproximado para leitura: **00:05:00 min****Dúvida**Ponto de entrada que permite adicionar nova opção no menu/*browse* do contas a pagar (FINA050) e funções do contas a pagar (FINA750)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - Todas as versões  
  
**Solução**Ponto de entrada: F050ROT

Este permite modificar os itens de menu do *browse* de seleção de títulos a pagar , por meio de edição da variável aRotina (passada como parâmetro no ponto de entrada) . 

O retorno deve conter a variável aRotina customizada, com as opções que podem ser selecionadas. 

**PoC**

```
#Include 'Protheus.ch'  
#Include 'FWMVCDEF.ch'  
  
User Function F050ROT()  
  
Local aArea := GetArea()  
Local aRotina := Paramixb // Array contendo os botoes padrões da rotina.  
  
// Tratamento no array aRotina para adicionar novos botoes e retorno do novo array.  
Aadd(aRotina, { "F050ROT", "U_F050ROTMSG", 0, 8, 0,.F.})  
  
RestArea(aArea)  
  
Return aRotina  
  
User Function F050ROTMsg()  
  
Aviso( "F050ROT", "Ponto de Entrada F050ROT", {"Ok"}, 2 )  
  
Return .T.
```

**Exemplo:**

**Saiba mais:**  
[F050ROT](https://tdn.totvs.com/pages/viewpage.action?pageId=515670644)
