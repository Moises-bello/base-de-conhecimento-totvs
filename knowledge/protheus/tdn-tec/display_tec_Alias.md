---
content_hash: 961ac1b1ee0a229c6b6fccfb35afb6ea12c1bfd0dd0ebf0e79d30a5265c4b4f6
fetched_at: '2026-07-02T19:24:22.513305+00:00'
page_id: '270895177'
product: protheus
source: tdn-tec
title: Alias
type: documentation
url: https://tdn.totvs.com/display/tec/Alias
version: 2
---

Alias

Retorna o alias de uma área de trabalho especificada.

## Sintaxe

false

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| nWorkArea | numérico | Indica o número (entre 0 e 511) da área de trabalho que será verificada. |  |  |

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| cAlias | caractere | Retorna o alias da área de trabalho, no formato string, em letras maiúsculas. Caso o parâmetro (nWorkArea) não seja informado, o retorna será o alias da área de trabalho corrente ou, se não houver nenhum arquivo em uso, uma string vazia (""). |

## Observações

Alias() é uma função de banco de dados utilizada para determinar o alias da área de trabalho especificada. Alias é o nome atribuído a uma área de trabalho quando um arquivo de banco de dados está em uso. O nome atribuído é o nome real do arquivo de banco de dados ou um nome que foi explicitamente atribuído através da cláusula ALIAS usada na abertura da tabela através do  ou da função

Alias() é o inverso da função . Alias() retorna o alias através do número da área de trabalho e Select() o número da área de trabalho através do alias.

## Exemplos

cppEclipsetruefalse

## Veja também
