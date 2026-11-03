---
content_hash: 1f118f0cd107b0b85947c6547861bacb17cf6364a1bd448779fc1b5169f4f7e0
fetched_at: '2026-06-29T00:08:04.037457+00:00'
page_id: '235333973'
product: rm
source: tdn-rm
title: ER_PCREQ-10754_Fluxo_PEP_2_-_Medicamento_de_Uso_Comum/Medicamento_Uso_Individual/Medicamento_do_Paciente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=235333973
version: 120
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS GESTÃO HOSPITALAR | **Módulo** | RM SAÚDE |
| **Segmento Executor** | Saúde | | |
| **Projeto** | * [R\_SAU\_RM\_V12\_1516](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B11311%5D+%3D+R_SAU_RM_V12_1516 "R_SAU_RM_V12_1516") | **IRM** | * [PCREQ-10751](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10207%5D+%3D+PCREQ-10751 "PCREQ-10751") |
| **Requisito** | * [PCREQ-10754](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-10754 "PCREQ-10754") | **Subtarefa** | * [SAU\_DEV-4574](http://jira.totvs.com.br/browse/SAU_DEV-4574) |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

## Objetivo

    Esta especificação tem como objetivo garantir a correta integração entre PEP 2.0 e RM Saúde, durante a Checagem de Medicamentos e Liberação de Aprazamento.

## Definição da Regra de Negócio

**RN001  -** Ajustar o comportamento das ações de **"Liberação de Aprazamento"** e **"Checagem de Medicamentos",** para que o comportamento do sistema seja idêntico ao atual no PEP RM.

      Ao checar algum item, o sistema deverá verificar se o medicamento prescrito é um  "**Item fracionado de uso individual que é faturado na checagem**" ou  "**Item de uso coletivo que é faturado somente na checagem**". Caso seja, o sistema deverá lançar o item na conta do paciente, já no momento em que a checagem for executada.

     Na ação de Liberação de aprazamento, o sistema, dependendo da parametrização do PEP2, já realiza a checagem de todos os itens. Neste caso, o sistema deverá executar o mesmo fluxo descrito acima, para cada checagem executada.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Checagem de item | Alteração | PLT - PEP 2.0 | **RN001** |
| Liberação de Aprazamento | Alteração | PLT - PEP 2.0 | **RN001** |

**Exemplo de Aplicação:**

1. No RM Saúde, acesse o menu **"Atendimento > Pronto Atendimento / Ambulatório > Registro de Atendimentos Externos"** e registre um novo atendimento em alguma unidade de atendimento que esteja configurada para utilização no PEP 2:
2. Acesse o menu **"Cadastros > Cuidados com o Paciente > Prescrição Médica > Padrões de Prescrição";**
3. Caso já exista algum medicamento configurado, valide se na aba **"Anexos > Padrão de Prescrição"** existe configuração;
4. Caso não esteja configurado, realize a configuração para o medicamento desejado;
5. Acesse o PEP 2 na mesma Unidade de Atendimento na qual o novo atendimento foi inserido;
6. Acesse a aba **"Evolução Médica"** e insira uma nova Evolução;
7. Acesse a aba **"Prescrição Médica"** e lance uma nova prescrição com o medicamento configurado;
8. Clique em **"Liberar Prescrição".** A prescrição será incluída na aba **"Planejamento Terapêutico";**
9. Acesse a aba **"Planejamento Terapêutico"** e clique em **"Liberar Aprazamento".** Neste momento, caso esteja corretamente configurado, o PEP2 efetuará a checagem de todos os itens que foram aprazados;
10. Acesse novamente o **RM Saúde** e verifique a conta do paciente. Caso o medicamento lançado seja um "**Item fracionado de uso individual que é faturado na checagem**" ou  "**Item de uso coletivo que é faturado somente na checagem**", o sistema terá lançado o item na conta do paciente;
11. Acesse novamente o PEP 2 e vá novamente até a aba **"Planejamento terapêutico",** no atendimento do mesmo paciente;
12. Clique sobre um dos aprazamentos que estão com o ícone  e clique em **"Desfazer Checagem"**;
13. Informe a justificativa e acesse novamente a conta do paciente, no **RM Saúde.** O sistema deverá ter realizado o estorno do item.

 

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
