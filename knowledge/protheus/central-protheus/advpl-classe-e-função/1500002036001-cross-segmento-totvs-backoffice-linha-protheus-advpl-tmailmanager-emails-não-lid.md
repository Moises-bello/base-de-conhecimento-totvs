---
article_id: 1500002036001
category: ADVPL - Classe e Função
content_hash: 3b71784644be3cb47a4cee91158fe13beb58ead1d87af6533b4a9d64d5acbcce
fetched_at: '2026-06-28T22:40:18.105945+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - TmailManager: Emails
  não lidos'
type: support-article
updated_at: '2022-06-14T17:19:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002036001-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-TmailManager-Emails-n%C3%A3o-lidos
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:02:00 min****Dúvida**Existe algum recurso ou alguma forma de capturarmos apenas dos e-mails não lido utilizando a classe ***TmailManager()***?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – AdvPL– A partir da versão 12  
  
**Solução**Está informação ou possamos dizer *flags* de e-mails ( Novos ou recentes, lidos ou não lidos, deletados, e outros...), é a provedora que disponibiliza via cabeçalho, onde as classes (***TMailMessage()*** e ***TMailMng()***) existe os métodos:  
**[TMailManager:StartGetAllMsgHeader()](https://tdn.totvs.com/display/tec/TMailManager%3AStartGetAllMsgHeader)**  
**[TMailMng:GetMsgHeader()](https://tdn.totvs.com/display/tec/TMailMng%3AGetMsgHeader)**  
  
Estes recurso só através de protocolo ***IMAP*** e também é necessário verificar quanto a provedora se disponibiliza as flags nos cabeçalhos para este tratamento.  
  
**Saiba mais**  
**[TMailManager Métodos](https://tdn.totvs.com/pages/viewpage.action?pageId=89621146)**
