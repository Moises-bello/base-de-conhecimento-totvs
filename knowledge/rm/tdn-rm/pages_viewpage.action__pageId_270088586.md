---
content_hash: fd1418821b26751d68025106f4c0a896094c647ad32ce0730e6bdec794a51a69
fetched_at: '2026-06-29T00:08:23.735932+00:00'
page_id: '270088586'
product: rm
source: tdn-rm
title: ER_SAUHRM02-350_Migração_Estoque_-_Movimentação_de_estoque
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270088586
version: 109
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### (Obrigatório)

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão Hospitalar | **Módulo** | Estoque |
| **Segmento Executor** | Saúde | | |
| **Projeto1** | SAUHRM02 | **IRM1** | SAUHRM02-348 |
| **Requisito1** | SAUHRM02-350 | **Subtarefa1** | SAUHRM02-473 |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### (Obrigatório)

## Objetivo

Esta implementação tem como objetivo a migração das telas, tanto de visão quanto de edição, da movimentação de estoque da linguagem Delphi para C# .NET.

### (Obrigatório)

## Definição da Regra de Negócio

**RN001 - Tela de visão**

Migrar a tela de visão da movimentação de estoque para a linguagem C#.NET disponibilizando todos os recursos que já existiam em Delphi. Ajustar o código fonte para melhor manutenção.

**RN002 - Tela de visão**

Migrar a tela de edição da movimentação de estoque para a linguagem C#.NET disponibilizando todos os recursos que já existiam em Delphi. Ajustar o código fonte para melhor manutenção.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Movimentação de estoque | [Alteração] | Estoques -> Movimentação de estoque (Tela de visão) | RN001 |
| Movimentação de estoque | [Alteração] | Estoques -> Movimentação de estoque (Tela de edição) | RN002 |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
