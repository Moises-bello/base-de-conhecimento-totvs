---
content_hash: 8150c4626367e14b473d0b4900522808e883c20e61e0d39e33c4c1657537271c
fetched_at: '2026-06-29T00:08:07.931420+00:00'
page_id: '237397704'
product: rm
source: tdn-rm
title: ER_PCREQ-10846_Alertas_encerramento_de_contas_com_valores_inferiores_a_X_reais
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-10846_Alertas_encerramento_de_contas_com_valores_inferiores_a_X_reais
version: 117
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS GESTÃO HOSPITALAR | **Módulo** | RM SAÚDE |
| **Projeto** | * [R\_SAU\_RM\_V12\_1516](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B11311%5D+%3D+R_SAU_RM_V12_1516 "R_SAU_RM_V12_1516") | **IRM** | * [PCREQ-10841](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10207%5D+%3D+PCREQ-10841 "PCREQ-10841") |
| **Requisito** | * [PCREQ-10846](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-10846 "PCREQ-10846") | **Subtarefa** | * [SAU\_DEV-4681](http://jira.totvs.com.br/browse/SAU_DEV-4681) |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

## Objetivo

 Este documento tem como objetivo especificar o requisito de Alertas no Enceramento de Contas com valores Inferiores a X Reais, onde a partir de um valor pré-definido, o sistema deverá efetuar validações e emitir bloqueios ou alertas no encerramento de contas.

## Definição da Regra de Negócio

 **RN001**

* Criar um grupo de parâmetros, na tela de Parâmetros Gerais, onde o comportamento do encerramento da conta será orientado. Os seguintes parâmetros deverão existir:  
  - **Utiliza verificação de valor mínimo no encerramento (Checkbox);**  
  - **Ação, que será um conjunto de 2 RadioButtons, com os valores Bloqueia e Alerta;**  
  - **Valor Mínimo, que será um TextBox, onde o valor mínimo deverá ser informado;**  
  - **Tipos de Lançamentos, que será um grupo de CheckBox, com as opções Honorários, Diárias, Taxas e Serviços, MatMed e Diagnose e Terapia.**

**RN002**

* Na etapa de geração de relatório do encerramento, na rotina de Encerramento de Conta, incluir uma validação que deverá verificar se o parâmetro "**Utiliza verificação de valor mínimo no encerramento**" está marcado. Caso esteja, o sistema deverá prosseguir com a emissão de alertas ou até mesmo de bloqueio de encerramento, dependendo da parametrização.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Parâmetros Gerais | Alteração | Opções > Parâmetros > Parâmetros Gerais | **RN001** |
| Encerramento de Conta | Alteração | Faturamento > Particular e Convênios > Lançamentos na Conta do Paciente | **RN002** |

**Exemplo de Aplicação:**

1. Acessar o menu "**Opções > Parâmetros > Parâmetros Gerais**", aba “**FaturamentoII**”;
2. Marcar o CheckBox “**Utiliza verificação de valor mínimo no encerramento**” e parametrizar demais opções conforme desejado;
3. Acessar o menu "**Atendimento > Pronto Atendimento / Ambulatório > Registro de Atendimentos Externos**";
4. Incluir um novo atendimento;
5. Na aba Guia/Autorização, incluir uma guia para o paciente;
6. Acessar a Elaboração de Contas do Paciente e lançar alguns itens de SADT, MatMed, Honorários, Diarias e Taxas/Serviços na conta do paciente;
7. Encerrar a conta e verificar se o sistema respeitou as regras parametrizadas.

## Protótipo de Tela

**Protótipo 01**

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
