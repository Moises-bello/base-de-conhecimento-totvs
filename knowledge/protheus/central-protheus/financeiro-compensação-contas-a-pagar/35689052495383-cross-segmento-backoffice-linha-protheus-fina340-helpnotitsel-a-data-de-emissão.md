---
article_id: 35689052495383
category: Financeiro - Compensação Contas a Pagar
content_hash: 7bdf118e4a9683707f3f8f3a0007f4dfcd75634c070af42a41491da49df2b0ba
fetched_at: '2026-06-28T22:37:33.637218+00:00'
product: protheus
section_id: 35057559197335
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - FINA340 - HELP:NOTITSEL - A data
  de emissão do titulo(EMIS1) posicionado não poderá ser maior que a data base do
  sistema
type: support-article
updated_at: '2025-10-17T19:37:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35689052495383-Cross-Segmento-Backoffice-Linha-Protheus-FINA340-HELP-NOTITSEL-A-data-de-emiss%C3%A3o-do-titulo-EMIS1-posicionado-n%C3%A3o-poder%C3%A1-ser-maior-que-a-data-base-do-sistema
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35689067870743) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Não estou conseguindo realizar a compensação do PA com a NF. É apresentado o **Help: NOTITSEL** - A data de emissão do título (EMIS1) posicionado não poderá ser maior que a data base do sistema.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.

**Solução**  
O erro ocorre devido ao fato de que a data-base do sistema é posterior à data de emissão do título a ser compensado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35689687224983)

Exemplo:

* Data de emissão no sistema: 13/10/2025
* Data de emissão da NF: 13/10/2025
* Data de emissão do PA: 14/10/2025

O PA foi emitido em 14/10/2025, e a data-base do sistema é 13/10/2025. Portanto, o PA não existia nessa data. Por essa razão, o Help só poderá efetuar a compensação do PA com datas de emissão posteriores à sua data de geração.
