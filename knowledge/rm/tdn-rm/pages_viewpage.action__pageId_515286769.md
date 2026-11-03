---
content_hash: 34a2d0e367f484493dcaa2d24c0c4694f63b9e4054f473c8afee372c1d61d4e3
fetched_at: '2026-06-29T00:10:26.855568+00:00'
page_id: '515286769'
product: rm
source: tdn-rm
title: EDUCACIONAL01-10914 DT Cadastro de disciplina com CODDISC com espaços em branco
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=515286769
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Educacional |
| Módulo: | TOTVS Gestão Educacional |
| Função: | Cadastro de Disciplina |
| Ticket: | #6719015 |
| Requisito/Story/Issue (informe o requisito relacionado) : | EDUCACIONAL01-10914 |

## **02. SITUAÇÃO/REQUISITO**

Cadastro de disciplina permite o inclusão do CODDISC com espaços no início/final. Isso pode gerar inconsistências em diversos processos do sistema devido a existência de TRIM() em algumas partes do fonte.

## **03. SOLUÇÃO**

Alterado o cadastro de disciplina para remover qualquer espaço em branco existente no início ou fim do campo CODDISC.
