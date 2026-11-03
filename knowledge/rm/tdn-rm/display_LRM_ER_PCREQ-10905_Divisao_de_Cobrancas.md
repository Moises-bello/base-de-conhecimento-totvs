---
content_hash: a1c59fd41e2e0620086250668d8cf10c4d6b0fbcd761b27ceff4351fd4096b0b
fetched_at: '2026-06-29T00:08:05.956943+00:00'
page_id: '236423721'
product: rm
source: tdn-rm
title: ER_PCREQ-10905_Divisao_de_Cobrancas
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-10905_Divisao_de_Cobrancas
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
| **Projeto** | * [R\_SAU\_RM\_V12\_1516](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B11311%5D+%3D+R_SAU_RM_V12_1516 "R_SAU_RM_V12_1516") | **IRM** | * [PCREQ-10905](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10207%5D+%3D+PCREQ-10905 "PCREQ-10905") |
| **Requisito** | * [PCREQ-10906](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-10906 "PCREQ-10906") | **Subtarefa** | * [SAU\_DEV-4765](http://jira.totvs.com.br/browse/SAU_DEV-4765) |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

## Objetivo

   Este documento tem como objetivo a especificação das funcionalidades necessárias para atender a demanda de customização do cliente Dr. Clin, segundo à regra de divisão de cobranças

## Definição da Regra de Negócio

 **RN001 -** Na tela de "**Condições Contratuais com Convênios**", será criado um anexo, chamado "**Regras de Divisão de Honorários**". Este anexo deve permitir que sejam configuradas regras específicas, por prestador, para a divisão de honorário, no momento do lançamento, em qualquer ponto do sistema. Este cadastro, deverá permitir a inclusão das seguintes informações:

* Cod. Prestador - Correspondente ao prestador, para o qual a regra será aplicada(**Obrigatório**);
* Cod. Especialidade - Correspondente a especialidade do prestador para a qual será aplicada a regra(**Não Obrigatório**) ;

  ***\*\*No caso de não preenchimento da especialidade, a regra se aplicará para todas as especialidades do médico;***
* Faixa Inicial - Valor inicial da faixa de procedimentos à qual a regra se aplicará(**Obrigatório**);
* Faixa Final - Valor final da faixa de procedimentos à qual a regra se aplicará(**Obrigatório**);
* Percentual do Prestador - Percentual que ficará com o prestador(**Obrigatório**).

  ***\*\*O restante do valor irá para o prestador principal da unidade de faturamento que está vinculada a unidade de atendimento para a qual está sendo lançado o item.***

**RN002 -** Em todos os pontos do **RM Saúde**, onde algum lançamento de honorário possa ser realizado, deverá ser implementada uma rotina para verificar se existe alguma regra de divisão, específica para o prestador responsável. Caso exista, o sistema deverá efetuar a divisão, conforme a parametrização realizada na **RN001.**

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Divisão de Cobrança | Criação | Cadastros > Faturamento > Condições Contratuais Com Convênios (Anexo Divisão de Cobrança) | **RN001** |
| Lançamento de Honorários | Alteração | - | **RN002** |

**Exemplo de Aplicação**

* Acesse o menu "**Cadastros > Faturamento > Condições Contratuais com Convênios**";
* Selecione a condição contratual desejada e acesse "**Anexos > Divisão de Cobranças**";
* Parametrize uma nova regra, conforme desejado e confirme a inclusão;
* Acesse a elaboração de contas de um paciente internado para o convênio configurado;
* Inclua um novo registro de honorário para um item qualquer, que esteja dentro da faixa parametrizada na regra de divisão de cobrança. O sistema deverá lançar 2 itens de honorário. Um para o **Prestador Informado** e o outro para o **Prestador Principal da Unidade de Faturamento** vinculada à **Unidade de Atendimento** do registro, respeitando o percentual parametrizado para a divisão .

### Protótipo de Tela

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
