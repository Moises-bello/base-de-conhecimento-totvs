---
content_hash: b7fef4996fc5968c014c73fb638b58fa06dc1be1bb48eb8641f3aa19c4d0abb2
fetched_at: '2026-06-29T00:09:31.273630+00:00'
page_id: '425458590'
product: rm
source: tdn-rm
title: Relatório Fixo por Etapa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458590
version: 5
---

O relatório fixo por etapa tem como objetivo extrair informações dos alunos no qual os mesmos possuem notas abaixo da média na etapa. Para este processo, os alunos serão apresentados em uma listagem que podem ser selecionados todos os  
alunos ou apenas alguns para geração do relatório.

É possível realizar configurações através da guia de configurações. As mesmas serão salvas no banco de dados para cada coligada, filial e nível de ensino.

Nas configurações se faz possível exibir/ocultar os campos do relatório, sendo os seguintes campos: Matrícula, Nome, Número do diário, código da situação de matrícula, situação de matrícula, falta, aulas dadas, resultado final, nota, conceito, etapas e somatório das notas.

Se faz válido também a exibição de etapas por código ou ordem. Caso o filtro seja por código, as etapas serão exibidas conforme o número de etapa selecionadas nas configuração. Se o filtro selecionado for por ordem, serão exibidas as etapas conforme a ordem exibida na turma/disciplina.

Na Guia Relatório, o usuário deverá informar como campo obrigatório: Filial, Período Letivo, Matriz Aplicada e como opcional, o campo Turma/Disciplina, e os parâmetros que serão ponto determinante para a extração do relatório proposto:

**1-** "Imprimir somente alunos com nota abaixo da média": Este parâmetro tem como objetivo, listar apenas alunos que possuem notas abaixo da média da etapa.

**2-** "Imprimir somente notas abaixo da média": Este parâmetro tem como objetivo, listar todos os alunos, classificados da seguinte forma:   
          **2.1** - Os alunos que possuem notas abaixo da média: Os alunos abaixo da média serão listados com as suas respectivas notas;  
          **2.2** - Os alunos que possuem notas acima da média: Os alunos acima da média serão listados sem a informação das notas.

**3**- "Imprimir notas abaixo da média com diferenciação": Este parâmetro tem como objetivo, listam todos os alunos, do mesmo critério do parâmetro listado no item 2, porém as notas abaixo da média estarão destacadas em vermelho e com \*\*\* (asterisco).
