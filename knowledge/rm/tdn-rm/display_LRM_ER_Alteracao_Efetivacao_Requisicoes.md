---
content_hash: 2ae6dfd5d5a472a21d33fb517dd122b296748429e073eb5c0f6be2f68ec672dd
fetched_at: '2026-06-29T00:06:04.348178+00:00'
page_id: '200908812'
product: rm
source: tdn-rm
title: ER_Alteracao_Efetivacao_Requisicoes
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_Alteracao_Efetivacao_Requisicoes
version: 1
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Pessoas | **Módulo** | RHU |
| **Segmento Executor** |  | | |
| **Projeto1** |  | **IRM1** |  |
| **Requisito1** |  | **Subtarefa1** |  |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** |  | **Réplica** |  |
| **País** | (  ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Efetivar a próxima alteração de dados funcionais progressivo das requisições de alteração de dados funcionais e de transferência com alteração de dados funcionais no processo de conclusão da tela de efetivação de requisições.

## Definição da Regra de Negócio

O processo de conclusão de requisições de alteração de dados funcionais e de transferência com alteração de dados funcionais será alterado para efetivar a próxima alteração de dados funcionais progressivo. Se não houver alteração de dados funcionais progressivo na requisição o processo continuará seu comportamento normal, concluindo a requisição. A próxima alteração de dados funcionais progressivo é a primeira pendente no anexo de alteração de dados funcionais progressivo, que pode ser acessado através da visão de efetivação de requisições (RH > Gestão de Pessoas > Valorização > Efetivações > Efetivar Alteração de Dados Funcionais / Efetivar Transferência c/ Alteração de Dados Funcionais). Se houver apenas uma progressão, o processo irá efetivar a progressão e também irá concluir a requisição. No caso de ser a última progressão, o processo irá efetivar a progressão e também irá concluir requisição. Caso houver mais de uma progressão, o processo irá efetivar apenas a próxima progressão e não irá concluir a requisição, pois a requisição só pode ser concluída depois de todas as progressões efetivadas.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Efetivações > Concluir | [Alteração] | RH > Gestão de Pessoas > Valorização > Efetivações > Efetivar Alteração de Dados Funcionais > Concluir | - |
| Efetivações > Concluir | [Alteração] | RH > Gestão de Pessoas > Valorização > Efetivações >  Efetivar Transferência c/ Alteração de Dados Funcionais > Concluir | - |
|  |  |  | - |

## Protótipo de Tela

**Protótipo 01**

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
