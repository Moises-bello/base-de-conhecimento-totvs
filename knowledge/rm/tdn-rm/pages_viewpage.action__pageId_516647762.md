---
content_hash: 0a01ecdab8dd5877726bce43b13ee75dc114df2437ee08fac31d4d093f5c48fb
fetched_at: '2026-06-29T00:10:27.803930+00:00'
page_id: '516647762'
product: rm
source: tdn-rm
title: FISCAL01-11029 DT EFD-REINF Processo de Geração dos Eventos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=516647762
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Processo de Geração de Eventos da EFD-REINF |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [FISCAL01-11029](https://jiraproducao.totvs.com.br/browse/FISCAL01-11029) |

## **02. SITUAÇÃO/REQUISITO**

Implementar a tela do processo para a geração dos eventos da Reinf a partir de um evento R-5011 selecionado na visão de Eventos Periódicos.

## **03. SOLUÇÃO**

Implementação do processo para Geração dos Registros da REINF.

O processo EFD-Reinf - Gerar Eventos será exibido em RM -> Gestão Fiscal -> Obrigações Acessórias -> SPED -> REINF -> Eventos Periódicos.

Comportamento do processo: Quando selecionado um ou muitos Eventos R-5011 na visão de Eventos Periódicos, o processo de geração será executado considerando o período de cada evento. Se não for selecionado nenhum evento R-5011 na visão de Eventos Periódicos, serão considerados todos os Eventos R-5011 com Status em Aberto para geração dos demais registros de evento.

Foi disponibilizado no processo a possibilidade de execução via agendamento de Serviço.
