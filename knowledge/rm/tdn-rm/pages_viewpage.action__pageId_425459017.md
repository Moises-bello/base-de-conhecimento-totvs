---
content_hash: 51c7d6eb845468fee7fed3137f512e4271f0c8d3396e3c1848c297b187631cb6
fetched_at: '2026-06-29T00:09:33.413434+00:00'
page_id: '425459017'
product: rm
source: tdn-rm
title: Digitação de Notas de Avaliações
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459017
version: 5
---

Neste item é possível informar as notas das avaliações para alunos.

Para auxiliar no processo de digitação das notas, é possível utilizar vários filtros para seleção dos alunos.

Na digitação das notas, também é possível adicionar um comentário independente para cada aluno.

Detalhes como Situação do Aluno na Turma/Disciplina, nota da Etapa, data da Avaliação poderão ser facilmente visualizadas neste item.

No campo Somatório, o professor pode inserir o valor total da soma de todas as notas dos alunos, desta forma é possível validar se as notas foram cadastradas corretamente e garantir que não houve erro de digitação.  
   
**Observação:**

Caso haja discordância entre o número registrado no campo Somatório e o que foi digitado no campo de Nota das Avaliações, o sistema emite um alerta informando que a soma das notas das avaliações esta diferente do valor informado no campo Somatório.

Durante o processo de lançamento das notas, o sistema define algumas regras para digitação.

Digitação de notas para avaliações do tipo numérico:

* Número da nota menor que zero
* Informar nota para uma etapa que não tenha pontos definidos
* Informar nota maior que a nota máxima da etapa.

Digitação de notas para avaliações do tipo conceitual:

* Informar um conceito que não esteja previamente cadastrado no grupo de conceitos da etapa.

Após a digitação das notas dos Alunos, é possível realizar a liberação de visualização das notas para os alunos. Esta liberação não influencia no período de digitação, desta forma caso o professor libere a visualização para os alunos as notas poderão ser alteradas normalmente, desde que obedeça o período de digitação.

**Observação:**

Ao liberar a visualização de uma etapa, o sistema liberará automaticamente a visualização de todas as avaliações relacionadas a esta etapa. Para retirar a visualização desta avaliação, é necessário retirar primeiramente a visualização da etapa.

Na liberação de visualização de uma avaliação, é possível habilitar a execução de uma fórmula previamente cadastrada.

Ao salvar a alteração ou cadastro das notas, há a possibilidade de executar uma fórmula automaticamente, desde que esta opção seja habilitada nos parâmetros do sistema.

O filtro de [Situação da Matrícula] vai listar os alunos com a situação de matrícula na disciplina conforme regra abaixo:

* Se o aluno **tiver** resultado final (aprovado, reprovado, etc), este filtro vai considerar a situação final do aluno;
* Se o aluno **não tiver** resultado final, este filtro vai considerar a situação do aluno na disciplina;
