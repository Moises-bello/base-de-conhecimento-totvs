---
content_hash: 5a05e7924a8fe5ff2b410fed2e3f61ba3aa965628f6147608e3a66474b21655c
fetched_at: '2026-06-29T00:10:22.026113+00:00'
page_id: '496027297'
product: rm
source: tdn-rm
title: MATFATCMPCRM01-6783 DT Conta Contábil para o SPED
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=496027297
version: 1
---

# Conta Contábil para o SPED

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Backoffice |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento. |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | LI.01.0025 | ESCRITURAÇÃO | |
| **Cadastros Iniciais:** | - |
| **Parâmetro(s):** | Gerar Escrituração deve estar marcado. |
| **Ponto de Entrada:** | - |
| **Tickets relacionados** | MATFATCMPCRM01-6783 |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | MATFATCMPCRM01-6783 |
| **País(es):** | Bra |
| **Banco(s) de Dados:** | SQLServer e Oracle |
| **Tabelas Utilizadas:** | TITMMOVFISCAL |
| **Sistema(s) Operacional(is):** | - |
| **Pacote:** | - |

## Descrição

Implementação do campo "Conta Contábil para o SPED" no Item do Movimento. Essa Conta Contábil será utilizada nas rotinas da EFD Contribuições, Sped Fiscal e Integração com o TAF.

## Procedimento para Utilização

 Com o parâmetro **Gerar Escrituração** da etapa **Fis - Escrituração 1/2** (parâmetros do Tipo de Movimento) **marcado**, o campo **Conta Contábil para o Sped** será exibido na aba **Integrações → Fiscal** do Item de Movimento.
