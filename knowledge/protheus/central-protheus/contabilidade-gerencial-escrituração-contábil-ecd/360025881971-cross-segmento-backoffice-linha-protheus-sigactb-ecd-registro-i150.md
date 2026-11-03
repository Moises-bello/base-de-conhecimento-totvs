---
article_id: 360025881971
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: 2a63979efdd368632d1b16e90cf4580bd41baf911778e5367f95478923aef444
fetched_at: '2026-06-28T22:40:44.723226+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECD REGISTRO I150
type: support-article
updated_at: '2023-06-13T18:58:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025881971-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-REGISTRO-I150
---

**Dúvida**Como é gerado o registro I150?  
   
 **Ambiente**Protheus – Contabilidade Gerencial – A partir da versão 11.80  
  
   
**Solução**O registro I150  identifica o período relativo aos saldos contábeis. A periodicidade do saldo é, no máximo, mensal, mas poderá conter fração de mês no caso de situação especial (cisão, fusão, incorporação ou extinção).

 No protheus esse registro é composto conforme calendário contábil selecionado na wizard da central de escrituração (CTBS001)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024781752/mceclip0.png)

Em caso de situação especial ou entrega trimestral, na rotina CTBA010 (CADASTRO + CALENDÁRIO CONTÁBIL).

Crie um calendário conforme período necessário  (caso não possua) e

informe na wizard da ECD ao gerar uma revisão.

\*Importante! Não precisa fazer amarração com moeda.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024793891/mceclip1.png)
