---
content_hash: b4b3b050d048cab93d3b6428f7d90de2edb7cd0274ea69746a7b5984dbeaa8f9
fetched_at: '2026-06-29T00:08:28.193273+00:00'
page_id: '271666811'
product: rm
source: tdn-rm
title: 327374 MEDU-2592 DT Relatório Balancete
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271666811
version: 106
---

# Relatório Balancete

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Contábil |
| **Função:** | Relatório Balancete |
| **Situação/Requisito:** | Ao gerar o relatório Balancete sistema está demorando muito, cerca de mais de 9 minutos. |
| **Solução/Implementação:** | Como o cliente trabalha com um plano de contas que possui mais de 60.000 contas contábeis, foi necessário mudar a forma como essas contas são selecionadas para terem seus saldos calculados.  Algumas recomendações que aumentam a velocidade do relatório e também da aplicação e suas integrações como um todo.  1 - Ao gerar o relatório acessar a aba "Filtros" e no campo 'Conta Contábil (Ativa / Inativa)' selecionar apenas contas contábeis 'Ativas'.  2 - É recomendado que se feche os períodos contábeis que não estão sendo mais utilizados o que traz ganho de performance para o ERP como um todo, pois os dados são movidos para as tabelas de histórico e caso seja necessário tirar um relatório em algum período fechado basta marcar a opção de "Buscar do histórico contábil". |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados**: | N/A |
| **Requisito (informe o requisito relacionado):** | N/A |

divs
