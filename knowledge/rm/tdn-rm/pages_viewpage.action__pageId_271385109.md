---
content_hash: 083224a908870a844396bc0608c25cd266b7287e85af31ec38f515e699d72c9a
fetched_at: '2026-06-29T00:08:26.797881+00:00'
page_id: '271385109'
product: rm
source: tdn-rm
title: ER SAUHRM02-594 Mascára de telefone para paciente e prestador
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271385109
version: 102
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS GESTÃO HOSPITALAR | **Módulo** | RM Saúde |
| **Segmento Executor** | Saúde | | |
| **Projeto** | SAUHRM02 | **IRM/EPIC** | SAUHRM02-28 |
| **Requisito/Story/Issue** | SAUHRM02-594 | **Subtarefa** | SAUHRM02-684 |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

   

## Objetivo

 *Este documento tem como objetivo especificar o requisito de utilização de máscara telefone celular para inserção nos cadastros de pacientes e prestadores.*

### Definição da Regra de Negócio

**RN001 -**  Criar parâmetro geral na aba Registro e Controle para configurar máscara do telefone com DDD.

Antes de configurar a máscara, o cliente deverá rever todo o seu cadastro de paciente e prestadores para ajustar à máscara desejada. Caso contrário, a aplicação da máscara poderá acarretar em perda da informação já cadastrada.

**RN002 -**  Configurar a máscara no cadastro de prestadores, aba Complemento 1

**RN003 -**  Configurar a máscara no cadastro de paciente (Acesso através do menu Atendimento/Recepção/Dados de um paciente)

 **RN004 -**  Configurar a máscara no registro de atendimento externo

 **RN005 -**  Configurar a máscara no registro de internações

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| [Parâmetros Gerais] | [Alteração] | [Opções-> Parâmetros -> Parâmetros Gerais] | **RN001** |
| [Cadastro de Prestadores] | [Criação] | Cadastros->Uso Geral ->Prestador | **RN002** |
| [Dados de um Paciente] | [Criação] | [Atendimento->Recepção->Dados de um Paciente] | **RN003** |
| [Atendimento Externo] | [Criação] | [Atendimento-> Pronto Atendimento/Ambulatório-> Registro de Atendimento ] | **RN004** |
| [Atendimento Interno] | [Criação] | [Atendimento-> Internação-> Registro de Internação] | **RN005** |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
