---
content_hash: 976a2254aa59e432ed958b551515a4a760a5df3c300579f1c197ff11e03f6412
fetched_at: '2026-06-29T00:09:08.372168+00:00'
page_id: '387295175'
product: rm
source: tdn-rm
title: 3318503 FOPROTINAS01-4675 DT Travamento na Visualização do Contexto ao Realizar
  Testes em Fórmulas de Funcionários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=387295175
version: 3
---

# Travamento em Contexto em teste de fórmula para funcionários

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção & Projetos. |
| **Módulo:** | TOTVS Folha de Pagamento. |
| **Função:** | Fórmula |
| **Situação/Requisito:** | Ao executar o contexto na área de teste de fórmula, tentando filtrar funcionários a tela trava pela quantidade grande registros a coligada corrente. |
| **Solução/Implementação:** | A consulta limita registros sob funcionários demitidos. Agora recupera-se da base funcionários ativos e que estam desligados no período de 3 meses que antecede a data de competência. |
| **Tickets relacionados:** | 3318503 |
