---
content_hash: fc05e65a4e734ef680d3715a6588be2a40a4a1d2225d0ba32394035f50a6d29c
fetched_at: '2026-06-29T00:10:43.076019+00:00'
page_id: '549507768'
product: rm
source: tdn-rm
title: FISCAL01-12675 DT Melhoria nos processos de transmissão e consulta do R-5011
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=549507768
version: 8
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Reinf |
| Ticket: | - |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-12675 |

## **02. SITUAÇÃO/REQUISITO**

1- Melhora no nome dos processos - Exemplo: alterar **"Transmitir"** para **"Transmitir Eventos Periódicos"**.

2- Log indicar quais eventos apresentaram erros.

3 - Mensagem nos processos de consulta\transmissão informando que será executado para todos eventos pendentes (hoje a mensagem é apresentada apenas na transmissão).

## **03. SOLUÇÃO**

1) Renomeado os processos para Transmitir Eventos Periódicos e Consultar Eventos Periódicos.  
2) Foram identificados os eventos que apresentaram erro pelo tipo e pelo identificador (tanto transmissão como consulta).  
3) Foi incluída a tela no processo de consulta (para o mesmo ser agendada em 3 camadas) e em ambos os processos foi incluído uma tela de diálogo para aprovação, caso não se selecione registros para execução.
