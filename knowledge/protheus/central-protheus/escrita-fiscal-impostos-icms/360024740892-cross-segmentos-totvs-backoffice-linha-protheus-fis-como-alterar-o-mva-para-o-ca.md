---
article_id: 360024740892
category: Escrita Fiscal - Impostos - ICMS
content_hash: 3a2bf31fc8352564cdff7e6207f5df6838630fa613d2d8fa42a1dba2f71fa482
fetched_at: '2026-06-28T22:39:24.106271+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS -  Como alterar o MVA
  para o calculo do ICMS ST?
type: support-article
updated_at: '2021-07-28T02:14:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024740892-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-alterar-o-MVA-para-o-calculo-do-ICMS-ST
---

**Dúvida**

Como alterar o MVA para o calculo do ICMS ST?  
  
**Ambiente**

Protheus -Faturamento - Compras - A partir da versão 11.80

**Solução**

Temos três opções para alterar o MVA para o calculo do ICMS ST, essa alteração é feita de forma manual.

1) UF x UF  - FISA080

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023423891/mceclip0.png)

Campo:  MVA (CFC\_MARGEM)

2) Exceção fiscal

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023384912/mceclip1.png)

Campo: F7\_MARGEM

Quando for para entradas configurar o campo UF busca = origem

3) Cadastro de produtos

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023385412/mceclip2.png)

B1\_PICMRET = Saídas

B1\_PICMENT = Entradas
