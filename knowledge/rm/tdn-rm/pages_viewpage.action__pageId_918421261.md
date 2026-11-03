---
content_hash: f40c2c50d56d34227c21752f906b5b1b8aab47e86169e3631b59110db0b817f7
fetched_at: '2026-06-29T00:12:06.985783+00:00'
page_id: '918421261'
product: rm
source: tdn-rm
title: FISCAL01-25269 - Evento Tributário Erro de Chave Duplicada
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=918421261
version: 3
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Evento Tributário - Vigência |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-25269 |

## **02. SITUAÇÃO/REQUISITO**

Ao incluir um novo cadastro de vigência tributária, é apresentado o erro:  
   
Chave Duplicada  
   
Possíveis causas:

* inclusão de registro cujo valor da chave primária já existe
* inclusão de registro cujo valor do índice único já existe

## **03. SOLUÇÃO**

 Foi disponibilizado script para correção do valor do campo responsável pelo autoincremento dos registros da vigência tributária.

No código foi efetuado um pequeno ajuste para correção do funcionamento do autoincremento da tabela referente a vigência tributária.

Disponível a partir da biblioteca 12.1.2410
