---
content_hash: fa533b35ae6d405db894e21987240b11a99a285e2d52bdd5e572bd95d8444ca1
fetched_at: '2026-06-29T00:09:33.325472+00:00'
page_id: '425458974'
product: rm
source: tdn-rm
title: Relatório Fixo por Avaliação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458974
version: 4
---

---

O relatório fixo por Avaliação tem como objetivo, extrair informações dos alunos no qual os mesmos possuem notas abaixo da média. Para este processo, o usuário terá duas condições:

**1-** Média da etapa: O cálculo será realizado pela média da etapa.  
**2-** Média da Avaliação: O cálculo será realizado pela média da Avaliação.

Os alunos serão apresentados em uma listagem que podem ser selecionados todos ou apenas alguns para geração do relatório.

Para exibir/ocultar os campos do relatório, existe opção para os seguintes campos: Matrícula, Nome, Número do diário, código da situação de matrícula, situação de matrícula, falta, aulas dadas, resultado final, nota, conceito, etapas e somatório das notas. Estas configurações serão salvas no banco de dados para cada coligada, filial e nível de ensino (Guia Configurações).

Na Guia Relatório, o usuário deverá informar como campo obrigatório: Filial, Período Letivo, Matriz Aplicada e como opcional, o campo Turma/Disciplina, e os parâmetros que serão ponto determinante para a extração do relatório proposto:

**1-** "Imprimir somente alunos com nota abaixo da média": Este parâmetro tem como objetivo, listar apenas alunos que possuem notas abaixo da média da etapa/Avaliação.  
**2-** "Imprimir somente notas abaixo da média": Este parâmetro tem como objetivo, listar todos os alunos, classificados da seguinte forma:   
**2.1** - Os alunos que possuem notas abaixo da média: Os alunos abaixo da média da etapa/avaliação, serão listados com as suas respectivas notas;  
**2.2** - Os alunos que possuem notas acima da média: Os alunos acima da média da etapa/ avaliação, serão listados sem a informação das notas.  
**3**- "Imprimir notas abaixo da média com diferenciação": Este parâmetro tem como objetivo, listam todos os alunos, do mesmo critério do parâmetro listado no item 2, porém as notas abaixo da média da etapas /avaliação estarão destacadas em vermelho e com \*\*\* (asterisco).

Obs: A exibição das notas do aluno no relatório possuem formatação, conforme o número de casas decimais definidos na disciplina da grade do aluno. Caso não seja definido o número de casas decimais, o relatório irá assumir que o número de casas decimais será zero, arredondando assim, as notas para um valor inteiro.
