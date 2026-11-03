---
content_hash: eba630575ab456e8b2ea22fd7d235cf7d44eea19dd7df1981843da4483c58391
fetched_at: '2026-06-29T00:09:07.750886+00:00'
page_id: '385845355'
product: rm
source: tdn-rm
title: DEDUANALYTICS-423 DT Fast Analytics - Valor de Acordos
type: documentation
url: https://tdn.totvs.com/display/LRM/DEDUANALYTICS-423+DT+Fast+Analytics+-+Valor+de+Acordos
version: 2
---

# NOME DO REQUISITO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Fast Analytics. |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Extração Fato Inadimplência. | N/A. | | Extração Fato A Receber | N/A |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Parametrização do Business Analytics no RM Integração. | N/A. | |
| **Cadastros Iniciais:** | N/A. |
| **Parâmetro(s):** | SPARAMGERAL.HABILITAFASTANALYTICS. |
| **Ponto de Entrada:** | N/A. |
| **Tickets relacionados** | N/A. |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | N/A |
| **País(es):** | Todos |
| **Banco(s) de Dados:** | SQL Server e Oracle. |
| **Tabelas Utilizadas:** | HCPARAMETROS  SPARAMGERAL |
| **Sistema(s) Operacional(is):** | Windows. |
| **Pacote:** | N/A |

## Descrição

Inclusão de campos para retornar o valor de acordo nas consultas das fatos Inadimplência e A Receber.

Fato de Inadimplência:

1-VLINADIMPLENCIAACORDO: Retorna o valor da inadimplência acumulada até o mês da extração referente as parcelas dos contratos de acordo que estão em atraso ou foram pagas com atraso.

2-VLINADIMPLENCIAACORDOMENSAL: Retorna o valor da inadimplência mensal referente as parcelas dos contratos de acordo que estavam em atraso até o mês da extração (mesmo que tenham sido pagas posteriormente).

Fato A Receber:

VLARECEBERACORDO: Retorna o valor a receber mensal referente as parcelas dos contratos de acordo com vencimento no mês da extração.
