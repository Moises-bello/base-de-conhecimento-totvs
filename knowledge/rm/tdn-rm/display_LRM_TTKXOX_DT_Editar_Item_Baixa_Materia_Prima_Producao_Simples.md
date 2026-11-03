---
content_hash: fdb3429954a65a4c3fcad1dad28ec786d3f5d899fb5df5b430e0c98f5535807f
fetched_at: '2026-06-29T00:06:17.912011+00:00'
page_id: '213986767'
product: rm
source: tdn-rm
title: TTKXOX_DT_Editar_Item_Baixa_Materia_Prima_Producao_Simples
type: documentation
url: https://tdn.totvs.com/display/LRM/TTKXOX_DT_Editar_Item_Baixa_Materia_Prima_Producao_Simples
version: 4
---

# EDITAR ITEM DE MOVIMENTO BAIXA DE MATÉRIA PRIMA (PRODUÇÃO SIMPLES)

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | **RM** |
| **Segmento:** | ***Construção e Projetos*** |
| **Módulo:** | **Gestão de Estoque, Compras e Faturamento** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | **MOV.002** | **EDICAO DE MOVIMENTO** |  | **Rotina(s) Envolvida(s)** | **Nom****e** **Técnico** | | --- | --- | | **MOV.007** | *FATURAMENTO/RECEBIMENTO* | | *MOV.035* | *ITEM DE MOVIMENTO* | | *EST.021* | *PROCESSO PRODUTIVO SIMPLES* | |
| **Cadastros Iniciais:** | *N/A* |
| **Parâmetro(s):** | *N/A* |
| **Ponto de Entrada:** | *N/A* |
| **Chamados relacionados** | **N/A** |
| **Requisito (ISSUE):** | **N/A** |
| **País(es):** | *N/A* |
| **Banco(s) de Dados:** | **SQL Server e Oracle** |
| **Tabelas utilizadas:** | **TMov, TItmMov** |
| **Sistema(s) operacional(is):** | **N/A** |
| **Versões/Release:** | **12.1.9 ou superior** |

## Descrição

Melhoria no sistema para permitir edição de item(ns) do Movimento de Baixa de Matéria Prima relacionado ao Processo Produtivo Simples (Produção Simples), quando o Movimento de Ordem de Produção (Produção Simples) conter apenas um item a ser produzido.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações do patch específico **12.1.9**deste chamado.

## Procedimento para Utilização

1. Através do "TOTVS Gestão de Estoque, Compras e Faturamento" acesse a aba "Estoque > Produção > Movimentação";
2. Selecione o Tipo de Movimento parametrizado para emissão de Ordem de Produção (Produção Simples) e escolha o filtro desejado;
3. Selecione o registro desejado na visão de movimentos disponíveis e clique no botão para "Receber" ou execute o Processo "Faturar/Receber";  
   Observações sobre a edição do movimento de Baixa de Matéria Prima:
   1. Será habilitada apenas se o movimento de Ordem de Produção houver somente um item;
   2. Aplicável somente para o Processo de Produção Simples;
   3. Faturamento da Ordem de Produção sem agrupamento de movimentos;
4. Proceda a edição desejada e salve o item e posteriormente o movimento de Baixa de Matéria Prima (Produção Simples).
