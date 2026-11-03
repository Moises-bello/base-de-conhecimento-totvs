---
content_hash: 674cd2234cc925da96f601f8d99d460cd3c3a65183e0689533eecfb4347cae62
fetched_at: '2026-06-29T00:08:36.065829+00:00'
page_id: '284337461'
product: rm
source: tdn-rm
title: ER SAUHRM02-1115 Ordenar os itens da Requisição de Estoque por Nome
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=284337461
version: 103
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

 

|  |  |  |  |
| --- | --- | --- | --- |
| Especificação |  |  |  |
| Produto | GESTÃO HOSPITALAR - RM | Módulo | Movimentação de Estoque |
| Segmento Executor | Saúde |  |  |
| Projeto¹ | R\_SAU\_HRM1617 | IRM¹ | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAU\_BACKLOG-1329 |
| Requisito¹ | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-1115 | SubTarefa¹ | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-1128 |
| Release de Entrega Planejada | 12.1.18 | Réplica | Não necessário |
| País | ( X ) Brasil  (  ) Argentina  (  ) México  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. |  |  |
| Outros |  |  |  |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

 

Ao utilizar a Movimentação de Estoque, na aba Movimentação/Prescrição, permitir que os itens da Grid possam ser ordenados pelas colunas "Código" e "Nome".

### Definição da Regra de Negócio

* *RN001: Na aba Movimentação/Prescrição, da movimentação de estoque ao clicar na  coluna "Código" ordenar os itens da Grid pelo Código.*
* *RN002: Na aba Movimentação/Prescrição, da movimentação de estoque ao clicar na  coluna "Nome" ordenar os itens da Grid pelo *Nome*.*

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| *Movimentação/Prescrição* | [Alteração] | Estoque / Movimentação de Estoque / Registro\* / Aba Itens da Prescrição | RN001 |
| *Movimentação/Prescrição* | [Alteração] | Estoque / Movimentação de Estoque / Registro\* / Aba Itens da Prescrição | RN002 |

\*Selecionar um registro

***Exemplo de Aplicação:***

* Permitir que os itens da Grid possam ser ordenados pelas colunas "Código" e "Nome", conforme opção do usuário.

***Tabelas Utilizadas***

* SZMOVIESTOQUEITEM - Movimentação de Estoque

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
