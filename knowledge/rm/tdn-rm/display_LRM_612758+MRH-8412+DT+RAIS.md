---
content_hash: 9fa6453e865f361543f0f00f163e9a03461586c9e62e4f7d002b5d7c98599749
fetched_at: '2026-06-29T00:08:29.661113+00:00'
page_id: '272156377'
product: rm
source: tdn-rm
title: 612758 MRH-8412 DT RAIS
type: documentation
url: https://tdn.totvs.com/display/LRM/612758+MRH-8412+DT+RAIS
version: 108
---

# RAIS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | RAIS |
| **Situação/Requisito:** | Funcionários demitidos com o Tipo de Demissão “N - Rescisão Indireta” e ao validar o arquivo da RAIS o sistema está levando o Código de Desligamento 11 (Rescisão de contrato de trabalho sem justa causa por iniciativa do empregador ou exoneração de oficio de servidor de cargo efetivo ou exoneração de cargo em comissão), porém deveria levar o código 20 (Rescisão com justa causa por iniciativa do empregado (rescisão indireta)). |
| **Solução/Implementação:** | Para funcionário demitido com o tipo “N - Rescisão Indireta” deverá levar o código do desligamento 20 na rais. |
| **Tickets relacionados:** | * [612758](http://jiraproducao.totvs.com.br/issues/?jql=cf%5B11086%5D+%3D+%22612758%22 "612758") |

divs
