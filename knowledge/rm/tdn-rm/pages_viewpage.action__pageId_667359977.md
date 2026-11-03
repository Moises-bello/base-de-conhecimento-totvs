---
content_hash: cab4189ba516b9b600c53243d9e3829ce7ece92c61e9aadf09e2e137c79cc7ed
fetched_at: '2026-06-29T00:11:16.378850+00:00'
page_id: '667359977'
product: rm
source: tdn-rm
title: FISCAL01-17291 - DT - Criar Validação REINF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=667359977
version: 3
---

## **01. DADOS GERAIS**

| Produto: | TOTVS |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | EFD-REINF |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-17291 |

## **02. SITUAÇÃO/REQUISITO**

O processo de **geração** e **transmissão** da EFD-Reinf deverá comparar o Ambiente do Evento com o Ambiente do parâmetro e, caso estejam configurados diferente, deverá ser apresentada uma mensagem de erro e o processo não poderá ser executado.

## **03. SOLUÇÃO**

Criada validação que quando o ambiente do evento for distinto do ambiente do parâmetro, não seja possível Transmitir e Consultar eventos Cadastrais, nem Transmitir, Consultar e Gerar eventos periódicos.

Disponível a partir da 12.1.34
