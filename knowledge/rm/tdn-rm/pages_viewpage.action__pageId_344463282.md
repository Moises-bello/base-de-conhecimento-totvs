---
content_hash: 5859e5b074b42ce8add8cb641ab13c2ac95a97aaa896929cbf6b09d0fd7d9643
fetched_at: '2026-06-29T00:08:53.211664+00:00'
page_id: '344463282'
product: rm
source: tdn-rm
title: RMFIN-1540 DT Inclusão da coluna CDTABELAINSUMO no processo de Esquema Apuração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=344463282
version: 1
---

# Inclusão da coluna CDTABELAINSUMO no processo de Esquema Apuração

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gesão de Custos |
| **Função:** | Esquema de apuração - tabela SZ0TABELAINSUMO |
| **Situação:** | Como analisa de custos eu preciso que o código da tabela do insumo seja importada pelo processo de Esquema de Apuração para manter a integridade dos códigos X tabelas. |
| **Solução:** | Alterações nos processos de esquema de apuração **Consumo Hospitalar** e **Consumo Pacote:**    Na etapa de validação do LAYOUT, incluída a verificação das colunas obrigatórias **CDTABELAINSUMO** e **NOTABELAINSUMO.**    Na etapa de importação dos dados do lançamento, incluída a coluna **CDTABELAINSUMO**.    Na etapa de tabelas auxiliares, alterado o método para incluir o Insumo e adicionada a coluna **SZ0INSUMO.CDTABELAINSUMO,** que é obrigatória.    Na etapa de tabelas auxiliares, criado um novo método para incluir os dados na **SZ0TABELAINSUMO** utilizando as colunas **CDTABELAINSUMO** e **NOTABELAINSUMO** da consulta SQL do sistema terceiro. |
| **Tabelas:** | SZ0TABELAINSUMO |
