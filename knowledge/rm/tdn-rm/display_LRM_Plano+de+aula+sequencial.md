---
content_hash: fd1295cb2830254d1cdd5e824cb0339d92eec006410804a9617b46f6ebffd656
fetched_at: '2026-06-29T00:09:30.841128+00:00'
page_id: '425458546'
product: rm
source: tdn-rm
title: Plano de aula sequencial
type: documentation
url: https://tdn.totvs.com/display/LRM/Plano+de+aula+sequencial
version: 2
---

O conceito de plano de aula sequencial é bem diferente do conceito da geração plano de aula. No plano de aula convencional baseia-se nas datas do período letivo ou turma/disciplina ou até de um período estipulado, para gerar o plano de aula.

Já o Sequencial não é executado por turma/disciplina, mas sim por turma, pois o conceito dele é ter uma turma onde as disciplinas vinculadas a ela tem aulas em módulos sequenciais, ou seja, as aulas de uma disciplina só começam após o término das aulas de outra disciplina.  
    
 Então nesse caso teremos aulas de uma turma/disciplina começando sempre depois do término da anterior à ela.  
    
 Por isso, ao ser executado, este assistente faz algumas configurações nas turmas, da seguinte forma:

* Imaginemos que a TURMA 301 tem 4 disciplinas: D001, D002, D003, D004.

Cada disciplina:

* 5 horas de Carga Horária;
* 2 aulas semanais;
* Cada aula tem 50 minutos.

Então, ao gerar plano de aula sequencial **para a TURMA 301**, na ordem¹ acima, o sistema começará a geração da disciplina D001 baseado na data inicial informada no assistente ATÉ atingir a quantidade da Carga Horária². Terminando o plano de aula da D001, o sistema irá preencher as datas iniciais e finais da turma/disciplina em questão, e também de seus horários. Feito isso, ele partirá para a próxima disciplina, no nosso caso D002 e assim sucessivamente até a ultima disciplina.  
  
**Importante:** Ao gerar um plano de aula sequencial, o sistema atualiza (quando já existem) as datas iniciais e finais da turma/disciplina e também dos horários desta. Para que o usuário tenha maior ciência disto, existe um "Termo de aceite" na tela, que impede a execução do mesmo em caso do usuário não concordar, apenas uma forma de garantir que o mesmo não foi executado de forma 'equivocada'.  
  
**Notas:**

1. A ordem das disciplinas de uma turma pode ser alterado no assistente, ou seja, o usuário define qual disciplina será a primeira e assim sucessivamente;
2. Neste assistente, a Carga horária da disciplina é ponto chave, assim como a duração da aula da turma/disciplina, pois a partir destas informações é que será definido o término do plano de aula da disciplina;
