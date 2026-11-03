---
content_hash: 4baf2ff5052260cfda428df75066ea11440297b0d8dfcdea0393e8c3fc0b9b02
fetched_at: '2026-06-29T00:10:47.388288+00:00'
page_id: '556879237'
product: rm
source: tdn-rm
title: DT- Contrato Suspenso
type: documentation
url: https://tdn.totvs.com/display/LRM/DT-+Contrato+Suspenso
version: 1
---

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | RH |
| **Módulo:** | TOTVS Folha de Pagamento - eSocial |
| **Função:** | Parametrizador |
| **Situação/Requisito:** | Conforme nossa Consultoria Jurídica, a MP 936/20 - Contagem férias e 13 salário na Suspensão de Contrato de Trabalho, gera dupla interpretação, podendo ou não descontar. Como deixou a decisão para os clientes, nesse caso o cliente deseja pagar e não quer reduzir os avós nas férias e no 13 salário, solicitamos que tenha um parâmetro no sistema para que o cliente, decida que quer ou não a redução no cálculo de férias e 13 salário. Hoje no sistema está tratando internamente, se o funcionário estiver com o Contrato Suspenso, o mesmo perde direito aos avós. |
| **Solução/Implementação:** | Criados os parâmetros "Afastamento por Contrato Suspenso mantém período aquisitivo de férias", "Afastamento por Contrato Suspenso mantém avos de 13º salário" e "Motivo do afastamento por Contrato Suspenso sem perda de avos" no Parametrizador em Folha Normal na pasta Afastamento 2/2. Também foi renomeada a pasta "Afastamento" para "Afastamento 1/2" movendo os campos " Evento para atestado médico (mensalista)", " Evento para atestado médico (horista)" e " Motivo de afastamento por COVID-19" para a pasta Afastamento 2/2. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | [FOPCALCULO01-10890](https://jiraproducao.totvs.com.br/browse/FOPCALCULO01-10890) e [FOPCALCULO01-10853](https://jiraproducao.totvs.com.br/browse/FOPCALCULO01-10853) |
| **Documento de Referência:** | [Afastamento 2/2](https://tdn.totvs.com.br/pages/viewpage.action?pageId=556879107) |
| **Pacote:** | N/A |
