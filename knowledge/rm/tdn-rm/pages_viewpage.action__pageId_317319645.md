---
content_hash: b65d17eeead2265715e32510ab51a9ba6814c0848fb0a8f75f8c2da9b8194d3f
fetched_at: '2026-06-29T00:08:47.007947+00:00'
page_id: '317319645'
product: rm
source: tdn-rm
title: ER MATFATCMPCRM01-1660 CT-e OS Aéreo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=317319645
version: 94
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Estoque, Compras e Faturamento | **Módulo** | Movimento |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | MATFATCMPCRM01 | **IRM/EPIC1** | MATFATCMPCRM01-1660 |
| **Requisito/Story/Issue1** |  | **Subtarefa1** |  |
| **Chamado/Ticket2** | NA | | |
| **País** | Brasil | | |
| **Outros** | NA | | |

## 

## Objetivo

Especificar as alterações necessárias no sistema para o envio de um CT-e OS modal aéreo.

## 

## Definição da Regra de Negócio

Parâmetros - Tipo de Movimento

* Na etapa Fis - Conhecimento de Transporte, no ComboBox Modal (TTMVEXT.MODAL) deve ser acrescentado o valor "Aéreo".

Envio do XML

* Quando **Modal** do CT-e OS igual a "Aéreo", a tag "modal" deve ser preenchida com "02-Aéreo".
* Quando **Modal** do CT-e OS igual a "Aéreo", o grupo de informações "infModal" não deve ser preenchido, pois não existe leiaute específico para este modal.
* Os demais grupos de informações não citados nessa especificação não sofrem alteração em relação a forma como já são gerados para os outros tipos de CT-e OS que estão no mercado.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| [ACAA040 – Parâmetros] | [Alteração] | [Atualizações -> Acadêmico-> Tesouraria] | - |
| [ACAA050 – Negociação Financeira] | [Envolvida] | [Atualizações -> Acadêmico-> Tesouraria] | - |
| [ACAA060 – Cadastro de Pedidos] | [Criação] | [Atualizações -> Acadêmico-> Cadastros] | - |

**Tabelas Utilizadas**

* TTMVEXT - Tipos de Movimento

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
