---
content_hash: 9da57f636b535461fcebc519bffc3e6532133d3ff0b5aa446321b0a32a42c48b
fetched_at: '2026-07-02T19:24:22.596327+00:00'
page_id: '270914904'
product: protheus
source: tdn-tec
title: TWebChannel.openSettings
type: documentation
url: https://tdn.totvs.com/display/tec/TWebChannel.openSettings
version: 1
---

TWebChannel.openSettings

Exibe a tela de configuração do periférico (camera, gps, etc), possibilitando habilitar/desabilitar o mesmo.

## Sintaxe

false )
]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| CodeFeature | numérico | Código do periférico a ser exibido, os códigos estão descritos no exemplo. | X |  |

## Observações

* Caso o periférico escolhido não exista no dispositivo móvel, exemplo NFC, nenhuma tela será apresentada.
* Função disponível em builds superiores a 7.00.131227A.

## Exemplos

cppEclipsetruefalse
