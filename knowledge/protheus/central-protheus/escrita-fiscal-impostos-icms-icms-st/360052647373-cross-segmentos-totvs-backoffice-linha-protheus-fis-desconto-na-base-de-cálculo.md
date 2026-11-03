---
article_id: 360052647373
category: Escrita Fiscal - Impostos - ICMS - Icms St
content_hash: 4050f7252e308557de549f661cbe35d5b38cbfd22ecd0bb2509c5eb010e013c6
fetched_at: '2026-06-28T22:39:20.478124+00:00'
product: protheus
section_id: 1500001538721
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Desconto na base
  de cálculo do ICMS ST
type: support-article
updated_at: '2021-07-13T17:30:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052647373-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Desconto-na-base-de-c%C3%A1lculo-do-ICMS-ST
---

**Dúvida**A base de calculo do ICMS ST está realizando o desconto cadastrado indevidamente.

**Ambiente**Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

Mesmo alterando o cadastro do TES no campo "Bs.ICMS ST" - F4\_STDESC = 2 - Valor Bruto, o Protheus continua realizando o desconto da base de cálculo.

Para o sistema considerar o valor Bruto na base de calculo do ICMS ST, será necessário configurar o parâmetro MV\_SOLBRUT = T.
