---
article_id: 13766432711703
category: NFe - Nota Fiscal Eletrônica
content_hash: bac19dc9e10704bef2ac6354408239aa613cd022fee0ec2f3ccd1f8753e19ba3
fetched_at: '2026-06-28T22:40:05.114241+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 546 Rejeição: NF-e
  de devolução com valor do ICMS superior a NF-e devolvida'
type: support-article
updated_at: '2025-06-17T19:31:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13766432711703-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-546-Rejei%C3%A7%C3%A3o-NF-e-de-devolu%C3%A7%C3%A3o-com-valor-do-ICMS-superior-a-NF-e-devolvida
---

**Dúvida**Como solucionar 546 Rejeição: NF-e de devolução com valor do ICMS superior a NF-e devolvida ?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões.

Cross Segmentos - TSS - a partir da versão 12

**Solução**

1. Acessar a  **rotina de transmissão SPEDNFE;**

![nfesefaz.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17384454671511)

2. Clique em **Outras ações -> Monitor -> faixa ->** Digite o número e série da nota;

**![monitor_faixa.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17384487341335)**

3. Clique no **botão Schema; Copie e Cole o conteúdo completo do XML.**

![546_rejeicao.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/13767757772055)

4. Verifique se o ***valor da TAG vICMS*** e igual da nota de origem, conforme o XML de exemplo:

* ***XML da nota de origem:***

![icms_origem.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/13766648441495)

* ***XML da nota de devolução:***

![saida_vicm.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/13766635308695)

5. Para notas com os valores corretos na rejeição***546 temos um parecer da consultoria de segmentos:***

***[Clique Aqui](https://www.totvs.com/blog/fiscal-clientes/nt-2022-005-v-1-10-rejeicao-nas-nf-e-de-devolucao/)***

6. Se sua empresa for do ***Regime normal e a devolução de emitente do Simples Nacional,*** realizar as configurações link abaixo:

***[Clique Aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=619742950)***

* ***Validação da Sefaz:***

***![](https://centraldeatendimento.totvs.com/hc/article_attachments/13766489817239)***
