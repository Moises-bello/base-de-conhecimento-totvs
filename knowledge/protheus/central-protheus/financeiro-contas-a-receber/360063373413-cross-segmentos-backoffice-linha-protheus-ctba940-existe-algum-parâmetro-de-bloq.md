---
article_id: 360063373413
category: Financeiro - Contas a Receber
content_hash: b383735321b7400c4debd5d9669c7566a29dc1bf574ab97c497b996b0687417d
fetched_at: '2026-06-28T22:38:13.872250+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - CTBA940 - Existe algum parâmetro
  de Bloqueio para desconciliar um título já conciliado a algum tempo
type: support-article
updated_at: '2025-02-05T19:40:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063373413-Cross-Segmentos-Backoffice-Linha-Protheus-CTBA940-Existe-algum-par%C3%A2metro-de-Bloqueio-para-desconciliar-um-t%C3%ADtulo-j%C3%A1-conciliado-a-algum-tempo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22702971962647)**Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**

Existe algum parâmetro de Bloqueio para desconciliar um título já conciliado há algum tempo?

**Exemplo**  
O parâmetro **MV\_DATAFIN** está configurado com o conteúdo 20200930, mas ao acessar o sistema com data base posterior ao dia 30/09/2020 está sendo permitido conciliar e/ou desconciliar movimentações bancárias.

**MV\_DATAFIN** = 20200930  
**MV\_BXDTFIN** = 2

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA380 - Todas as versões  
  
**Solução**Hoje no padrão do Protheus o único parâmetro de bloqueio na conciliação é o **MV\_DATAREC**, porém este parâmetro faz o bloqueio do range de data a ser conciliado e não o bloqueio do registro a ser desconciliado.

 A documentação oficial os parâmetros **(MV\_DATAFIN E MV\_BXDTFIN)**, não fazem bloqueio a conciliação.  
  
**Saiba mais**  
[Utilização do parâmetros MV\_DATAFIN e MV\_BXDTFIN](https://tdn.totvs.com/pages/releaseview.action?pageId=514730929)
