---
content_hash: 85a562f06815f9c5ed18bd65895403f788b3375a428e5ea673d96f0550a8fd4f
fetched_at: '2026-07-02T19:24:26.632439+00:00'
page_id: '579468210'
product: protheus
source: tdn-tec
title: Regex:Remove
type: documentation
url: https://tdn.totvs.com/display/tec/Regex%3ARemove
version: 3
---

Busca no primeiro parâmetro a quantidade de ocorrências\(segundo parâmetro\) do padrão e as remove.

## Sintaxe

, [ nCount ], [ lReverse ] )]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência | Observações |
| --- | --- | --- | --- | --- | --- |
| cText | String | Texto em que o padrão será procurado. O retorno ocorre nesse parâmetro, por referência. | X | X |  |
| nCount | Inteiro | Numero de ocorrências que devem ser removidas. Esse parâmetro é opcional, o padrão é 1, ou seja, se não for informado a primeira ocorrência será removida |  |  |  |
| lReverse | Lógico | Ordem de busca no texto. Esse parâmetro é opcional, o padrão é false. Se for informado true, a busca ocorre do final para o inicio \(direita->esquerda\) |  |  |  |

## Retorno

| Nome | Tipo | Descrição | Observações |
| --- | --- | --- | --- |
| ``` lRet ``` | Lógico | Indica se o método foi executado com sucesso | O novo texto, é retornado no parâmetro cText. |

## Observações

<Observações da função quanto a seu comportamento, a alteração do comportamento, alteração de parâmetros, alterações do retorno, etc.> 

## Exemplos

### true

cppExemplo Construtortrue

## Veja também
