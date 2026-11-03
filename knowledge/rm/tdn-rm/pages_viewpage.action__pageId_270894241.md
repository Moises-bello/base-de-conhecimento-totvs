---
content_hash: 45d9e0a6cd9ccd2533fe3b5ba36179305525180c5f9701fb5d8234189cff7001
fetched_at: '2026-06-29T00:08:24.194425+00:00'
page_id: '270894241'
product: rm
source: tdn-rm
title: ER_SAUHRM02_351_Migração_Registro_Atendimento_Interno/Externo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270894241
version: 111
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### (Obrigatório)

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão Hospitalar | **Módulo** | Registro de Atendimento |
| **Segmento Executor** | Saúde | | |
| **Projeto1** | SAUHRM02 | **IRM1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-349 |
| **Requisito1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-351 | **Subtarefa1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-480 |
| **Chamado2** |  | | |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### (Obrigatório)

## Objetivo

 Este documento tem como objetivo especificar o requisito de migração do Registro de Atendimentos tanto de pacientes externos como internos, bem como todas as rotinas que envolvem estes processos, da linguagem Delphi para C# .NET. Tem-se por objetivo arquitetar estas rotinas viabilizando uma maior usabilidade e disponibilidade de todas as rotinas envolvidas no registro de atendimento que são: Dados do Paciente, Dados do Atendimento, Guia e Autorização, Responsável pelo Atendimento, Pedido de Exames e Exames Solicitados. Além do ganho de performance que será adquirida com a migração para uma tecnologia mais atual que é o C# .NET.

### (Obrigatório)

## Definição da Regra de Negócio

## **RN001 - Dados do Paciente**

Migração de todas as rotinas referentes somente aos dados pessoais do paciente bem como as rotinas relacionadas à estes em forma de processos e anexos da nova MDI.

## **RN002 - Dados do Atendimento**

Nova tela que contemplará todas as rotinas referente aos dados do atendimento, bem como demais rotinas relacionadas em forma de processos e anexos da nova MDI.

## **RN003 - Guia e Autorização**

Nova tela que contemplará todas as rotinas referentes a solicitação e autorização de guias para procedimentos e exames, inclusão, alteração e exclusão de guias para faturamento, bem como demais rotinas relacionadas em forma de processos e anexos da nova MDI.

## **RN004 - Responsável pelo Atendimento**

Nova tela que contemplará todas as rotinas referentes ao cadastro, alteração e exclusão do responsável pelo atendimento, bem como demais rotinas relacionadas em forma de processos e anexos da nova MDI.

## **RN005 - Pedido de Exames**

Migração de todas as rotinas referentes aos pedidos de exames, bem como as integrações ao solicitar exames, geração de amostras, impressão de amostras e demais rotinas.

## **RN006 - Exames Solicitados**

Migração de todas as rotinas referentes aos exames solicitados, informações complementares, lançamento de guias automáticas, bem como todas as demais rotinas relacionadas em forma de processos e anexos da nova MDI.

## **RN007 - Tela Principal**

A tela principal englobará todas as rotinas descritas anteriormente viabilizando uma melhor usabilidade e disponibilidade das rotinas que o usuário necessitará. A tela principal funcionará como uma central do Registro de Atendimento, facilitando o acesso e uso das telas anteriormente explicadas nas RNs acima.

*<Na tabela abaixo informe quais são as rotinas envolvidas, o tipo de operação, a opção de menu e se necessário uma breve descrição das regras de negócio relacionadas a rotina>.*

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Dados do Paciente | [Criação] | Registro de Atendimento -> Central do Paciente / Dados do Paciente | **RN001** |
| Dados do Atendimento | [Criação] | Registro de Atendimento -> Central do Paciente / Dados do Atendimento | **RN002** |
| Guia e Autorização | [Criação] | Registro de Atendimento -> Central do Paciente / Guia e Autorização | **RN003** |
| Responsável pelo Atendimento | [Criação] | Registro de Atendimento -> Central do Paciente / Responsável pelo Atendimento | **RN004** |
| Pedido de Exames | [Criação] | Registro de Atendimento -> Central do Paciente / Pedido de Exames | **RN005** |
| Exames Solicitados | [Criação] | Registro de Atendimento -> Central do Paciente / Pedido de Exames / Exames Solicitados | **RN006** |
| Central do Paciente | [Criação] | Registro de Atendimento -> Central do Paciente | **RN007** |

**Exemplo de Aplicação**

1. Acesse a nova MDI.
2. Acesse o Registro de Atendimento e abra a Central do Paciente.
3. Localize ou cadastre um novo paciente, informando os dados pessoais do mesmo.
4. Pela Central do Paciente, após cadastrar o paciente, informe os dados do atendimento.
5. Pela Central do paciente, acesse a tela de Guia e Autorização e inclua as guias necessárias para faturamento e autorização bem como os procedimentos necessários para o atendimento.
6. Antes de finalizar o cadastro do atendimento do paciente será obrigatório acessar a tela de responsável pelo atendimento e cadastrar um responsável.
7. Ainda se necessário será possível solicitar e validar exames através das telas de Pedido de Exames e Exames Solicitados.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
