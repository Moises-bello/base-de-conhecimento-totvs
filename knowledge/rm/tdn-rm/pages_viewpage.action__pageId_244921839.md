---
content_hash: 7705aa4dff4095a056dda86e5b2a564d4cb3354b47e3671e7715ca8dae52ce2f
fetched_at: '2026-06-29T00:08:15.721902+00:00'
page_id: '244921839'
product: rm
source: tdn-rm
title: ER_SAUHRM01-662_Ação_na_interação_medicamentosa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244921839
version: 121
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS GESTÃO HOSPITALAR | **Módulo** | RM Saúde |
| **Segmento Executor** | Saúde | | |
| **Projeto** | SAUHRM01 | **IRM** | SAUHRM01-389 |
| **Requisito** | SAUHRM01-662 | **Subtarefa** | SAUHRM01-663 |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

## Objetivo

 Ajustar os campos no cadastro de Interação Medicamentosa do RM.

## Definição da Regra de Negócio

**RN001 –** Fazer as seguintes modificações no cadastro de Interação Medicamentosa do RM:

 

* Alterar o *label* do RM de "Classificação de Risco" para "Classificação de Risco / Nível de Interação";
* Alterar o *label* do RM de "Observação" para "Observação / Risco";
* Acrescentar o campo "Ação" (campo texto).

 

 

 

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Cadastro de Interações Medicamentosas | Alteração | RM > Cadastros > Cuidados com o Paciente >  Prescrição Médica > Interações Medicamentosas | RN001 |

## Protótipo de Tela

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
