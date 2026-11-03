---
content_hash: 0244d44e0bdc006430b6d2e58cbc4e41ce56e917f5424fdd462cae458a9ce563
fetched_at: '2026-07-02T19:24:23.124770+00:00'
page_id: '270914919'
product: protheus
source: tdn-tec
title: TWebChannel.testDevice
type: documentation
url: https://tdn.totvs.com/display/tec/TWebChannel.testDevice
version: 1
---

TWebChannel.testDevice

Retorna o Status do periférico (camera, gps, etc), informando se o mesmo esta habilitado ou não.

## Sintaxe

false, < callback > )
]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| feature | numérico | Código do periférico a ser testado, os códigos estão descritos no exemplo. | X |  |
| callback | caractere | Função JavaScript (callBack) disparada ao fim do processamento, recebendo True caso o periférico esteja habilitado e False caso contrário. | X |  |

## Observações

* O teste CONNECTED\_MOBILE (Conectado via 3G ou 4G) somente retornará True caso a conexão WIFI esteja desabilitada.
* Função disponível em builds superiores a 7.00.131227A.

## Exemplos

cppEclipsetruefalse
