---
content_hash: 5d1b6501645de41aaa19612aad2e8dffb5d16efd1b0d33662dc64662d5108843
fetched_at: '2026-06-29T00:10:30.904711+00:00'
page_id: '520112225'
product: rm
source: tdn-rm
title: FISCAL01-11358 DT EFD-REINF Processo Transmissão de Eventos R-20XX
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=520112225
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Processo de Transmissão de Eventos da EFD-REINF R-20XX |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-10378 |

## **02. SITUAÇÃO/REQUISITO**

Implementar o processo para a transmissão do evento R-20XX da Reinf.

## **03. SOLUÇÃO**

Foi implementado o processo de Transmissão do Evento R-20XX para o TSS.

O processo EFD-Reinf - Transmitir Evento será exibido em RM -> Gestão Fiscal -> Obrigações Acessórias -> SPED -> REINF -> Eventos Periódicos -> Transmissão de Eventos .

Regras para Transmissão:

O Evento R-1000 com o Status [Autorizado].

O Evento R-5011 com o Status [Aberto].

O Evento R-20XX deve estar com o Status [Alterado, Inconsistente, Não Transmitido ou Rejeitado].

Especificação geral: 

Especificação dos Eventos Períodicos: 

Caso um evento R-20XX esteja com o status Pendente Exclusão ou Excluído, será exibida uma lookup com referência para o evento R-9000 correspondente.
