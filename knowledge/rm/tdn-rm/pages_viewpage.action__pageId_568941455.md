---
content_hash: fb8e763097eb113ba1dd368dfee5f5169acd5d559589aaa6e17708bf19da91c0
fetched_at: '2026-06-29T00:10:51.559762+00:00'
page_id: '568941455'
product: rm
source: tdn-rm
title: Matrícula em lote no Itinerário Formativo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=568941455
version: 15
---

Este processo está disponível somente para o Ensino Básico.

Esse processo permite realizar a matrícula em lote de um ou mais alunos em um ou mais itinerários formativos e suas respectivas disciplinas. Para executar o processo no TOTVS Educacional acesse **Matrícula e Avaliação > Matrícula > Mais > Matrícula no itinerário formativo em lote.**

A **pré-condição** para **execução** do processo é que o aluno esteja matriculado em período letivo ativo em uma turma com matriz curricular que possua itinerários formativos vinculados.

Campos obrigatórios

* Período letivo.
* Situação de matrícula.
* Itinerário formativo.

Ao abrir o processo será exibido **três grids** e um componente de filtro, segue abaixo.

* A **primeira grid** será apresentada as  disponíveis do contexto. As que forem selecionadas serão utilizadas no filtro de alunos, ou seja, serão buscados os alunos cuja a situação de matrícula no período letivo seja igual as que forem selecionadas.
* A **segunda grid** é de , serão exibidos todos que possuem disponibilidade, ou seja, é necessário que a  no qual o itinerário formativo está vinculado possua uma  para o período letivo selecionado. Além disso, este itinerário deverá ter  para matrícula. Vale lembrar que um mesmo  poderá estar vinculado a mais de uma  por isso se existir no mínimo uma  uma alguma parametrização por curso o mesmo será exibido na grid, caso contrário não será exibido.
* A **terceira grid** são as disciplinas que possui oferta no período letivo selecionado. Somente será exibidos as disciplinas que pertencem aos itinerários formativos selecionados na grid anterior, independente dos **filtros** abaixo, ou seja, neste momento não feito nenhuma checagem se os alunos selecionados pelo **filtro**logo abaixo batem com as matrizes aplicadas das turmas/disciplinas selecionadas. Esta validação será feita durante a execução do processo. **Nunca** um aluno de uma matriz aplicada X será matriculado uma turma/disciplina de matriz aplicada Y, caso isso for acontecer o processo descartará a turma/disciplina e passará para a próxima selecionada. Diante deste cenário uma mensagem conforme abaixo será exibida no log do processo.

É importante ressaltar que é possível filtrar as turmas/disciplinas pelas colunas da grid, clicando no ícone .

Para **execução** do processo selecione um **período letivo**, uma ou mais **situações de matrícula**, uma ou mais **itinerários** e uma ou mais **disciplinas** do itinerário.

A seleção dos alunos a serem matriculados pode ser feita utilizando a opção de **filtro genérico**, por **Período Letivo/Matriz Aplicada** ou por **Consulta SQL**. Vale lembrar que a seleção de filtro é **opcional**.

O processo somente irá realizar a matrícula nas disciplinas do itinerário formativo e no próprio itinerário formativo.

Execução fracionada do processo - Fracionamento de job

O processo poderá ser executado em três camadas com ou sem de jobs, para executar com o  é necessário configurar o mesmo utilizando a classe de job **EduMatriculaItinerarioFormativoEmLoteSliceableData**:

---

**[Novo Ensino Médio](https://tdn.totvs.com/x/C3R9IQ)**

* [Itinerário Formativo](https://tdn.totvs.com/x/gjmeI)
* [Itinerário Formativo da Matriz Curricular](https://tdn.totvs.com/x/ThVxIQ)
* [Turma/Disciplina do Itinerário Formativo](https://tdn.totvs.com/x/jBVxIQ)
* [Parametrização por Curso](https://tdn.totvs.com/x/x-xbGQ)
* [Disponibilidade do Itinerário Formativo](https://tdn.totvs.com/x/VQx9IQ)
* [Matricular Aluno](https://tdn.totvs.com/x/4vtbGQ)
