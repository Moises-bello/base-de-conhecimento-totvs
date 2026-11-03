---
content_hash: 1dab63916b46da5c618d7562e8d0ffae92d2cc27659e8e16eb590d9c06e469e6
fetched_at: '2026-06-29T00:08:05.618452+00:00'
page_id: '235599993'
product: rm
source: tdn-rm
title: ER_PCREQ-10836_PEP2_Uso_de_novo_serviço_para_salvar_alergias_no_PEP
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=235599993
version: 111
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### (Obrigatório)

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão Hospitalar | **Módulo** | Saúde |
| **Segmento Executor** | Saúde | | |
| **Projeto1** | * [R\_SAU\_RM\_V12\_1516](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B11311%5D+%3D+R_SAU_RM_V12_1516 "R_SAU_RM_V12_1516") | **IRM1** | * [PCREQ-10835](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10207%5D+%3D+PCREQ-10835 "PCREQ-10835") |
| **Requisito1** | * [PCREQ-10836](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-10836 "PCREQ-10836") | **Subtarefa1** | SAU\_DEV-4601 |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### (Obrigatório)

## Objetivo

 Este requisito tem a finalidade de realizar a integração do cadastro de alergias do paciente entre o TOTVS Gestão Hospitalar e o PEP 2.0. As alergias serão cadastradas no RM através do painel de classificação de risco, ou seja, a cada registro da classificação de risco, será possível definir as alergias do paciente. 

### (Obrigatório)

## Definição da Regra de Negócio

**RN001**

No painel da classificação de risco, existirá uma área onde será possível informar as alergias do paciente. Ao informar cada uma das alergias, o sistema enviará a informação para o PEP 2 através da integração. No PEP 2 também será possível informar as alergias para o paciente.

Ao carregar as informações no painel de classificação de risco, o Gestão Hospitalar irá acessar o serviço de integração para verificar se existem alergias cadastradas no PEP 2 para o paciente que ainda não estão no cadastro local, e caso exista, realizará o cadastro das mesmas.

O cadastro das alergias será feito apenas no PEP 2 e será enviado para o Gestão Hospitalar através da integração (fazendo um sincronismo das informações). No Gestão Hospitalar apenas será possível informar quais alergias o paciente possui, através do painel da classificação de risco.

A opção de informar as alergias do paciente apenas estará disponível, inicialmente, caso o Gestão Hospitalar utilize a integração com o PEP 2.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Painel de classificação de risco | [Alteração] | Atendimento / Pronto Atendimento/Ambulatório / Painel de classificação de risco | RN001 |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
