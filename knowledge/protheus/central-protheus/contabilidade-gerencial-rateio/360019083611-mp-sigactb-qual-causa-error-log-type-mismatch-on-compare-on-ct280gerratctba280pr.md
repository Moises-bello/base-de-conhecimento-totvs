---
article_id: 360019083611
category: Contabilidade Gerencial - Rateio
content_hash: f1476f6011b790ed0f0f863b6285627643b1a17edb097805dc49c9ffde227d72
fetched_at: '2026-06-28T22:40:35.590106+00:00'
product: protheus
section_id: 1500001548962
source: central-protheus
title: 'MP-SIGACTB QUAL CAUSA ERROR LOG: type mismatch on compare  on CT280GERRAT(CTBA280.PRW)?'
type: support-article
updated_at: '2021-04-28T15:25:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019083611-MP-SIGACTB-QUAL-CAUSA-ERROR-LOG-type-mismatch-on-compare-on-CT280GERRAT-CTBA280-PRW
---

**Dúvida**MP-SIGACTB QUAL CAUSA ERROR LOG: type mismatch on compare on CT280GERRAT(CTBA280.PRW)?

**Ambiente**Microsiga Protheus  – Contabilidade Gerencial – A partir da versão 11.80]  
  
   
**Solução**

Este erro esta ocorrendo pois não foi encontrada a pergunta 14 (Atualiza Saldo ?) Avalie no CONFIGURADOR o grupo de perguntas CTB280, a ausência desta pergunta.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360014778771/mceclip0.png)

Segue abaixo exemplo das telas do configurador conforme o padrão, para comparar com sua base demonstrando as perguntas da rotina.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360014748912/mceclip1.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014749312/mceclip2.png)

Identificando a ausência das perguntas, orientamos aplicar o UPDDISTR para atualização do dicionário de dados.

![](https://totvssuporte.zendesk.com/attachments/token/22yzX0RnC852lFjQfvSn2iu3L/?name=inline349976049.png)
