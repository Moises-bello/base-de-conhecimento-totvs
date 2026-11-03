---
content_hash: 9956925c0530e3861ec26fdc66447fc5a29efd3ce0874836631b2151a37b0b5d
fetched_at: '2026-06-29T00:06:28.528242+00:00'
page_id: '233754026'
product: rm
source: tdn-rm
title: ER_R_FRW_INOVBH-28_Validacao_Dados_Planilha_RM
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_R_FRW_INOVBH-28_Validacao_Dados_Planilha_RM
version: 132
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | Globais |
| **Requisito** | R\_FRW\_INOVBH-28 | | |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

## Objetivo

 Possibilitar a validação dos dados inseridos na planilha. Destaca-se a possibilidade de criar listas suspensas nas células em que a validação de dados está ativada.

## Definição da Regra de Negócio

 A API da PlanilhaRM dá suporte à validação dos dados inseridos nas células da planilha eletrônica. A validação de dados está disponível somente através da API, não sendo possível o usuário configurar a validação utilizando a visão (formulário).

A validação dos dados pode ser configurada utilizando a propriedade Validation da classe PlanRMRange. Essa propriedade expõe os membros e métodos da classe PlanRMValidation que são descritos na tabela abaixo:

|  |  |
| --- | --- |
| **Propriedades** | |
| **Nome** | **Descrição** |
| AlertStyle | Recupera o estilo de alerta utilizado quando uma validação falha. O estilo do alerta é representado pelo enumerável "PlanRMValidationAlertStyle". |
| ErrorMessage | Define a mensagem de erro a ser exibida quando uma validação falha. |
| ErrorTitle | Define o título da mensagem de erro configurada na propriedade "ErrorMessage". |
| Formula1 | Retorna a primeira fórmula de validação. |
| Formula2 | Retorna a segunda fórmula de validação. |
| IgnoreBlank | Define se a validação deve ser ignorada caso a fórmula de validação se refere à uma célula em branco. |
| InCellDropdown | Define se uma lista suspensa será utilizada para fazer a validação do dado da célula. |
| InputMessage | Define a mensagem mostrada quando uma das células representadas está ativa. |
| InputTitle | Define o título da mensagem da propriedade configurada na propriedade "InputMessage". |
| Operator | Retornar o operador de validação. O operador é representado pelo enumerável "PlanRMValidationOperator". |
| ShowError | Define se erros serão mostrados caso uma validação falhe. |
| ShowInputMessage | Define se uma mensagem de entrada deve ser exibida quando uma das células representadas está ativada. |
| Type | Retorna o tipo de validação. O tipo da validação é representado pelo enumerável "PlanRMValidationType". |
| Value | Retorna verdadeiro se todas as células representadas coincidem com seu critério de validação. |

|  |  |
| --- | --- |
| **Métodos** | |
| **Nome** | **Descrição** |
| Add(PlanRMValidationType type, PlanRMValidationAlertStyle alertStyle, PlanRMValidationOperator validationOperator, string formula1, string formula2) | Adiciona uma validação de dados existente no grupo de células selecionadas. |
| Delete() | Remove a validação de dados do grupo de células selecionadas. |
| Modify(PlanRMValidationType type, PlanRMValidationAlertStyle alertStyle, PlanRMValidationOperator validationOperator, string formula1, string formula2) | Modifica uma validação de dados existente no grupo de células selecionadas. |

***Exemplo de Aplicação:***

c#1Validação de Dadostrue

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
