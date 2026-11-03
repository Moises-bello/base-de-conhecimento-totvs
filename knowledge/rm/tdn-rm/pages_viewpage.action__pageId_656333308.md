---
content_hash: 966a06f01fe13a3003f8c2c2a7c4c24e4add8388481f8b426c0af52de9204b5d
fetched_at: '2026-06-29T00:11:13.131863+00:00'
page_id: '656333308'
product: rm
source: tdn-rm
title: 11770748 FISCAL01-16224 DT - DIRF Lançamentos de Importação - Tributo IRRF
  Importação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=656333308
version: 2
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | DIRF |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-16224 |

**02. SITUAÇÃO/REQUISITO**

Ao gerar a Rotina da DIRF os Lançamentos de Importação com o Tributo IRRF Importação não são gerados. Isto ocorre conforme o   
Log porque o Campo Indicador de Retenção não foi preenchido.

## **03. SOLUÇÃO**

Ajuste na geração da Dirf para que os Lançamentos de Importação com o Tributo IRRF Importação sejam gerados corretamente

obs.: Será incluído na Dirf mesmo que o Valor do Tributo de Importação do Lançamento Fiscal não tenha valor.
