---
content_hash: db234fa2ca7bb4bddfb8c76cd0358d1a9899bfff9e8b1fd953e4382e9c80f117
fetched_at: '2026-06-29T00:08:17.880946+00:00'
page_id: '259559331'
product: rm
source: tdn-rm
title: TUSWKW_DT_Relatórios_Extrato_de_Cliente/Fornecedor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=259559331
version: 117
---

# Relatórios - Extrato de Cliente/Fornecedor

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | Educacional |
| **Módulo:** | Gestão Financeira |
| **Função:** | Relatórios - Extrato de Cliente/Fornecedor |
| **Situação/Requisito:** | Ao gerar o Relatório Razão de Cliente/Fornecedor nas versões Delphi, as opções Subtrair impostos e tributos do valor do lançamento e Mostrar devoluções nos lançamentos só a pagar ou só a receber eram normalmente exibidas ao usuário. Agora, no Extrato de Cliente/Fornecedor das versões atuais, estas opções não são apresentadas ao usuário. Cliente precisa destes dados para gerar o relatório como ocorria nas versões anteriores. |
| **Solução/Implementação:** | Melhoria no processo de Relatório Extrato Cliente/Fornecedor. Agora o sistema também a possibilidade de trabalhar com os seguintes parâmetros no formulário: "Usar valor em impostos e tributos no valor do lançamento" e "Mostrar devoluções nos lançamentos só a pagar ou só a receber no relatório de extrato cliente/fornecedor".  - Usar valor sem impostos e tributos no valor do lançamento:  Quando o parâmetro estiver selecionado, o sistema irá gerar o relatório extrato cliente/fornecedor descontando do valor original do lançamento. Os impostos são: IRRF, INSS e Tributos(PIS, COFINS e CSLL).  - Mostrar devoluções nos lançamentos só a pagar ou só a receber no relatório de extrato cliente/fornecedor:  Quando este parâmetro estiver marcado o sistema deverá mostrar as devoluções no relatório de razão quando forem marcados lançamentos só a pagar ou só a receber. |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | FIN000230 |

divs
