---
content_hash: 20fc9a5ed25ea1406aa287c4b3f93dfa5ddc0a1c1872fcfc11310771df54402d
fetched_at: '2026-07-02T19:24:21.357344+00:00'
page_id: '266976241'
product: protheus
source: tdn-tec
title: VarIsUID
type: documentation
url: https://tdn.totvs.com/display/tec/VarIsUID
version: 1
---

VarIsUID

Verifica se o identificador da sessão de variáveis globais fornecido está associado a um HashMap global.

## Sintaxe

false )
]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| cUID | caractere | Identificador da sessão de variáveis globais. | X |  |

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| lRet | lógico | Retorna **.T.** se o **<cUID>** fornecido **está associado** a um HashMap global ou **.F.** se o **<cUID>** fornecido **não está associado** a um HashMap global. |

## Observações

* O **<cUID>** fornecido na verificação deve estar no mesmo formato do usado na criação da sessão nomeada de variáveis globais.
* Para criar uma sessão nomeada de variáveis globais deve-se usar a função **VarSetUID**.
* Para remover uma sessão nomeada de variáveis globais deve-se usar a função **VarClean**.

## Exemplos

cppEclipsetruefalse

## Veja também
