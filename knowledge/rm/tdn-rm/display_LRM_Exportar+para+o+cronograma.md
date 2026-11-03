---
content_hash: 704e49855ddd82810f567b6d8b72fdbb19f4e09d9a1c8453dc9c61da4eaf2f1d
fetched_at: '2026-06-29T00:11:29.429486+00:00'
page_id: '736983190'
product: rm
source: tdn-rm
title: Exportar para o cronograma
type: documentation
url: https://tdn.totvs.com/display/LRM/Exportar+para+o+cronograma
version: 11
---

Ainda com o intuito de continuar facilitando o uso e o gerenciamento da Planilha Executiva, foi disponibilizado um processo que possibilita exportar tanto o que foi realizado quanto o previsto.

Ao clicar em "Exportar para o Cronograma", você pode personalizar essa sincronização de acordo com as opções:

* Considerar % concluído: Ao marcar esta opção, o sistema considerará o percentual de conclusão informado para cada item na Planilha Executiva e o atualizará no cronograma e na planilha de atividades, refletindo o avanço real de cada tarefa.
* Exportar % concluído : Ao marcá-la, o sistema exportará o percentual de conclusão atual para o primeiro período ainda não fechado no cronograma.
* Recalcular planejamento: Ao selecionar esta opção, o sistema recalculará todo o planejamento do projeto com base nos novos valores de conclusão das tarefas. Isso pode ajustar as datas de término previstas e identificar possíveis desvios do cronograma original.
* Recalcular cronograma: Essa opção é ideal para manter o cronograma sempre atualizado.

**Processo de exportação do Realizado:**

Caso haja alguma tarefa com alguma inconsistência (como grandezas diferente no cronograma ) será exibido um log informando quais não foram consideradas na exportação.

Somente após o ajuste manual  e reexecutando novamente o processo é que serão exportadas.

É importante destacar que esse processo não é automático, ou seja , caso haja uma importação nova ou alguma alteração é necessário executar novamente o processo para que a atualização reflita na planilha de atividades e no cronograma.

**Processo de exportação do Previsto:**

**Regra de exportação:** Ao exportar a planilha executiva para o cronograma, o sistema sempre exporta 100% do previsto, independentemente do percentual de vínculo das tarefas com os itens. Quando existem múltiplas tarefas vinculadas a um mesmo item, o sistema redistribui os percentuais proporcionalmente de forma que representem a totalidade (100%).

**Lógica de recálculo:** Como o sistema exporta sempre 100% do previsto, ele redistribui o somatório dos percentuais identificados para que eles representem a totalidade. Ou seja, o sistema responde à pergunta: “Se X% é o meu novo 100%, quanto valem cada um dos percentuais originais de cada tarefa?”

**Exemplo de memória de cálculo:**

* **Cenário A – Tarefa única:** Quando existe apenas uma tarefa vinculada ao item, independentemente do percentual de vínculo, o sistema a exporta representando 100% do previsto.
* **Cenário B – Múltiplas tarefas:** Quando existem duas ou mais tarefas vinculadas, o sistema identifica o somatório total dos percentuais e realiza o recálculo proporcional automaticamente.

Considere duas tarefas com percentuais de vínculo de 41% e 30%, totalizando 71% (conforme ilustração abaixo):

* **Tarefa 10101:** (30 ÷ 71) × 100 = 42,25%
* **Tarefa 10102:** (41 ÷ 71) × 100 = 57,75%

Este método garante que o cronograma previsto seja sempre exportado com 100%, redistribuindo os percentuais de forma proporcional entre as tarefas vinculadas ao item da planilha executiva.

**Tarefa 10101:**

**Tarefa 10102:**

**PROCESSO DE EXPORTAÇÃO:**

**PLANILHA EXECUTIVA APÓS EXPORTAÇÃO:**

**Tarefa 10101:** (30 ÷ 71) × 100 = 42,25%

**Tarefa 10102:** (41 ÷ 71) × 100 = 57,75%
