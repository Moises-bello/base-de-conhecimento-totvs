---
content_hash: 1a6cbb2a8717c71872a76c04128ca5ce589be2a9624605b695a2869da423701f
fetched_at: '2026-07-02T19:24:23.120759+00:00'
page_id: '270914914'
product: protheus
source: tdn-tec
title: TWebChannel.runAdvpl
type: documentation
url: https://tdn.totvs.com/display/tec/TWebChannel.runAdvpl
version: 1
---

TWebChannel.runAdvpl

Executa um comando ADVPL através do Javascript, retornando o valor processado via ADVPL para a função Javascript definida como callBack na chamada original.

## Sintaxe

false, < callback > )
]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| command | caractere | Comando ADVPL a ser executado no AppServer embutido no CloudBridge. | X |  |
| callback | caractere | Função JavaScript (callBack) disparada ao fim do processamento ADVPL do comando solicitado. | X |  |

## Observações

* Função disponível em builds superiores a 7.00.131227A.

## Exemplos

cppEclipsetruefalse
