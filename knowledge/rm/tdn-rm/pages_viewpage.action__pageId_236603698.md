---
content_hash: f7cc4669795b029ddb5364aa697dec9d774a8e7939c08a52cd75dc6121ad489c
fetched_at: '2026-06-29T00:08:07.094970+00:00'
page_id: '236603698'
product: rm
source: tdn-rm
title: ER_PCREQ-10895_Processamento_de_Requisição_na_tela_de_Edição
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=236603698
version: 116
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### 

# Processamento de requisição na tela de edição

### (Obrigatório)

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão Hospitalar | **Módulo** | Saúde |
| **Segmento Executor** | Saúde | | |
| **Projeto1** | * [R\_SAU\_RM\_V12\_1516](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B11311%5D+%3D+R_SAU_RM_V12_1516 "R_SAU_RM_V12_1516") | **IRM1** | * [PCREQ-10841](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10207%5D+%3D+PCREQ-10841 "PCREQ-10841") |
| **Requisito1** | * [PCREQ-10895](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-10895 "PCREQ-10895") | **Subtarefa1** | SAU\_DEV-4729 |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### (Obrigatório)

## Objetivo

 Este requisito tem a finalidade de incluir um botão com o nome "Processar" na tela de edição da requisição de estoque. Este botão terá a mesma funcionalidade do botão "Processar" da tela principal (View) da movimentação de estoque, ou seja, irá processar a requisição.

Dependendo do perfil do usuário logado, o botão irá aparecer com o nome "Imprimir", assim como na view principal da movimentação de estoque.

### (Obrigatório)

## Definição da Regra de Negócio

Na tela de edição da movimentação de estoque, existirá um botão chamado "Processar" que terá a mesma função que o outro de mesmo nome na tela de view da movimentação de estoque. Caso o perfil do usuário logado não permita o processamento, o botão terá o nome de "Imprimir", para que a requisição seja impressa.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
