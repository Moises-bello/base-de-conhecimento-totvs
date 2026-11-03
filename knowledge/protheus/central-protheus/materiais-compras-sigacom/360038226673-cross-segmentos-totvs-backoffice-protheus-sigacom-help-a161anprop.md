---
article_id: 360038226673
category: Materiais - Compras (SIGACOM)
content_hash: 169215c1907115ce70a634cbaf24310014c643c89c64395a033a8448981e0aa4
fetched_at: '2026-06-28T22:41:08.927936+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Help A161ANPROP
type: support-article
updated_at: '2022-05-12T21:21:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038226673-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Help-A161ANPROP
---

**Dúvida**

Help A161ANPROP

**Ambiente**  
Protheus – Compras – A partir da versão 12  
  
**Causa**

Na Análise de Cotação o sistema apresenta Help **A161ANPROP**

"Impossível sugerir proposta vencedora pois existem fornecedores sem preço unitário informado para um ou mais itens da proposta!" "Utilize o critério de avaliação por item ou informe preço unitário para todos os itens de todas as propostas para que a análise por proposta possa ser realizada."

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049537594/mceclip4.png)

O problema ocorre quando na rotina de *Análise de Cotação* (**MATA161**) no **F12** o pergunte da marcação automática está como **SIM** e a análise consta como **PROPOSTA**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049537394/mceclip1.png)

O sistema realiza a validação de somente prosseguir com a marcação dos vencedores caso os critérios da análise por proposta estiverem atendidos, pois a análise está em execução por proposta, ou seja o sistema consulta se todos os itens foram atualizados com relação aos valores:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360050427953/mceclip3.png)

**Solução**

Será possível prosseguir apenas se todos os itens forem atualizados os valores na rotina *Atualiza Cotações* (**MATA150**) ou se a análise for realizada por **ITEM** no pergunte **F12:**

**![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049538514/mceclip5.png)**
