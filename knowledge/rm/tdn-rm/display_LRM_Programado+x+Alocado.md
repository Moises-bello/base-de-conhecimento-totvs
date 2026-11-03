---
content_hash: 3e092e886301ffce5c0ca1a15af28faeafb9ef0cb8f5914fa5624eaaf0c01f8a
fetched_at: '2026-06-29T00:09:16.862712+00:00'
page_id: '421385590'
product: rm
source: tdn-rm
title: Programado x Alocado
type: documentation
url: https://tdn.totvs.com/display/LRM/Programado+x+Alocado
version: 3
---

---

Este anexo estará disponível apenas se o [parâmetro de projetos](https://tdn.totvs.com.br/pages/viewpage.action?pageId=421385196) estiver definido para que a planilha de apontamentos seja a 'Planilha de Atividades.

O objetivo desta tela é apenas a visualização detalhada da "Alocação de Mão de Obra – Programado X Alocado" - Menu | Cadastro | Mobilidade | Folha Tarefa =| Anexos | Programado x Alocado.

Essa visão será um anexo do cadastro de Folha Tarefa, para exibição de informações relacionadas com as Quantidades Programadas e Quantidades Alocadas de cada Tarefa.

Esta tela deverá apenas exibir os insumos do tipo mão de obra, que serão necessários para a execução da tarefa, ou seja, não será exibido alocações de insumos diferentes do tipo "mão de Obra".

A medida em que as equipes são alocadas em suas respectivas tarefas, será atualizado o campo de quantidade de horas alocadas por insumo; Portando aqui não será possível editar nenhum dos dados pois os mesmos ficarão disponíveis somente para consulta, apenas para a visualização de quanto já foi alocado na tarefa e o quanto ainda precisa ser alocado, ou mesmo se houve superalocação de horas na tarefa.

**Observações:**

Somente haverá visualização se já houver pelo menos um Processo completo de Alocação de Mão de Obra Realizado.  O cálculo irá não considerar Cenários inativos ou Cenários que não tenham sido alocados (equipes que estejam "Ativas").  Esta opção não estará ativa caso não haja nenhum projeto aberto.  Será exibido apenas alocações de insumos do tipo "Mão de obra".  Não Haverá "% Alocada" acima de 100%.

As Cores identificadas no campo "% Alocada" lista uma visão panorâmica do porcentagem alocada, irá variar entre tons (Vermelho, laranja e Verde).

Legenda de cores do campo "% Alocada":

Vermelho  = Menos de 25% Alocação  laranja  = Maior ou igual a 25% de alocação e Menos de 50% de Alocação.  Verde Claro  = Maior ou Igual a 50% de alocação e Menos de 75% de Alocação.  Verde Escuro  = Maior ou Igual a 75% de alocação   Até     100% de Alocação.

Exemplo:

A tarefa 001.01.01 precisa de 1000 Homem/hora para ser executada no período de uma semana (determinado pela Folha Tarefa - Data Início e Data Fim). Ao vincular a tarefa à equipe, o sistema verifica se a tarefa possui mais de um turno e verifica se existe algum membro da equipe (insumo) apto a realizar a tarefa. Esta verificação consiste em analisar o período da folha, a quantidade a ser apontada, capacidade produtiva de cada insumo e verificar se o mesmo não está alocado em algum período semelhante ao da Folha Tarefa. Caso esteja, as horas deste membro não serão consideradas no processo. Caso negativo, as horas deste membro serão consideradas para execução da tarefa. Se a quantidade de horas dos membros da equipe não for suficiente, O percentual será exibido; Exemplificando se o percentual for de 51% de uma determinada alocação,o campo "% Alocado" estará com a barra de Status em 51% e na cor "Verde Claro", indicando que a alocação é Maior ou Igual a 50% e Menor que 75%.

Na Necessidade de se alterar as informações exibidas, Ex:. Selecionar quantas equipes forem necessários para cumprimento de 100% da tarefa, o mesmo poderá retornar ao Menu | Cadastro | Mobilidade | Folha Tarefa =| ANEXOS | ALOCAÇÃO DE MÃO DE OBRA e realizar as devidas alterações.

---
