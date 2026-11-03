---
content_hash: 698453336b700d2f42aa31fee4a37a2db866353d01d6a7fa37cdb0f27fd395fe
fetched_at: '2026-06-29T00:08:07.075545+00:00'
page_id: '236603370'
product: rm
source: tdn-rm
title: ER_PCREQ-9998_PEP_1_Alerta_quando_da_Liberação_de_um_EXAME
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=236603370
version: 112
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### 

# PEP 1 - Alerta quando da liberação de um exame

### (Obrigatório)

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão Hospitalar | **Módulo** | Saúde |
| **Segmento Executor** | Saúde | | |
| **Projeto1** | R\_SAU\_RM\_V12\_1516 | **IRM1** | * [PCREQ-9991](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10207%5D+%3D+PCREQ-9991 "PCREQ-9991") |
| **Requisito1** | * [PCREQ-9998](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-9998 "PCREQ-9998") | **Subtarefa1** | SAU\_DEV-4221 |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### (Obrigatório)

## Objetivo

 Este requisito tem a finalidade de incluir um alerta na tela do Prontuário Eletrônico do Paciente (PEP 1) que seja exibido sempre que existir um exame com status "Liberado" cujo médico responsável seja o médico vinculado ao usuário logado.

 

### (Obrigatório)

## Definição da Regra de Negócio

Implementar um alerta na tela do prontuário eletrônico, que seja exibido sempre que existir um exame com status "Liberado" cujo médico responsável seja aquele vinculado ao usuário logado no sistema.

Ao clicar no alerta, será exibida uma tela com uma tabela mostrando os nomes dos pacientes e os números da ordens de serviço dos pedidos do exames. Nessa tela será possivel selecionar um registro e teclar no botão de OK, fazendo com que o paciente selecionado seja carregado no PEP, mostrando suas respectivas informações.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
