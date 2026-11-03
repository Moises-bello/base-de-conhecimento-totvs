---
content_hash: b5c75e7f5e135ae54e5677ce3144bd3e5f38904a8545e16ccc63586162478322
fetched_at: '2026-06-29T00:06:15.466170+00:00'
page_id: '210056205'
product: rm
source: tdn-rm
title: TTO876_DT_Codigo_Enquadramento_IPI_Para_Tributo_Item_Movimento
type: documentation
url: https://tdn.totvs.com/display/LRM/TTO876_DT_Codigo_Enquadramento_IPI_Para_Tributo_Item_Movimento
version: 3
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
| **Versões/Release:** | *12.1.7.113* |
| **Versão Corrigida:** | *12.1.7.113 ou superior* |
| **Versão Expedida:** | *12.1.7.113 ou superior* |

## Descrição

Disponibilização de campo para informação do "Código de Enquadramento IPI" para Tributo do Item de Movimento.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *12.1.7.113 ou superior* deste chamado

## Procedimento para Utilização

1. No módulo*TOTVS Gestão de Estoque Compras e Faturamento* acesse o tipo de movimento para emissão de Nota Fiscal;
2. Após preenchimento dos dados necessários, na inclusão do Item de Movimento terá na aba "Tributos e Valores / Tributos" disponibilizada a coluna para informar o "Código de Enquadramento IPI".
