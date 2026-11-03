---
article_id: 36227332999575
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: ddaec1aa6084f1226910b48eac10640c963cd801a67490054b41151b0b5c555c
fetched_at: '2026-06-28T22:37:55.082757+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Retorno cnab puxando
  dois totalizadores
type: support-article
updated_at: '2025-11-12T12:00:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36227332999575-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Retorno-cnab-puxando-dois-totalizadores
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36227336189207) Tempo aproximado para leitura: **00:05 min**  
  
**Ocorrência**  
Ao retornar, o CNAB está gravando dois totalizadores.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.2210.  
  
**Solução**  
Quando a baixa do CNAB ocorrer para títulos de diferentes filiais, será gravado um registro totalizador por filial, desde que o parâmetro MV\_BXCNAB esteja configurado com o valor 'S'.
