---
content_hash: 01a4254bd9e3a5912a94e3cab6d729d9d8dac6d66871e31f3fa6fdd42fa6f414
fetched_at: '2026-06-29T00:08:11.385780+00:00'
page_id: '242390906'
product: rm
source: tdn-rm
title: ER_SAUHRM01-330_Melhorias_no_Mapa_de_dispensação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=242390906
version: 109
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS GESTÃO HOSPITALAR | **Módulo** | RM Saúde |
| **Projeto** | * SAUHRM01 | **IRM** | * SAUHRM01-329 |
| **Requisito** | * SAUHRM01-330 | **Subtarefa** | * SAUHRM01-362 |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

## Objetivo

   Esta especificação tem como objetivo a melhoria na usabilidade da tela de Mapa de Dispensação.

## Definição da Regra de Negócio

**RN001 -**Alterar a visualização da tela de processamento dos itens, fazendo com que, quando marcado o parâmetro "Utiliza Modelo Otimizado de Separação Prévia", a navegação seja por Prontuário e não por Requisição.

    **RN002 -**Melhorar usabilidade da tela para que após feita uma confirmação de item, o foco passe para o campo de digitação do código do item.

    **RN003 -**Após a seleção do lote, disparar evento de confirmação do item.

    **RN004 -** Permitir o processamento de itens, mesmo que hajam itens pendentes de confirmação (Processamento parcial).    

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Mapa de Dispensação | Alteração | Estoques > Mapa de Dispensação | **RN001, **RN002, **RN003, **RN004******** |

**Exemplo de Aplicação:**

1. Acesse o menu "Estoques > Mapa de Dispensação".
2. Selecione a unidade de estoque e o Filtro desejado.
3. Dê um duplo clique nos registros desejados e execute as seguintes funções:
   1. Confirmação de Item.
   2. Navegação entre prontuários.
   3. Seleção de Lote.
   4. Processamento Parcial.
4. As funcionalidades deverão ter o comportamento de acordo com as RN destacadas acima.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
