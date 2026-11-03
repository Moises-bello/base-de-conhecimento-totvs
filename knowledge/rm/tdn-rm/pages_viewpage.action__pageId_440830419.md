---
content_hash: e0b59854e5215b2e99f9f04e44f9f78c1e9f200dbc12e19e0db7929a12788df1
fetched_at: '2026-06-29T00:09:53.055260+00:00'
page_id: '440830419'
product: rm
source: tdn-rm
title: Quadro de Permanência - TOP
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=440830419
version: 4
---

---

A distribuição da mão de obra e equipamentos no tempo, deve se tornar um dos principais fatores gerador do orçamento e seu respectivo custo e o consumo de material não deve ser o item de maior preocupação desse tipo de orçamento e sim a distribuição dos recursos horários no tempo.

No Quadro de Permanência é possível ajustar no tempo os recursos de tipo mão de obra e equipamento.

O objetivo principal dessa modalidade de cálculo é atender as empresas que tem como seu maior foco a venda de projetos onde o principal recurso a ser consumido é a mão de obra.

Os cálculos de custo unitário e custo total sofrem impactos da vigência, e caso o insumo tenha vigência cadastrada, essa irá alterar o seu custo unitário e consequentemente o custo total.

Na Planilha

O impacto da permanência do recurso no custo do projeto se dará através da utilização da funcionalidade de insumo derivado.

Um equipamento dentro da planilha de atividades será representado por uma etapa, e nesta etapa estarão contidos todos os recursos que esse equipamento demandar.

Atividades relacionadas a um insumo derivado serão calculadas somente durante o processo de calculo do projeto, e sempre que o quadro de permanência ou o valor desse insumo for alterado, essa alteração refletirá na atividade (após atualizar a planilha de atividades), alterando a sua quantidade e ou o seu custo unitário, e consequentemente alterando o custo total.

A vigência de preços irá impactar no custo total tanto do quadro de permanência quanto do valor da tarefa. Portanto, ela deverá sempre ser considerada em todos os processos referentes à permanência.

A quantidade informada para cada período do insumo no quadro de permanência deverá ser transportada para o cronograma previsto da atividade originada pela permanência desse insumo. (tipo de derivação definida na aba insumo derivado). O sistema fará o lançamento automaticamente no cronograma.  
   
Colunas disponíveis no quadro de Permanência:

* **Código:** Código do Insumo;
* **Descrição:** Descrição do Insumo;
* **Unidade:** Unidade do Insumo;
* **Pico Hmês:** Maior valor informado para o recurso em todos os períodos;
* **Total HxMês:** Soma total de horas em todos os períodos;
* **Unidade de Serviço:** Unidade de Serviço agrupador do insumo. Somente estará disponível, se na exportação o agrupamento selecionado foi por Unidade ou Local de Serviço;
* **Local de Serviço:** Local de Serviço agrupador do insumo. Somente estará disponível, se na exportação o agrupamento selecionado foi por Local de Serviço;
* **Colunas de períodos:** Colunas para cada período do cronograma;
* **Custo Unitário:** Valor de cada hora do recurso;
* **Custo Total:** Valor total considerando Custo Unitário X Total HxMês.

As colunas que permitirão a edição dos valores serão apenas as dos períodos relacionados com o cronograma e no nível máximo de detalhamento utilizado na exportação, respeitando o vínculo existente de Unidade ou Local de Serviços às atividades.
