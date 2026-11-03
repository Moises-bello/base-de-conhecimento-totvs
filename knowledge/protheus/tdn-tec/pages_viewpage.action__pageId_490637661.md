---
content_hash: 2f74b31030517ebafcc47b57fe70dacc908dcb7f5b0009b9b0dcdf5bd9add55f
fetched_at: '2026-07-02T19:24:24.853878+00:00'
page_id: '490637661'
product: protheus
source: tdn-tec
title: Seção [BTMonitor] - Chave TraceECEnable
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=490637661
version: 3
---

Habilita o trace das funcionalidades de EC (exit call) no log da API do BTMonitor.

## Valores válidos

| Valor | Descrição |
| --- | --- |
| 0 (zero) (Padrão) | Desabilita o trace das funcionalidades de EC no log da API do BTMonitor. |
| <> 0 (diferente de zero) | Habilita o trace das funcionalidades de EC no log da API do BTMonitor. |

## Observações

* O log gerado pela configuração desta chave é independente do gerado a partir da configuração das demais chaves de log do BTMonitor;
* A completa configuração do log do BTMonitor depende das configurações de ,  e .

## Exemplo

Habilita o trace das funcionalidades de EC no log da API do BTMonitor:

## Abrangência

Builds [17.3.0.8](http://tdn.totvs.com/display/tec/Application+Server+-+17.3.0.8).

## Veja também
