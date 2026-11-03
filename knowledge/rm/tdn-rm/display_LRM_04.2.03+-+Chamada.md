---
content_hash: 9d854fb82332d74dadcaa1ee685e39e4d13fc46a31ae02f176162dabd85bdeee
fetched_at: '2026-06-29T00:09:02.518027+00:00'
page_id: '379318398'
product: rm
source: tdn-rm
title: 04.2.03 - Chamada
type: documentation
url: https://tdn.totvs.com/display/LRM/04.2.03+-+Chamada
version: 25
---

## 04.2.03.01 - Chamada dos alunos

Essa funcionalidade permite ao professor marcar presença ou ausência por aluno em um determinado dia.

Dica

Clique nas imagens a seguir para ampliar.

Informação

A partir da release 12.1.20, a funcionalidade de "Chamada" do TOTVS Educa Mobile conta com uma inteligência para preencher a data de digitação e selecionar automaticamente a etapa com base na data atual.

Para que isso seja possível, no "Cadastro de Etapas" do sistema as datas de "início" e "término" das etapas devem estar preenchidas.

Por exemplo: temos uma etapa chamada "Etapa 01 Faltas" cadastrada no sistema com data de início para "01/02/2018" e data de término para "02/03/2018" . Quando um professor acessar a funcionalidade de "Chamada" do TOTVS Educa Mobile no dia "15/02/2018", automaticamente a etapa "Etapa 01 Faltas" virá selecionada e a data de digitação será preenchida com a data de "15/02/2018".

> *Caso exista mais de uma etapa de falta que compreenda a data atual ou etapas sem data início e/ou término, o sistema não irá carregar a etapa automaticamente e o usuário deverá selecionar a etapa desejada, assim como já era feito anteriormente.*

Informação

A partir da release 12.1.29, a funcionalidade de "Chamada" do TOTVS Educa Mobile conta com uma funcionalidade de liberação de frequência diária pelo professor.

Para que isso seja possível, o parâmetro do sistema "Justificar as faltas e liberar frequência pelo coordenador definido na turma/disciplina" deve estar DESMARCADO (TOTVS Gestão Educacional | Configurações | Parâmetros | 15.01 - Secretaria | Notas/Faltas). Ou seja, essa opção de liberar frequência diária após salvar será exibida se a instituição **NÃO** utilizar a liberação pelo coordenador, pois se esse parâmetro estiver marcado, quem faz a liberação é o coordenador e somente pelo portal através de outra opção de menu já existente.

A opção de "Salvar" funcionará conforme atualmente, porém quando a opção de liberar estiver marcada, também será marcado o campo de controle "FrequenciaDispWeb" do plano de aula (SPLANOAULA.FREQUENCIADISPWEB = 1).

Para mais informações, acesso o [documento técnico](https://tdn.totvs.com/x/LmzNI) dessa novidade.
