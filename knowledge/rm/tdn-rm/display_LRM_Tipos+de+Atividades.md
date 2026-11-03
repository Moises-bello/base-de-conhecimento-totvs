---
content_hash: 0b70c398fe1fe700f45ed778b5b2bbd5d12b342360f9ca2f14365b5def8f225f
fetched_at: '2026-06-29T00:08:09.865258+00:00'
page_id: '240293497'
product: rm
source: tdn-rm
title: Tipos de Atividades
type: documentation
url: https://tdn.totvs.com/display/LRM/Tipos+de+Atividades
version: 3
---

## Tipos de Atividade

Para entender o movimento de ensino, são consideradas três tipos de Atividades:

**1 - Disciplina**

São atividades realizadas dentro de sala de aula. (aulas a lecionar) e são ofertadas ao público externo,  isto é, há matriculas de alunos nesta atividade e é alocado um ou mais professores para pagamento.

Base de cálculo : Para cada Disciplina multiplica o **salário hora aula** x **carga horária semanal** x f**ator mensal**, normalmente (4.5)

Carga horária semanal de cada atividade é igual a Horas aulas semanais x fator (4.5)

Podem ou não compor o salário contratual do professor

**2 - Atividades Extras**

São atividades realizadas fora de sala de aula e NÃO são ofertadas ao público externo.

A atividade extra não está ligada diretamente a grade do aluno. É uma atividade exclusiva do professor, ministrada por ele. Toda atividade extra é vinculada a um grupo de atividade que  
será cadastrado anterior a atividade.

Estas atividades podem compor ou NÃO o salário do professor. Essa informação pode ser definida no Grupo de Atividade, na própria atividade extra ou na vinculação da atividade extra com o professor.

Exemplo :  (Coordenação, Monitoria, Correção de provas, etc) .

No grupo de atividade você deve selecionar os campos utilizados no cálculo para que seja possível preencher essas informações, ou seja, selecionar o campo 'Atividade remunerada' e 'Carga horária'.

Base de cálculo : Para cada atividade extra multiplica o valor da hora  x carga horária  x fator mensal(4.5)

**Localização no Produto:** TOTVS Educacional - Currículo e Oferta - Professores: Atividade Extra ou Grupo de Atividade

**3 - Atividades Complementares**

O centro de custo na atividade ofertada é buscado do grupo de atividade que é informado na modalidade durante o cadastro da atividade ofertada. Esse grupo de atividade é o mesmo cadastrado para a atividade extra. Todo o valor a ser calculado para o professor no TOTVS Folha de pagamento por ministrar esta atividade ofertada será gerado para este centro de custo.

São as atividades que o professor realiza para complementar sua carga horária (Ofertadas pela secretaria), realizadas fora de sala de aula.

Estas atividades normalmente NÃO compõe o salário do professor.

Exemplo : (Seminários, palestras, pesquisas,  que são remuneradas porém NÃO compõe salário.

Base de cálculo : Para cada atividade complementar  multiplica o valor da hora  x carga horária  x fator mensal (4.5)
