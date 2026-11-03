---
content_hash: 5aec361dc8e92e9adfc6a68fb65e61dd5b87df04bf5333ee0c47458f9b8558c6
fetched_at: '2026-06-29T00:06:28.519566+00:00'
page_id: '233753879'
product: rm
source: tdn-rm
title: ER_PCREQ-9894_Acesso_WEB_Agenda_de_Cirurgias
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-9894_Acesso_WEB_Agenda_de_Cirurgias
version: 121
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS HOSPITALAR | **Módulo** | RM SAUDE |
| **Segmento Executor** |  | | |
| **Projeto1** | * [R\_SAU\_RM\_V12\_1516](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B11311%5D+%3D+R_SAU_RM_V12_1516 "R_SAU_RM_V12_1516") | **IRM1** | PCREQ-9898 |
| **Requisito1** | * PCREQ-9898 | **Subtarefa1** | SAU\_DEV-4126 |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

 O objetivo desta implementação é disponibilizar o acesso Web à Agenda de Cirurgia, permitindo que sejam verificadas as informações da cirurgia (Ex.: Nome do Paciente, Data/Hora, Local, Procedimento). Além disso, esta implementação proporcionará o processo de solicitação de reagendamento das cirurgia/procedimento, na qual irá inserir esta solicitação direto no painel de reagendamento do RM Gestão Hospitalar. 

## Definição da Regra de Negócio

**RN001** - Quando o usuário logar no sistema através do browser, será exibida uma lista de cirurgias, nas quais este usuário está vinculado. Buscando, inicialmente, as cirurgias a partir das 00h00min do dia em que esta sendo feito o login dentro dos próximos sete dias, até às 23:59 do último dia deste período. Após o primeiro carregamento é possível escolher o período que deseja-se realizar a busca de cirurgias agendadas.

**RN002** - Na lista de cirurgias, são exibidas apenas as cirurgias cirurgias que estão com o "status" igual à "agendada" e que a informação de sistema "reagendar" é igual a "falso".

**RN003** - Toda vez que ocorrer alguma alteração na cirurgia, através do RM Gestão Hospitalar, a sua informação de sistema "reagendar" será atribuída para "falso", até mesmo em casos onde foi solicitado reagendamento, mas que o processo ainda não foi realizado. 

 

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| [Agenda de Cirurgias] | [Alteração] | [Atendimento - Agenda de Cirurgias] | - |
| [Agenda de Cirurgias] | [Alteração] | [Atendimento - Log Alterações uMov.me] | - |

***Exemplo de Aplicação:***

* ### *Solicitar o reagendamento da cirurgia através do menu "Agenda Cirurgica" > Selecionar uma Cirurgia > Botão Reagendar > Preencher 'observação' > Botão Reagendar"*
* *Buscar uma cirurgia dentro de um período através do menu *"Agenda Cirurgica" > Selecionar uma data inicial no container de Data > Selecionar uma data final no container de Data > Botão de pesquisa (lupa)"***.*

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
