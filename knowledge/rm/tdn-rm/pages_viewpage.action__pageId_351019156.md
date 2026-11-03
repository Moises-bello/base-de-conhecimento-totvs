---
content_hash: b2f468e8b7874431167476fda0232d66aa1b2e3c5f25fb8d760cca9083a009e9
fetched_at: '2026-06-29T00:08:55.854057+00:00'
page_id: '351019156'
product: rm
source: tdn-rm
title: DT Bloco K - Geração do Saldo das Contas Consolidadas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=351019156
version: 5
---

# Geração do Saldo das Contas Consolidadas

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Educacional* |
| **Módulo:** | **TOTVS Gestão Contábil*.* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Atualização do Saldo das Contas do Plano de Contas Consolidado | CtbAtualizaSaldoConsolidadoProcAction |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | SPED Contábil | CtbSpedContabilProcessAction | |  |  | |
| **Cadastros Iniciais:** | *N/A* |
| **Parâmetro(s):** | *N/A* |
| **Ponto de Entrada:** | *N/A.* |
| **Tickets relacionados** | *N/A* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | [CONTROLADORIA01-1200](http://jiraproducao.totvs.com.br/browse/CONTROLADORIA01-1200);[CONTROLADORIA01-1560](http://jiraproducao.totvs.com.br/browse/CONTROLADORIA01-1560) |
| **País(es):** | *Brasil.* |
| **Banco(s) de Dados:** | *SQLSever / Oracle* |
| **Tabelas Utilizadas:** | *N/A* |
| **Sistema(s) Operacional(is):** | *Windows.* |

## Descrição

O processo "Atualização do Saldo das Contas do Plano de Contas Consolidado" tem como objetivo gerar os saldos das contas do Plano de Contas Consolidado, bem como os valores Eliminados entre as empresas Controladas Ativas e Controladora.

**Execução do processo:**

No modulo TOTVS Gestão Contábil ir no menu Obrigações Acessórias > Bloco K > Cálculo Saldo Consolidado.

Na tela do processo marcar os parâmetros e executar. Obs.: O campo "Período de Cálculo do Saldo" deve ser a mesma data da Escrituração que será gerada na rotina "Gerar SPED Contábil".
