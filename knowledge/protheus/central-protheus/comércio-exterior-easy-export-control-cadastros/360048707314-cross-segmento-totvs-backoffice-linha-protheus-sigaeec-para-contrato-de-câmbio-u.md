---
article_id: 360048707314
category: Comércio Exterior - Easy Export Control - Cadastros
content_hash: d775b319085587e10e9d2a88a2ed82b9d120f2c9f5fee4ca6cdcf089aca12587
fetched_at: '2026-06-28T22:36:57.373751+00:00'
product: protheus
section_id: 1500001549302
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Para contrato
  de câmbio, utilize um banco em moeda nacional.
type: support-article
updated_at: '2022-06-09T17:16:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048707314-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Para-contrato-de-c%C3%A2mbio-utilize-um-banco-em-moeda-nacional
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min****Dúvida**Ao liquidar câmbio apresenta a mensagem: Moeda cadastrada  no banco diverge com a informada no cadastro de Moedas, como ajustar?

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360073681573/mceclip1.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – Todas versões  
  
**Solução**Para que a mensagem não seja apresentada para o tipo de recebimento antecipado de contrato de câmbio, o campo **A6\_MOEDA** precisa estar configurado com o Numeral 1 e o campo **A6\_MOEEASY** com o conteúdo R$, caso estejam com outra moeda a mensagem será apresentada.  
Acesse o cadastro de bancos tabela SA6 e verifique a moeda informada no campo A6\_MOEDA, e se o campo **A6\_MOEEASY** está referenciado com a mesma moeda informada no campo moeda, caso não, faça o ajuste e realize o procedimento novamente.

![](https://totvssuporte.zendesk.com/attachments/token/AJ7TEAn88ORjm7fhlohMUbO4F/?name=inline94672884.png)​![](https://totvssuporte.zendesk.com/attachments/token/tIw8MGYxV0KcIu3dvICMpwjPf/?name=inline-1844551846.png)​ 

É necessário também que para o símbolo da moeda utilizada no campo **A6\_MOEEASY**, seja informado no cadastro de moeda (SYF), o campo **YF\_MOEFAT**.
