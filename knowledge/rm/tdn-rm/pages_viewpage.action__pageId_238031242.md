---
content_hash: fa33efbd0e0774237ca2b75cf78d4581a2843fc4c182a16e5863d72875926521
fetched_at: '2026-06-29T00:08:08.350653+00:00'
page_id: '238031242'
product: rm
source: tdn-rm
title: ER_SAUHRM01-48_Log_Alteração_Cadastro_Leitos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=238031242
version: 122
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
| **Projeto** | SAUHRM01 | **IRM** | [SAUHRM01-37](http://jiraproducao.totvs.com.br/browse/RHRM01-37) |
| **Requisito** | [SAUHRM01-48](http://jiraproducao.totvs.com.br/browse/RHRM01-48) | **Subtarefa** | [SAUHRM01-204](http://jiraproducao.totvs.com.br/browse/RHRM01-204) |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

## Objetivo

*Este documento tem como objetivo especificar o requisito de Log para controle de alterações no cadastro de leitos.*

## Definição da Regra de Negócio

**RN001** - Permitir que sejam logadas as alterações feitas no cadastro de leitos, bem como motivo da alteração, usuário e data de alteração.

**RN002** - Permitir que sejam logadas as alterações feitas no cadastro de leitos (controle de ocupação de leitos), bem como motivo da alteração, usuário e data de alteração.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| [Cadastro de Leitos] | [Alteração] | [Cadastros > Registro e Controle > Leitos] | RN001 |
| [Controle de Ocupação de Leitos] | [Alteração] | [Atendimento > Internação > Controle de Ocupação de Leitos] | RN002 |

Exemplo de Aplicação:

* Alterar o cadastro de leito, informando o motivo.
* Atualizar Controle de Ocupação de Leito, informando o motivo
* Acessar Anexo > Log de Leitos

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
