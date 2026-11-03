---
content_hash: dcf85bff879f44679691f824e2117e8f466b3c8353d246bcb753f83f5852d124
fetched_at: '2026-07-02T19:24:23.116575+00:00'
page_id: '270914910'
product: protheus
source: tdn-tec
title: TWebChannel.pairedDevices
type: documentation
url: https://tdn.totvs.com/display/tec/TWebChannel.pairedDevices
version: 1
---

TWebChannel.pairedDevices

Retorna a lista de dispositivos Bluetooth pareados através da função Javascript definida como callBack na chamada original.

## Sintaxe

false )
]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| callback | caractere | Função JavaScript (callBack) disparada ao fim do processamento. | X |  |

## Observações

* Função disponível em builds superiores a 7.00.131227A.
* O retorno será um objeto JSON onde a propriedade "devices" conterá um array de dispositivos com as propriedades "name" e "address". "Devices" será "undefined" caso nenhum dispositivo esteja pareado ou a interface Bluetooth esteja desativada.

## Exemplos

cppEclipsetruefalse
