---
content_hash: dc766ceea047ee641717d496bde551e8f8dc6f837701ed6ac5ebff5b20ed0eba
fetched_at: '2026-06-29T00:09:32.431078+00:00'
page_id: '425458847'
product: rm
source: tdn-rm
title: Mudar Turma/Turno
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458847
version: 22
---

A partir das versões **12.1.2205.219, 12.1.2209.163 e 12.1.2302**, este processo passou por uma reestruturação de layout e incremento de funcionalidade referente ao **itinerário formativo** (ensino básico).

## Geral

O processo de mudança de turma/turno consiste em alterar a matrícula de um aluno no período letivo, mudando a turma atual para uma nova turma, sendo que as turmas em questão possuem o mesmo turno. Este processo permite fazer a matrícula nas disciplinas da nova turma e levar para estas disciplinas as notas e faltas já existentes nas disciplinas da turma anterior.

Este processo irá gravar o número do diário no histórico de alteração de matrícula no período letivo, caso a opção **numerar aluno automaticamente** esteja marcada nos parâmetros educacionais da matrícula.

Na realização do processo, **ocorrerá o cancelamento** do contrato financeiro se a situação de matrícula no período letivo de origem estiver parametrizada para cancelar o contrato.

Para os casos em que o contrato de origem será cancelado e consequentemente os lançamentos em aberto, e se o sistema estiver parametrizado para **Cancelar Remessa automaticamente ao cancelar o lançamento financeiro quando o boleto estiver com status Remetido ou Registrado**, os lançamentos em que o boleto esteja com status igual a remetido ou registrado terão a remessa cancelada e será apresentado uma mensagem de alerta no log do processo.

## Ensino básico

Além de efetuar a mudança de turma é possível efetuar a mudança de turno do aluno.  
Ao mudar de turno será criada uma nova matrícula no período letivo para o aluno e para esta será feita a matrícula nas disciplinas. Nesse cenário, a situação de matrícula da nova matrícula no período letivo será a mesma da matrícula da turma de origem, a situação de matrícula do período letivo da turma antiga será alterada para a configurada no campo **Origem** do grupo **Situação de matrícula do período letivo**, já a situação de matrícula das disciplinas de destino é definido pelo parâmetro do processo **Situação de matrícula das disciplinas após a mudança de turma**.  
Caso não seja feita mudança no turno da turma, não será criado um novo registro de matrícula no período letivo. Nesse cenário, as disciplinas da nova turma serão inseridas na matricula do período letivo do aluno com o status definido na **Situação de matrícula das disciplinas após a mudança de turma,** no campo "Destino" e as disciplinas da turma antiga terão seu status alterado para a situação definida no campo "Origem".

O grupo **Situação de matrícula do período letivo** somente será exibido quando a turma de destino for de um turno diferente do turno da turma da matrícula do período letivo e se for do contexto de ensino básico.

### Mudança de turma de itinerário formativo

Para mudança de turma de disciplinas de itinerário formativo .

### Data de matrícula das disciplinas na turma destino

Parâmetro exclusivo do contexto de ensino básico e de preenchimento obrigatório. Sua função é dizer qual data será considerada na matrícula de cada turma/disciplina de destino. É possível escolher uma das três opções disponíveis.

* Data de matrícula da disciplina na turma origem: as turmas/disciplinas de destino irão ter como data de matrícula a mesma data da origem correspondente.
* Data de matrícula do período letivo: as turmas/disciplinas de destino irão ter como data de matrícula a mesma data de matrícula no período letivo.
* Data de execução do processo: as turmas/disciplinas de destino irão ter como data de matrícula a mesma data da execução do processo.

### Aproveitar contrato

Opção **exclusiva** do contexto de ensino básico, onde o usuário poderá definir no processo se deseja ou não aproveitar o contrato **na mudança de turno** através do parâmetro **a****proveitar contrato na mudança de turma**, mas para que o contrato seja aproveitado, as seguintes premissas abaixo devem ser obedecidas.   
1. O plano de pagamento das matrizes de origem e destino deverão ser os mesmos;  
2. O status da matrícula de origem deve estar configurado para não cancelar o contrato e o status da matrícula de destino, deve estar configurado para exigir contrato.  
3. O centro de custo e default contábil das matrizes de origem e destino deverão ser os mesmos.

