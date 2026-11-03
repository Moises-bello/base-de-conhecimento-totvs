---
content_hash: 159334d2226126be2c36710b31749c47bb6e10188e8d544e36d91995878ed820
fetched_at: '2026-06-29T00:08:04.622167+00:00'
page_id: '235575695'
product: rm
source: tdn-rm
title: ER_PCREQ-10854_Filtro de BPA por Unidade de Atendimento
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-10854_Filtro+de+BPA+por+Unidade+de+Atendimento
version: 115
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## 

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS HOSPITALAR | **Módulo** | RM SAUDE |
| **Segmento Executor** | SAÚDE | | |
| **Projeto** | R\_SAU\_RM\_V12\_1516 | **IRM** | PCREQ-10854 |
| **Requisito** | PCREQ-10854 | **Subtarefa** | SAU\_DEV-4653 |
|  |  | | |
| **País** | (X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
|  |  | | |

   

## Objetivo

 Esta implementação tem como objetivo adicionar filtro no BPA por unidade de atendimento

*.*

## Definição da Regra de Negócio

**RN001** - Permitir  criação de filtros no BPA por id ou descrição da unidade de atendimento.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Lançamentos de Procedimentos BPA | Alteração | Faturamento > Faturamento Sus > Lançamento de Procedimentos BPA | **RN001** |
|  |  |  |  |
|  |  |  |  |

**Exemplo de Aplicação:**

* Acessar o menu **"Faturamento > Faturamento Sus > Lançamento de Procedimentos BPA"**
* Clicar novo
* Campo Cód Unidade Atendimento ou Unidade Atendimento
* Executar novo filtro

## Protótipo de Tela

**Protótipo 01**

**Protótipo 02**

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
