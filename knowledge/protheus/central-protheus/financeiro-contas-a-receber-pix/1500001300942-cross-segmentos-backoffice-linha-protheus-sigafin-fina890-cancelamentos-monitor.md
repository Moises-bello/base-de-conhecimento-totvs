---
article_id: 1500001300942
category: Financeiro - Contas a Receber - PIX
content_hash: 9f829c44ac227ffbcffc6788a40c1314b318024f292363f25db8620d60a86ff0
fetched_at: '2026-06-28T22:38:16.516569+00:00'
product: protheus
section_id: 1500001539301
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA890 - Cancelamentos
  Monitor PIX
type: support-article
updated_at: '2022-04-29T19:31:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001300942-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA890-Cancelamentos-Monitor-PIX
---

**Dúvida**O que são cancelamentos no monitor PIX?  
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus - Financeiro - FINA890 - A partir das versões 12.1.25  
  
**Solução**O caso mais básico de cancelamento é quando se altera o complemento do título, na aba **PIX** para **Gera PIX** = Não ( **Alteração do título** -> **Outras Ações** -> **Complemento de Título**).   
Dessa forma, no **Monitor PIX** (**FINA890**) o título irá alterar a legenda para 6 (cancelamento solicitado), sendo necessário o envio do arquivo de cancelamento ao banco, para que altere para a legenda 7 ( cancelamento enviado ao banco).   
Após se efetuar o retorno do arquivo do banco, pela rotina de **Retorno de Cobranças** (**FINA200**), no **Monitor PIX**, a legenda irá alterar para 8 (Cancelado).  
  
**Exemplo de Alteração do campo****![cancelamento_pix2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001239082/cancelamento_pix2.PNG)**

**Exemplo de legenda de Cancelamento do Monitor PIX**

**![cancelamento_pix.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360100144554/cancelamento_pix.PNG)** **Saiba mais**[Pagamentos](https://tdn.totvs.com/pages/releaseview.action?pageId=569478747) [instantâneo](https://tdn.totvs.com/pages/releaseview.action?pageId=569478747)[s](https://tdn.totvs.com/pages/releaseview.action?pageId=569478747) [- PIX](https://tdn.totvs.com/pages/releaseview.action?pageId=569478747)
