---
content_hash: e226dd5fe0f5ab2c3072b7a0882dcf32d89f1b200f81f3e4cdfef3293d18fd15
fetched_at: '2026-06-29T00:06:28.051004+00:00'
page_id: '233744153'
product: rm
source: tdn-rm
title: ER_PCREQ-10197_Adaptação_Atendimentos_ELETIVOS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=233744153
version: 120
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS GESTÃO HOSPITALAR | **Módulo** | Painel de Atendimentos Eletivos |
| **Projeto** | * [R\_SAU\_RM\_V12\_1516](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B11311%5D+%3D+R_SAU_RM_V12_1516 "R_SAU_RM_V12_1516") | **IRM** | * [PCREQ-9983](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10207%5D+%3D+PCREQ-9983 "PCREQ-9983") |
| **Requisito** | * [PCREQ-10197](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-10197 "PCREQ-10197") | **Subtarefa** | * [SAU\_DEV-4281](http://jira.totvs.com.br/browse/SAU_DEV-4281) |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

## Objetivo

    Esta implementação tem como objetivo fazer com que o sistema, quando devidamente parametrizado, liste no painel de classificação de riscos, além dos atendimentos de urgência, os eletivos.

## Definição da Regra de Negócio

**RN001  -** Deverá ser adicionado ao cadastro de unidade de atendimento, um parâmetro, que terá a função de controlar se a unidade permite ou não que atendimentos eletivos sejam incluídos na lista do Painel de Classificação de Riscos.

   **RN002** - Quando um atendimento for criado, deverá ser executada a verificação se a unidade de atendimento para a qual o atendimento está sendo incluído, permite que atendimentos eletivos sejam incluídos no Painel, caso positivo, o atendimento deverá seguir o mesmo fluxo dos atendimentos de urgência, ficando a parametrização do fluxo da unidade a cargo do usuário.

|  |  |  |  |
| --- | --- | --- | --- |
| Rotina | Tipo de Operação | Opção de Menu | Regras de Negócio |
| [Cadastro de Unidade de Atendimento] | [Alteração] | [Cadastros > Uso Geral > Unidades de Atendimento] | **RN001** |
| [Registro de Atendimentos Externos] | [Atendimento] | [Atendimento > Pronto Atendimento/Ambulatório > Registro de Atendimentos Externos] | **RN002** |

**Exemplo de Aplicação:**

* Configurar o "**Painel de Classificação de Riscos**", incluindo o plantão para um horário que compreenda o horário atual;
* Acessar o menu "Cadastros > Uso Geral > Unidades de Atendimento" e marcar o checkbox "**Inclui Atendimentos Eletivos no Painel**";
* Incluir um novo atendimento externo, do tipo "**Eletivo**" e para a mesma unidade de atendimento parametrizada;
* Acessar o painel de classificação de riscos e verificar se o atendimento recém incluído aparece corretamente.

**Tabelas Utilizadas**

* **SZUNIDATEND**

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
