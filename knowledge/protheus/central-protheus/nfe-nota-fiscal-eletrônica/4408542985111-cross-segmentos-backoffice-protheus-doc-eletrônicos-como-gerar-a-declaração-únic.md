---
article_id: 4408542985111
category: NFe - Nota Fiscal Eletrônica
content_hash: 3256f72651cd727c778ac3f18c52ed8e7bcfa62c3c49511aacd415534688ff63
fetched_at: '2026-06-28T22:40:01.662122+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar a Declaração
  Única de Importação (DUIMP)'
type: support-article
updated_at: '2021-09-16T18:34:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408542985111--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-a-Declara%C3%A7%C3%A3o-%C3%9Anica-de-Importa%C3%A7%C3%A3o-DUIMP
---

**Dúvida**

Como gerar a Declaração Única de Importação (DUIMP) ?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

**1-** Quando **não usa integração** com o **módulo SIGAEIC é necessário que o parâmetro MV\_EASY= N**

**![20201201_145829.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360101037393/20201201_145829.gif)**

**2-** Acesse a rotina ****Livros Fiscais**-> **Atualizações**->**Movimentos**->**NF manual de Entrada**->**Outras ações**->**Complementos**->**Importação:****

****![20201201_145142.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360101036933/20201201_145142.gif)****

3 - Fazer o complemento de **importação nos Livros fiscais e preencher o campo** **CD5\_NDI - No. da DI/DA.**

![20210916_110449.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4408761481879/20210916_110449.gif)

* **Saiba mais:**

Aumentamos o campo **CD5\_NDI  -** Número do Documento de Importação (DI/DSI/DA) para até 15 caracteres, assim será possível registrar informações da **Declaração Única de Importação (DUIMP).**

**![CD5_NDI.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4408768814615/CD5_NDI.JPG)**

[Clique Aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=627094959)

![ndi.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4408778961047/ndi.JPG)

* Para que o campo seja **Aumentado realizar as atualizações do link abaixo:**

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Nota técnica 2020.005](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052495714)
