---
content_hash: eeb684f14a4c7f99f0a8f65cffdbe78fb5002d53d3e456f5b1cc738586f81598
fetched_at: '2026-06-29T00:11:28.433421+00:00'
page_id: '731215106'
product: rm
source: tdn-rm
title: 03 - Gestão de turmas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=731215106
version: 47
---

Nesta etapa é possível realizar o gerenciamento das turmas que foram criadas a partir das demandas de vagas para as disciplinas.

**OBS**. Agrupar demanda, Desagrupar demanda, Realocar demanda, Desalocar demanda Adicionar gerencial/gerenciada, Remover gerencial/gerenciada, Alterar capacidade e Desalocar turmas. Todas essas ações emitirão validação caso o idhabilitacaofilial já possua oferta gerada.

A ação de "Adicionar disciplinas" também foi bloqueada quando a disciplina adicionada é do mesmo idhabilitacaofilial que já tem oferta gerada.

### Filtros disponíveis

Os filtros **curso**, **habilitação**, **matriz** e **turno** funcionam da mesma forma que no passo ,  para mais informações acesse: [funcionamento dos filtros](https://tdn.totvs.com/display/LRM/01+-+Executar+demanda#id-01Executardemanda-Funcionamentodosfiltros).

#### Período

O filtro de período ficará habilitado a partir do momento que se seleciona algum curso e ele será preenchido com os períodos de todas as habilitações e matrizes ativas do respectivo curso.

#### Disciplina

O filtro de disciplina fica sempre disponível para seleção, e é um campo lookup com multi-seleção de dados. Ele irá refletir as respectivas disciplinas das matrizes ativas a medida em que forem selecionadas as informações de curso, habilitação, matriz, e período.

#### Status,

O filtro de status ficará sempre disponível para seleção e é um campo que será possível selecionar apenas 4 opções.

* Todos os status
* 1 - abaixo do esperado
* 2 - dentro do esperado
* 3 - acima o esperado

Mais abaixo está explicando cada status deste.

#### Turma

O filtro de turma também ficará sempre disponível para seleção e é um campo lookup com multi-seleção. Ele irá refletir as respectivas turmas que foram geradas para o passo de  a medida em que forem selecionadas as informações de curso, habilitação e matriz.

Ao preencher os filtros e clicar em Selecionar, serão exibidas no grid as informações das turmas geradas na etapa de . Vale ressaltar que o nome da disciplina **sempre** será o nome completo dela.

A coluna de status da turma pode apresentar os seguintes valores:

* - abaixo do esperado, significa que a demanda de vagas para a turma é menor que a capacidade mínima de alunos para a turma.
* - dentro do esperado, significa que a demanda de vagas para a turma é maior ou igual à capacidade mínima e menor ou igual à capacidade máxima de alunos para a turma.
* - acima do esperado, significa que a demanda de vagas para a turma é maior que a capacidade máxima de alunos para a turma.

A capacidade mínima e máxima de alunos para uma turma corresponde aos valores informados nos campos Mín. alunos e Máx. alunos do modelo de turma selecionado na geração da turma.

Mesmo com a alteração desses valores no modelo de turma posteriormente, as turmas que já foram geradas utilizando o respectivo modelo de turma continuarão com os valores de capacidade mínima e máxima de alunos que o modelo de turmas possuía quando foram geradas.

A coluna Demanda/Capacidade contém a informação da demanda de vagas para a turma e a capacidade máxima de alunos para a turma.

O botão adicionar disciplinas, permite cadastrar disciplinas que não foram geradas pelo processo de executar demanda. Pois as mesmas não tinham sido ofertadas nos período anterior.

**OBS: Ter a permissão atribuída corretamente ao usuário.**

Ao selecionar o cadastro por disciplina da matriz curricular, só serão exibidas matrizes que estão com o status Atual ou Ativa.

**OBS: A ação de "Adicionar disciplinas" também será bloqueada quando a disciplina adicionada é do mesmo idhabilitacaofilial que já tem oferta gerada.**

No modelo de turmas só serão listados os modelos para disciplinas que contenha matriz curricular.

Ao ser criada a turma dessa disciplina, o número de aulas semanais da turma será herdado do cadastro da disciplina da matriz curricular referente.

Como a disciplina livre não possui Curso, Habilitação e Matriz, no seu cadastro é obrigatório informar o turno e a demanda regular.

No modelo de turmas só serão listados os modelos para disciplinas livres.

Ao ser criada a turma dessa disciplina, o número de aulas semanais da turma será herdado do cadastro da disciplina referente.

Segue mediante permissão as ações disponíveis para as turmas criadas:

* [Atualização de dados](https://tdn.totvs.com/pages/viewpage.action?pageId=910000300)



* [Adicionar gerencial/gerenciada](https://tdn.totvs.com/pages/viewpage.action?pageId=789400337)
* [Remover gerencial/gerenciada](https://tdn.totvs.com/pages/viewpage.action?pageId=789402645)
* [Adicionar Subturma](https://tdn.totvs.com/display/LRM/Adicionar+Subturmas)
* [Remover Subturma](https://tdn.totvs.com/display/LRM/Remover+a+Subturma)
