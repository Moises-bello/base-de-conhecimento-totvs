---
content_hash: 8f0a9af90014d71236b9578d8aef9897020365e82f48a3241dcd87b33ad0c114
fetched_at: '2026-06-29T00:11:56.449146+00:00'
page_id: '866030661'
product: rm
source: tdn-rm
title: FISCAL01-23772 - Alteração na geração da tag codpais da NFS-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=866030661
version: 2
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Enviar NFS-e |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado): | FISCAL01-23772 |

## **02. SITUAÇÃO/REQUISITO**

Ao enviar a NFSE pelo TSS se a tag "codpais" é gerada a mesma fica fora da ordem esperada.

## **03. SOLUÇÃO**

Alterada a ordem de geração das tags do grupo "prestacao" para ficar de acordo com a seguinte documentação:

Disponível a partir da biblioteca 12.1.2310
