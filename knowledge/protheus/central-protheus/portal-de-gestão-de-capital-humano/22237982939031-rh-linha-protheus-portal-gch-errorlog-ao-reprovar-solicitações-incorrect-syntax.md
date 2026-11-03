---
article_id: 22237982939031
category: Portal de Gestão de Capital Humano
content_hash: 10cd952251938c34dceead88332e9a5931925cef9e45b29adc826e8b6a2dccaa
fetched_at: '2026-06-28T22:42:58.987760+00:00'
product: protheus
section_id: 206960887
source: central-protheus
title: RH - Linha Protheus - Portal GCH - Errorlog ao reprovar solicitações Incorrect
  syntax near '='
type: support-article
updated_at: '2024-03-21T14:34:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22237982939031-RH-Linha-Protheus-Portal-GCH-Errorlog-ao-reprovar-solicita%C3%A7%C3%B5es-Incorrect-syntax-near
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22237982903447) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Ao realizar a recusa de uma solicitação no **Portal GCH** é apresentado a mensagem ***Internal Server Error**.*Ao analisar o *console.log* é apresentado erro de sintaxe (*query*).  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Portal Gestão de Capital Humano – Todas as versões  
  
**Solução**O erro de sintaxe ocorre devido a uma montagem incorreta na ***query*** dentro do fonte **APIGETSTRUCTURE**e a sua correção está no *patch* abaixo:  
  
**12.1.2210**: <https://suporte.totvs.com/portal/p/10098/download?e=1139090> ;   
**12.1.2310**: <https://suporte.totvs.com/portal/p/10098/download?e=1139088> ;   
**12.1.33**: <https://suporte.totvs.com/portal/p/10098/download?e=1139089> ;  
  
Ou aplicando o [**acumulado do RH**](https://suporte.totvs.com/portal/p/10098/download#000006/all/all/search/RH_EXPEDICAO_CONTINUA).

**Saiba Mais  
[Artigos Sobre Portal Gestão Capital Humano](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960887-RH-Portal-de-Gest%C3%A3o-de-Capital-Humano)  
[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)**
