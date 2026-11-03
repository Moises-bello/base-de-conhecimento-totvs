---
content_hash: 9d540271e978e8a16e690c43dcc2ac0314a66b62eccee7f630267f3127bd71ce
fetched_at: '2026-06-29T00:08:20.263556+00:00'
page_id: '268575799'
product: rm
source: tdn-rm
title: ER_SAUHRM02-71_Informaçoes_SZLOGATENDIMENTO
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=268575799
version: 108
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS GESTÃO HOSPITALAR | **Módulo** | RM Saúde |
| **Segmento Executor** | Saúde | | |
| **Projeto** | SAUHRM02 | **IRM** | SAUHRM02-73 |
| **Requisito** | SAUHRM02-71 | **Subtarefa** | SAUHRM02-109 |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

   

## Objetivo

 

*Este documento tem como objetivo especificar o requisito de informações na tabela SZLOGATENDIMENTO*

## Definição da Regra de Negócio

RN001 - Gravar campos  CODPACIENTE e CODATENDIMENTO na  tabela SZLOGATENDIMENTO ,nas fases Inicio da Triagem e Termino da Triagem quando a triagem for feita após o registro de atendimento.

 

RN002  -Gravar a Data/Hora atual do servidor caso o campo DATASENHAATENDIMENTO venha nulo ao registrar alterações no atendimento  no status "Paciente gerou nova senha de Atendimento"

 

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Registro de atendimento Externo | [Alteração] | Atendimento/ Pronto Atendimento /Ambulatório / Registro de Atendimentos Externos | RN001 |

Tabelas Utilizadas

* SZLOGATENDIMENTO

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
