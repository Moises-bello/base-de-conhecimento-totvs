---
content_hash: a7daa6e4f3741de7cb4bc7c2711e230fd1dc69962290ec625d350a3c28c299dd
fetched_at: '2026-07-02T19:24:23.424990+00:00'
page_id: '448600751'
product: protheus
source: tdn-tec
title: Seção [BTMonitorAppD] - Chave LogMinLevel
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=448600751
version: 7
---

Define o nível mínimo do log gerado pelo Agent da AppDynamics.

## Valores válidos

| Valor | Descrição |
| --- | --- |
| 2 (Padrão) | Define o nível mínimo do log gerado do Agent da AppDynamics como INFO. |
| 0 <= <nível\_mínimo> <= 5 | Define o nível mínimo do log gerado do Agent da AppDynamics como o informado pelo usuário. |
| <nível\_mínimo> < 0 ou <nível\_mínimo> > 5 | Define o nível mínimo do log gerado do Agent da AppDynamics como INFO. |

## Observações

* Os níveis de log gerados pelo Agent da AppDynamics e suportados pelo BTMonitor são:

  | Nível | Nome | Observação |
  | --- | --- | --- |
  | 0 | TRACE | Todas as mensagens de log são gravas. |
  | 1 | DEBUG |  |
  | 2 | INFO | Nível padrão. |
  | 3 | WARNING |  |
  | 4 | ERROR |  |
  | 5 | FATAL | Apenas as mensagens dos erros mais severos são gravadas. |

## Exemplo

Habilita o log do Agent da AppDynamics em nível TRACE:

## Abrangência

Builds [17.3.0.8](http://tdn.totvs.com/display/tec/Application+Server+-+17.3.0.8).

## Veja também
