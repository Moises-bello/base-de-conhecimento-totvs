---
content_hash: 5d538938bd0ac92d7c7e9f8f1d278e6a720c1f1109d34395a8dd7f7b8561b3a4
fetched_at: '2026-06-29T00:08:05.088724+00:00'
page_id: '235583759'
product: rm
source: tdn-rm
title: ER_PCREQ-10843_Taxas_de_Comercialização_MATMED
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=235583759
version: 114
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS HOSPITALAR | **Módulo** | RM SAUDE |
| **Segmento Executor** | SAÚDE | | |
| **Projeto** | R\_SAU\_RM\_V12\_1516 | **IRM** | PCREQ-10841 |
| **Requisito** | PCREQ-10843 | **Subtarefa** | SAU\_DEV-4660 |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

  

## Objetivo

Esta implementação tem como objetivo adicionar automaticamente as taxas relativas a um novo lançamento de MATMED na conta do paciente.

## Definição da Regra de Negócio

**RN001** - Ao adicionar um lançamento de MATMED na conta do paciente, verificar se esse procedimento possui taxa vinculada. Caso sim, adicionar na aba "Taxas e Serviços".

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Lançamentos na Conta do Paciente | Alteração | Tesouraria > Lançamentos na Conta do Paciente | **RN001** |

## **Exemplo de Aplicação:**

* Incluir na conta do paciente procedimentos com taxa
* Verificar se a taxa foi adicionada a conta

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
