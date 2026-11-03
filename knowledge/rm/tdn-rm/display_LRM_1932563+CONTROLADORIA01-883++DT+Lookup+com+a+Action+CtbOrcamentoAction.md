---
content_hash: 42156932468439faf24a65c44383d5cfb5dd0d2f9854df743b6b951479e96bce
fetched_at: '2026-06-29T00:08:49.460153+00:00'
page_id: '330832183'
product: rm
source: tdn-rm
title: 1932563 CONTROLADORIA01-883  DT Lookup com a Action CtbOrcamentoAction
type: documentation
url: https://tdn.totvs.com/display/LRM/1932563+CONTROLADORIA01-883++DT+Lookup+com+a+Action+CtbOrcamentoAction
version: 4
---

# Uso de lookup com a action CtbOrcamentoAction

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Contábil |
| **Função:** | Uso de lookup com a action CtbOrcamentoAction |
| **Situação/Requisito:** | Ao utilizar a action “ctborcamentoaction” para criação de look nas telas de cadastro de Modelo de Negócio e Formulários do projeto de metadados o sistema retorna a seguinte mensagem:  Ocorreu um problema ao efetuar a leitura da visão de lookup: Não é possível encontrar a tabela 0. |
| **Solução/Implementação:** | Implementação dos métodos "DoReadLookupView" e "DoReadLookupValues" no DataServer CtbOrcamentoData para que o mesmo seja utilizado em lookups do ERP. Os métodos irão retornar os dados dos orçamentos da coligada corrente. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | N/A. |
| **Requisito:** | N/A. |
