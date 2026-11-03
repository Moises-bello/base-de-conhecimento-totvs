---
content_hash: 2dfed2d6f6fb8db8dea2ca1bdf2c336d9ef26eeb4d4ca88db17b46fb3e775b71
fetched_at: '2026-06-29T00:09:30.910176+00:00'
page_id: '425458559'
product: rm
source: tdn-rm
title: Associar Professores aos Horários da Turma/Disciplina
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458559
version: 7
---

O processo de associar professores aos horários da turma/disciplina possibilita ao usuário realizar o vínculo do professor a todos os horários das turma/disciplinas a partir da execução de apenas um processo.  
   
O processo permite vincular professores a horário de Turmas/Disciplinas, Turmas/Disciplinas gerenciadas, permite vincular mais de um professor ao horário e ate mesmo associar o professor desconsiderando ponto para pagamento.   
   
**Associar professor aos horários de uma turma/disciplina padrão:**

* Acesse a tela de edição da turma/disciplina e execute o processo: Associar Professores aos Horários da Turma/Disciplina.
* Mantenha todos os parâmetros desmarcados e execute o processo.
* O professor será associado a todos os horários da turma/disciplina selecionada caso exista apenas um professor cadastrado para essa turma/disciplina.
* Se existir mais de um professor cadastrado para a turma/disciplina, uma outra etapa será exibida dentro do processo para que o usuário faça a correlação entre os professores e os horários. O usuário precisará **clicar no professor e arrastá-lo para o horário desejado para fazer esse vínculo.** O contrário também é verdadeiro, caso o usuário queira remover um professor do horário, basta clicar no professor do horário e arrastá-lo para a listagem de professores.

Professores Inativos ou Demitidos

Caso o professor esteja inativo ou demitido, o mesmo não será exibido no processo de "associar professor aos horários da turma/disciplina", mesmo estando vinculado a turma/disciplina.

Se existir apenas um professor vinculado a turma/disciplina e esse professor estiver inativo ou demitido, o processo será executado com erro indicando que não existe professor e/ou horário cadastrado.

Se existir mais de um professor vinculado a turma/disciplina e um ou mais professores estiverem inativos ou demitidos, esses professores não serão exibidos na listagem carregada no processo para a realização do vínculo entre os professores e horários.

Para identificar se o professor está inativo ou demitido, acesse o cadastro do professor, anexo "filiais do professor", verifique se o campo "Ativo" está marcado ou clique na chapa do professor, caso exista, e verifique a situação dele no RH.

**Associar professor aos horários de uma turma/disciplina quando já existir professor associado.**

* Acesse a tela de edição da turma/disciplina e execute o processo: Associar Professores aos Horários da Turma/Disciplina
* Marcar o parâmetro: Associar novo professor ao horário quando já existir professor
* O professor será associado aos horários independente dos mesmos terem ou não professores já associados.

**Associar professor aos horários de uma turma/disciplina desconsiderando ponto**

* Acesse a tela de edição da turma/disciplina e execute o processo: Associar Professores aos Horários da Turma/Disciplina
* Marcar o parâmetro: Desconsiderar ponto para pagamento
* O professor será associado aos horários com o parâmetro "desconsiderar ponto para pagamento" marcado.

**Associar professores aos horários em turma/disciplina gerenciada**

* Acesse a tela de edição da turma/disciplina e execute o processo: Associar Professores aos Horários da Turma/Disciplina
* Marcar o parâmetro: Associar professores aos horários em turma/disciplinas gerenciadas
* O professor será associado aos horários da turma/disciplina mesmo ela sendo gerenciada por outra turma/disciplina
