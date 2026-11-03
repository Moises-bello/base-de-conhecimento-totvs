---
content_hash: 441d1b3c32900a077e0886da07513eab037ac9f2498699a06f0817ac62b5ae29
fetched_at: '2026-06-29T00:08:09.724089+00:00'
page_id: '239038888'
product: rm
source: tdn-rm
title: ER_SAUHRM01-53_Lançamento_Automático_Exames_APAC
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=239038888
version: 119
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS HOSPITALAR | **Módulo** | TOTVS HOSPITALAR |
| **Segmento Executor** | SAÚDE | | |
| **Projeto** | SAUHRM01 | **IRM** | SAUHRM01-38 |
| **Requisito** | SAUHRM01-53 | **Subtarefa** | SAUHRM01-259 |
| **País** | (X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

   

## Objetivo

 

*Este documento tem como objetivo especificar o requisito de Lançamento automático de exames de atendimento externo na APAC*

## Definição da Regra de Negócio

**RN001** - Lançar automaticamente os exames solicitados em atendimento externo ou Unidade de diagnóstico/Pedido de exames paciente interno na APAC quando é faturado SADT e configurado o parâmetro Executa Lançamentos de APAC na geração de pedidos de exames

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Registro de Atendimentos Externos | [Criação] | [Atendimento>Pronto Atendimento/Ambulatório> Registro de Atendimentos Externos] | RN001 |

*Exemplo de Aplicação:*

* Acesse Opçoes > Parâmetros > Parâmetros Sus Configurar o parâmetro Executa Lançamentos de APAC na geração de pedidos de exames
* Acesse Atendimento>Pronto Atendimento/Ambulatório> Registro de Atendimentos Externos e lançar solicitações de exames

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
