---
content_hash: a9d378f2c1dc8ee2a0cddb3a2ac87eb40ce5fa44ddab31ef1d0311280c146e55
fetched_at: '2026-06-29T00:11:28.427191+00:00'
page_id: '731214985'
product: rm
source: tdn-rm
title: 02 - Visualizar demanda
type: documentation
url: https://tdn.totvs.com/display/LRM/02+-+Visualizar+demanda
version: 30
---

Passo responsável por listar todas as demandas geradas de cada curso.

### Filtros disponíveis

Os filtros **curso**, **habilitação**, **matriz** e **turno** funcionam da mesma forma que no passo , para mais informações acesse: [funcionamento dos filtros](https://tdn.totvs.com/display/LRM/01+-+Executar+demanda#id-01Executardemanda-Funcionamentodosfiltros).

#### Período

O filtro de período ficará habilitado a partir do momento que se seleciona algum curso e ele será preenchido com os períodos de todas as habilitações e matrizes ativas do respectivo curso.

#### Disciplina

O filtro de disciplina fica sempre disponível para seleção, e é um campo lookup com multi-seleção de dados. Ele irá refletir as respectivas disciplinas das matrizes ativas a medida em que forem selecionadas as informações de curso, habilitação, matriz, e período.

#### Turma

O filtro de turma também ficará sempre disponível para seleção e é um campo lookup com multi-seleção. Ele irá refletir as respectivas turmas que foram geradas para o passo de  a medida em que forem selecionadas as informações de curso, habilitação e matriz.

Além do filtro, dois botões estão disponíveis, o **limpar**e o **selecionar**.O botão **limpar** efetua a limpeza dos dados que a grid trouxe e reinicia todos os filtros, ou seja, ficando na opção de todos(as) selecionado. Já o botão **selecionar** executa o filtro e faz o preenchimento da grid. Ao clicar em **selecionar** o filtro é encolhido, podendo ser expandido pelo ícone .

A grid irá conter as disciplinas que tenham no mínimo 1 vaga de demanda de períodos anteriores ou no mínimo 1 vaga de demanda regular, ou seja, se estes campos forem zero a disciplina não irá ser exibida na grid. A coluna de demanda total é a soma do valor da coluna de demanda de períodos anteriores com demanda regular. Vale ressaltar que o nome da disciplina **sempre** será o nome completo dela.

A coluna de turma, irá ser preenchida se esta disciplina possuir turma criada, quando se fala em turma criada, é uma turma criada dentro da estrutura do planejamento de oferta, ela não reflete na estrutura oficial de oferta.

Se demanda tiver sido gerada com base em alunos matriculados no período anterior, será possível clicar no número da demanda e verificar quais são os alunos demandantes.

O botão adicionar disciplinas, permite cadastrar disciplinas que não foram geradas pelo processo de executar demanda. Pois as mesmas não tinham sido ofertadas nos período anterior .

**OBS: Ter a permissão atribuída corretamente ao usuário.**

Ao selecionar o cadastro por disciplina da matriz curricular, só serão exibidas matrizes que estão com o status Atual ou Ativa.

**OBS: A ação de "Adicionar disciplinas" também seá bloqueada quando a disciplina adicionada é do mesmo idhabilitacaofilial que já tem oferta gerada.**

No modelo de turmas só serão listados os modelos para disciplinas que contenha matriz curricular.

Como a disciplina livre não possui Curso, Habilitação e Matriz, no seu cadastro é obrigatório informar o turno e a demanda regular.

No modelo de turmas só serão listados os modelos para disciplinas livres.

Para visualizar as disciplinas livres , informe no filtro por curso, a opção (TURMA LIVRE).

Para criar turmas, é necessário selecionar no grid as demandas para as quais se deseja gerar turmas e selecionar o modelo de turma que deverá ser utilizado para a geração de turmas dessas demandas:  
**OBS: Ter a permissão atribuída corretamente ao usuário.**

Ao tentar selecionar disciplinas de demandas diferentes (uma com matriz curricular e a outra livre) , o sistema não permite criar turmas.

O botão "Criar turmas" só fica habilitado após a seleção de pelo menos uma demanda no grid e a seleção do modelo de turma a ser utilizado.

Após clicar no botão "Criar turmas" o sistema enviará os dados para processamento e retornará uma mensagem informando a situação dos registros que foram enviados para processamento:

O grid será recarregado e será possível ver o código da turma criado na coluna "Turma" no grid, para a demanda cuja criação de turma já tenha sido finalizada.

Se forem selecionadas demandas para as quais já foram criadas turmas, o sistema retornará uma mensagem informando que esses registros não foram enviados para processamento:

**Por fim, após realizar o processamento da criação da turma, será executada uma rotina que irá atualizar o status dessa etapa na tabela SPLETIVOPLANETAPAS . A etapa em questão é a 3, seus status passará a ser 2 e ATIVA será atualizado de 0 para 1.   
Também será atualizada a etapa 6, conforme abaixo.**
