---
content_hash: 39892074d0ea234382f1f14231433fd2fffc3b638f67031b93f7b3167af80579
fetched_at: '2026-06-29T00:06:03.541017+00:00'
page_id: '198956124'
product: rm
source: tdn-rm
title: ER_migracao_relatorio_insumos_do_projeto
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_migracao_relatorio_insumos_do_projeto
version: 6
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Obras e Projetos | **Módulo** | Relatórios |
| **Segmento Executor** | Construção & Projetos | | |
| **Projeto1** | R\_C&P\_TOP007 | **IRM1** | PCREQ-6014 |
| **Requisito1** | PCREQ-6015 | **Subtarefa1** | PDR\_CP\_TOP007-1379 |
| **Chamado2** | Não se aplica. | | |
| **Release de Entrega Planejada** | 12.1.7 | **Réplica** | Não |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | Pré-Requisitos para melhor entendimento da especificação:  TOTVS Reports - <http://wikihelp.totvs.com.br/WikiHelp/Rpt/Rpt.Reports.aspx>  Planilhas - <http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.Planilhas.aspx>  Insumos - <http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.Insumos.aspx> | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

 Migração dos relatórios do Tipo Insumos do Projeto para o TOTVS Reports.

## Definição da Regra de Negócio

O Relatório de Insumos do Projeto exibe todos os insumos utilizados no projeto (vide Protótipo 02). 

Haverá um relatório: 

* 04.005 – Insumos utilizados no Projeto – Locais e Globais

Ele poderá ser acessado da seguinte maneira no sistema: 

* No menu Relatórios -> Insumos no Projeto.

**Restrições** 

* Este relatório será padrão no sistema e o usuário não poderá editar ou excluir o mesmo.
* Em contra partida o usuário poderá realizar uma cópia ou exportar o relatório para um novo e editando-o assim para as suas necessidades.

**Filtros** 

* Por cenário e tipo de planilha
* Faixa de tarefas (tarefa inicial e tarefa final)
* Por Insumos
* Por Grupo de Custo
* Por Unidade

Importante

Nos filtros de Insumos, Grupos de Custo e Unidades serão permitidos a escolha de no máximo 100 itens de cada.

Para que um relatório seja gerado pelo Menu Relatórios -> Insumos -> Insumos do projeto, o mesmo tem que ser do tipo Insumos do Projeto e no primeiro detalhe (Banda) do relatório dever conter a tabela de Insumos/Composições do Projeto (MRELRECURSO).

## 1.1          Detalhamento dos campos

|  |  |  |
| --- | --- | --- |
| **Relatórios**  **04.003 – Insumos utilizados no Projeto e**  **004.005 - Insumos utilizados no Projeto – Locais e Globais** | | |
| **Campo** | **Descrição** | **Origem dos dados** |
| Cód. do Insumo | Código do Insumo | MISM.CODISM |
| Descrição do Insumo | Descrição do Insumo | MISM.DESCISM |
| Un | Unidade de medida do Insumo (Ex.: Kg, M², m, etc) | MISM.CODUND |
| Preço Unitário | Preço unitário para o Insumo | MISM.VALOR |

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Relatórios | Alteração | Construção e Projetos -> Relatórios -> Insumos -> Insumos do projeto | - |

**Tabelas Utilizadas**

* MRELRECURSO – Relatório de recursos
* GCOLIGADA – Coligadas
* MISM – Insumos
* MPRJ – Projetos
* GIMAGEM – Imagens

## Protótipo de Tela

**Protótipo 01**

## Protótipo 02

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
