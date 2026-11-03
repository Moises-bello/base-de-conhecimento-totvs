---
article_id: 20126176309527
category: Financeiro - Comissão
content_hash: e2b3563b1c3f20d344bcb9e5ebd0c56222e87476ccaa8daffb11eb1391f3a455
fetched_at: '2026-06-28T22:37:50.680220+00:00'
product: protheus
section_id: 26655771327895
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN -  Nos títulos liquidados
  o campo comissão apresenta em branco
type: support-article
updated_at: '2025-07-30T20:45:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20126176309527-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Nos-t%C3%ADtulos-liquidados-o-campo-comiss%C3%A3o-apresenta-em-branco
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20126192671895) Tempo aproximado para leitura: **00:03 min****Dúvida**Ao realizar uma liquidação os campos de vendedor e comissão apresenta em branco.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA460 - Todas as versões  
  
**Solução**A gravação dos campos referentes à base de cálculo e valor a ser pago de comissão para o vendedor na tabela **Contas a Receber** (**SE1**) não terão seus valores gravados quando a origem dos títulos for da rotina **Liquidação** (**FINA460**). Para o correto cálculo da comissão, bem como a base de comissão, a rotina irá buscar os valores no título "**Pai**" e realizar os devidos cálculos.

**Saiba Mais**  
[Liquidação Receber - FINA460](https://tdn.totvs.com/pages/releaseview.action?pageId=545236275)

[Recalculo de comissão - FINA440](https://tdn.totvs.com/pages/releaseview.action?pageId=312162528)
