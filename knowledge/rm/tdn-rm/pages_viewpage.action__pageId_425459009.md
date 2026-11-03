---
content_hash: 5451ef3317b354690664adc2f64ae181e2ccd5c4596e5d010b910a846279f66f
fetched_at: '2026-06-29T00:09:33.390101+00:00'
page_id: '425459009'
product: rm
source: tdn-rm
title: Processo Matrícula de Disciplina em Lote
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459009
version: 7
---

Esse processo permite realizar a matrícula de um ou mais alunos em uma ou mais disciplinas.  
   
Para executar o processo no RM acesse: Educacional | Matrícula e Avaliação | Matrícula | Mais | Matrícula de disciplina em lote.

### Matricular em disciplinas de outras filiais

É possível executar o processo para matricular em disciplinas de outras filiais, caso a parametrização por curso permita tal operação. Para isso é necessário as seguintes pré-condições:

* Possuir um aluno matriculado em um período letivo em uma filial.
* Possuir uma turma/disciplina em outra filial cadastrada com uma disciplina que se deseja matricular.
* Cadastrar o relacionamento, nas 2 filiais, entre filiais da mesma coligada: Currículo e Oferta | Auxiliares | Relação de cadastro | Entre filiais da mesma coligada
* Configurar a parametrização por curso para permitir a matrícula em disciplinas de outras filiais: Currículo e Oferta | Parametrização por curso | Aba: Configuração de matrícula | Permite matrícula em turmas/disciplinas de filiais diferentes
* Executar o processo de matrícula em lote para matricular o aluno na disciplina da outa filial.
* Executar o teste utilizando filtro por RA, pela matriz aplicada, por consulta SQL.
* Validar a mensagem que é exibida caso a parametrização não permita a matrícula em disciplinas de outras filiais.

### Ensino Básico

Esse processo também poderá ser utilizado no ensino básico.

Importante

O processo não efetua matricula nas disciplinas do .

Caso deseja efetuar a matrícula em lote no itinerário formativo e suas disciplinas execute o processo de .
