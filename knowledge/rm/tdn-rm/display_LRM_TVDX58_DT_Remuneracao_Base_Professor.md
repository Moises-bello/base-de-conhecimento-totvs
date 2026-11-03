---
content_hash: 827d2b977b94cdf5f6c1f96e466feef04fdec5ddcfeeb9d8e9301fabf6cad7a9
fetched_at: '2026-06-29T00:08:15.159367+00:00'
page_id: '244733115'
product: rm
source: tdn-rm
title: TVDX58_DT_Remuneracao_Base_Professor
type: documentation
url: https://tdn.totvs.com/display/LRM/TVDX58_DT_Remuneracao_Base_Professor
version: 3
---

# REMUNERAÇÃO BASE DE PROFESSOR

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **Folha de Pagamento** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Remuneração Base* | *Remuneração Base de Professor* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Remuneração Base** | *Remuneração Base de Professor* | | **Férias**  *13o.Salário*  *Rescisão*  *Salário Maternidade* | **Cálculo de Férias**  *Cálculo da 13o. Salário*  *Cálculo de Rescisão*  *Cálculo de Salário Maternidade* | |
| **Cadastros Iniciais:** | *Sindicato, Eventos* |
| **Parâmetro(s):** | *Compõe Remuneração Base de Professor Utiliza cálculo de média de Remuneração Base para Professor* |
| **Ponto de Entrada:** | *N/A* |
| **Chamados Relacionados** | *TVDX58, TVNCI9* |
| **Requisito (ISSUE):** | *Folha* |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL Server, Oracle* |
| **Tabelas Utilizadas:** | *PEVENTO, PSINDIC, PSINDREMBASE, PFREMBASE, PFREMBASEMES, PFREMBASEMESEVT, PFREMBASEEVTMED* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

Implementação da Remuneração Base de Professor.

Opções de Cálculo:

* Maior Remuneração
* Média da Remuneração
* Última Remuneração
* Comparativo Media X Última Remuneração
