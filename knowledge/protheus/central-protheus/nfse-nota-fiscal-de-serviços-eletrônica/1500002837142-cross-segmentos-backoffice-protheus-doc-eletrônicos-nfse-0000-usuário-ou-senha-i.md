---
article_id: 1500002837142
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 75ef2acce581f9cd91f2fc9191c36f329994d7424cfa07bda3e019f28235f1a8
fetched_at: '2026-06-28T22:39:56.255602+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - 0000 - Usuário
  ou Senha Inválido(s)
type: support-article
updated_at: '2025-07-14T21:46:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002837142-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-0000-Usu%C3%A1rio-ou-Senha-Inv%C3%A1lido-s
---

**Dúvida**Ao transmitir uma nota fiscal de serviço ocorre a rejeição: **"0000 - Usuário ou Senha Inválido(s)."**

![Rejeicao_000.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360101518534/Rejeicao_000.PNG)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**A rejeição "0000 - Usuário ou Senha Inválido(s)" ocorre quando os campos **"Nome de usuário"** e **"Senha"** na ultima tela do wizard.config ficam **vazios** ou possuem um conteúdo **incorreto**.  
  
![05.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360103673633/05.jpg)  
  
Entre em contato com a prefeitura, informe que está emitindo notas **via webservice** e que precisa do **usuário e senha do webservice**.  
Preencha corretamente essas informações no wizard.config, retransmita e monitore a nota.
