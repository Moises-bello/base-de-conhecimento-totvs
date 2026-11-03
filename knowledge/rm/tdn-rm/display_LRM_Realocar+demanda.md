---
content_hash: d70d0e1bcbf42ab1b126c3c3fbcbb6137334facf57f4210cfabb97bca135ecb1
fetched_at: '2026-06-29T00:11:44.079666+00:00'
page_id: '809513560'
product: rm
source: tdn-rm
title: Realocar demanda
type: documentation
url: https://tdn.totvs.com/display/LRM/Realocar+demanda
version: 10
---

Permite realizar a realocação de demandas, flexibilizando a futura geração de turmas/disciplinas de acordo com a necessidade da instituição.

Para realizar a realocação de demanda, é necessário selecionar o registro que possua a demanda maior que a capacidade, conforme abaixo:

Caso o usuário tente executar a realocação para turmas de capacidade inferior a demanda, o sistema emitirá mensagem alertando dessa premissa.

Existes duas formas de realizar a realocação de demanda excedente:

Priorizar a lotação máxima das turmas

Nesta opção o sistema vai realocar a capacidade máxima de cada turma e, somente depois, pular para a próxima turma para continuar o processo.

Exemplo:

Demanda 40 / Capacidade 30

Serão criadas 2 turmas para realocação, sendo 1 turma de 30/30 e a outra turma de 10/30, totalizando os 40 alunos da demanda original.

Equalizar a demanda nas turmas

Nesta opção o sistema fará a realocação deixando a demanda mais próxima da capacidade em todas as turmas, fazendo um balanceamento entre elas.

Exemplo:

Demanda 40 / Capacidade 30

Serão criadas 2 turmas para realocação, com 20(Demanda)/30(Capacidade) , totalizando os 40 alunos da demanda original.

Após a realocação, será possível identificar, através da coluna "Ações", quais são as turmas de demanda realocada e a turma de demanda original, bem como visualizar através do detalhamento, o relacionamento entre elas:

**OBS:** As novas turmas/disciplinas geradas após realocação herdam a informação de Número de aulas por semana da turma/disciplina origem.
