---
content_hash: 1a7daf18532a351305f62ba14c49d6658bc6d946dd25cc7986ecc1efe1285495
fetched_at: '2026-06-29T00:10:47.399283+00:00'
page_id: '556885286'
product: rm
source: tdn-rm
title: 'FISCAL01-10545 DT REINF: Tratar erro de FK na exclusão de Lançamento Fiscal'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=556885286
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Lançamento Fiscal |
| Ticket: | - |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-10545 |

## **02. SITUAÇÃO/REQUISITO**

Os processos de manutenção do Lançamento Fiscal devem ser ajustados para considerarem o vínculo com o Evento da Reinf.

Exclusão deve informar que existe um Evento relacionado e que o Lançamento poderá ser excluído somente se o Evento for excluído também.

O Cancelamento deverá fazer a mesma consistência da Exclusão.

## **03. SOLUÇÃO**

**Funcionalidade: Lançamento Fiscal**Dado que um lançamento fiscal está vinculado a um evento da Reinf (RM),  
Ao tentar excluir ou cancelar,  
O sistema não deve possibilitar   
E deve informar ao usuário para excluir primeiro o evento vinculado.
