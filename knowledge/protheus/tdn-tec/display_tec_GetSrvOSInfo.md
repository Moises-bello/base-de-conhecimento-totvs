---
content_hash: 1a40fbb1a82838d9070009cadd11569704f504f067fbc1a018377cdc8e36f062
fetched_at: '2026-07-02T19:24:18.995542+00:00'
page_id: '223168615'
product: protheus
source: tdn-tec
title: GetSrvOSInfo
type: documentation
url: https://tdn.totvs.com/display/tec/GetSrvOSInfo
version: 1
---

GetSrvOSInfo

Retorna informações do sistema operacional onde o Application Server está sendo executado.

## Sintaxe

false

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| cSrvOsInfo | caractere | Retorna uma string contendo as informações do Sistema Operacional onde o Application Server está sendo executado. |

## Observações

O formato da string apresenta diferenças entre as builds Windows e Linux do Application Server.

Abaixo, observe o exemplo de string retornada pela função no Sistema Operacional Windows:

cppEclipsefalsefalse

Neste exemplo, pode-se observar as informações retornadas referente a versão do sistema operacional onde está sendo executado o Application Server.

## Exemplos

cppEclipseExemplo 1truefalse

## Abrangência

Função disponível a partir da build 7.00.100601A-20100601

## Veja também
