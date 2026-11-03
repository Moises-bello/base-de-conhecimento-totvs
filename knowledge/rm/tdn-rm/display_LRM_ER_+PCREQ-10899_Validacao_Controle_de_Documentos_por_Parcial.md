---
content_hash: 1d6ef5ae4fde263a36927573a176366f1ce149f6cf56fa819f344fe3b9784906
fetched_at: '2026-06-29T00:08:07.806926+00:00'
page_id: '237390786'
product: rm
source: tdn-rm
title: ER_ PCREQ-10899_Validacao_Controle_de_Documentos_por_Parcial
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_+PCREQ-10899_Validacao_Controle_de_Documentos_por_Parcial
version: 118
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS GESTÃO HOSPITALAR | **Módulo** | Saúde |
| **Projeto** | * [R\_SAU\_RM\_V12\_1516](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B11311%5D+%3D+R_SAU_RM_V12_1516 "R_SAU_RM_V12_1516") | **IRM** | * [PCREQ-10841](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10207%5D+%3D+PCREQ-10841 "PCREQ-10841") |
| **Requisito** | * [PCREQ-10899](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-10899 "PCREQ-10899") | **Subtarefa** | * [SAU\_DEV-4779](http://jira.totvs.com.br/browse/SAU_DEV-4779) |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

### Objetivo

   Esta especificação tem como objetivo implementar a validação por parcial, na criação de novos documentos na tela de Registro de Documentos.

### Definição da Regra de Negócio

**RN001**

* Criar um parâmetro, na tela de Parâmetros Gerais, com a descrição **Apenas um Documento por Parcial**.

**RN002**

* Na tela de Controle de Documentos (Faturamento/Controle de Documentos), incluir uma validação ao salvar um novo documento, para que quando o parâmetro criado na **RN001** estiver marcado, faça com que o sistema não permita a inclusão de mais de um documento de um mesmo tipo em uma mesma parcial.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Parâmetros Gerais | Alteração | Opções / Parâmetros / Parâmetros Gerais | **RN001** |
| Controle de Documentos | Alteração | Faturamento / Controle de Documentos | **RN002** |

**Exemplo de Aplicação:**

1. Acesse o menu **Faturamento / Controle de Documentos.**
2. Inclua um novo documento para um paciente qualquer.
3. Inclua novamente um documento do mesmo tipo para o paciente. O sistema deverá alertar o usuário e, caso este deseje prosseguir, deverá permitir a inclusão do documento.
4. Acesse o menu **Opções / Parâmetros / Parâmetros Gerais**e assinale a opção **Apenas um Documento por Parcial.**
5. Execute novamente os passos de **1** a **3**.
6. O sistema não deverá permitir que o documento seja incluído, alertando ao usuário sobre a parametrização realizada.

 

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
