---
content_hash: 3fa6a6028244bcca665c5c7d904655ca76378e99af7477322896d08db22c8e1c
fetched_at: '2026-06-29T00:11:05.493167+00:00'
page_id: '631603750'
product: rm
source: tdn-rm
title: TOPEXECONTROL01-17535 DT Melhoria no fonte de carga de dados de pedido
type: documentation
url: https://tdn.totvs.com/display/LRM/TOPEXECONTROL01-17535+DT+Melhoria+no+fonte+de+carga+de+dados+de+pedido
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | Protheus |
| Linha de Produto: | Microsiga Protheus® |
| Segmento: | BackOffice |
| Módulo: | Estoque/Custos (SIGAEST) |
| Função: | SUP001 - Carga de dados de pedido para apropriação |
| País: | Todos |
| Ticket: | N/A |
| Requisito/Story/Issue (informe o requisito relacionado) : | TOPEXECONTROL01-17535 |

## **02. SITUAÇÃO/REQUISITO**

A mensagem OrderAssignmentsInformation retorna somente o primeiro erro encontrado.

## **03. SOLUÇÃO**

Ajuste para que a mensagem OrderAssignmentsInformation não pare ao encontrar o primeiro erro. Executando assim todo o processo, armazenando todos os erros possíveis e retornando para o cliente.

## **04. DEMAIS INFORMAÇÕES**

N/A

## **05. ASSUNTOS RELACIONADOS**

N/A
