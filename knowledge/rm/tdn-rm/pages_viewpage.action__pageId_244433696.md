---
content_hash: 7ffa524a8b64bc7b741c5a6f535cd3726f440d00045889b71d42018e73552c56
fetched_at: '2026-06-29T00:08:13.936845+00:00'
page_id: '244433696'
product: rm
source: tdn-rm
title: ER_SAUHRM01-286_Classificação_de_Risco_-_Parâmetros_por_estação_de_trabalho
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244433696
version: 118
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS GESTÃO HOSPITALAR | **Módulo** | RM Saúde |
| **Segmento Executor** | Saúde | | |
| **Projeto** | SAUHRM01 | **IRM** | SAUHRM01-391 |
| **Requisito** | SAUHRM01-286 | **Subtarefa** | SAUHRM01-477 |
| **Chamado** | TUDAB0 | | |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_ | | |

## Objetivo

  Esta especificação tem como objetivo detalhar a adição do campo 'Sala' na tela de Classificação de Risco, para que o médico possa confirmar ou alterar a sala em que irá trabalhar.

## Definição da Regra de Negócio

 

**RN001** 

1. Criar um campo de texto 'Sala' na tela de Classificação de Risco, para que o médico possa confirmar ou alterar a sala em que irá trabalhar.
2. Este campo deve estar visível e disponível para edição caso o cliente utilize os parâmetros por usuário e não por estação de trabalho.
3. Ao entrar na tela de classificação de risco ou fazer alteração, este campo deve utilizar o mesmo valor do campo 'Nº do Guichê/Sala' da tela de Parâmetros por Estação de Trabalho.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Painel de Classificação de Risco | Alteração | [Atendimento -> Pronto Atendimento/Ambulatório -> Painel de Classificação de Risco] | RN001 |

**Exemplo de Aplicação:**

1. Acessar o menu "Atendimento > Pronto Atendimento/Ambulatório > Painel de Classificação de Risco";
2. Preencher o campo 'Sala' com a sala na qual o médico irá trabalhar;
3. Gravar o valor do campo clicando no botão ao lado direito do campo.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
