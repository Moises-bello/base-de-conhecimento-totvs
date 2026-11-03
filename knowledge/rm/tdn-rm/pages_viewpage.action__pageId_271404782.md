---
content_hash: 88e53018c27cb53ca5aec654f27128574436c52acb6e07856131bbc0acbe6dce
fetched_at: '2026-06-29T00:08:27.278451+00:00'
page_id: '271404782'
product: rm
source: tdn-rm
title: ER SAUHRM02-591 Vínculo do Agendamento de Cirurgia e Central de autorização
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271404782
version: 106
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS GESTÃO HOSPITALAR - RM | **Módulo** | Faturamento / Central de Autorizações |
| **Segmento Executor** | Saúde | | |
| **Projeto1** | SAUHRM02 | **IRM/EPIC1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-595 |
| **Requisito/Story/Issue1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-591 | **Subtarefa1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-670 |
| **País** | ( X  ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Esta especificação tem como objetivo detalhar a melhoria à ser implementada nas funcionalidades de Agendamento de Cirurgias e Central de Autorizações do produto TOTVS Gestão Hospitalar. A melhoria consiste-se na automatização dos status correlacionados da Agenda de Cirurgia (status da cirurgia) e Central de Autorizações (status da guia). Através deste processo, o sistema era vincular as alterações do status da agenda de cirurgia, atualizado o status das guias de autorização de forma automática.

## Definição da Regra de Negócio

**RN001** - Quando realizar o agendamento da cirurgia (Agenda de Cirurgia), é necessário vincular o registro com um pré -registro de atendimento interno (Registro de Atendimento Interno).  
**RN002** - Ao realizar o vinculo entre agendamento e pré-registro de atendimento interno (RN001), verificar se existe guia na Central de Autorizações.  
**RN003** - Quando houverem guias na central de autorizações para o atendimento vinculado (RN002), o sistema deve exibir para o usuário uma tela na qual o usuário vai escolher quais guias estão vinculadas ao agendamento em questão.  
**RN004** - Além da exibição automática da tela de vinculo de guias com o agendamento (RN003), o usuário deve poder acessar a mesma tela através de um botão (ex.: Vinculo de Guias), para atualizar/editar as guias que estão vinculadas.  
**RN005** - Devido ao fato dos status da Agenda de Cirurgia serem divergentes dos status da Central de autorizações, é necessário implementar um cadastro para que o usuário realize um vinculo entre esses status, estabelecendo uma relação "de-para".

* SZCENTRALAUTORIZACAO.**STATUSGUIA**
* SZAGENDACIRURGICA.**CODSTATUS**

**RN006** - Sempre que o status da Agenda de Cirurgia for atualizado, o seu correspondente na Central de Autorizações, conforme cadastro da RN005, deve ser atualizado.

Observação

A atualização automática é realizada apenas no workflow Agenda de Cirurgia > Central de Autorizações. O processo inverso não é contemplado neste requisito.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Registro de Atendimento Interno | [Pré-requisito] | Atendimento / Internação / Registro de Internações | RN001 |
| Agenda de Cirurgias | [Alteração] | Atendimento / Agendamento / Agenda de Cirurgias | RN002, RN003, RN004 |
| Vinculo de Guias | [Criação] | Cadastros / Faturamento / Vinculo de Guias | RN005 |
| Central de Autorizações | [Alteração] | Faturamento / Central de Autorizações | RN006 |

***Exemplo de Aplicação:***

* *Automatizar o processo de sincronização dos status da Agenda de Cirurgia e da Central de Autorizações*

***Tabelas Utilizadas***

* *SZRELCENTRALAGCIRURG – Vínculo da agenda cirúrgica com a central de autorizações*
* *SZAGENDACIRURGICA - Agenda de Cirurgias*
* *SZCENTRALAUTORIZACAO - Central de Autorizações*
* *SZRELSTATUSAGCIRURGCENTRAL  - Correlação ente os status da agenda cirúrgica com o status da central de autorização*

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
