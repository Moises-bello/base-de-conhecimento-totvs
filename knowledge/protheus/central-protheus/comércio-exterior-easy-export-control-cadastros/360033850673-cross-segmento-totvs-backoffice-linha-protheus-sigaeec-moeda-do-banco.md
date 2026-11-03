---
article_id: 360033850673
category: Comércio Exterior - Easy Export Control - Cadastros
content_hash: b3cfa545ca67c03341ebf07077eba196e925ee131a10176a86f4bab468b12a17
fetched_at: '2026-06-28T22:36:57.366907+00:00'
product: protheus
section_id: 1500001549302
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Moeda do Banco
type: support-article
updated_at: '2022-06-09T20:01:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033850673-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Moeda-do-Banco
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Ao liquidar câmbio apresenta a mensagem: Moeda cadastrada  no banco diverge com a informada no cadastro de Moedas, como ajustar?

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043599653/mceclip0.png)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – Todas versões  
  
**Solução**Acesse o cadastro de bancos tabela SA6 e verifique a moeda informada no campo A6\_MOEDA, e se o campo A6\_MOEEASY está referenciado com a mesma moeda informada no campo moeda, caso não, faça o ajuste e realize o procedimento novamente.

![](https://totvssuporte.zendesk.com/attachments/token/AJ7TEAn88ORjm7fhlohMUbO4F/?name=inline94672884.png)​![](https://totvssuporte.zendesk.com/attachments/token/tIw8MGYxV0KcIu3dvICMpwjPf/?name=inline-1844551846.png)

​ 

É necessário também que para o símbolo da moeda utilizada no campo A6\_MOEEASY, seja informado no cadastro de moeda (SYF), o campo YF\_MOEFAT.
