---
article_id: 360045025034
category: NFe - Nota Fiscal Eletrônica
content_hash: 6ce0ccdb47d2c3390355f763059f8c72e10b63bf442b2e9803d0c71fe5475b39
fetched_at: '2026-06-28T22:40:03.158229+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  029: Falha de
  schema nas Tags PIS e COFINS'
type: support-article
updated_at: '2021-07-28T13:31:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045025034-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-029-Falha-de-schema-nas-Tags-PIS-e-COFINS
---

**Dúvida**Como solucionar a falha de Schema referente as TAGs PIS e COFINS ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

1 - Ao gerar **falha de Schema referente ao PIS e COFINS** verifique se o seu XML gerou conforme o exemplo abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360063165213/mceclip0.png)

2- Conforme o XML acima não foi preenchido a situação tributária do **Pis e do Cofins** que é obrigatória.

3- Para a correção preencher o CST do PIS e do Cofins, campo do PIS Sit. Trib. Pis **"F4\_CSTPIS"** o campo do cofins Sit. Trib. Cof. **"F4\_CSTCOF" .**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360063165533/mceclip1.png)

4- Após isso, **exclua a nota** e gere novamente.
