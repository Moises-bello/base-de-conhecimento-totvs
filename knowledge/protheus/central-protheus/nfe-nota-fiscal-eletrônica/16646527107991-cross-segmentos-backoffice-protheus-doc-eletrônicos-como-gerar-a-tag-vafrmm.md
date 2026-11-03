---
article_id: 16646527107991
category: NFe - Nota Fiscal Eletrônica
content_hash: cb2d14cee8ebc0051a57b89f5dd39002d505161eb405228bded276058431ac8a
fetched_at: '2026-06-28T22:40:06.677701+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar a TAG
  vAFRMM
type: support-article
updated_at: '2025-06-13T12:29:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16646527107991-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-a-TAG-vAFRMM
---

**Dúvida**Qual campo é preenchido para gerar a TAG vAFRMM  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

**1-** Quando **não é utilizada a integração** com o **módulo SIGAEIC é necessário que o parâmetro MV\_EASY= N**

**![20201201_145829.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/16646536167831)**

**2-** Acesse a rotina ****Livros Fiscais**-> **Atualizações**->**Movimentos**->**NF manual de Entrada**->**Outras ações**->**Complementos**->**Importação:****

****![20201201_145142.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/16646504618903)****

3. Preencher o campo no complemento de **importação nos Livros fiscais.** **CD5\_VTRANS - Via de Transporte internacional informada na DI.****1=**Marítima;

![REBOQUE.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/16647104367895)

4- Preencher o campo no complemento de **importação nos Livros fiscais, Conforme o fonte do **NFESEFAZ e o preencher o campo** CD5\_VAFRMM**

* ***Validação da Sefaz:***

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16646894996119)
