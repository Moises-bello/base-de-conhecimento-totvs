---
content_hash: 87902a28ca3d29f7cf9d36b6e62edff658ae9f90a4a885427f6c67567874ed37
fetched_at: '2026-06-29T00:10:30.911049+00:00'
page_id: '520116393'
product: rm
source: tdn-rm
title: EDUCACIONAL01-11858 DT Inclusão de Responsável Financeiro via WS de Aluno
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=520116393
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Educacional |
| Módulo: | TOTVS Educacional |
| Função: | WS Aluno |
| Ticket: | #7396022 |
| Requisito/Story/Issue (informe o requisito relacionado) : | EDUCACIONAL01-11858 |

## **02. SITUAÇÃO/REQUISITO**

Sistema permite inserir para o aluno via WS um responsável financeiro de coligada diferente da coligada do aluno (isso só deve ser permitido se o cliente/fornecedor for global)

## **03. SOLUÇÃO**

Modificação do Web Service de aluno para não permitir o cadastro de cliente/fornecedor de outra coligada como responsável financeiro do aluno. Esse cenário só é permitido para o caso do cliente/fornecedor global (coligada = 0).
