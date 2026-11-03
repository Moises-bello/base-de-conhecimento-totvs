---
article_id: 360006975351
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 1bfc0834918684dae2f1de5da60f71d09a53b67a35f76ed0cad31d736d832b49
fetched_at: '2026-06-28T22:40:47.319510+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECF - Array out of bounds
  ( 1 of 0 ) on PARAMECF(CTBS101.PRW)
type: support-article
updated_at: '2022-07-18T12:15:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006975351-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-Array-out-of-bounds-1-of-0-on-PARAMECF-CTBS101-PRW
---

**Ocorrência**

* Ao tentar Incluir um revisão da ECF é apresentado o error abaixo

TOTVS Build 7.00.131227A-20170721 NG   
THREAD ERROR ([6608], Usuário, SPODxxxx) 18/06/2018   
array out of bounds ( 1 of 0 ) on PARAMECF(CTBS101.PRW) 30/05/2018 09:45:22 line : 306   
  
**Ambiente**

#### Cross Segmento - Backoffice Linha Protheus - SIGACTB -  a partir versão P12.1.17 **Solução**Verifique o Índice CS0

![1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360007270931/1.png)

Verifique na Tabela SX2 a tabela CS0

![2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360007270971/2.png)
