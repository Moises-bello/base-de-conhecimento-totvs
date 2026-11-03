---
article_id: 36227336267927
category: Financeiro - Contas a Receber - Comunicação Bancária CNAB
content_hash: fd2c80f0bb3e08ed1c6ece82bcec970d5b20a573dcebe9735f2ead071e7b33e6
fetched_at: '2026-06-28T22:37:47.997084+00:00'
product: protheus
section_id: 26656449081111
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Retorno cnab puxando
  dois totalizadores
type: support-article
updated_at: '2025-11-12T12:00:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36227336267927-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Retorno-cnab-puxando-dois-totalizadores
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36227333056535) Tempo aproximado para leitura: **00:05 min**  
  
**Ocorrência**  
Ao retornar, o CNAB está gravando dois totalizadores.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.2210.  
  
**Solução**  
Quando a baixa do CNAB ocorrer para títulos de diferentes filiais, será gravado um registro totalizador por filial, desde que o parâmetro MV\_BXCNAB esteja configurado com o valor 'S'.
