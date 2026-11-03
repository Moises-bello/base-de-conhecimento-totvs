---
article_id: 4409771918487
category: Financeiro - Consultas / Relatórios
content_hash: bff59dbc34feb397dc58eea8aa7ba3113b4444db68c133114bba8837dccfab52
fetched_at: '2026-06-28T22:37:58.410271+00:00'
product: protheus
section_id: 1500001539561
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINR190 - O relatório
  está apresentando valor do Acréscimo na coluna Jur/Multa quando tem desconto no
  título
type: support-article
updated_at: '2021-09-30T19:34:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409771918487-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINR190-O-relat%C3%B3rio-est%C3%A1-apresentando-valor-do-Acr%C3%A9scimo-na-coluna-Jur-Multa-quando-tem-desconto-no-t%C3%ADtulo
---

**Dúvida** O Relatório de baixa está apresentando valor do Acréscimo na coluna Jur/Multa, quando tem desconto  no titulo?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro- FINR190 - Todas as versões  
  
**Solução**A partir da correção da **Patch DFINGRV-19892**

12.1.17:<https://r.totvs.io/p/1012067> ;  
12.1.23:<https://r.totvs.io/p/1012068> ;   
12.1.25:<https://r.totvs.io/p/1012069> ;  
12.1.27:<https://r.totvs.io/p/1012070> ;

O sistema começou apresentar no **Relatório de baixas FINR190,** na coluna **Jur/Multa** o valor do campo **Acréscimo** baixado, quando havia um desconto junto ao titulo.

**Importante**O sistema sempre gravou o valor do acréscimo no campo **E5\_VLJUROS**.

Na regra de mercado financeiro **Acrescimo/Juros/Multa** são tratados com a mesma finalidade.
