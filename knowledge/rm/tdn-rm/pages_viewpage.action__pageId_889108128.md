---
content_hash: cfef0ec11c8d3ac86b08e2917354571a15a5e6116403d6cf8a10379e66d33caf
fetched_at: '2026-06-29T00:12:01.197971+00:00'
page_id: '889108128'
product: rm
source: tdn-rm
title: Detalhamento de Cálculos -
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=889108128
version: 2
---

---

* **Insumos**
  + Quantidade Total do Insumo na Tarefa: Quantidade a ser executada na tarefa X Horas necessárias do insumo na tarefa;
  + Horas necessárias para realização da tarefa no período da Folha Tarefa: Deve considerar o calendário do projeto e parametrização de sábados, domingos e feriados.
    - (Dias úteis da Folha Tarefa X Quantidade Total do Insumo na Tarefa) / Dias úteis da Tarefa.
  + Capacidade Real: Para o cálculo da capacidade real do insumo, o sistema levará em consideração, em primeiro momento, o Calendário do Recurso da Tarefa. Caso não esteja preenchido irá considerar o Calendário da Atividade, aba "Mão de Obra", que retornará quantos turnos estão sendo considerados, no período, para a execução da tarefa e a quantidade de dias úteis (dias úteis - dias parados) programados para a tarefa selecionada no período. Caso a aba "Mão de Obra" não esteja preenchida, o sistema irá verificar na aba "Geral".  Caso não encontre informações, será verificada a jornada do próprio insumo e pôr fim a jornada informada nos parâmetros do projeto. Ao verificar a capacidade, será consultada a existência da equalização de insumos. Caso exista percentual de horas adotado, para o referente insumo, então a capacidade será calculada considerando-se o referido valor que consta na equalização (o campo “H.E. Adotado %”), podendo ser alocada a quantidade de horas extras até o limite máximo definido na equalização, se necessário. Caso não exista equalização ou o seu percentual seja zero significa que não será permitido à utilização de horas extras do insumo na tarefa;
  + Quantidade Alocada: Soma de toda quantidade alocada para o insumo da equipe na tarefa item da Folha Tarefa;
  + Saldo: Diferença entre Horas necessárias para realização da tarefa no período da Folha Tarefa e a Quantidade Alocada;
    - Horas Necessárias - Quantidade Alocada.
* **Tarefas**
  + Diferente dos insumos da tarefa, onde os valores são baseados em homem-hora, os valores das tarefas para o anexo de Alocação de Mão de Obra serão definidos em relação à unidade da tarefa, tendo como exemplo uma tarefa que possui unidade “M3” e insumos com unidade “HH”;

    - Quantidade Alocada no Item: Horas totais de mão de obra alocadas no item da Folha / Necessidade total de mão de obra da tarefa;
    - Quantidade Total Necessária na Folha Tarefa: (Dias Úteis da Folha \* Quantidade da Tarefa) / Dias Úteis da Tarefa;
    - Saldo no Item: Quantidade Total Necessária na Folha Tarefa - Quantidade Alocada no Item;
    - Saldo Total da Tarefa: Quantidade da Tarefa – Quantidade Total Alocada para a Tarefa.
