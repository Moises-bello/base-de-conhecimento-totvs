---
content_hash: b3129351a71afc45713474034aceabf9dc7b972903f2ebb631ffcd89085c1de3
fetched_at: '2026-07-02T19:24:23.393071+00:00'
page_id: '448600076'
product: protheus
source: tdn-tec
title: Seção [BTMonitorAppD] - Chave ApplicationTierName
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=448600076
version: 5
---

Define o nome da camada de aplicação na aplicação instrumentada pelo BTMonitor no controlador do AppDynamics.

## Valores válidos

| Valor | Descrição |
| --- | --- |
| BTMONITOR\_TIER\_NAME\_DEFAULT (Padrão) | Nome padrão da camada de aplicação na aplicação instrumentada pelo BTMonitor no controlador do AppDynamics. |
| <texto\_definido\_pelo\_usuário> | Qualquer texto definido pelo usuário, respeitando as observações listadas. |

## Observações

* O nome da camada de aplicação deve ser único na aplicação instrumentada;
* O tamanho máximo do nome da camada de aplicação deve ser de 100 caracteres;
* Além de números e caracteres em caixa alta e baixa, os seguintes caracteres especiais podem ser usados:

## Exemplo

Define o nome da camada de aplicação **SomeTierName01** na aplicação instrumentada SomeApplicationName01:

## Abrangência

Builds [17.3.0.8](http://tdn.totvs.com/display/tec/Application+Server+-+17.3.0.8).

## Veja também
