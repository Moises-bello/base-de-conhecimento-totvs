---
content_hash: 9e0114e7dd31366ef2863d3e7a8c24fe0957b66dd6f77e0de88b95f7190984c9
fetched_at: '2026-06-29T00:09:55.671508+00:00'
page_id: '450139074'
product: rm
source: tdn-rm
title: Matrícula por Prioridade
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=450139074
version: 8
---

---

Na funcionalidade de matrícula por prioridade, podemos definir uma prioridade no sistema para que cada matrícula que possua a situação de matrícula designada como "Prioridade", seja validada e os alunos sejam matriculados conforme a ordem de prioridade parametrizada.

Para informar os parâmetros de prioridade, deve-se acessar: ***Configurações | Parâmetros | Matrícula | Movimento 3/4.***

Nesta tela, podemos informar qual a situação de matricula que indica "**Lista de prioridade**" e qual a ordem de prioridade para a realização de matrícula.

Os campos que podem e devem ser informados na **parametrização**, são:

**Ordem de Prioridade** - Define a ordem que o sistema seguirá no processo.

**Fórmulas** - Quando os itens de prioridade "**Possível formando**" e "**Aluno regular**" forem necessários, uma fórmula deverá ser informada nos campos referentes a seus parâmetros.

Essas fórmulas permitirão que o sistema realize a classificação das matrículas conforme os itens referentes.

false

As fórmulas definidas nos parâmetros de possível formando ou aluno regular precisam ter como retorno os valores **"0"** ou **"1"**, que indicarão um valor positivo ou negativo para o devido item de prioridade.

**Situação de matrícula que indica Lista de Prioridade (Obrigatório)** - Indica qual a situação de matrícula será validada como "Lista de Prioridade".

Sem este parâmetro o processo não permitirá filtrar matrículas, que por sua vez não habilitará o avanço do processo.

Para executar o processo, acesse: ***Educacional | Matrícula e Avaliação | Matrícula | Mais | Matrícula por prioridade***.

No passo de parametrização adicional do processo, é possível matricular alunos de outra turma e inserir os alunos que não estão matriculados na lista de espera.

Após a execução do processo, todas as matrículas terão suas situações de matrículas alteradas para a nova situação informada nas suas etapas. Caso tenha sido parametrizado para a utilização de lista de espera, as matrículas que não forem efetivadas serão atribuídas com a situação de matrícula definida para alunos em lista de espera.
