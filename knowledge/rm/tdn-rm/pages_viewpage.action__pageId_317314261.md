---
content_hash: 78f066e63c034508d5ea6b73c42da91cc755680f41bd309f351f2baeb1d50dbf
fetched_at: '2026-06-29T00:08:46.971669+00:00'
page_id: '317314261'
product: rm
source: tdn-rm
title: 1134743 MATESTCNTFTOF01-875 DT Consistência - Contrato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=317314261
version: 95
---

# ITEM DE CONTRATO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento. |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Contrato | CtrCntAction. |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Faturamento Contrato | CtrFaturamentoContratoProcAction. | |
| **Cadastros Iniciais:** | Antes de iniciar o uso do módulo de Manutenção de Contratos é importante que o sistema esteja devidamente parametrizado e as tabelas utilizadas na elaboração do contrato sejam cadastradas.  Parâmetros de Contrato: <http://wikihelp.totvs.com.br/WikiHelp/EST/EST.Contratos.aspx>  Tabelas de Contrato: <http://wikihelp.totvs.com.br/WikiHelp/EST/EST.TabelasContratos.aspx> |
| **Parâmetro(s):** | Orçamento no Tipo de Movimento |
| **Ponto de Entrada:** | N/A. |
| **Tickets relacionados** | N/A. |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | N/A. |
| **País(es):** | Brasil. |
| **Banco(s) de Dados:** | SQL Server e Oracle. |
| **Tabelas Utilizadas:** | N/A |
| **Sistema(s) Operacional(is):** | Windows 7 Service Pack1 e superiores. |

## Descrição

Permitir aos usuários do módulo de Contratos, ao utilizar orçamento e seu tipo de contrato afetar orçamento o correto processo de faturamento.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. No **Gestão de Estoque, Compras e Faturamento**, acesse **Ambiente >> Parâmetros >> Gestão de Estoque, Compras e Faturamento**
2. Nos parâmetros do tipo de movimento, Etapa 46 - Orçamento. Configure item a seguir:
   1. Controla Orçamento

## Procedimento para Utilização

1. No Gestão de Estoque, Compras e Faturamento, acesse Contratos / Manutenção de Contratos.

O sistema apresenta a janela de Filtros - Contratos. Selecione uma opção de filtro.

2. Selecione um contrato para ser faturado, acesse processo "Faturamento Contrato"

O sistema apresenta a janela de processo "Faturamento Processo".

3. Na janela de processo "Faturamento Processo".

Selecione o tipo de movimento

Execute

4. Se o tipo de contrato estiver definido para afetar orçamento, vai consistir se o tipo de movimento está parametrizado para **Contorlar Orçamento**, se não estiver vai ser exibido mensagem informando a necessidade de configurar o tipo de movimento.

Mensagem: Tipo do contrato: "Código do contrato" afeta orçamento, tipo de movimento: "Tipo Movimento" precisa ter orçamento configurado.

divs
