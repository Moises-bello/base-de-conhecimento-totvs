---
content_hash: 0ef74591ad06428557ae5d32ca3ae92c949bfcf9531073c65330a6c4367b6421
fetched_at: '2026-06-29T00:06:27.482307+00:00'
page_id: '232822799'
product: rm
source: tdn-rm
title: ER_PCREQ-10002_Campo_Alterar_o_Título_do_Exame
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=232822799
version: 120
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS SAÚDE | **Módulo** | RM SAÚDE |
| **Projeto** | * [R\_SAU\_RM\_V12\_1516](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B11311%5D+%3D+R_SAU_RM_V12_1516 "R_SAU_RM_V12_1516") | **IRM** | * [PCREQ-9999](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10207%5D+%3D+PCREQ-9999 "PCREQ-9999") |
| **Requisito** | * [PCREQ-10002](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-10002 "PCREQ-10002") | **Subtarefa** | * [SAU\_DEV-4236](http://jira.totvs.com.br/browse/SAU_DEV-4236) |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

### Objetivo

    O objetivo desta especificação é disponibilizar a funcionalidade de alteração de títulos de exames, para que um mesmo título de exame seja exibido para exames com link.

## Definição da Regra de Negócio

   **RN001 -** Quando o link entre exames for realizado, o sistema deve permitir ao usuário selecionar um título, que será utilizado na impressão dos mesmos.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| [Controle de Pedidos de Exames] | [Alteração] | Controle de Pedidos de Exames]]> | **RN001** |

**Exemplo de Aplicação:**

* Acesse o menu "**Unidades Diagnóstico > Controle de Pedidos de Exames**".;
* Aplique um filtro que traga ao menos um exame do paciente desejado;
* Selecione o filtro e Clique no botão "**Link Laudos**", no cabeçalho da página;
* Selecione os exames com os quais deseja realizar o **Link;**
* Clique em "**Relacionar**";
* Avance o documento até o status "**Emitir Resultado**". O nome digitado deverá aparecer para os exames do link.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
