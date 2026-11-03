---
content_hash: f0f3ef3c4efcc783fc56fb2284f01119ae1b93c584718d5dbd495db481776495
fetched_at: '2026-06-29T00:10:35.569659+00:00'
page_id: '531018926'
product: rm
source: tdn-rm
title: 7299771 FISCAL01-11256 - Geração C197 - Campo 02 Código de Ajuste RJ
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=531018926
version: 4
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Código de Ajuste |
| Ticket: | 7299771 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-11256 |

## **02. SITUAÇÃO/REQUISITO**

Ao cadastrar um Código de Ajuste com o mesmo Código de Ajuste já cadastrado foi apresentado a seguinte mensagem:

Não foi possível salvar o cadastro! Os dados estão em duplicidade (Registro, Aplicar em, Estado, Código de Ajuste).

Ao invés de erro, apresentar mensagem que o código já existe na tabela e confirmar a inclusão.

## **03. SOLUÇÃO**

Foi retirado a unique key UQDCODIGOAJUSTE da tabela DCODIGOAJUSTE (Necessita a execução da marcação LI.2020.01\_03).

Ao invés de um erro, o sistema agora passa a apresentar uma mensagem de que o código já existe na tabela e indaga o usuário sobre a sua inclusão.
