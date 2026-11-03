---
content_hash: ee4e4d5b90acd8a9502a294aa91a8e6c9c43dd4b35cf1b7f9871e751911d169f
fetched_at: '2026-06-29T00:10:25.835475+00:00'
page_id: '505755944'
product: rm
source: tdn-rm
title: Movimento de Ensino
type: documentation
url: https://tdn.totvs.com/display/LRM/Movimento+de+Ensino
version: 2
---

Neste menu, será definido como será considerado o salário do professor para o cálculo do movimento de ensino.

Usa salário Hora/Jornada fixa

Quando esta flag estiver **marcada**, o sistema passa a calcular o salário do professor da seguinte forma:  
Salário = Valor Hora × Jornada contratada (sendo que a jornada é informada no cadastro do funcionário (jornada semanal), e convertida em horas mensais com base em um fator de conversão).

Se esta flag estiver **desmarcada**, o sistema calculará o salário multiplicando o Valor Hora pela jornada realizada, sem limitações contratuais.

Consiste hora contratada x Hora distribuídas

Esta flag só ficará habilitada caso a flag 'Usa salário Hora/Jornada Fixa' esteja **marcada**.

Quando esta flag estiver **marc****ada**, ela impede que o cálculo prossiga se houver **inconsistência** entre a **jornada contratada** (no cadastro do colaborador) e a **soma das cargas horárias distribuídas** nas disciplinas/turmas atribuídas ao professor.

Se esta flag estiver **desmarcada**, o sistema não fará nenhum tipo de validação entre o que foi contratado e o que foi distribuído e permitirá duas situações distintas:

* que o professor tenha menos carga horária distribuída do que o contratado e o sistema pagar integralmente, mesmo que ele não tenha aulas suficientes.
* que o professor tenha mais carga horária distribuída que o contratado e o sistema pagará apenas pela jornada fixa, podendo haver sobrecarga horária sem compensação, a não ser os eventos complementares sejam configurados manualmente.

Atualiza Jornada conforme carga horaria da atividade do professor

Quando a flag "Atualiza Jornada conforme carga horária da atividade do professor" está **marcada**, o sistema calcula e atualiza a jornada contratada do docente com base:

* Nas atividades vinculadas a ele (disciplinas, turmas, componentes curriculares);
* No número de aulas semanais atribuídas;
* Na duração de cada aula (ex: 50 min, 60 min).

Esses dados são somados para compor a jornada semanal (em horas) e, a partir disso, é calculada a jornada mensal (geralmente multiplicando por 4,5).

Se esta flag estiver **desmarcada**, o sistema não altera automaticamente a jornada do professor, as jornadas semanal e mensal utilizadas no cálculo da folha deverão ser informadas manualmente no cadastro do funcionário (ou herdada de parametrizações anteriores).

Considera jornada semanal do salário composto baseado na quantidade de aulas

Esta flag só ficará habilitada caso a flag 'Atualiza jornada conforme carga horaria da atividade do professor' esteja **marcada**.

Quando esta flag está **marcada**, o sistema considera o número de aulas e a Duração da Aula informadas no cadastro de movimento de ensino importado das atividades do tipo T - Turma/disciplina para o cálculo de movimento de ensino e irá exibir no cadastro de Salário composto e Funcionários a Jornada em quantidade de aulas semanais e mensais nos respectivos cadastros. Também será habilitado em ambos cadastros o campo Jornada (Carga Horária) com o total de horas semanais e mensais respectivamente.
