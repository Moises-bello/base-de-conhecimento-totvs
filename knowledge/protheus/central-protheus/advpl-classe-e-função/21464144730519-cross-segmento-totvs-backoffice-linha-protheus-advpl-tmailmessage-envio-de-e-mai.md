---
article_id: 21464144730519
category: ADVPL - Classe e Função
content_hash: 7c30567cac8efe5ccb6a727eea0ee600891e48c4e5feb59d664b77651bbecfee
fetched_at: '2026-06-28T22:40:14.219541+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - TMailMessage envio
  de e-mail para mais de um destinatário
type: support-article
updated_at: '2024-02-19T19:01:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21464144730519-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-TMailMessage-envio-de-e-mail-para-mais-de-um-destinat%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21464159538199) Tempo aproximado para leitura: **00****:01:00 min**

**Dúvida**Classe *TMailMessage* não está enviando e-mail para mais de um destinatário.  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 12  
  
**Solução**

Ao configurar o disparo de e-mail para mais de um usuário deve separar as contas de e-mail por ponto e virgula (**;**), porem em alguns casos como, por exemplo, o provedor Amazon-Ses aceita apenas o caractere virgula (**,**) como separador.  
  
**Exemplos**

Outlook:

oMessage:cTo := "conta1@seuprovedor.com;conta2@seuprovedor.com;conta3@seuprovedor.com"

Amazon-Ses:

oMessage:cTo := "conta1@seuprovedor.com,conta2@seuprovedor.com,conta3@seuprovedor.com"

 

**Saiba mais**

[TMailMessage](https://tdn.totvs.com/display/tec/TMailMessage%3AcTo)

[TMailManager](https://tdn.totvs.com/display/tec/Classe+TMailManager)
