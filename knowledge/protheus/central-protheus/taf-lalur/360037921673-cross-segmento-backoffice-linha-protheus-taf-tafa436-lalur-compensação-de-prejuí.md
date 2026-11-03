---
article_id: 360037921673
category: TAF - Lalur
content_hash: e272aee0ed6671f2583f76d7edb9d3aaaa738a0291e316a6257c66787ca12bdc
fetched_at: '2026-06-28T22:41:31.053268+00:00'
product: protheus
section_id: 4404425263639
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - TAF - TAFA436 - Lalur Compensação
  de prejuízo parte B com reflexo na parte A
type: support-article
updated_at: '2021-09-09T11:48:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037921673-Cross-Segmento-Backoffice-Linha-Protheus-TAF-TAFA436-Lalur-Compensa%C3%A7%C3%A3o-de-preju%C3%ADzo-parte-B-com-reflexo-na-parte-A
---

**Dúvida** Compensação de prejuízo parte B com reflexo na parte A  
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus – TAF – A partir da versão 11.80  
  
**Solução**Rotina TAFA436, cadastro conta na parte B com o prejuízo anterior.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007458061/mceclip4.png)

No cadastro do Evento tributário (rotina TAFA433) aba "compensação de prejuízo/Base negativa" informamos a conta da parte B, código para ficha de reflexo na parte A, o percentual de compensação e qual o limite que o percentual será aplicado.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007296342/mceclip3.png)

Na simulação (TAFA433) e na apuração (TAFA444) quando é apurado **Lucro no Período** há possibilidade de compensar um prejuízo anterior.

Na simulação, note que o valor da compensação é 30% do valor da Receita Operacional, conforme limite definido no evento tributário.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007442701/mceclip0.png)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007292022/mceclip1.png)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007447021/mceclip2.png)

Lalur:

[MP\_SIGACTB LALUR/LACS: CADASTRO, APURAÇÃO E INTEGRAÇÃO COM ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018585831-MP-SIGACTB-LALUR-LACS-CADASTRO-APURA%C3%87%C3%83O-E-INTEGRA%C3%87%C3%83O-COM-ECF?source=search)
