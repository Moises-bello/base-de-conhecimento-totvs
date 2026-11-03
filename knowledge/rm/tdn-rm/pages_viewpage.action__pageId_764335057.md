---
content_hash: 306abaae002a3dddf67ec055e2f81c1260b6752d5048ea076278b9446c11f10f
fetched_at: '2026-06-29T00:11:33.994976+00:00'
page_id: '764335057'
product: rm
source: tdn-rm
title: FISCAL01-6365 - DT - Alteração no log das rotinas de EFD contribuições e SPED
  Fiscal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=764335057
version: 2
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | EFD contribuições e SPED Fiscal |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-6365 |

## **02. SITUAÇÃO/REQUISITO**

Cliente sugere melhoria na mensagem de erro apresentada nas rotinas fiscais. Hoje o sistema emite uma mensagem informando como identificador do lançamento o identificador da situação tributária, e para os usuários que não possui acesso ao banco não é possível localizar o lançamento fiscal utilizando os filtros existentes na ferramenta.

## **03. SOLUÇÃO**

Foi alterado o log do erro ao carregar dados dos itens do lançamento.

Foi adicionado um novo resource para atender ao log, apresentando o IdLafAgrup (id do lançamento) e o DocIni (Número do documento).

Disponível à partir da biblioteca 12.1.2310
