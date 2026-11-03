---
content_hash: 79e9433e25ac30502e1ce04d720d94847062205f786ad0ff4c830980b5405d13
fetched_at: '2026-07-02T19:24:22.524892+00:00'
page_id: '270900219'
product: protheus
source: tdn-tec
title: TCUnique
type: documentation
url: https://tdn.totvs.com/display/tec/TCUnique
version: 3
---

TCUnique

Cria ou apaga uma índice de chave unica para uma determinada tabela.

## Sintaxe

false, [ cColumns ] )
]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| cTabela | caractere | Nome da tabela a criar ou apagar o índice de chave única. | X |  |
| cColumns | caractere | Nome da(s) coluna(s) para a criação do índice único. Caso este parâmetro não seja informado, e já exista um índice de chave única para a tabela informada, este será apagado. |  |  |

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| Retorna | numérico | 0 no caso de sucesso, e um número negativo em caso de erro. |

trueObservações

* Quando necessário criar uma chave unica com mais de uma coluna, deve ser utilizado o sinal de mais(+) separando as colunas informadas.
* Não é possível informar o nome do índice único a ser criado. O nome para o índice criado no SGDB é montado com o nome da tabela em questão seguido do sufixo "\_UNQ".
* A criação do índice de chave única exige que a tabela em questão esteja aberta pelo processo atual em modo de acesso exclusivo.
* A utilização de um índice único exige um campo interno de controle adicional chamado de R\_E\_C\_D\_E\_L\_, automaticamente acrescentado na estrutura da tabela caso ele não exista. A partir do DBAccess com build igual ou superior a 20160718, este campo passou a ser criado automaticamente juntos dos outros campos de controle do DBAccess.

## Exemplos

cppEclipsetruefalse

## Veja também
