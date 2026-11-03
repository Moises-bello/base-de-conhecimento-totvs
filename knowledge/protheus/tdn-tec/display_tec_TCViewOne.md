---
content_hash: 3470145eda50bb0070eb1f71ab0c25391b74d668d595e43c9e0c39a3dd7d50f6
fetched_at: '2026-07-02T19:24:20.471581+00:00'
page_id: '249956747'
product: protheus
source: tdn-tec
title: TCViewOne
type: documentation
url: https://tdn.totvs.com/display/tec/TCViewOne
version: 9
---

TCViewOne

Cria uma view para uma tabela no modelo 1 para 1, ou seja, todos os campos da tabela serão mapeados na view.

## Sintaxe

false, < cTable > )
]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| cView | caractere | Nome da view a ser criada. | X |  |
| cTable | caractere | Nome da tabela master da view. | X |  |

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| lRet | lógico | Retorna **.T.** se a view foi criada, caso contrário, retorna **.F.** e o motivo do erro pode ser verificado com a função . |

## Observações

**Possíveis causas de falha:**

* Já existe uma tabela ou view no SGBD, com o nome informado em cView;
* A tabela informada em cTable não existe no SGBD;
* A tabela informada em cTable é uma view ou tabela temporária;
* A tabela informada em cTable, já está relacionada como tabela auxiliar de outra view ().

## Exemplos

cppEclipsetruefalse

## Abrangência

Esta função está disponível no Application Server - build 7.00.131227A, com data de geração superior a 09/08/2016 e depende de um DBAccess com build superior a 20160402.

## Veja também
