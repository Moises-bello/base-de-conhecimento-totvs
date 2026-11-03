---
content_hash: 733a978b13b332f24b336039ba53d82447c26b32f3bab8c4c9ebdb210b42526c
fetched_at: '2026-06-29T00:08:09.198688+00:00'
page_id: '239028075'
product: rm
source: tdn-rm
title: ER_SAUHRM01-46_Tag_Controle_Acesso
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_SAUHRM01-46_Tag_Controle_Acesso
version: 120
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS HOSPITALAR | **Módulo** | RM SAUDE |
| **Segmento Executor** | SAÚDE | | |
| **Projeto** | SAUHRM01 | **IRM** | SAUHRM01-35 |
| **Requisito** | SAUHRM01-46 | **Subtarefa** | SAURM01-182 |
| **País** | (X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

## Objetivo

 *Este documento tem como objetivo especificar o requisito de Tag para controle de acesso de lançamentos  de contas e de data de entrada para atendimento.*

## Definição da Regra de Negócio

**RN001** - Vincular o acesso para lançamentos na Elaboração de Contas - Especial de acordo com acesso as demais abas

**RN002** - Permitir a edição da data de entrada após registrada no registro de atendimento externo

**RN003** - Permitir a edição da data de entrada após registrada no registro de atendimento interno

 

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Lançamentos na Conta do Paciente | [Alteração] | [Tesouraria>Lançamentos na Conta do Paciente] | RN001 |
| Registro de Atendimentos Externos | [Alteração] | [Atendimento>Pronto Atendimento/Ambulatório> Registro de Atendimentos Externos] | RN002 |
| Registro de Internações | [Alteração] | [Atendimento> Internação > Registro de Internações ] | RN003 |

Exemplo de Aplicação:

        RN001

* Acessar  [Tesouraria>Lançamentos na Conta do Paciente]
* Na aba Especial, os tipos de Lançamento que devem estar habilitados são de acordo com a permissão de cada uma das demais abas

      RN002

* Acessar Cadastros > Segurança > Perfil > Parâmetros RM Saúde
* Configurar o parâmetro Altera data de um atendimento Externo
* Acessar Atendimento>Pronto Atendimento/Ambulatório> Registro de Atendimentos Externos e verificar se esta ou não habilitado a alteração da data de atendimento em um registro existente

RN003

* Acessar Cadastros > Segurança > Perfil > Parâmetros RM Saúde
* Configurar o parâmetro Altera data de um atendimento  Interno
* Acessar Atendimento> Internação > Registro de Internações e verificar se esta ou não habilitado a alteração da data de atendimento em um registro existente

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
