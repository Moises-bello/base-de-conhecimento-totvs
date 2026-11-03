---
article_id: 360025357652
category: Contabilidade Gerencial - Balancetes
content_hash: 89e9d844f360bdfbb6586da8ae7808e221087809a6be50d72c079db8099d04c7
fetched_at: '2026-06-28T22:41:04.206340+00:00'
product: protheus
section_id: 1500001537281
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBR140 VALORES DECIMAIS
  NO RELATÓRIO NÃO SÃO EXIBIDOS CORRETAMENTE
type: support-article
updated_at: '2023-11-10T15:52:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025357652-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBR140-VALORES-DECIMAIS-NO-RELAT%C3%93RIO-N%C3%83O-S%C3%83O-EXIBIDOS-CORRETAMENTE
---

**Ocorrência**

Valores decimais na emissão do relatório CTBR040 não são exibidos corretamente, a ultima casa é cortada

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024415511)

**Ambiente**Protheus  – Contabilidade gerencial  – A partir da versão 11.80  
  
**Causa**

Situação pode estar sendo apresentada devido a configuração da moeda no cadastro. Diante disso acesse a rotina CTBA140 e verifique quantas posições o numero de decimal (CTO\_DECIM) esta cadastrado

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024411991)

**Solução**Verifique a configuração da moeda no cadastro, e como esta compartilhada.
