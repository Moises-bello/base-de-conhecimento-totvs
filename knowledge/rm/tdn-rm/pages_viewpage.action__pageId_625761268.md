---
content_hash: ab77dbbe05770dedfc93ec23a1d71347bfdc6ac0b9611fd23465814b468b266c
fetched_at: '2026-06-29T00:11:04.203291+00:00'
page_id: '625761268'
product: rm
source: tdn-rm
title: FISCAL01-15458 - DT Parâmetros de Processos - Processo FECP Fundo de Combate
  a Pobreza - MDI
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=625761268
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Cadastro Parâmetros de Processos |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | 1. [FISCAL01-15458](https://jiraproducao.totvs.com.br/browse/FISCAL01-15458) |

## **02. SITUAÇÃO/REQUISITO**

Considerar o novo cadastro .Net verificando o parâmetro HABILITANOVOCADPARAMPROCESSO da tabela DPARAMETROS para o cálculo do FECP RJ e considerar o parâmetro de processo pela filial de contexto.

***SubGrupo do Processo:***

Produtos não considerados no cálculo do FECP

## **03. SOLUÇÃO**

A geração de Lançamentos do FECP RJ passa a considerar também os processos da MDI com base no parâmetro ***HABILITANOVOCADPARAMPROCESSO.**.*
