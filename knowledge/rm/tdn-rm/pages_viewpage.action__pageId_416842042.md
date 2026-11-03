---
content_hash: 718155a197dc8d9097aa699ae67cdf14ada7fe6e249ab12d7008d0820d5da1cb
fetched_at: '2026-06-29T00:09:12.204708+00:00'
page_id: '416842042'
product: rm
source: tdn-rm
title: 2467378 FOPCALCULO01-3532 Diferença Salarial - Pensão Alimentícia
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=416842042
version: 1
---

# Pensão Alimentícia

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Diferença Salarial |
| **Situação/Requisito:** | Ao efetuar o cálculo da diferença salarial para funcionário que possui dependente que deixou de incidir em pensão após a data base do ajuste salarial, é efetuado o lançamento de evento de estorno de pensão correspondente ao valor descontado na época.  Se não há histórico de quando o funcionário deixou de ser pensionista, o produto deve-se verificar a existência de historio de desconto de pensão e somente calcular a diferença de pensão caso tenha. |
| **Solução/Implementação:** | Criação de data fim de validade da pensão alimentícia e do campo percentual no movimento de pensão, para tratamento correto do cálculo da diferença de pensão. |
| **Tickets relacionados:** | 2467378 |
