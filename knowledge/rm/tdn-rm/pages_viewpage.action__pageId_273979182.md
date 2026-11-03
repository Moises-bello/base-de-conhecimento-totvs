---
content_hash: 9dd6906396269f2263306ceb05f7c2cfc3f39470da9ccf5bdfc6828ec07d515c
fetched_at: '2026-06-29T00:08:31.970503+00:00'
page_id: '273979182'
product: rm
source: tdn-rm
title: ER SAUHRM02-1017 Melhorias no Kit pré-montado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=273979182
version: 106
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS GESTÃO HOSPITALAR | **Módulo** | RM Saúde |
| **Segmento Executor** | Saúde | | |
| **Projeto** | SAUHRM02 | **IRM/EPIC1** | SAUHRM02-1016 |
| **Requisito/Story/Issue** | SAUHRM02-1017 | **Subtarefa** | SAUHRM02-1018 |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

## Objetivo

Permitir que o usuário possa incluir itens no kit pré-montado através de um campo de pesquisa, não sendo obrigatório o uso de código de barras.

Criar uma tela para a visualização dos kits pré-montados existentes na base de dados.

## Definição da Regra de Negócio

RN001 - Na tela "Monta/Desfaz KIT de Mat/Med", quando o usuário clicar no botão "Incluir" e entrar com um valor em branco no campo "Código de barras", deverá aparecer uma janela para pesquisa manual do item desejado.

RN002 - Criar no menu "Estoques" uma tela de visualização de todos os Kits Pré-montados cadastrados na base de dados.

RN003 - Criar uma tela anexa contendo a listagem dos itens que fazem parte do Kit pré-montado.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Monta/Desfaz Kit de Mat/Med | [Alteração] | Estoques / Monta/Desfaz Kits de MATMED | RN001 |
| Kit Pré-montado de MATMED | [Criação] | Estoques / Kit Pré-montado de MATMED | RN002 |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
