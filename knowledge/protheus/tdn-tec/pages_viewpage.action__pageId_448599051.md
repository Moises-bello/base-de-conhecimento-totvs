---
content_hash: 4b3b63a3ae58a3d66961e23959ed738d0323641a7b376b44fb3ba021d5c3d7dc
fetched_at: '2026-07-02T19:24:23.376515+00:00'
page_id: '448599051'
product: protheus
source: tdn-tec
title: Seção [BTMonitor] - Chave Type
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=448599051
version: 2
---

Define o tipo da instância de monitoramento habilitada no BTMonitor.

## Valores válidos

| Valor | Descrição |
| --- | --- |
| 0 (Padrão) | Define a instância de monitoramento do BTMonitor como vazia, sem monitoramento. |
| diferente de 0 | Define a instância de monitoramento do BTMonitor para um tipo específico. |

## Observações

* Se o tipo definido não for suportado, habilita a instância de monitoramento do BTMonitor como vazia, sem monitoramento;
* Se o BTMonitor não estiver habilitado em , habilita a instância de monitoramento do BTMonitor como vazia, sem monitoramento;
* Os tipos específicos de instância de monitoramento do BTMonitor atualmente suportados são:

  | Valor | Tipo de instância |
  | --- | --- |
  | 0 | Vazia, sem monitoramento. |
  | 1 | AppDynamics. |

## Exemplo

Habilita o BTMonitor com uma instância de monitoramento do tipo AppDynamics:

## Abrangência

Builds [17.3.0.8](http://tdn.totvs.com/display/tec/Application+Server+-+17.3.0.8).

## Veja também
