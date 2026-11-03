---
content_hash: 4fb46ba1e31e2a93a105a8b8fefca17a8ad485269b4e3137ab2b07a03ec938c9
fetched_at: '2026-06-29T00:06:15.365361+00:00'
page_id: '210053372'
product: rm
source: tdn-rm
title: TTBJWH_DT_Cálculo_CBHPM_Elaboração_de_Contas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=210053372
version: 5
---

# Ajuste no Cálculo do CBHPM na aba de Diagnose e Terapia da Elaboração de Contas

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Função:** | Cálculo do CBHPM |
| **Situação:** | Ao inserir um exame do padrão CBHPM que contenha incidências, não é levado em consideração o número de incidências ao calcular o valor do exame. |
| **Solução:** | Alterado a fórmula de cálculo dos exames que contenham incidência para calcular o valor do exame.  A fórmula usada para o cálculo é: **Valor do Exame + (Quantidade do Filme (m²) X Incidência X Valor do Filme)**. |
| **Versões/Release:** | 11.82.41 |

divs
