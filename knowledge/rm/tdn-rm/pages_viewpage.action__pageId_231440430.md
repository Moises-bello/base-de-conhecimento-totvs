---
content_hash: 572bdf165cb0b697ebefb1d278a09af381df0d2ce282c65f1525ae7d6097263f
fetched_at: '2026-06-29T00:06:27.154933+00:00'
page_id: '231440430'
product: rm
source: tdn-rm
title: ER_PCREQ-10000_Gestão_de_Entrega_da_2ª._Via_de_Laudo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=231440430
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
| **Requisito** | * [PCREQ-10000](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-10000 "PCREQ-10000") | **Subtarefa** | * [SAU\_DEV-4224](http://jira.totvs.com.br/browse/SAU_DEV-4224) |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

## Objetivo

   Esta implementação tem como objetivo alterar o atual funcionamento da tela de Controle de Pedidos de Exames, incluindo no fluxo atual a possibilidade de Impressão de 2ª via do Laudo, sem a perda da referência do responsável pela retirada da primeira via. 

 

## Definição da Regra de Negócio

**RN001 -**Permitir a impressão da segunda via do laudo sem precisar cancelar a entrega.

 

**RN002 -**Tornar visível ao usuário o nome da pessoa, para quem o laudo foi entregue.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| [Controle de Pedidos de Exames] | [Alteração] | [Unidades Diagnóstico > Controle de Pedidos de Exames] | **RN001, RN002** |

**Exemplo de Aplicação:**

* Acessar o menu "**Unidades Diagnóstico > Controle de Pedidos de Exames**";
* Selecionar um exame qualquer e avançar as etapas até a etapa de "**Entregar Exame**";
* Digitar o nome do "**Responsável pela Retirada**" e clicar em OK;
* O nome do responsável pela retirada deverá ficar disponível ao posicionar o mouse sobre o registro, no histórico de Controle;
* Caso o status do Exame esteja como "**Entregue**", o campo "**Executar Ação**" deverá ter a ação "**Entregar Exame (2ª via)**";
* Quando Entregue a segunda via do Exame, este novo registro deverá persistir o nome do "**Responsável pela Retirada**" que for digitado.

**Tabelas Utilizadas**

* **SZHISTORICOSTATUS**

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
