---
content_hash: c9aef4303fb14750c1abc978f31b79d18f9d8f20ea854dc3ea9cbdda5c624ee8
fetched_at: '2026-07-02T19:24:22.573462+00:00'
page_id: '270914805'
product: protheus
source: tdn-tec
title: TWebChannel.barCodeScanner
type: documentation
url: https://tdn.totvs.com/display/tec/TWebChannel.barCodeScanner
version: 1
---

TWebChannel.barCodeScanner

Inicia a captura do código de barras retornando o código capturado e seu formato para a função Javascript definida como callBack na chamada original.

## Sintaxe

false )
]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| callback | caractere | Função JavaScript (callBack) disparada ao fim da captura do código de barras. | X |  |

## Observações

* Função disponível em builds superiores a 7.00.131227A.
* O retorno será um objeto JSON contendo o valor decodificado do código de barras e o nome do formato de código de barras lido. Exemplo de retorno {"format":"EAN\_13","code":"7891172000256"}

## Exemplos

cppEclipsetruefalse
