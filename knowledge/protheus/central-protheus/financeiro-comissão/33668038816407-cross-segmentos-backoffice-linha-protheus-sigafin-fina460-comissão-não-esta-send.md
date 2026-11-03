---
article_id: 33668038816407
category: Financeiro - Comissão
content_hash: f9cedb927c84d0a6c3b4cc196a75b4620ed73ac33cf57e363e7b834cb7d2af9f
fetched_at: '2026-06-28T22:37:50.812761+00:00'
product: protheus
section_id: 26655771327895
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA460 - Comissão
  não esta sendo gerada com base no título liquidado
type: support-article
updated_at: '2025-07-24T11:12:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33668038816407-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA460-Comiss%C3%A3o-n%C3%A3o-esta-sendo-gerada-com-base-no-t%C3%ADtulo-liquidado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33668038790295) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
A comissão não está sendo gerada com base no título liquidado. Como proceder para corrigir essa situação?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – Todas as releases   
  
**Solução**  
Os campos referentes à base de cálculo e ao valor de comissão a ser pago ao vendedor não são gravados na tabela de Contas a Receber (SE1) quando os títulos têm origem na rotina de Liquidação (FINA460). Nesses casos, o sistema considera os dados do título original ('Pai') para realizar o cálculo correto da comissão e da respectiva base, assegurando que os valores sejam apurados e processados de forma adequada.

**Saiba mais**

[**FINA460 - Liquidação a receber**](https://tdn.totvs.com/pages/viewpage.action?pageId=545236275#FINA460Liquida%C3%A7%C3%A3oareceberP12-09.COMISS%C3%83O)
