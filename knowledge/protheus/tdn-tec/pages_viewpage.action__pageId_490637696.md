---
content_hash: a846f7357e7cd1fc8a42b340ac0b072e4aaa8ce1c19a5584549fee824bafe658
fetched_at: '2026-07-02T19:24:24.858962+00:00'
page_id: '490637696'
product: protheus
source: tdn-tec
title: Seção [BTMonitor] - Chave LogLevel
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=490637696
version: 2
---

Configura o nível do log da API do BTMonitor.

## Valores válidos

| Valor | Descrição |
| --- | --- |
| 0 (zero) | Configura o log da API do BTMonitor no nível TRACE, habilitando mensagens deste tipo e dos seguintes. |
| 1 (um) | Configura o log da API do BTMonitor no nível DEBUG, habilitando mensagens deste tipo e dos seguintes. |
| 2 (dois) | Configura o log da API do BTMonitor no nível INFO, habilitando mensagens deste tipo e dos seguintes. |
| 3 (três) (Padrão) | Configura o log da API do BTMonitor no nível WARN, habilitando mensagens deste tipo e dos seguintes. |
| 4 (quatro) | Configura o log da API do BTMonitor no nível ERROR, habilitando mensagens deste tipo e dos seguintes. |
| 5 (cinco) | Configura o log da API do BTMonitor no nível FATAL, habilitando mensagens deste tipo e dos seguintes. |

## Observações

* Um nível de log determinado habilita mensagens do seu tipo e dos tipos seguintes, superiores a ele em gravidade;
* O log gerado pela configuração desta chave é independente do gerado a partir da configuração das demais chaves de log do BTMonitor;
* A completa configuração do log do BTMonitor depende das configurações de ,  e .

## Exemplo

Configura o log da API do BTMonitor no nível WARN, habilitando mensagens do tipo WARN, ERROR e FATAL:

## Abrangência

Builds [17.3.0.8](http://tdn.totvs.com/display/tec/Application+Server+-+17.3.0.8).

## Veja também
