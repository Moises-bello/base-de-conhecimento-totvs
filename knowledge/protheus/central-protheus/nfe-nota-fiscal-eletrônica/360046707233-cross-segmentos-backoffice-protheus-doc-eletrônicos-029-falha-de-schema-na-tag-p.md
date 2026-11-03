---
article_id: 360046707233
category: NFe - Nota Fiscal Eletrônica
content_hash: e943c440e97a2e7c6bc84cb688aa19b592d452b81196729f572143adcc0ff7c0
fetched_at: '2026-06-28T22:40:00.399255+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 029 : Falha de
  schema na Tag pRedBc'
type: support-article
updated_at: '2021-10-11T15:21:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046707233--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-029-Falha-de-schema-na-Tag-pRedBc
---

**Dúvida**Como solucionar a falha de Schema referente a TAG pRedBc ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

1 - Ao gerar falha de Schema referente ao **pRedBc** verifique se o seu XML gerou conforme o exemplo abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360065482174/mceclip0.png)

2- Conforme o XML acima não foi gerada a **TAG  pRedBC** que é obrigatória ao utilizar a situação tributária **20, 70 ou 90** do IMCS.

3- Para a correção preencher o  campo no TES **% red. do ICMS "F4\_BASEICM"**para **o ICMS normal**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080363753/mceclip0.png)

4-  Caso tenha calculo de ICMS-ST para a correção preencher o  campo no TES **% red. do ICMS ST "F4\_BSICMS-St"**

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080364253/mceclip2.png)**

5- Se a empresa utilizar Redução via exceção fiscal preencher o campo **% red. do ICMS** "**F7\_MARGEM"**

**para o ICMS normal**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080364733/mceclip3.png)

6- Se a empresa utilizar Redução via exceção fiscal e caso tenha ICMS-ST preencher o campo **% red. do ICMS ST**  **% red. do ICMS** "**F7\_BSICMST"**

**![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079245494/mceclip4.png)**

7- Após isso, **exclua a nota** e gere novamente.

8- Caso a situação tributária da nota esteja errada, alterar no  **TES** no campo **Sit. trib. ICMS** **(F4\_SITTRIB) para um CST diferente de 20, 70 ou 90.**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041920134/mceclip2.png)

9- Após isso, **exclua a nota** e gere novamente. Se for utilizar o mesmo pedido digite novamente o TES para que a situação tributária seja atualizada no pedido de venda.

* **Saiba Mais:**

1- Caso seja nota com a s**ituação tributária 90** no qual a nota não possui valor do ICMS conforme o exemplo abaixo:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360065483134/mceclip1.png)

2- Essa falha de schema acontece devido a TAG **pRedBC não ter o "zero".**  
  
Houve correção no **fonte do NFESEFAZ** que consta no link abaixo:  
  
[MP - NFE - Documentos Eletrônicos NFe / NFSe / MDFe / MDe](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043005493)   
  
  
3- Aplique a patch e **Compile o NFESEFAZ**

4- Após isso, **exclua a nota** e gere novamente.
