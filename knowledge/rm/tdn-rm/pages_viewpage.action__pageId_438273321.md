---
content_hash: 4bbd5b606c74a5d0ac9dbe9f058af12eb52b8953752713e159f1962852989bc1
fetched_at: '2026-06-29T00:09:52.186040+00:00'
page_id: '438273321'
product: rm
source: tdn-rm
title: DT TOP Mobile - Apontar com mais de 100% no Avanço Físico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=438273321
version: 2
---

# TOP MOBILE - APONTAR COM MAIS DE 100% NO AVANÇO FÍSICO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão de Obras e Projetos |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Apontamento de Avanço Físico | Apontamento de Avanço Físico | |
| **Cadastros Iniciais:** | Projeto, Insumos, Tarefas, Coletor, Usuário de Coletor, Folhas Tarefas |
| **Parâmetro(s):** | Não se aplica |
| **Ponto de Entrada:** | Não se aplica |
| **Tickets relacionados** | Não se aplica |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | [TOPORCAPLAN001-4486](http://jiraproducao.totvs.com.br/browse/TOPORCAPLAN001-4486) |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server e Oracles). |
| **Tabelas Utilizadas:** | Não se aplica |
| **Sistema(s) Operacional(is):** | Windows |
| **Pacote:** | Não se aplica |

## Descrição

Possibilidade de realizar o apontamentos de tarefas no Avanço Físico que ultrapassam os 100% de conclusão.

## Procedimento para Utilização

Para que a produção real do executado na obra possa ser possível, o TOP Mobile permite que os apontamentos de Avanço Físico possam ser definidos acima de 100% do planejado, pois em muitos casos a quantidade planejada é apenas uma estimativa e não reflete a realidade.

Sendo assim temos dois cenários em que esse apontamento acima de 100% pode refletir no TOTVS Obras e Projetos:

* **Quantidade Planejada do item na Falha Tarefa ser 100% da quantidade definida para a tarefa no projeto:**
  + Tarefa 001.01.01, Quantidade = 100
  + Item da Folha Tarefa, Quantidade Planejada = 100
  + Percentual do Apontamento = 200%
  + Percentual Concluído no PERT = 100%
* **Quantidade Planejada do item na Falha Tarefa ser menos de 100% da quantidade definida para a tarefa no projeto:**
  + Tarefa 001.01.02, Quantidade = 100
  + Item da Folha Tarefa, Quantidade Planejada = 25
  + Percentual do Apontamento = 200%
  + Percentual Concluído no PERT = 50%
