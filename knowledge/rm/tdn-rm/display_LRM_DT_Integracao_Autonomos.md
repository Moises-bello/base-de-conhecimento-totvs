---
content_hash: 2f04381db7f52833d15f5ba83e60d06f92e14640a47252aa1b35898d7fcfa30c
fetched_at: '2026-06-29T00:06:14.592829+00:00'
page_id: '210048017'
product: rm
source: tdn-rm
title: DT_Integracao_Autonomos
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Integracao_Autonomos
version: 3
---

# INTEGRAÇÃO FINANCEIRA RM x PROTHEUS (AUTÔNOMOS)

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **TOTVS Folha de Pagamento** |
| **Rotina:** | | **Rotina** | Nome Técnico | | --- | --- | | *Encargos* | *Integração Financeira* | |
| **Versões/Release:** | *12.1.6* |

## Descrição

O objetivo dessa implementação é possibilitar o cálculo dos encargos dos autônomos provenientes de outros backoffices nos processos: **Geração do SEFIP, Guia de INSS e Folha Analítica.**

## Procedimento para Utilização

**Configurar a integração:**

A partir desse momento o sistema já está preparado para receber mensagens do tipo EXTERNALAUTONOMOUSPAYMENT.

Através da nova visão criada **Encargos / Autônomos**, é possível verificar todos os funcionários autônomos integrados através da mensagem única.

**Executar os processos**

• Sefip

› Executar o **Sefip Encargos / Sefip / Geração Sefip** marcando o novo parâmetro.

› Verificar se os autônomos foram incluídos no arquivo.

• Guia

› Executar a guia (Encargos->Guia de INSS) marcando o novo parâmetro

›  Verificar se as guias dos autônomos foram geradas e com os autônomos

› Verificar se o(s) lançamento(s) foi(ram) gerado(s)

• Folha Analítica

› Executar o processo **Folha Mensal / Folha Analítica** marcando o parâmetro.

› Verificar se os autônomos foram processados
