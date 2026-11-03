---
content_hash: a9dfbbb98ebaaa84cefc56f444a1bbcce102cb1c188e5989d69d32cbb2e6efca
fetched_at: '2026-06-29T00:08:22.730847+00:00'
page_id: '269439259'
product: rm
source: tdn-rm
title: ER_SAUHRM02-396_Devolução_de_Paciente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269439259
version: 114
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | GESTÃO HOSPITALAR - RM | **Módulo** | Estoques / Movimentação de Estoques |
| **Segmento Executor** |  | | |
| **Projeto1** | SAUHRM02 | **IRM1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-346 |
| **Requisito1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-326 | **Subtarefa1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-396 |
| **Chamado2** |  | | |
| **País** | ( **X** ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### Objetivo

 Esta especificação tem como objetivo detalhar a melhoria à ser implementada na funcionalidade de Movimentação de Estoque do produto TOTVS Gestão Hospitalar. A melhoria consiste-se em apresentar apenas os itens associados ao atendimento e/ou à requisição em movimentações do tipo Devolução p/ Paciente, com o objetivo de agregar uma melhoria operacional ao produto.

### Definição da Regra de Negócio

***RN001** - Permitir a parametrização de filtrar apenas os itens associados a requisição informada nas movimentações de estoque do tipo Devolução p/ Paciente.*

********RN002** -**** **Em movimentação de estoque do tipo Devolução p/ Paciente, apresentar apenas os itens associados ao atendimento na tela de pesquisa dos itens da prescrição [Figura 2].****

****RN003** - Em movimentação de estoque do tipo Devolução p/ Paciente [Figura 1], quando for informada o número da Req. associada, apresentar apenas os itens associados a requisição na tela de pesquisa dos itens da prescrição [Figura 2].**

 

Figura 1

Figura 2

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Parametrizar filtro de itens da prescrição | [Parametrização] | Opções / Parâmetros / Parâmetros Gerais / Estoques | RN001 |
| Filtrar os itens associados ao atendimento | [Alteração] | Estoques / Movimentação de Estoque / Requisição\* / Itens da Requisição | RN002 |
| Filtrar os itens associados a requisição | [Alteração] | Estoques / Movimentação de Estoque / Requisição\* / Itens da Requisição | RN002 |

*\*Selecionar um registro*

***Exemplo de Aplicação:***

* *Facilitar o processo de seleção do item que será devolvido, não havendo a necessidade de exibir todos itens cadastrados no sistemas.*

***Tabelas Utilizadas***

* SZMOVIESTOQUE - Movimentação de Estoque
* SZMOVIESTOQUEITEM - Itens da Movimentação de Estoque

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
