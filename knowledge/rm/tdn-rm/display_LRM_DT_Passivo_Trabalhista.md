---
content_hash: 6487c4cc1551b474f2a92e900bb7c087d4cbfd68f6b97c833a8c3e002006b779
fetched_at: '2026-06-29T00:06:25.070042+00:00'
page_id: '224130103'
product: rm
source: tdn-rm
title: DT_Passivo_Trabalhista
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Passivo_Trabalhista
version: 2
---

# PASSIVO TRABALHISTA

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **TOTVS Folha de Pagamento** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Passivo Trabalhista | Valor de desconto | |
| **Versão/Release:** | *12.1.4* |

## Descrição

Foi acrescentado no relatório do Passivo Trabalhista o valor de desconto de IRRF.

## Procedimento para Utilização

Foi criado no Wizard do Passivo Trabalhista um parâmetro para executar o cálculo de IRRF. Marcando este parâmetro o sistema irá calcular e exibir no relatório os valores de IRRF e IRRF 13º. Visando uma maior customização do relatório, foi criado também um parâmetro para executar ou não o cálculo do INSS que já era feito pelo sistema anteriormente. Desta forma é possível gerar o relatório desconsiderando os descontos de encargos (INSS e IRRF). Desmarcando os parâmetros, o campo respectivo não será calculado e não será exibido no relatório.
