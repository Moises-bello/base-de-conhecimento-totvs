---
article_id: 360026453571
category: Escrita Fiscal - Impostos - IR
content_hash: 894c6fffb5d16ed389e3d06b424458e9df01a1584f98712eb46c9a5eed448616
fetched_at: '2026-06-28T22:39:31.842339+00:00'
product: protheus
section_id: 1500001549802
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS -  Como utilizar o
  botão retenção no documento de entrada
type: support-article
updated_at: '2021-06-17T13:11:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026453571-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-utilizar-o-bot%C3%A3o-reten%C3%A7%C3%A3o-no-documento-de-entrada
---

**Ocorrência**

No módulo Compras (aba duplicatas), cliente não consegue ativar o botão retenção localizado no canto inferior direito na rotina MATA103:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025643831/mceclip0.png)

**Ambiente**

Protheus – MATA103 – A partir da versão 11.80.  
  
**Causa**

Esse incidente ocorre, pois é necessário ativar o parâmetro para habilitar o botão retenção e só funciona pelo tratamento na emissão, pelo tratamento na baixa a rotina não permite manipula-lo.  
  
**Solução**

Para solucionar essa ocorrência, configure os seguintes parâmetros:

MV\_AC10925 = 1 - Permite alteração

MV\_BX10925 = 2 - Tratamento do PCC pela emissão.
