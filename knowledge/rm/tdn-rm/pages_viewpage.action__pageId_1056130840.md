---
content_hash: 6382c8034c0508377942a790e192de03a294d3157f410e87ceee7aee2b37ccf4
fetched_at: '2026-06-29T00:05:51.825723+00:00'
page_id: '1056130840'
product: rm
source: tdn-rm
title: Ajuste e Evoluções Abr/2026 (NFS-e) - TPF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1056130840
version: 5
---

# Conteúdo

1Conteúdononenone

# 1. Sobre

Esta atualização traz atualizações no xml do layout TPF.

# 2. Versões para atualização

Biblioteca RM:

* 12.1.2506.296
* 12.1.2510.219
* 12.1.2602.137

# 3. Principais Alterações

## Incluído os novos valores para a tag tpRetPisCofins e atualizado a tag "csll"

* O valor da tag **"tpRetPisCofins"** será gerado da seguinte forma:

Se não houver os tributos **IBS/CBS**

| **Código** | **PIS Retido?** | **COFINS Retido?** |
| --- | --- | --- |
| **1** | Sim | Sim |
| **2** | Não | Não |

Se houver **IBS/CBS**

| **Código** | **PIS Retido?** | **COFINS Retido?** | **CSLL Retida?** |
| --- | --- | --- | --- |
| **0** | Não | Não | Não |
| **3** | Sim | Sim | Sim |
| **4** | Sim | Sim | Não |
| **5** | Sim | Não | Não |
| **6** | Não | Sim | Não |
| **7** | Não | Sim | Sim |
| **8** | Não | Não | Sim |
| **9** | Sim | Não | Sim |

* O valor da tag **"csll"** será gerado com a soma dos valores de CSLL, PIS e COFINS Retidos

Exemplo

## Alterado a montagem dos grupos de IBS e CBS.

Os grupos deixam de ser gerados somente quando os tributos IBS e CBS possuem base de calculo e passam a considerar também se o somatório dos valores do serviço é igual a 0.

## Alterada a geração da tag regimeTribSN.

Foi alterada a geração da tag regimeTribSN para considerar os campos "Optante Regime Simplificado" e "Sublimite excedido" dos dados fiscais da filial.
