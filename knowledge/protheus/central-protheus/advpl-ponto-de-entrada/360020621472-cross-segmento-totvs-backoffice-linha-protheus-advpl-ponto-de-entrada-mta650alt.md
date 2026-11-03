---
article_id: 360020621472
category: ADVPL - Ponto de Entrada
content_hash: df7d453aaf1034d07c2ce743bbfda305ff1242258b0b80e3f35f4d9046173771
fetched_at: '2026-06-28T22:40:12.692416+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Ponto de entrada
  MTA650ALT não habilita campos  para alteração '
type: support-article
updated_at: '2021-11-17T13:16:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020621472-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Ponto-de-entrada-MTA650ALT-n%C3%A3o-habilita-campos-para-altera%C3%A7%C3%A3o
---

**Dúvida**Ao utilizar o PE **MTA650ALT**, alguns campos não habilitam a edição.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – Todas as versões.   
  
**Solução**  
Este ponto de entrada só habilitara os campos que são editáveis na alteração.

***Obs.: O sistema não permite a alteração da quantidade de ordens de produção, independente de prevista ou firme.***

**[É possível alterar a quantidade uma Ordem de Produção (OP) depois de aberta?](http://tdn.totvs.com/pages/viewpage.action?pageId=268583980)**

Utilize os campos editáveis conforme exemplo abaixo:

```
User function MTA650ALT()  
  
Local aAlter := Paramixb[1]  
  
//-- Rotina de customização do usuário  
//-- Bloqueados padrão não serão habilitados  
AADD(aAlter,"C2_PEDIDO")  
AADD(aAlter,"C2_ITEMPV")  
  
//--campos editaveis  
AADD(aAlter,"C2_QTSEGUM")  
AADD(aAlter,"C2_REVISAO")  
AADD(aAlter,"C2_ITEMCTA")  
AADD(aAlter,"C2_CLVL")  
AADD(aAlter,"C2_OPC")  
  
Return aAlter
```

**Saiba Mais****[MTA650ALT - Liberar campos para alteração da OP](http://tdn.totvs.com/pages/releaseview.action?pageId=6089466)**
