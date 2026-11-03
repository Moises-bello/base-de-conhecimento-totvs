---
content_hash: e573bf1a11f3620a8fde393181e32791cb4d1cfd15ddbc822de16e12a1fff4fd
fetched_at: '2026-06-29T00:06:25.923663+00:00'
page_id: '224451461'
product: rm
source: tdn-rm
title: ER_PCREQ-9955_Divisão_de_Honorários_na_Solicitação_de_Exames
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=224451461
version: 128
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS HOSPITALAR | **Módulo** | Saúde |
| **Projeto** | * [R\_SAU\_RM\_V12\_1516](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B11311%5D+%3D+R_SAU_RM_V12_1516 "R_SAU_RM_V12_1516") | **IRM** | * [PCREQ-9954](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10207%5D+%3D+PCREQ-9954 "PCREQ-9954") |
| **Requisito** | * [PCREQ-9955](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-9955 "PCREQ-9955") | **Subtarefa** | * [SAU\_DEV-4141](http://jira.totvs.com.br/browse/SAU_DEV-4141) |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

 

## Objetivo

     Disponibilizar a funcionalidade de Divisão de Cobrança na tela de Solicitação de Exames.

## Definição da Regra de Negócio

   Atualmente, existe na tela de elaboração de contas, a funcionalidade de divisão de cobrança, que é ativada no lançamento de um item na aba **Diagnose e Terapia**, sempre que o botão  estiver pressionado.

   A mesma regra de divisão deverá ser implantada na tela de solicitação de exames, onde sempre que o botão estiver pressionado, ocorra a divisão dos valores, conforme a seguinte regra:

   - **Valor do Honorário** vai para o **Profissional Executante** e o **Valor de UCO** vai para o **Prestador Principal da Unidade de Faturamento,** na qual está cadastrada a Unidade de Atendimento, onde o **SADT** está sendo lançado.

   Deve-se também, adicionar ao sistema um parâmetro. Quando este parâmetro estiver marcado, o botão deverá ficar sempre selecionado, não necessitando da ação contínua do usuário para a ativação da funcionalidade.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| [Parâmetros Gerais] | [Alteração] | [Opções -> Parâmetros -> Parâmetros Gerais] | - |
| [Registro de Atendimentos Externos] | [Alteração] | [Atendimento -> Pronto Atendimento/Ambulatório -> Registro de Atendimentos Externos] | - |

**Exemplo de Aplicação:**

* **Acessar o menu "Atendimento -> Pronto Atendimento/Ambulatório -> Registro de Atendimentos Externos" e registrar um novo atendimento externo;**
* **Acessar a aba "Pedido de Exames" e incluir um novo pedido;**
* **Acessar a aba "Exames Solicitados". Clicar no ícone  e solicitar um novo exame;**
* **Acessar a elaboração de contas e verificar se a divisão de cobrança foi realizada, conforme as regras.**

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
