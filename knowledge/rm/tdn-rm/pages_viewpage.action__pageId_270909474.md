---
content_hash: ff3c4e9c18f1828c433a625be61a4f709d8324c1dbd01c3896ce46c3a7aad895
fetched_at: '2026-06-29T00:08:24.882645+00:00'
page_id: '270909474'
product: rm
source: tdn-rm
title: ER SAUHRM02-484 Obrigatoriedade do Médico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270909474
version: 107
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS GESTÃO HOSPITALAR | **Módulo** | RM Saúde |
| **Segmento Executor** | Saúde | | |
| **Projeto** | SAUHRM02 | **IRM** | SAUHRM02-481 |
| **Requisito** | SAUHRM02-484 | **Subtarefa** | SAUHRM02-551 |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

### Objetivo

**Este documento tem como objetivo especificar o requisito de Obrigatoriedade do médico responsável e do médico solicitante para registrar atendimentos interno e externos.**

### Definição da Regra de Negócio

**RN001 -**  Criar parâmetro geral na aba Registro e Controles II

**RN002 -**  Aplicar parâmetro nas rotinas de registro atendimento interno e externo.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| [Parâmetros Gerais] | [Alteração] | [Opções-> Parâmetros -> Parâmetros Gerais] | **RN001** |
| [Atendimento Interno] | [Criação] | [Atendimento-> Internação-> Registro de Internação] | **RN002** |
| [Atendimento Externo] | [Criação] | [Atendimento-> Pronto Atendimento/Ambulatório-> Registro de Atendimento ] | **RN002** |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
