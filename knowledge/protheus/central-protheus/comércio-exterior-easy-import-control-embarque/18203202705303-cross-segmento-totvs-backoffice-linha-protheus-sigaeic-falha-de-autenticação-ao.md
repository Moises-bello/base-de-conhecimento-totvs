---
article_id: 18203202705303
category: Comércio Exterior - Easy Import Control - Embarque
content_hash: d098657247f39b6478e1e764676b0619b32407bd2a0c1381b3643cba731f5dde
fetched_at: '2026-06-28T22:39:48.789149+00:00'
product: protheus
section_id: 1500001538381
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus  - SIGAEIC - Falha de autenticação
  ao enviar para o despachante o e-mail do numerário
type: support-article
updated_at: '2023-11-07T11:34:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18203202705303-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Falha-de-autentica%C3%A7%C3%A3o-ao-enviar-para-o-despachante-o-e-mail-do-numer%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18203214301847) Tempo aproximado para leitura: **05:00 min** **Dúvida**Ao efetuar a Solicitação de Numerário, está ocorrendo falha de autenticação ao enviar o e-mail para o despachante.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
  
**Solução**Para a correta parametrização do disparo de e-mails, pedimos por gentileza que valide os seguintes parâmetros, tendo como base uma conta "**GMAIL"**por exemplo:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18202756620951)

Um detalhe importante sobre contas do "**GMAIL"**é que para utilizá-las através do Protheus é necessário configurar a utilização da "**senhas de app**" conforme a seguinte documentação: [Application Server - Uso de e-mail com GMail](https://tdn.totvs.com/display/tec/Application+Server+-+Uso+de+e-mail+com+GMail?spaceEditingRestriction=true)  
  
Após gerado a "**senha de app**", é necessário informar a mesma dentro dos parâmetros "**MV\_RELAPSW**" e "**MV\_RELPSW**".  
  
**Saiba mais:**  
[Application Server - Uso de e-mail com GMail](https://tdn.totvs.com/display/tec/Application+Server+-+Uso+de+e-mail+com+GMail?spaceEditingRestriction=true)  
[Configuração do servidor de email](https://tdn.totvs.com/pages/releaseview.action?pageId=416852555)  
[E-mail numerário](https://tdn.totvs.com/pages/releaseview.action?pageId=454832898)
