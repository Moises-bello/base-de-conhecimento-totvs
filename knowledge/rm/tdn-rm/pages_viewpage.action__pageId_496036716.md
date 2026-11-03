---
content_hash: d3f29277062e78677f610df777b4cb6cfa0752fcd28cdd09d57a67fc3bcd5e1a
fetched_at: '2026-06-29T00:10:22.041406+00:00'
page_id: '496036716'
product: rm
source: tdn-rm
title: FISCAL01-9574 DT Anexo Filtro de Operações
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=496036716
version: 4
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Cadastro de Parâmetros de Processo |
| Ticket: | FISCAL01-9574 |
| Requisito/Story/Issue (informe o requisito relacionado) : | Cadastro de Parâmetros de Processo |

## **02. SITUAÇÃO/REQUISITO**

Implementar um anexo no cadastro de subgrupo, que deve ser habilitado quando o processo for “EFD Contribuições” e grupo igual a "CPRB" apresentando uma grid e barra de ferramentas onde possibilita o usuário fazer a manutenção (CRUD) dos filtros de operações.  
  
Nesta issue iremos implementar apenas o CRUD incluindo, salvando e editando.

## **03. SOLUÇÃO**

Criação do cadastro de filtro de operação anexo aos parâmetros de processo ().

* Caso o TOTVS Gestão Fiscal esteja integrado com o TOTVS Gestão Contábil, o sistema apresentará o campo "Conta Contábil" como lookup. Do contrário, o mesmo será apresentado como texto livre.
* No campo Base de Cálculo, podem ser parametrizados utilizando um dos 8 valores opcionais parametrizados no TOTVS Gestão Financeira. Neste sentido, a descrição destes valores pode variar a depender do que estiver parametrizado no TOTVS Gestão Financeira.
