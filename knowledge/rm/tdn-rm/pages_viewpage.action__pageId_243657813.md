---
content_hash: a7b1eef4c26f91402d1de803d41d79a766a5c9f2f37bbb8bf1a44770ed4a4749
fetched_at: '2026-06-29T00:08:13.242953+00:00'
page_id: '243657813'
product: rm
source: tdn-rm
title: ER_SAUHRM01-34_Controle_Exames_Movimentação_Status
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243657813
version: 120
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## 

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS HOSPITALAR | **Módulo** | RM SAUDE |
| **Segmento Executor** | SAÚDE | | |
| **Projeto** | SAUHRM01 | **IRM** | SAUHRM01-36 |
| **Requisito** | SAUHRM01-34 | **Subtarefa** | SAUHRM01-410 |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

## Objetivo

 

*Este documento tem como objetivo especificar o requisito de  Regularizar a Movimentação de Status no *Controle de Exames**

## Definição da Regra de Negócio

**RN001** -  Validar o status dos exames a serem vinculados. Caso sejam os status abaixo não será possível finalizar a vinculação.

               'X' – Cancelado;

               'M' – Registro Médico;

               'T' – Execução Externa;

               'F' – Entrega.

**RN002** - Movimentar o status de todos os laudos vinculados a um mesmo pedido de exame

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Controle do Pedido de Exames | [Alteração] | Unidade de Diagnóstico > Controle de Pedidos de Exames | RN001 |
| Controle do Pedido de Exames | [Alteração] | Unidade de Diagnóstico > Controle de Pedidos de Exames | RN002 |

**Exemplo de Aplicação:**

1. Acesse o menu **"Unidade de Diagnóstico > Controle de Pedidos de Exames"**
2. Lincar exames. Verificar que os status  'X' ,  'M', 'T'  e   'F' mostram mensagem que o status é inválido.
3. Mover status de um dos exames. Verificar se todos exames lincados mudam de status.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
