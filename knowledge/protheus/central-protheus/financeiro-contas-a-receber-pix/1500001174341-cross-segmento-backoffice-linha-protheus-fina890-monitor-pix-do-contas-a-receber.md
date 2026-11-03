---
article_id: 1500001174341
category: Financeiro - Contas a Receber - PIX
content_hash: 53ef6f8b614891db0dc348170db361dd3f527909f8e9138c3de35b692f1b50b5
fetched_at: '2026-06-28T22:38:16.449824+00:00'
product: protheus
section_id: 1500001539301
source: central-protheus
title: Cross Segmento  Backoffice Linha Protheus - FINA890 - Monitor PIX do Contas
  a Receber
type: support-article
updated_at: '2025-05-27T11:44:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001174341-Cross-Segmento-Backoffice-Linha-Protheus-FINA890-Monitor-PIX-do-Contas-a-Receber
---

**Dúvida**O que é o Monitor PIX do Contas a Receber?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – Financeiro - FINA890 - A partir da versão 12.1.23  
  
**Solução**É uma nova rotina, do **Contas a Receber,** que será responsável por todo o controle de títulos que podem ser recebidos pela forma de pagamento **PIX**.   
A rotina deve ser inserida no Menu **Atualizações**, **Comunic. Bancária**. O seu código é **FINA890**, pois será incluído no menu padrão somente nas versões superiores à versão 12.1.27.  
Todo o título, gerado no módulo Financeiro ou Faturamento, que tenha o campo **Gera PIX** = Sim, estará automaticamente relacionado no **Monitor PIX**.  
Esta nova tabela que armazenará as informações dos títulos em **PIX** (**tabela F71**) deve ter o mesmo compartilhamento da tabela de títulos a **Receber** (tabela **SE1**) do ambiente.  
  
**Legendas dos títulos na rotina Monitor PIX**

![legenda_monitor_pix.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360102253553)  
  
**Saiba mais**  
[Pagamentos instantâneos - PIX](https://tdn.totvs.com/pages/releaseview.action?pageId=569478747#Pagamentosinstant%C3%A2neos-PIX-03.CONTASARECEBER)
