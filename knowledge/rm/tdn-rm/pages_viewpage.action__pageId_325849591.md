---
content_hash: 8aea623886e000dc7a2c781878495faa0c6c279eecae577c7c68a651c7508729
fetched_at: '2026-06-29T00:08:48.495518+00:00'
page_id: '325849591'
product: rm
source: tdn-rm
title: 1507867 FINANCEIRO01-3353 DT Lançamento - Acordo - Cancelamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=325849591
version: 2
---

# Lançamento - Acordo - Cancelamento

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projeto |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Lançamento - Acordo - Cancelamento |
| **Situação/Requisito:** | Ao cancelar o Acordo, o boleto do lançamento gerado por acordo é cancelado e o lançamento em aberto oriundo do Educacional fica sem boleto associado mesmo com o parâmetro "Reutilizar Último Boleto ao cancelar Acordo de Lançamentos oriundos do Educacional" marcado. |
| **Solução/Implementação:** | Retirado parâmetro "Reutilizar Último Boleto ao cancelar Acordo de Lançamentos oriundos do Educacional" da classe de parâmetros do acordo. Esse parâmetro não faz mais sentido com as novas regras de registro online definida pela FEBRABAN devido a não ser possível registrar um mesmo boleto que já foi registrado, com isso se faz necessário gerar um novo boleto. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | FIN000166 |
| **Documento de Referência:** | N/A |