Quando esta opção estiver marcada o sistema **NÃO** irá cancelar o contrato da turma original, mesmo se o centro de custo da turma **destino** for diferente da **origem**. Caso o parâmetro esteja desmarcado o processo irá prover dois campos de datas de preenchimento obrigatório, que são as datas para cancelamento dos lançamentos e contratos.

O contrato **não irá cancelar** mesmo se, ao realizar a mudança de turma com aproveitamento do contrato financeiro, a situação de matrícula no período letivo de destino não exigir contrato financeiro.

## Ensino superior

Apenas será feita a troca de turma, nunca a troca de turno, mesmo que a turma de destino possua um turno diferente da turma da matrícula do período letivo. Com isso, em nenhum momento será criado uma nova matrícula no período letivo, é feita apenas a alteração da situação de matrícula das disciplinas antigas e a matrícula nas disciplinas novas.

Neste contexto será exibido a etapa de **seleção de disciplina**, onde o usuário poderá selecionar as turmas/disciplinas que serão alteradas para o aluno. Nesta etapa poderão ser visualizadas informações das disciplinas e suas turmas/disciplinas.

### Manter turma de origem

Parâmetro **exclusivo** do contexto de ensino superior, tem por finalidade ao ser marcado, não alterar a turma da matrícula no período letivo do aluno se esta turma estiver preenchida.

## Apagar o número do diário da origem

No processo existe a possibilidade apagar ou manter o número do diário do aluno na matrícula de origem do aluno. Para apagar o número do diário é necessário marcar o item **Apagar o número do diário da origem**, o mesmo será apagado **mesmo que a data limite da numeração automática** da parametrização por curso esteja vencida.

### Ensino básico

Ao marcar este parâmetro o número do diário da matrícula no período letivo e da disciplina, ambos da origem, serão apagados.

### Ensino superior

Ao marcar este parâmetro apenas o número do diário da matrícula na disciplina, da origem, que será apagado, pois não existe este número na matrícula no período letivo.

### Copiar registros de presença diária para a turma de destino

Quando um aluno é transferido de uma turma ou disciplina para outra, o sistema faz automaticamente a **cópia das faltas (frequências)** da turma antiga para a nova.

Durante esse processo, o sistema **verifica cada falta registrada** e tenta encontrar uma **aula correspondente** na nova turma, na **mesma data**.  
Caso essa aula exista, a falta é copiada para a nova turma **mantendo o mesmo tipo de ausência ou presença** e também a **justificativa**, se houver.

Se o aluno tiver **duas faltas no mesmo dia**, o sistema também copia as duas, desde que existam **duas aulas no mesmo dia** na nova turma (por exemplo, aula 1 e aula 2).

Por outro lado, se **não existir aula correspondente** para aquela data na nova turma, o sistema **não copia a falta**, mas **registra um aviso no log** informando que a falta daquele dia **não foi copiada por não existir plano de aula correspondente**.

Esse registro serve apenas como informação — o processo **não é interrompido**, e o sistema continua copiando as demais faltas normalmente.

## Remanejar turma mista de origem com a de destino

Disponível a partir das versões: 12.1.33.275, 12.1.34.177, 12.1.2205.116 e 12.1.2209.

Caso esteja marcado ao realizar a mudança de turma a turma mista de origem é remanejada para turma/disciplina de destino e a sua situação de matrícula será mesma da turma/disciplina de destino, caso contrário a turma mista irá permanecer vinculada à turma/disciplina de origem e sua situação de matrícula será a mesma da origem.

Veja Também

---

[Boletim Técnico: Troca de Turno na Matrícula](http://tdn.totvs.com/download/attachments/187531888/EDU_BT_Troca_de_Turno_PCREQ-4201.pdf?version=1&modificationDate=1430339880000&api=v2)
