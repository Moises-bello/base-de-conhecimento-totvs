---
content_hash: 55c89cf09a864a337c9eb929fdca9de7162d3e4e5a8f588a80bc22a31e6c318d
fetched_at: '2026-06-29T00:06:03.220882+00:00'
page_id: '198951389'
product: rm
source: tdn-rm
title: ER_migracao_relatorio_insumos_por_tarefas
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_migracao_relatorio_insumos_por_tarefas
version: 3
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Obras e Projetos | **Módulo** | Relatórios |
| **Segmento Executor** | Construção & Projetos | | |
| **Projeto1** | R\_C&P\_TOP007 | **IRM1** | PCREQ-6016 |
| **Requisito1** | PCREQ-6017 | **Subtarefa1** | PDR\_CP\_TOP007-1393 |
| **Chamado2** | Não se aplica. | | |
| **Release de Entrega Planejada** | 12.1.7 | **Réplica** | Não |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | Pré-Requisitos para melhor entendimento da especificação:  TOTVS Reports - <http://wikihelp.totvs.com.br/WikiHelp/Rpt/Rpt.Reports.aspx>  Planilhas - <http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.Planilhas.aspx>  Insumos - <http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.Insumos.aspx> | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Migração dos relatórios do Tipo Insumos por Tarefas para o TOTVS Reports.

## Definição da Regra de Negócio

 

O Relatório de insumos por tarefas exibe todos os insumos de uma determinada tarefa do projeto, contendo o código do insumo, descrição do insumo, código da tarefa, descrição da tarefa, unidade de medida, quantidade, preço unitário e preço total da tarefa por insumo. Exibe ainda o valor total por insumo da tarefa. 

Ele poderá ser acessado de duas maneiras no sistema: 

* No RM Reports dentro do TOTVS Construção e Projetos na área Sistema, no menu Gestão e será do tipo 48 – Insumos por tarefas;
* No menu Relatórios -> Insumos por tarefas.

**Restrições** 

* Com a migração o relatório não terá mais a opção de recalcular a Curva ABC.
* Este relatório será padrão no sistema e o usuário não poderá editar ou excluir o mesmo.
* Em contra partida o usuário poderá realizar uma cópia ou exportar o relatório para um novo e editando-o assim para as suas necessidades.

**Filtros** 

* Cenário
* Tipo de Planilha (Atividades ou Serviços)
* Intervalo de código de tarefas

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Relatórios | Alteração | Construção e Projetos -> Relatórios -> Insumos -> Insumos por Tarefas | - |

***Tabelas Utilizadas***

* *GCOLIGADA - Coligadas*
* *MPRJ - Projetos*
* *MABCISMTRF - Curva ABC de Insumos*
* *MISM - Insumos*
* *MTAREFA - Tarefas*
* *GIMAGEM - Imagens*

## Protótipo de Tela

**Protótipo 01**

* **Relatório:** informação do código do relatório a ser impresso. Nessa pesquisa aparecerão somente relatórios do tipo “Planilha de tarefas”.
* **Imprimir direto da impresso:** permite a impressão diretamente sem visualização do relatório.

**Protótipo 02**

**Insumos por tarefas:** serão listados os dados das tarefas (código da tarefa, descrição da tarefa) e dos insumos (código do insumo, descrição, unidade de medida, quantidade, preço unitário, preço total) agrupados por tarefa.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
