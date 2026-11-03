---
content_hash: 03a00f470d03d8d24f3d11d0598c9c52660dd328ecdfba5677de3a21f1fe08eb
fetched_at: '2026-06-29T00:08:51.701047+00:00'
page_id: '338362818'
product: rm
source: tdn-rm
title: DT Parâmetro Definir data baixa do Acordo com Aprovação.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=338362818
version: 4
---

# Parâmetro para definir a data da baixa do acordo quando utiliza Aprovação.

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Geração de Acordo | Geração de Acordo |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Baixa de Lançamento | Baixa de Lançamento | | Template de Acordo | Template de Acordo | |
| **Cadastros Iniciais:** | Definir no template de acordo uma data para ser utilizada no acordo quando utiliza-se efetivação. |
| **Tickets relacionados** | 1517332 |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | <http://jiraproducao.totvs.com.br/browse/FINANCEIRO01-4397>  0c783de1-186e-383b-975c-a1acd7d76cb5FINANCEIRO01-12089 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL e Oracle |
| **Tabelas Utilizadas:** | FTEMPLATEACORDO |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Quando template de acordo for parametrizado para Efetivação como 'Ao Aprovar' ou 'Ao pagar primeira parcela', será possível definir uma data de Aprovação/Sistema ou Geração do Acordo, para realizar a baixa dos lançamentos que serão baixados por acordo.

A partir da versão 12.1.27 a opção Data Aprovação/Sistema" foi alterada para "Data Sistema" mantendo o comportamento atual do sistema e foi criada a opção "Data Aprovação/Efetivação", quando selecionada essa opção e a Efetivação for "Ao aprovar"  ou "Ao Pagar primeira Parcela", a data da baixa dos lançamentos de origem do acordo poderão ser a data de aprovação ou a data da baixa da primeira parcela . 

## Procedimento para Configuração

* Escolher dentre as opções, qual a data que deverá ser utilizada na baixa dos lançamentos baixados por acordo.

## Procedimento para Utilização

* Se a data de Baixa utilizada for a 'data geração do acordo', o sistema irá utilizar a data do acordo para baixar os lançamentos do acordo.

* Se a data de Baixa for a 'Aprovação/Sistema', o sistema irá utilizar a data do atual para baixar os lançamentos do acordo.

IMPORTANTE: Lembrando que para Templates de Acordo que não foram definidos, ainda utilizarão a data do Acordo para realizar a Baixa.
