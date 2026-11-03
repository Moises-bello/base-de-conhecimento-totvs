---
content_hash: adc956d84b52bb97a4193718ae25e8a0de4414f6f45d1f64a241c9a0ce38a386
fetched_at: '2026-06-29T00:06:13.993712+00:00'
page_id: '208349617'
product: rm
source: tdn-rm
title: TTMERF_DT_Codigo_Enquadramento_IPI_Para_Tributo_Item_Movimento
type: documentation
url: https://tdn.totvs.com/display/LRM/TTMERF_DT_Codigo_Enquadramento_IPI_Para_Tributo_Item_Movimento
version: 2
---

# CÓDIGO DE ENQUADRAMENTO IPI PARA TRIBUTO DO ITEM DE MOVIMENTO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | ***Gestão de Estoque Compras Faturamento*** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | **MOV.001** | *INCLUSAO DE MOVIMENTO* | | **MOV.013** | *COPIA A PARTIR DE OUTRO MOVIMENTO* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *NF-E* | *NF-E* | | *FIS.005**INT* | *FISCAL - TABELAS DE TRIBUTACAO* | |
| **Cadastros Iniciais:** | *Tributos.* |
| **Parâmetro(s):** | *Tributos para o Item de Movimento* |
| **Ponto de Entrada:** | *N/A* |
| **Chamados Relacionados** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL e Oracle* |
| **Tabelas Utilizadas:** | *TMov, TTrbMov* |
| **Sistema(s) Operacional(is):** | *N/A* |
| **Versões/Release:** | *11.82.41.101* |
| **Versão Corrigida:** | *11.82.41.101 ou superior* |
| **Versão Expedida:** | *11.82.42* |

## Descrição

Disponibilização de campo para informação do "Código de Enquadramento IPI" para Tributo do Item de Movimento.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *11.82.41.101 ou superior* deste chamado

## Procedimento para Utilização

1. No módulo*TOTVS Gestão de Estoque Compras e Faturamento* acesse o tipo de movimento para emissão de Nota Fiscal;
2. Após preenchimento dos dados necessários, na inclusão do Item de Movimento terá na aba "Tributos e Valores / Tributos" disponibilizada a coluna para informar o "Código de Enquadramento IPI".
