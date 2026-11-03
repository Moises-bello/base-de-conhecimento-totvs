---
content_hash: 0abcc24f0284b93e197b717696bc40e5d5e02021f68bb7c949af3b19046e2fcd
fetched_at: '2026-06-29T00:08:51.618918+00:00'
page_id: '337351667'
product: rm
source: tdn-rm
title: DT Opção de quebra por natureza ou centro de custo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=337351667
version: 1
---

# Opção de quebra por natureza ou centro de custo

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão Financeira* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Fluxo de Caixa | Fluxo de Caixa |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Inclusão de Lançamentos | Lançamento - Inclusão / Alteração | | Inclusão de Extratos | Extrato de Caixa - Inclusão | | Aplicação Financeira | Aplicação Financeira | | Baixa | Baixa | |
| **Cadastros Iniciais:** | Lançamentos, Extratos, Aplicação Financeira |
| **Parâmetro(s):** | Considerar Centro de Custo por Natureza |
| **Ponto de Entrada:** | N/A |
| **Tickets relacionados** | N/A |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | <http://jiraproducao.totvs.com.br/browse/FINANCEIRO01-2968> |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | Oracle e SqlServer |
| **Tabelas Utilizadas:** | FCFO; FLAN; FLANRATCCU; FLANBAIXA; FLANBAIXARATCCU; TTBORCAMENTO; FPARAM; FACORDOREL; FLANORIGINAL; FAPLFIN; FTIPOAPLFIN; FXCX; |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Criar uma opção nos parâmetros para que Fluxo de Caixa para seja quebrado por Natureza Orçamentaria ou Centro de Custo.

## Procedimento para Configuração

1. Nos Parâmetros do Financeiro | Contas a Pagar / a Receber | Recursos Adicionais parametrizar conforme abaixo:

## Procedimento para Utilização

1. Em TOTVS Gestão Financeira, Gestão Financeira, Fluxo de Caixa, foi criado na aba de parâmetros, o parâmetro "Considerar Centro de Custo por Natureza". Quando marcado, o sistema ordena e classifica os valores baseados também no Centro de Custo marcados para aquela Natureza Orçamentaria.
