---
content_hash: 967b37c70b700a092a2bc1464dea36fe6891773296250314010695d418e79065
fetched_at: '2026-06-29T00:06:00.302774+00:00'
page_id: '195301192'
product: rm
source: tdn-rm
title: ER_migracao_relatorio_medicao_completa
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_migracao_relatorio_medicao_completa
version: 11
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Obras e Projetos | **Módulo** | Relatórios |
| **Segmento Executor** | Construção & Projetos | | |
| **Projeto1** | R\_C&P\_TOP007 | **IRM1** | PCREQ-6199 |
| **Requisito1** | PCREQ-6200 | **Subtarefa1** | PDR\_CP\_TOP007-1208 |
| **Chamado2** | Não se aplica. | | |
| **Release de Entrega Planejada** | 12.1.7 | **Réplica** | Não |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | Pré-Requisitos para melhor entendimento da especificação:  TOTVS Reports - <http://wikihelp.totvs.com.br/WikiHelp/Rpt/Rpt.Reports.aspx>  Contrato - <http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.Contrato.aspx>  Períodos do Contrato - <http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.PeriodosContrato.aspx>  Medição de Itens - <http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.MedicaoContrato.aspx> | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Migração dos relatórios do Tipo Medição Completa para o TOTVS Reports.

## Definição da Regra de Negócio

 

O Relatório de Medição Completa exibe a quantidade e valor (medido e acumulado) das medições associadas as tarefas de um determinado período do contrato. (vide Protótipo 02).

Haverá dois tipos de relatórios, um exibindo a medição completa normamente e outro com detalhamento de retenção: 

* 03.003 – Medição Completa;
* 03.006 – Medição Completa com Detalhamento de Retenção.

Ele poderá ser acessado da seguinte forma no sistema:

* No menu Relatórios -> Medição Completa.

**Restrições** 

* Este relatório será padrão no sistema e o usuário não poderá editar ou excluir o mesmo.
* Em contra partida o usuário poderá realizar uma cópia ou exportar o relatório para um novo e editando-o assim para as suas necessidades.

**Filtros** 

* Contrato e período do mesmo

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Relatórios | Alteração | Construção e Projetos -> Relatórios -> Medição Completa | - |

**Tabelas Utilizadas** 

* MRELMEDICAO – Relatório de Medição
* MTRF – Tarefas da planilha de atividades
* MPRJ – Projetos
* MCNT – Contratos
* GCOLIGADA – Coligadas
* GIMAGEM – Imagens
* FCFO – Clientes/Fornecedores

## Detalhamento dos campos

|  |  |  |
| --- | --- | --- |
| **03.003 – Medição Completa** | | |
| **Campo** | **Descrição** | **Origem dos dados** |
| Número do Contrato | Número do Contrato escolhido no filtro | MCNT.NUMCNT |
| Número do Período | Número do período escolhido no filtro | MRELMEDICAO.PERIODOMED |
| Data Início | Data de Início do período do contrato | Consulta SQL: 012 – Data Início do Período (DATAINICIO) |
| Data Fim | Data de Fim do período do contrato | Consulta SQL: 012 – Data Fim do Período (DATAFIM) |
| Cliente/Fornecedor | Nome fantasia do cliente ou fornecedor do contrato | FCFO.NOMEFANTASIA |
| Projeto | Código e Descrição do Projeto | MPRJ.CODPRJ / MPRJ.DESCRICAO |
| Código | Código da Tarefa que está no contrato | MTAREFA.CODTRF |
| Descrição | Descrição da Tarefa que está no contrato | MTAREFA.NOME |
| Un | Unidade de medida da Tarefa que está no contrato | MTAREFA.CODUND |
| Preço | Valor unitário do item contratado | Fórmula: 07 – Valor unitário do item contratado (VALORUNITITEM) |
| Quant. Medida | Quantidade medida no período | MRELMEDICAO.QUANTMEDIDA |
| Quant. Acumulada | Quantidade medida acumulada de um serviço (somando-se os períodos anteriores) | Fórmula: 04 - Quantidade medida acumulada de um serviço (QTDEMEDACUMSERVICO) |
| Valor Medido | Valor medido para o período | Expressão: Quantidade Medida \* Preço |
| Valor Acumulado | Valor medido acumulado de um serviço (somando-se os períodos anteriores) | Fórmula: 01 – Valor medido acumulado de um serviço (VALORMEDACUMSERVICO) |
| Valor medição no mês | Valor total medido do período escolhido no filtro | Totalizador: Somatório do campo Valor Medido. |
| Valor medição acumulada | Valor total acumulado do período escolhido no filtro | Totalizador: Somatório do campo Valor Acumulado |
| Valor Retido/Deduzido no mês | Valor total retido e deduzido do período escolhido no filtro | Totalizador: Somatório do campo Valor (Retenções/Deduções) |
| Valor Líquido no mês | Valor da medição no mês subtraído do valor retido/deduzido no mês | Expressão: Totalizador medido no mês - Totalizado Retido/Deduzido |

O relatório 03.006 – Medição Completa com Detalhamento de Retenção possui os mesmos campos do anterior detalhado, porém com uma banda a mais para o Detalhamento de Retenção Contratual que é detalhado na tabela abaixo:

|  |  |  |
| --- | --- | --- |
| **03.006 – Medição Completa com Detalhamento de Retenção** | | |
| **Campo** | **Descrição** | **Origem dos dados** |
| Tipo | Tipo do detalhamento da Retenção. Pode ser R (Retenção) ou D (Dedução) | MPDODETRET.TIPO |
| Valor | Valor da Retenção | MPDODETRET.VALOR |
| Código | Código da Retenção ou Dedução | MTIPODETRET.CODIGO |
| Descrição | Descrição da Retenção ou Dedução | MTIPODETRET.DESCRICAO |

Importante

Para que um relatório seja gerado pelo Menu Relatórios -> Medição Completa, o mesmo tem que ser do tipo Medição Completa e no primeiro detalhe (Banda) do relatório dever conter a tabela de Medição Completa (MRELMEDICAO).

## Protótipo de Tela

**Protótipo 01: Filtros do Relatório**

****Protótipo 012: Leiaute do Relatório****

## Fluxo do Processo

## **Diagrama de Entidade-Relacionamento**

 

 

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
