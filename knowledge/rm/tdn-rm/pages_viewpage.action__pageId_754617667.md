---
content_hash: 9a3331e23d45098c4d52baecf76c79a16729184589a3d4cdb14c95a2a7fd8be5
fetched_at: '2026-06-29T00:11:33.237724+00:00'
page_id: '754617667'
product: rm
source: tdn-rm
title: Mudança de turma de itinerário formativo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=754617667
version: 8
---

## Geral

Para que a turma de origem que tenha turma/disciplina matriculada da itinerário formativo seja feita a mudança de turma alguns regras deverão ser obedecidas.

### Mudança de turma de itinerário formativo

Para que a turma de origem que tenha turma/disciplina matriculada da itinerário formativo seja feita a mudança de turma alguns regras deverão ser obedecidas.

#### Mudança de turma mantendo o mesmo turno (mesma matriz aplicada\*)

1. Toda turma/disciplina de itinerário formativo, matriculada e com a situação de matrícula que conta como aluno na turma/disciplina, da turma de origem deve existir na turma de destino. Caso contrario a operação de mudança de turma, na sua totalidade, não deve ocorrer e deverá informar no log. Exemplo: a turma de origem tem duas disciplinas de itinerário IT1 e IT2, sendo que o aluno está matriculado nas duas. A turma de destino tem apenas uma disciplinas de itinerário IT1. Com isso ao mudar a turma não será possível, porque o destino tem apenas IT1. O processo todo será cancelado, nada será alterado. Entretanto, se o parâmetro **permite mudança parcial de turmas/disciplinas de itinerário formativo** estiver marcado, será feito a mudança de turma. No exemplo supracitado, a disciplinas IT1 da origem terá sua situação de matrícula alterada e a mesma matriculada na turma de destino.
2. Quando a turma de destino é somente uma turma de itinerário formativo ela jamais assumirá o campo turma na matrícula do período letivo do aluno. Exemplo: o aluno está matriculado em uma turma que tem disciplinas normais e de itinerário. A turma destino tem apenas disciplinas de itinerário. Ao mudar a turma, ela será feita, porém a turma da matrícula do período letivo não será alterada.
3. Para que uma turma normal seja alterada, basta que apenas uma turma/disciplina exista no destino, todavia para o itinerário todas ativas devem existir, exceto se o parâmetro **permite mudança parcial de turmas/disciplinas de itinerário formativo** estiver marcado.
4. A mudança de turmas/disciplinas de itinerário não deve incluir disciplinas novas para o aluno, caso elas existam no destino, apenas o que é relacionado com a turma de origem. Exemplo: a turma de origem tem duas disciplinas de itinerário IT1 e IT2, sendo que o aluno está matriculado nas duas. A turma de destino tem IT1, IT2 e IT3. Com isso, ao efetuar a mudança de turma a disciplina IT3 não será matriculado para o aluno, apenas as que possuem sua correspondência na origem.

##### Aluno matriculado na turma que contém disciplinas normais e de itinerário formativo

* Turma destino contém disciplinas normais e de itinerário formativo: a mudança de turma irá ocorrer para as turmas normais e de itinerário formativo, conforme os critérios e parâmetro já citados acima.
* Turma destino contém apenas disciplinas normais (turma que não contém turma/disciplina relacionada a nenhum itinerário): a mudança de turma irá ocorrer para disciplinas normais alterando a turma da matrícula do período letivo do aluno e  será mantido inalterada as matrículas nas turmas/disciplinas de itinerário da origem.
* Turma de destino contém apenas disciplinas de itinerário formativo: a mudança de turma irá ocorrer para as disciplinas de itinerário formativo sem alterar a turma da matrícula do período letivo do aluno e mantém inalterada as matrículas nas disciplinas normais na origem.

##### Aluno matriculado em uma turma distinta com as disciplinas normais, e em outras turmas de itinerário formativo

* Será apresentado uma grid para fazer o de-para de origem e destino das turmas de itinerário formativo do aluno. Ao preencher estamos sinalizando a mudança de turma, para os que não forem preenchidos, permanecem como estão. Vale ressaltar que todas as regras citadas para a mudança de turma que envolve disciplinas de itinerário, também valem quando a grid é preenchida. Esta grid somente é exibida se o aluno possui matrícula em disciplinas de outra turma que não seja a turma do período letivo.
* As turmas que serão apresentadas na grid, são todas as turmas de origem que contenham pelo menos **uma** disciplinas de itinerário matriculada, porém a única turma que não irá aparecer neste grid é a turma que o aluno estiver matriculado no período letivo.
* A grid de-para de origem e destino poderá não ser preenchida em sua totalidade, indicando assim, que não ocorrerá mudança de turma para os itinerários das turmas de origem exibidas na grid.
* É obrigatório o preenchimento da grid ou da turma destino do período letivo.
* Caso o parâmetro **permite mudança de turma sem realizar mudança de turmas de itinerário formativo** estiver marcado, a grid ficará desabilitada.

##### Permite mudança parcial de turmas/disciplinas de itinerário formativo

Este parâmetro tem a finalidade de quebrar a regra de totalidade de disciplinas de itinerário na origem e destino, ou seja, com ele habilitado será possível mudar a turma de itinerário mesmo que no destino não se tenha todas as disciplinas de itinerário da origem, com isso, as disciplinas que não possuem a sua correspondência no destino, permanecerão inalteradas. Outro detalhe é que, ao marcar este parâmetro não será possível marcar o parâmetro **permite mudança de turma sem realizar mudança de turmas de itinerário formativo**.

##### Permite mudança de turma sem realizar mudança de turmas de itinerário formativo

Parâmetro responsável por desconsiderar toda turma/disciplina de itinerário na origem, ou seja, ao executar o processo todas as turmas/disciplinas de itinerário formativo permanecerão inalteradas em sua origem.

#### Mudança de turma para turma de outro turno (outra matriz aplicada\*)

Caracteriza em uma nova matrícula no período letivo, caso não exista, com isso para um aluno matriculado em uma turma que contém turmas disciplinas normais mais de itinerário, a mudança só irá realizar caso a turma de destino tenha no mínimo uma turma disciplina normal e todas as turmas disciplinas de itinerário ativas. As mesmas turmas disciplinas de itinerário formativo de origem precisam esta cadastradas na turma de destino, caso contrário o processo não é realizado exibindo uma mensagem contento a explicação do erro.

As regras abaixo valem apenas para o processo de mudança de turma por aluno, não são válidas para o processo de mudança de turma em lote:

* Aluno matriculado em uma turma distinta com as disciplinas normais, e em outras turmas de itinerário formativo é necessário realizar a relação de "de para" no outro turno (outra matriz aplicada\*), toda origem deve ser preenchida com uma turma de destino no outro turno (outra matriz aplicada\*). Caso uma turma não seja seleciona o passo (etapa) não avança.
* Ao selecionar uma turma com o turno (matriz aplicada\*) diferente os parâmetros: ''**permite mudança de turma sem realizar mudança de turmas de itinerário formativo**'' e "**permite mudança de turma sem realizar mudança de turmas de itinerário formativo",** ficaram desabilitados**.**

**\*Matriz aplicada:**junção do curso, habilitação, matriz curricular e turno.
