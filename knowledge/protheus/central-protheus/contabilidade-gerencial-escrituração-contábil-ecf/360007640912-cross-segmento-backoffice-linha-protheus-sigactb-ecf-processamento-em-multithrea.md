---
article_id: 360007640912
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 74bc5e8bbbf3fff081cdb998aa079e8864972e3428fac350bfe3ec43f7ab2609
fetched_at: '2026-06-28T22:40:47.759189+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECF - Processamento
  em MultiThreads
type: support-article
updated_at: '2023-03-23T11:55:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007640912-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-Processamento-em-MultiThreads
---

**Dúvida**

Tem alguma forma de gerar o ECF em varias Threads para melhorar a performance?

**Ambiente**

Protheus – Contabilidade Gerencial – 12.1.17  
  
   
**Solução**

Para sanar esta dúvida, verifique a utilização do parâmetro MV\_TAFMTOF na seguinte documentação do tdn: <http://tdn.totvs.com/pages/releaseview.action?pageId=240288717>

Através deste parâmetro é possível determinar quantas threads devem ser utilizadas para a geração dos arquivos magnéticos das obrigações fiscais do TAF.
