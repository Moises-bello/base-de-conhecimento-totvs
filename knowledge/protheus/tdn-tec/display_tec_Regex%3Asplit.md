---
content_hash: 1b58e0774e28173c2a8b6b0fbcde32aaa6715ce7c670fbbe0a746b783f05a5a9
fetched_at: '2026-07-02T19:24:26.653695+00:00'
page_id: '579468598'
product: protheus
source: tdn-tec
title: Regex:split
type: documentation
url: https://tdn.totvs.com/display/tec/Regex%3Asplit
version: 2
---

Divide a *string* recebida no primeiro parâmetro em cada ocorrência do padrão.

## Sintaxe

, < aSplit >, [ nCount ] )]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência | Observações |
| --- | --- | --- | --- | --- | --- |
| cText | String | Texto em que será dividido. | X |  |  |
| aSplit | Array | Parâmetro deve ser passado por referência. é alimentado com as partes do texto dividido pelo padrão. | X | X |  |
| nCount | Integer | Informa quantas posições devem ser preenchidas no array de retorno, ou seja, quantas divisões são desejadas no texto original. |  |  |  |

## Retorno

| Nome | Tipo | Descrição | Observações |
| --- | --- | --- | --- |
| ``` lRet ``` | Lógico | Indica se o método foi executado com sucesso | Caso retorne falso, verifique GetError() |

## Observações

<Observações da função quanto a seu comportamento, a alteração do comportamento, alteração de parâmetros, alterações do retorno, etc.> 

## Exemplos

### true

cppExemplo Construtortrue

## Veja também
