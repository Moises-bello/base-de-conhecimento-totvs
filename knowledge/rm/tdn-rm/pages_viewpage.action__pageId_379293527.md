---
content_hash: 8ee0f07937fe04531062615a4574258186c3b738b4aae5891674a61cb411680e
fetched_at: '2026-06-29T00:09:02.183221+00:00'
page_id: '379293527'
product: rm
source: tdn-rm
title: DT Cupom Fiscal com Cliente / Fornecedor de fora do Estado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=379293527
version: 86
---

# CUPOM FISCAL COM CLIENTE / FORNECEDOR DE FORA DO ESTADO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção & Projetos |
| **Módulo:** | TOTVS Gestão de Estoque, Compras e Faturamento |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Cupom Fiscal | MovCupomFiscalData |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | MovCupomFiscalData | Cupom Fiscal | |
| **Tickets relacionados** | Não se aplica. |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server e Oracle |
| **Tabelas Utilizadas:** | TCUPOMFISCAL - Cupom Fiscal  TMOV - Movimento |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Esta melhoria tem como objetivo possibilitar que o TOTVS Gestão de Estoque, Compras e Faturamento, durante a inclusão de Cupom Fiscal via TotvsMessage ou Web Service, tratar a questão do Cliente / Fornecedor de fora do estado. 

## Funcionamento

Durante o processo de inclusão do Cupom Fiscal, seja via  primeiro TotvsMessage ou Web Service, será atendida a regra abaixo.

* Caso o CPF do Adquirente venha preenchido e Nome do Adquirente esteja em branco, será feita uma consulta no cadastro de Cliente / Fornecedores para buscar o nome do mesmo.
* Caso seja encontrado mais de um cadastro com o mesmo CPF/CNPJ, não será preenchido o Nome do Adquirente.

Independente do Cupom Fiscal ser do tipo "SAT" ou "Normal", a regra será a mesma.

divs
