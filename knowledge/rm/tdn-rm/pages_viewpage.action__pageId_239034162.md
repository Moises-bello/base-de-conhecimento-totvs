---
content_hash: 5215b98bade85871bc50a515f768584cff98599bbee0c6df352c2f17272076c1
fetched_at: '2026-06-29T00:08:09.358464+00:00'
page_id: '239034162'
product: rm
source: tdn-rm
title: ER_SAUHRM01-49_Inativar_Cadastro_Procedimentos_Cirúrgicos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=239034162
version: 118
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS HOSPITALAR | **Módulo** | RM SAUDE |
| **Segmento Executor** | SAÚDE | | |
| **Projeto** | SAUHRM01 | **IRM** | SAUHRM01-37 |
| **Requisito** | SAUHRM01-49 | **Subtarefa** | SAUHRM01-226 |
| **País** | ( X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

   

## Objetivo

 

*Este documento tem como objetivo especificar o requisito de Inativar Cadastro de Procedimentos Cirúrgicos*

## Definição da Regra de Negócio

**RN001** - Permitir que um procedimento cirúrgico possa ser inativado.

**RN002** - Permitir  que somente procedimentos cirúrgicos ativos sejam incluídos no agendamento de cirurgias

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| [Procedimentos para Agenda de Cirurgia ] | [Alteração] | [Cadastros>Cuidado com o Paciente > Cirurgias > Procedimentos para Agenda de Cirurgia ] | RN001 |
| [Agenda de Cirurgias] | [Criação] | [Atendimento> Agendamento > Agenda de Cirurgias] | RN002 |

**Exemplo de Aplicação:**

1. Acesse o menu **"Cadastros>Cuidado com o Paciente > Cirurgias > Procedimentos para Agenda de Cirurgia"** para ativar/inativar um procedimento
2. Acesse o menu **"Atendimento> Agendamento > Agenda de Cirurgias".**  
   Para procedimentos inativos o agendamento não será permitido.

 

**Tabelas Utilizadas**

* **SZPROCCIRURGICO- Tabela de procedimentos cirúrgicos disponíveis para agendamento**

## Dicionário de Dados

|  |  |
| --- | --- |
| **Campo** | STATUSPROC |
| **Tipo** | varchar |
| **Tamanho** | 1 |
| **Valor Inicial** | A |
| **Mandatório** | Sim (X ) Não (  ) |
| **Descrição** | Status |
| **Título** | Ativo |
| **Picture** |  |
| **Help de Campo** | Status do Procedimento A - Ativo I- Inativo |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
