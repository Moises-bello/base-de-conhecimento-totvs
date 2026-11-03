---
content_hash: 7f38fb8fb42087dcd091eed4137891c1d5d78f23ac7c277f8ef970c8106d98cc
fetched_at: '2026-06-29T00:08:13.591751+00:00'
page_id: '244428186'
product: rm
source: tdn-rm
title: ER_SAUHRM01-285_Tipo_de_Guia_na_Central_de_Autorização_para_Padrões_que_a_Utilizam
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244428186
version: 115
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS GESTÃO HOSPITALAR | **Módulo** | RM Saúde |
| **Segmento Executor** | Saúde | | |
| **Projeto** | SAUHRM01 | **IRM** | R\_SAU\_HRM1516 |
| **Requisito** | SAUHRM01-285 | **Subtarefa** | SAUHRM01-466 |
| **Chamado** | TTYUPC | | |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Este documento tem como objetivo especificar a alteração na tela de Central de Autorização, para que não seja exigido o Tipo de Guia quando for realizar a autorização dos lançamentos para os convênios que utiliza-se de codificação de informação diferente de ANS - TISS.

## Definição da Regra de Negócio

**RN001**

1. Ao realizar a Autorização dos Lançamentos para os convênios que utiliza-se de Codificação de informação diferente de ANS - TISS, não deve ser exigido o tipo de guia.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Central de Autorização | Alteração | [Faturamento -> Central de Autorizações] | RN001 |

**Exemplo de Aplicação**

1. Acessar o menu "Faturamento > Central de Autorizações";
2. Selecionar um registro e entrar nos detalhes do mesmo;
3. Acessar a opção "Processos > Realizar Autorização dos Lançamentos";

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
