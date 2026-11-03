---
content_hash: 6a097a6ef4e6e73418983d964fead5f776b155fde80e8979b589c19339eb7081
fetched_at: '2026-06-29T00:09:31.901466+00:00'
page_id: '425458778'
product: rm
source: tdn-rm
title: Cadastro de Competências
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458778
version: 4
---

---

A instituição de ensino superior (IES) poderá oferecer aos seus alunos certificados por Competência.  
Este tipo de certificado consiste no seguinte. A IES cria certificados diversos, informa como será a avaliação destes e cada aluno que cumprir os requisitos deste, terá direito aquela competência.  
   
Exemplo: Digamos que exista na IES uma competência de nome "Gerente Projetos Júnior", a qual todo e qualquer aluno que cumprir uma carga horária de 100 horas dentre um grupo de disciplinas(que a instituição define) terá direito a ele. Logo se um aluno de um curso qualquer tiver cumprido tais requisitos, ele terá direito a este Certificado.  
   
Lembrando que o Certificado por competência, não tem ligação com Curso ou Matriz Aplicada. Ele funciona por metas, ou seja, cumpriu os requisitos, está apto ao mesmo.  
   
Cada competência poderá ter um tipo de avaliação diferente:

1. Nº **mínimo** de créditos;

2. Carga horária **mínima** (CH);

3. Nº **mínimo** de disciplinas.

Em cada competência, a IES poderá definir quais disciplinas fazem parte deste grupo. Estas disciplinas são cadastradas no anexo de Disciplinas, é um cadastro simples, onde o usuário localiza a disciplina baseado no cadastro de disciplinas do sistema e faz o vinculo com a competência que está cadastrando.  
   
A partir daí, basta que o aluno cumpra o necessário estipulado no tipo de avaliação para que tenha a competência, **não necessariamente terá que cursar todas as disciplinas vinculadas nela**.  
   
É possível fazer a analise dos dados obtidos pelo aluno na competência utilizando Fórmula para cálculo.  
   
A fórmula é utilizada para saber na digitação dos dados obtidos pelo aluno referentes ao cumprimento dos requisitos para a certificação. A fórmula é utilizada para calcular se o aluno está apto a receber o certificado daquela competência em questão ou não.

As funções do Educacional disponíveis para utilização da fórmula são:

**TotalDiscCompetencia** - Total de disciplinas o aluno já cumpriu em uma Competência

**TotalCreditosCompetencia** - Total de créditos que o aluno já cumpriu em uma Competência

**TotalCHCompetencia** - Total de CH que o aluno já cumpriu em uma competência

Importante

As demais funções de fórmula do Educacional não funcionam para este cadastro. Somente as funções listadas acima.

 O resultado da fórmula deve ser S ou N *Tipo S = está apto* *Tipo N = Não está apto*
