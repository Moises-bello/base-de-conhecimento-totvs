---
content_hash: 3cf86cdb80167d0f2e9d1d1b4902134a8705fac067c3529ec41aeb3826901546
fetched_at: '2026-07-02T19:24:26.643118+00:00'
page_id: '579468321'
product: protheus
source: tdn-tec
title: Regex:Replace
type: documentation
url: https://tdn.totvs.com/display/tec/Regex%3AReplace
version: 3
---

Busca na *string* informada no primeiro parâmetro a quantidade\(terceiro parâmetro\) de ocorrências do padrão, trocando pelo valor informado no terceiro parâmetro.

## Sintaxe

, < cNewText >, [ nCount ], [ lReverse ] )]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência | Observações |
| --- | --- | --- | --- | --- | --- |
| cText | String | Texto em que o padrão será procurado. O retorno ocorre nesse parâmetro, por referência. | X | X |  |
| cNewText | String | TTexto pelo qual o padrao encontrado será substituido | X |  |  |
| nCount | Inteiro | Numero de trocas a serem efetuadas. Caso esse valor nao seja passado, apenas a primeira ocorrência é trocada. |  |  |  |
| lReverse | Lógico | Ordem de busca no texto. Esse parâmetro é opcional, o padrão é false. Se for informado true, a busca ocorre do final para o inicio \(direita->esquerda\) |  |  |  |

## Retorno

| Nome | Tipo | Descrição | Observações |
| --- | --- | --- | --- |
| ``` lRet ``` | Lógico | Indica se o método foi executado com sucesso | O novo texto, é retornado no parâmetro cText. |

## Observações

\* Se nCount não for informado, troca apenas a primeira ocorrência. A busca é realizada da esquerda para direita, caso necessite que seja invertido usar quarto parâmetro.

## Exemplos

### true

cppExemplo Construtortrue

## Veja também
