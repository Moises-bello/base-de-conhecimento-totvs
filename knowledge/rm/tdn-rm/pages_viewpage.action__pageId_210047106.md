---
content_hash: 2eb481a267769faf34ed0d19a5d8306884901b6f93d3a42fa5cadbf6489c0ea3
fetched_at: '2026-06-29T00:06:14.531781+00:00'
page_id: '210047106'
product: rm
source: tdn-rm
title: TTMEHX_DT_Formato_Impressão_do_DACTE_no_XML
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=210047106
version: 1
---

# FORMATO DE IMPRESSÃO DO DACTE NO XML

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | ***Gestão de Estoque Compras Faturamento*** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | **CTE.004** | *CT-E - RELATÓRIO* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *CTE.001* | *CT-E - PARAMETRIZAÇÃO DE MOVIMENTO* | |
| **Cadastros Iniciais:** | *Movimento de CT-e.* |
| **Parâmetro(s):** | *Tipo de Impressão do CT-e* |
| **Ponto de Entrada:** | *N/A* |
| **Chamados Relacionados** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL e Oracle* |
| **Tabelas Utilizadas:** | *TCTe, TTMvExt* |
| **Sistema(s) Operacional(is):** | *N/A* |
| **Versões/Release:** | *11.82.42* |
| **Versão Corrigida:** | *11.82.42* |
| **Versão Expedida:** | *11.82.42* |

## Descrição

Ajuste para que o sistema considere corretamente o formato do relatório definido no Tipo de Movimento etapa “Fis – Conhecimento de Transporte” (1: Retrato; 2: Paisagem).

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *11.82.42 ou superior* deste chamado

## Procedimento para Utilização

1. No módulo*TOTVS Gestão de Estoque Compras e Faturamento* acesse a parametrização do tipo de movimento para emissão de Conhecimento de Transporte Eletrônico (CT-e) e altere através da etapa "Fis - Conhecimento de Transporte" o formato da impressão do relatório DACTE;
2. Acesse a emissão de movimento de CT-e e inclua novo movimento;
3. Acesse a tela para envio do CT-e (Vendas / Faturamento / Conhecimento de Transporte Eletrônico) e transmita o movimento recém-criado;
4. O sistema deverá preencher no XML o conteúdo da tag <tpImp> que com o valor "1" para o formato Retrato e "2" para o formato Paisagem.
