---
article_id: 360021640451
category: Escrita Fiscal - Impostos - Cálculos
content_hash: 81b6d937e5c9d527384dfd199f375e35aac20acd0598fa41de9e44f78bdea967
fetched_at: '2026-06-28T22:39:31.131301+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Ratear os impostos
  nas notas fiscais de saída -  Retenções
type: support-article
updated_at: '2021-07-29T14:01:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021640451-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Ratear-os-impostos-nas-notas-fiscais-de-sa%C3%ADda-Reten%C3%A7%C3%B5es
---

**Dúvida**Como ratear (ou não) os impostos que são calculados nas notas fiscais de saída através do módulo Faturamento?

**Ambiente**Protheus – Financeiro – A partir da versão 11.80  
   
**Solução**

Na gravação do documento de saída, para tratamento dos impostos financeiros devem ser observados os seguintes parâmetros:

**• MV\_RTIPESP**

• **MV\_RTIPFIN**

**Exemplo:**

• Se o parâmetro MV\_RTIPFIN estiver configurado com .T. e o parâmetro MV\_RTIPESP estiver configurado como 000000 ou 111111, no documento de saída, os impostos serão rateados em todas as parcelas. Caso esteja configurado como 222222, os impostos serão atribuídos na primeira parcela.

ou

• Quando o parâmetro MV\_RTIPFIN estiver configurado com .F. e parâmetro MV\_RTIPESP estiver como 000000 ou 222222, no documento de saída, os impostos serão atribuídos na primeira parcela. Caso esteja configurado como 111111, serão rateados em todas as parcelas.

Situação:

Cliente tem PCC e IR, mas somente o IR será considerado na primeira parcela, o cliente está com o parâmetro MV\_RTIPFIN = .T. O QUE FAZER?

R: MV\_RTIPFIN = .T. e MV\_RTIPESP = 000000

Para não ratear somente um imposto o cliente precisa compreender qual a posição do IR, neste caso é necessário verificar a sequência abaixo:

MV\_RTIPESP = 0         0         0        0        0        0

Pela ordem:    ISS    IRRF   INSS   CSLL    COF     PIS

Com isso, o parâmetro MV\_RTIPESP ficará desta forma:

MV\_RTIPESP = 020000
