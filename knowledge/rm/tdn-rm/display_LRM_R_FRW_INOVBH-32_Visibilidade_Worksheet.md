---
content_hash: 145a6f4c5d7f3b9831c163179cbde3bb729b25b2551cf428ffb01ff93b71cc0c
fetched_at: '2026-06-29T00:06:30.049869+00:00'
page_id: '235310071'
product: rm
source: tdn-rm
title: R_FRW_INOVBH-32_Visibilidade_Worksheet
type: documentation
url: https://tdn.totvs.com/display/LRM/R_FRW_INOVBH-32_Visibilidade_Worksheet
version: 117
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | Globais |
| **Requisito** | R\_FRW\_INOVBH-32 | | |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

## Objetivo

 Possibilitar a alteração da visibilidade de um worksheet.

## Definição da Regra de Negócio

 A API da PlanilhaRM dá suporte à alteração da visibilidade das worksheets da planilha eletrônica. A alteração da visibilidade está disponível somente através da API, não sendo possível o usuário alterá-la utilizando a visão (formulário).

A visibilidade pode ser configurada utilizando a propriedade Visible da classe PlanRMWorksheet. Essa propriedade retorna um enumerado cujos valores estão descritos na tabela abaixo:

|  |  |
| --- | --- |
| **PlanRMSheetVisibility** | |
| **Valor** | **Descrição** |
| Visible | Define que a worksheet será visível. |
| Hidden | Define a que a worksheet não será visível. |
| VeryHidden | Define a worksheet não será visível e que o usuário não terá a opção de torná-la visível. |

***Exemplo de Aplicação:***

c#1Validação de Dadostrue

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
