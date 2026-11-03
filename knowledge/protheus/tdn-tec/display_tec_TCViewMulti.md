---
content_hash: bdbe4ea109d0a294bdc6672e5fea19efbc29650591eecb3f9aacbc39deac15e4
fetched_at: '2026-07-02T19:24:20.478636+00:00'
page_id: '251035679'
product: protheus
source: tdn-tec
title: TCViewMulti
type: documentation
url: https://tdn.totvs.com/display/tec/TCViewMulti
version: 4
---

TCViewMulti

Cria uma view para multiplas tabelas, sendo possível, mapear somente os campos que são relevantes a regra de negócio.

## Sintaxe

false, < cTable >, < cStruct > )
]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| cView | caractere | Nome da view a ser criada. | X |  |
| cTable | caractere | Nome da tabela master da view. | X |  |
| cStruct | caractere | Estrutura da view a ser criada, que consiste de uma lista de valores separados por virgula, onde é necessário informar a tabela e o campo da tabela que será mapeada na view, veja o exemplo abaixo. | X |  |

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| lRet | lógico | Retorna **.T.** se a view foi criada, caso contrário, retorna **.F.** e o motivo do erro pode ser verificado com a função . |

## Observações

**Possíveis causas de falha:**

* Já existe uma tabela ou view no SGBD, com o nome informado em cView;
* A tabela informada em cTable não existe no SGBD;
* A tabela informada em cTable é uma view ou tabela temporária;
* A tabela informada em cTable, já está relacionada como tabela auxiliar de outra view;
* Alguma tabela informada em cStruct, já está relacionada como tabela master de outra view;
* Alguma tabela informada em cStruct, já está relacionada como tabela auxiliar de outra view, que tem uma tabela master diferente;
* Alguma tabela e/ou campo informado em cStruct, não existe fisicamente no SGBD;
* Foram especificados um ou mais campos repetidos em cStruct.

## Exemplos

cppEclipsetruefalse

## Abrangência

Esta função está disponível no Application Server - build 7.00.131227A, com data de geração superior a 09/08/2016 e depende de um DBAccess com build superior a 20160402.

## Veja também
