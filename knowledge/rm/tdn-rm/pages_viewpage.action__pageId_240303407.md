---
content_hash: 0bc9f5ed8e34ac29780dc5670b4f72bede7b8c1bc5f0e4899aec7d319583883e
fetched_at: '2026-06-29T00:08:10.203382+00:00'
page_id: '240303407'
product: rm
source: tdn-rm
title: ER_SAUHRM01-300_ Agendamento_Consulta_RM_Saude_Campo_N°_Carteira
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=240303407
version: 4
---

|  |
| --- |
| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo** **extremamente** **técnico.** |

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS HOSPITALAR | **Módulo** | RM SAÚDE |
| **Segmento Executor** | SAÚDE | | |
| **Projeto1** | SAUHRM01 | **IRM1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM01-388 |
| **Requisito1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM01-300 | **Subtarefa1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM01-455 |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

# Objetivo

Atualmente o Cliente Caixa de Assistência Saúde Integrada- (SSISAUDE), utiliza o sistema de Gestão de planos de Saúde (GPS) integrado com o Gestão Hospitalar - RM-Saúde no que tange a Agenda de consultas .  
 **A Solicitação do cliente é que o campo carteira do convênio seja implementado no grid da tela de Agenda de atendimentos.**

# Definição da Regra de Negócio

**RN001** –inserir no **grid da tela de** Agenda de atendimentos o campo **carteira do convênio**(ver protótipo de tela);

# Fora do Escopo

* Outras informações que não estiverem descritas neste documento;.
* Alterações no processo de integração já existentes;

|  |  |  |  |
| --- | --- | --- | --- |
| Rotinas Envolvidas |  |  |  |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** |
| Cadastro de pacientes-GPS | Inclusão |  |
| Agendamento de consultas RM | Inclusão | Atendimento/agendadamentos/Agenda de Atendimentos |

# Protótipo de Tela

As imagens de telas destacadas a seguir são consideradas apenas protótipos, as mesmas poderão sofrer alterações em função da atualização de componentes utilizados no sistema, devem ser utilizadas apenas para exemplificar a forma de iteração que os usuários possuirão ao acessar o RM, o fluxo de negócio e a forma em que os dados e informações serão manipuladas.

# Fluxo do Processo

* Cliente entra com os dados na tela de cadastro de beneficiário do GPS-DATASUL

* Através da integração os dados são replicados para o Sistema RMSAUDE para efetuar o agendamento de consultas e atendimentso de pacientes. Telas abaixo Sistema RM.
