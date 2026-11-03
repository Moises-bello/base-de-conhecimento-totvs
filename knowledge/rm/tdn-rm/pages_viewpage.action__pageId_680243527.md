---
content_hash: f0a458684b43262ed43aa2f59d30a54af61d464020ed2b42e2bfb4f07717847d
fetched_at: '2026-06-29T00:11:17.436008+00:00'
page_id: '680243527'
product: rm
source: tdn-rm
title: Relatório Mão de Obra
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=680243527
version: 5
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tela Mão de Obra**
   1. **Principais Campos e Parâmetros**
4. **Tabelas utilizadas**

## **01. VISÃO GERAL**

O relatório tem o objetivo de apresentar as informações de programa, tarefa, localização, quantidades, homens/dia e percentual da produção.

As informações serão agrupadas e totalizadas por programa, tarefa, localização e apresentará dados da produção de acordo com o período selecionado, tonelada para o programa/tarefa/localização, quantidade de produção, valor da produção e percentual do valor em relação do total geral.

Para geração do relatório, deverão ser preenchidos os campos da tela abaixo:

* Selecionar os filtros de funcionários por seção ou seleção de funcionários.

* Selecionar o Período que o relatório será emitido, informando a data de início e fim do período.

* Selecionar a Produção Agrária que o relatório será emitido.

* Selecionar a Tarefa que o relatório será emitido.

Deverá ser informado/selecionado o Código do relatório “**FOPREL00196 - Folha Agrária - Mão de Obra**”.

**Observação:** Este relatório deverá ser importado em **Gestão** | **RM Reports**.

Informar as Finalidades das Tarefas que deseja ser emitidas no relatório.

No Relatório serão listadas as seguintes colunas:

**Programa** - São listadas as descrições do programa informado nos parâmetros do relatório.

1. Caso o usuário não selecione um programa na interface de parâmetros/filtros, serão listados TODOS os programas constantes na produção para o período informado.

**Tarefa** - São listadas as descrições do programa informado nos parâmetros do relatório.

1. Caso o usuário não selecione uma tarefa na interface de parâmetros/filtros, serão listados TODOS os programas constantes na produção para o período informado.

**Local** - Serão listados os códigos da unidade agrária da produção.

**Tonelada** - Será listada a somatória da tonelada da produção de acordo com o programa, tarefa e unidade agrária, onde a finalidade esteja relacionada com a regra de cálculo definida para a produção.

1. Caso nenhuma finalidade seja selecionada pelo usuário nos parâmetros/filtros, serão consideradas todas as finalidades, isto é, não irá fazer restrição de finalidade.

**Qtde/Unid.** - Será listado o somatório da quantidade produzida, de acordo com o programa, tarefa e unidade agrária em que a finalidade da tarefa seja uma das selecionadas no parâmetro de lista de finalidades.

1. Caso nenhuma finalidade seja selecionada pelo usuário nos parâmetros/filtros, serão consideradas todas as finalidades, isto é, não irá fazer restrição de finalidade.

**Diária** - Serão listados o somatório do homem/dia da produção de acordo com o programa, tarefa e unidade agrária em que a finalidade da tarefa seja uma das selecionadas no parâmetro de lista de finalidades.

1. Caso nenhuma finalidade seja selecionada pelo usuário nos parâmetros/filtros, serão consideradas considerar todas as finalidades, isto é, não irá fazer restrição de finalidade.

**Vlr R$** - Serão listados os somatórios do valor produzido que serão a quantidade da produção multiplicada pelo preço unitário de acordo com o programa, tarefa e unidade agrária cuja finalidade da tarefa seja uma das selecionadas no parâmetro de lista de finalidades.

1. Caso nenhuma finalidade seja selecionada pelo usuário nos parâmetros/filtros, serão consideradas todas as finalidades, isto é, não irá fazer restrição de finalidade.

**Percentual** - Serão listados os percentuais obtidos pelo cálculo Valor R$ em relação ao Total Geral do Valor R$.

**Sub-Total da tarefa** -  Serão listados um sub-total da tarefa a cada quebra de tarefa selecionada pelo usuário nos parâmetros/filtros.

**Sub-Total da Programa** - Serão listados um sub-total do programa a cada quebra de programa selecionado pelo usuário nos parâmetros/filtros.

**Total geral** - Serão listados para as colunas totalizadores de Toneladas, Qtde/Unid, Diárias, Vlr R$ e Perc. (Percentual).

Para cada coluna de valores existirá um totalizador que deverá proceder conforme regra informada em cada campo.

**Total de func. de férias em dd/mm/aaaa :** - Serão listados os números de funcionários com a situação '**F - Férias**' na seção e período selecionado pelo usuário nos parâmetros/filtros.

**Total de func. efetivos em dd/mm/aaaa :** - Serão listados os números de funcionários com a situação '**A - Ativo**' na seção e período selecionado pelo usuário nos parâmetros/filtros.

## **02. EXEMPLO DE UTILIZAÇÃO**

Foi acessado o menu Folha Agrária | Produção | Mão de Obra e a base exemplo existem vários casos parametrizados.

Na tela de parâmetros foi parametrizado da seguinte forma:

Depois de executado apresenta o relatório no seguinte modelo:

## **03.****TELA: Mão de Obra**

**Principais Campos e Parâmetros**

| Ação | Descrição |
| --- | --- |
| Quebra de seção | Seleciona a seção |
| Seleção de Funcionários | Seleciona os funcionários |
| Período | Seleciona o Período que o relatório será emitido |
| Programação Agrária | Seleciona a Programação Agrária que o relatório será emitido. |
| Tarefa | Seleciona a Tarefa que o relatório será emitido. |
| Código do Relatório | O relatório “FOPREL00196 - Folha Agrária - Mão de Obra” deve ser importado em Gestão /  RM Reports para ser selecionado no Código do Relatório. |

## **04. TABELAS UTILIZADAS**

* PFUNC
* VTAREFA
* PFHSTSIT
* PPESSOA
* PPRODUCAOAGRARIA
* PSECAO
* PRGRCALCTAREFAAGRARIA
* PFUFERIASPER
