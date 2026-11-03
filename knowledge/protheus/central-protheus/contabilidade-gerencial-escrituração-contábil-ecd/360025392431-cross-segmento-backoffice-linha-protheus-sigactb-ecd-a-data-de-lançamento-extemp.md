---
article_id: 360025392431
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: 1ab73ef0963b051e5a3b35ecf23179c44b14c73730a00dd0a1aa73568307adf4
fetched_at: '2026-06-28T22:40:44.693984+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECD A DATA DE LANÇAMENTO
  EXTEMPORANEO (I200 DT_LCTO_EXT) DEVE SER ANTERIOR À DATA DE INICIO DA ESCRITURAÇÃO.
type: support-article
updated_at: '2022-05-18T10:29:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025392431-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-A-DATA-DE-LAN%C3%87AMENTO-EXTEMPORANEO-I200-DT-LCTO-EXT-DEVE-SER-ANTERIOR-%C3%80-DATA-DE-INICIO-DA-ESCRITURA%C3%87%C3%83O
---

**Ocorrência**

Ao gerar um lançamento X (extemporâneo) é gerado o seguinte erro no PGE:

"I200 - A DATA DE LANÇAMENTO EXTEMPORÂNEO (I200 DT\_LCTO\_EXT) DEVE SER ANTERIOR À DATA DE INICIO DA ESCRITURAÇÃO."

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023868192/mceclip0.png)  
   
 **Ambiente**Protheus– Contabilidade Gerencial– A partir da versão 11.80.  
   
 **Causa**

* Data do lançamento extemporâneo  (I200 DT\_LCTO\_EXT).

Dever ser anterior à data inicio da escrituração, isso porque lançamentos extemporâneos são referentes a períodos anteriores, caso não seja possível precisar a data a que se refiram os fatos do lançamento extemporâneo, informar a data de encerramento do exercício em que ocorreram esses fatos.

**Solução**

A data do lançamento contábil (CT2) deve ser no período da entrega, porem a DATA LANÇAMENTO EXTEMPORÂNEO (opção outras ações) deve ser anterior ao período de entrega da escrituração.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023873351/mceclip1.png)**

**Saiba mais:**

**<http://tdn.totvs.com/display/PROT/ECD_SPED_CONTABIL_Alteracoes_para_Leiaute_7_00>**
