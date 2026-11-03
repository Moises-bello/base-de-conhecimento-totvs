---
content_hash: 6462a1acf3f35f1a312e23ac997cc1fd5e34b1cfa93833572fe88b41a652b5a9
fetched_at: '2026-06-29T00:06:05.730339+00:00'
page_id: '201726749'
product: rm
source: tdn-rm
title: DT_FÓRMULA_VISUAL_FATURAMENTO_DE_MOVIMENTO
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=201726749
version: 1
---

# FÓRMULA VISUAL - FATURAMENTO DE MOVIMENTO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Faturamento |  |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Fórmula Visual |  | |  |  | |
| **Cadastros Iniciais:** | Fórmula Visual |
| **Parâmetro(s):** |  |
| **Ponto de Entrada:** |  |
| **Chamados relacionados** |  |
| **Requisito (ISSUE):** | PCREQ-5387 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server, Oracle |
| **Tabelas utilizadas:** | GATIVIDADESWORKFLOW |
| **Sistema(s) operacional(is):** | Windows 7 SP1 ou superior. |
| **Versões/Release:** | 12.1.7. |

## Descrição

Disponibilização de atividades de Fórmula Visual para permitir a elaboração de Fórmulas Visuais que chamem os serviços disponíveis na tela de movimentos. Os serviços disponibilizados neste ciclo são: 

* Cancelamento de Movimento
* Exclusão de Movimento
* Faturamento de Movimento
* Alteração do Movimento
* Alteração do Rateio por Centro de Custo do Movimento
* Alteração do Rateio por Departamento do Movimento
* Alteração de Item de Movimento
* Alteração de Numero de série do Item de Movimento
* Alteração de Lote do Item de Movimento
* Alteração de Grade do Item de Movimento
* Alteração do Rateio por Centro de Custo do Item de Movimento
* Alteração do Rateio por Departamento do Item de Movimento

## Procedimento para Implantação

**Inclusão de Fórmulas Visuais**

Acessar TOTVS Gestão de Estoque, Compras e Faturamento | Guia Gestão | Fórmula Visual | Fórmula Visual, as Atividades de Fórmulas Visuais estarão disponíveis na Aba ‘Atividades’.

O usuário deverá criar as fórmulas visuais de acordo com a necessidade e vincular em processos do tipo de movimento desejado.

## Procedimento para Utilização

1. Incluir a Fórmula Visual no tipo de movimento através do botão PROCESSOS;
2. Após criar o movimento, executar a mesma para que seja executada a Atividade de acordo com a configuração.

## Vídeo

Não há.
