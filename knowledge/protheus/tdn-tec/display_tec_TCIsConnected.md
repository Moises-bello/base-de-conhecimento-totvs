---
content_hash: 54b7d95cf1d01ffc89440a94d400730730dc86f22b9b5a89a62d0e4d490e1d1a
fetched_at: '2026-07-02T19:24:21.618607+00:00'
page_id: '268803225'
product: protheus
source: tdn-tec
title: TCIsConnected
type: documentation
url: https://tdn.totvs.com/display/tec/TCIsConnected
version: 2
---

TCIsConnected

Função para verificar se está conectado no banco de dados.

## Sintaxe

false

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| nHwnd | numérico | Número da conexão. |  |  |

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| lRet | lógico | Retorna **.T.** se está conectado, caso contrário, retorna **.F.** |

## Observações

* Se não for informado o número da conexão será utilizado o valor que está em **TCGetConn**, ou seja, a conexão atual.

## Exemplos

cppEclipsetruefalse

## Veja também
