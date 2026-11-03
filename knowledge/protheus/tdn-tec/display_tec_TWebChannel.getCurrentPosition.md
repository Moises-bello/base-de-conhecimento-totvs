---
content_hash: 957c2d0fbbcf277205985b874db6f40e48ac3aabcd3fcb09f2c61ea2a7d862ab
fetched_at: '2026-07-02T19:24:22.582685+00:00'
page_id: '270914838'
product: protheus
source: tdn-tec
title: TWebChannel.getCurrentPosition
type: documentation
url: https://tdn.totvs.com/display/tec/TWebChannel.getCurrentPosition
version: 1
---

TWebChannel.getCurrentPosition

Recupera a posição do GPS, quando este estiver ativo no dispositivo móvel.

## Sintaxe

false )
]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| callback | caractere | Função JavaScript (callBack) disparada ao fim do processamento, recebendo a posição do GPS. | X |  |

## Observações

* Função disponível em builds superiores a 7.00.131227A.
* A posição GPS retornada será um objeto JSON contendo a latitude e longitude em graus no formato decimal, por exemplo {"latitude":"-23.50590","longitude":"-46.64300"}

## Exemplos

cppEclipsetruefalse
