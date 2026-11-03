---
article_id: 4408533637399
category: NFe - Nota Fiscal Eletrônica
content_hash: 9a26edd078356885d66fc133ac88a2325ca592f6e05e7a039746eb9bdbc12b63
fetched_at: '2026-06-28T22:40:01.709282+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar a TAG
  NDraw'
type: support-article
updated_at: '2022-03-22T19:01:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408533637399--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-a-TAG-NDraw
---

**Dúvida**Como gerar a TAG NDraw  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

![ndraw.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4408778062999/ndraw.JPG)

**1-** Quando **não usa integração** com o **módulo SIGAEIC é necessário que o parâmetro MV\_EASY= N**

**![20201201_145829.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360101037393/20201201_145829.gif)**

**2-** Acesse a rotina ****Livros Fiscais**-> **Atualizações**->**Movimentos**->**NF manual de Entrada**->**Outras ações**->**Complementos**->**Importação:****

****![20201201_145142.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360101036933/20201201_145142.gif)****

3 - Fazer o complemento de **importação nos Livros fiscais e preencher o campo** **CD5\_ACDRAW**

![ndraw.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4408778619927/ndraw.gif)

* **Saiba mais:**

Na **nota técnica 2020.005** o campo  passa a ser **Alfanumérico e a quantidade de caracteres permitida aumentou para até 20.**

[Clique Aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=624111487)

* Para que o campo seja **Alfanumérico é necessário realizar as atualizações do link abaixo:**

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Nota técnica 2020.005](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052495714)
