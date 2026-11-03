---
content_hash: fb6c7bbde2cc0b126a3e7ae828c4447d1fab499bca39a5366405209bfa5d3c3c
fetched_at: '2026-06-29T00:06:27.551437+00:00'
page_id: '233734776'
product: rm
source: tdn-rm
title: ER_PCREQ-9985_Inteligência_na_Gestão_de_Filas_do_PRONTO_SOCORRO
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=233734776
version: 122
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS GESTÃO HOSPITALAR | **Módulo** | RM SAÚDE |
| **Projeto** | * [R\_SAU\_RM\_V12\_1516](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B11311%5D+%3D+R_SAU_RM_V12_1516 "R_SAU_RM_V12_1516") | **IRM** | * [PCREQ-9983](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10207%5D+%3D+PCREQ-9983 "PCREQ-9983") |
| **Requisito** | * [PCREQ-9985](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-9985 "PCREQ-9985") | **Subtarefa** | * [SAU\_DEV-4170](http://jira.totvs.com.br/browse/SAU_DEV-4170) |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

## Objetivo

   Esta implementação tem como objetivo modificar a atual lógica de gestão das filas no Painel de Classificação de Riscos, para que não ocorram situações em que pacientes com classificações de menor gravidade fiquem sem atendimento no tempo parametrizado.

## Definição da Regra de Negócio

 **RN001 -**No form de classificação de riscos, deve ser alterada a lógica da gestão das filas, seguindo as seguintes regras:

* Tempo máximo para espera deverá ser o parametrizado no sistema, em "**Cadastros e Parametrização de Riscos**";
* Conforme a configuração de "**Critérios de Chamada de Atendimento**", sistema deverá também respeitar a "**Quantidade de pacientes que serão chamados, antes que o paciente com o tempo limite de atendimento ultrapassado seja chamado**";

 **RN002 -** No Painel de Chamados, remover o tipo da fila da frente da unidade de atendimento para baixo do local de atendimento.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Painel de Classificação de Riscos | Alteração | Atendimentos > Pronto Atendimento/Ambulatório > Painel de Classificação de Riscos | **RN001** |
| Painel de Chamados | Alteração | Painel de Chamados | **RN002** |

**Exemplo de Aplicação:**

**RN001**

* Acessar o menu "**Cadastros > Uso Geral > Classificação de Riscos > Cadastro e Parametrização de Riscos**";
* Cadastrar os Riscos desejados, atentando para o campo **Valor.** Quanto maior o valor, mais prioritária será a classificação do item;
* Para cada item, acessar o menu "**Anexos > Critérios de Chamada de Atendimento**" e parametrizar os critérios, informando a quantidade de pacientes que serão chamados na classificação mais urgente, antes que um menos urgente seja chamado;
* Incluir alguns novos atendimentos, classificados como Urgência, para alguma unidade em que o Painel de Classificação de Riscos esteja parametrizado;
* Acessar o Painel de Classificação de Riscos nesta unidade;
* Chamar as senhas e verificar se o comportamento da aplicação reflete a parametrização realizada;

**RN002**

* Incluir um Atendimento Externo do tipo Urgência em uma unidade que o Painel de Classificação de Riscos esteja monitorando;
* Acessar o Painel de Classificação de Riscos e Chamar a Senha;
* Verificar se Label que corresponde ao "**Tipo da fila**" está no local correto(abaixo do local de atendimento).

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
