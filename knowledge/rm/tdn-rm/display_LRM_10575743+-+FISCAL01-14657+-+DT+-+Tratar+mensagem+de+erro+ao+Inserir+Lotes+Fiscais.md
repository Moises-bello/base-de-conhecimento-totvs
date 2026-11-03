---
content_hash: 9d5a1de2b1ea6da99d9acb488cb09e016dc53fa387cc256815cb9bf3d2658d54
fetched_at: '2026-06-29T00:11:05.391728+00:00'
page_id: '630580600'
product: rm
source: tdn-rm
title: 10575743 - FISCAL01-14657 - DT - Tratar mensagem de erro ao Inserir Lotes Fiscais
type: documentation
url: https://tdn.totvs.com/display/LRM/10575743+-+FISCAL01-14657+-+DT+-+Tratar+mensagem+de+erro+ao+Inserir+Lotes+Fiscais
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Inserir Lotes Fiscais |
| País: | Brasil |
| Ticket: | 10575743 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-14657 |

## **02. SITUAÇÃO/REQUISITO**

Solicitamos uma tratativa na mensagem abaixo, uma vez que ela é “genérica” não fica claro qual informação é obrigatória para inclusão do Lote:  
Violação de chave estrangeira Possíveis causas:  - exclusão de registro que possui outros registros associados  - inclusão de registro detalhe sem um registro mestre associado.

## **03. SOLUÇÃO**

O erro se dava pelo motivo de que o Lote inserido não pertencia à filial atual do usuário, com isso, foi implementado que ao clicar em Inserir Lotes Fiscais e em seguida no *lookup* Lote Contábil, o mesmo retornará somente os Lotes que pertencem à Coligada atual do usuário.

Disponível a partir da versão 12.1.33
