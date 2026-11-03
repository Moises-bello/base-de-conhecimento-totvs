---
content_hash: 34c26925aec6146d48e6993ad1cd942dedf744afa3fc7dd8baa1f42829b89df9
fetched_at: '2026-06-29T00:06:27.307904+00:00'
page_id: '232819191'
product: rm
source: tdn-rm
title: ER_PCREQ-10001_Adequação_Visão_Controle_de_Pedidos_de_Exames
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=232819191
version: 120
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS SAÚDE | **Módulo** | RM SAÚDE |
| **Projeto** | * [R\_SAU\_RM\_V12\_1516](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B11311%5D+%3D+R_SAU_RM_V12_1516 "R_SAU_RM_V12_1516") | **IRM** | * [PCREQ-9999](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10207%5D+%3D+PCREQ-9999 "PCREQ-9999") |
| **Requisito** | * [PCREQ-10001](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-10001 "PCREQ-10001") | **Subtarefa** | * [SAU\_DEV-4230](http://jira.totvs.com.br/browse/SAU_DEV-4230) |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

## Objetivo

    Esta implementação tem como objetivo, fornecer ao usuário a visão do profissional executante, na tela de controle de pedidos de exames.

## Definição da Regra de Negócio

**RN001 -**Ao acessar a view de Controle de Pedidos de exames, o usuário deverá ter, dentre as informações do registro, o nome do profissional executante.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| [Controle de Pedidos de Exames] | [Alteração] | [Unidades Diagnóstico > Controle de Pedidos de Exames] | **RN001** |

**Exemplo de Aplicação:**

* Acessar a tela de controle de pedidos de exames e executar um filtro que permita a exibição de pelo menos um item na grid;
* A grid deverá conter o registro do profissional executante.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
