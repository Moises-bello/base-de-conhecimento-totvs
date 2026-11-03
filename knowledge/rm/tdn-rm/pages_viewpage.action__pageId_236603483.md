---
content_hash: 337e4927eb56f4c29b914719477fe6d5928b67f71fc6888fc2135711719957de
fetched_at: '2026-06-29T00:08:07.085721+00:00'
page_id: '236603483'
product: rm
source: tdn-rm
title: ER_PCREQ-10897_Indicação_de_médico_COOPERADO
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=236603483
version: 113
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

# Indicação de médico COOPERADO

### (Obrigatório)

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão Hospitalar | **Módulo** | Saúde |
| **Segmento Executor** | Saúde | | |
| **Projeto1** | * [R\_SAU\_RM\_V12\_1516](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B11311%5D+%3D+R_SAU_RM_V12_1516 "R_SAU_RM_V12_1516") | **IRM1** | PCREQ-10841 |
| **Requisito1** | * [PCREQ-10897](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-10897 "PCREQ-10897") | **Subtarefa1** | SAU\_DEV-4743 |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### (Obrigatório)

## Objetivo

 Este requisito tem a finalidade de adicionar a flag "Cooperado" no cadastro do credenciamento de prestadores para que, ao selecionar um médico, tanto no registro de atendimento quando na Elaboração de Contas, seja exibida uma mensagem informando que o médico é COOPERADO para aquele credenciamento. 

### (Obrigatório)

## Definição da Regra de Negócio

**RN001**

No menu "Cadastros/Uso Geral/Prestador -> Anexo Credenciamento" será incluido um campo chamado "Cooperado" do tipo checkbox para informar se o médico é ou não Cooperado naquele credenciamento.

**RN002**

No Registro de Atendimento Interno, Registro de Atendimento Externo, e Elaboração de Contas, ao selecionar um prestador responsável, o sistema irá verificar se o médico está credenciado, e caso esteja, verificará a marcação do campo "Cooperado". Se estiver marcado, o sistema irá exibir uma mensagem informando que o médico é cooperado para aquele credenciamento.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
