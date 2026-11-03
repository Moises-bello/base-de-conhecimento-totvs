---
content_hash: 4f9f418b4a42e50a7812547aa6970ec71bddd3ba3783a5e162139719f6d1a302
fetched_at: '2026-06-29T00:08:19.328110+00:00'
page_id: '267781117'
product: rm
source: tdn-rm
title: ER_SAUHRM02-29_Adaptação_do_menu_server
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=267781117
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
| **Projeto** | SAUHRM02 | **IRM** | SAUHRM02-28 |
| **Requisito** | SAUHRM02-29 | **Subtarefa** | SAUHRM02-87 |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

## Objetivo

Transportar os menus do projeto RM.Sau para o projeto RM.Sau.Server.

No arquivo SauMenuController devem ser incluídos/revisados todos os componentes que formam o menu da MDI nova.

 

## Definição da Regra de Negócio

**RN001**

1. Criar no projeto RM.Sau.Server, arquivo SauMenuController.cs, as chamadas para as telas do sistema, existentes no projeto RM.Sau, arquivo SauRibbonControl.cs.
2. Remover as partes do código referentes ao antigo menu.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Menu RM | [Alteração] | Todo o menu | RN001 |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
