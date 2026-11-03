---
content_hash: c031b1e1edec4540db595f22b4611d2fe5b1eff94c7b60f7fbf2b400c36bef15
fetched_at: '2026-06-29T00:08:09.979038+00:00'
page_id: '240298489'
product: rm
source: tdn-rm
title: ER_SAUHRM01-47_Pesquisa_Plantonistas
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_SAUHRM01-47_Pesquisa_Plantonistas
version: 116
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS GESTÃO HOSPITALAR | **Módulo** | RM Saúde |
| **Segmento Executor** | Saúde | | |
| **Projeto** | SAUHRM01 | **IRM** | SAUHRM01-37 |
| **Requisito** | SAUHRM01-47 | **Subtarefa** | SAUHRM01-193 |
| **Chamado** | TTNT79 - Pesquisa Plantonistas | | |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_ | | |

## Objetivo

 Este documento tem como objetivo especificar a adição do campo 'Plantonista' na pesquisa por médico do registro de atendimentos externos.

## Definição da Regra de Negócio

**RN001**

1. Criar uma opção 'Plantonistas', para realizar a filtragem dos médicos disponíveis através deste critério na tela de atendimento externo.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Registro de atendimentos externos | Alteração | [Atendimento -> Pronto Atendimento/Ambulatório -> Registro de Atendimentos Externos] | RN001 |

**Exemplo de Aplicação:**

1. Acessar o menu "Atendimento > Pronto Atendimento/Ambulatório > Registro de Atendimentos Externos";
2. Preencher as informações referentes ao atendimento;
3. Acessar a aba "Dados Atendimento";
4. Informar os dados do prestador e realizar a pesquisa.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
