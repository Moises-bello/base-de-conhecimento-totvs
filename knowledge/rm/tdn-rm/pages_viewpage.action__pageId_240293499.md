---
content_hash: a99e72748157a00a896ff15a4528ec5316f1fba44c22d497ebc78962eb306a4e
fetched_at: '2026-06-29T00:08:09.867818+00:00'
page_id: '240293499'
product: rm
source: tdn-rm
title: Parametrização da Integração com a Folha de Pagamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=240293499
version: 4
---

**Caminho:** TOTVS Educacional - Configurações - Parâmetros - Integração - Folha

### Parâmetros Folha 1/2

* **Permitir cadastrar professor que não seja funcionário:** Para que seja possível cadastrar no sistema professores que não serão vinculados a um funcionário cadastrado no TOTVS Folha de Pagamento é necessário que este parâmetro esteja marcado nos parâmetros do sistema.
* **Utilizar valor da hora/aula:** Define se irá utilizar o valor da hora/aula definido na titulação ou no cadastro de professores da turma/disciplina.
* **Origem do Centro de Custo:** Ao buscar o rateio do salário do professor  o sistema pode considerar da turma/disciplina ou da matriz aplicada da turma/disciplina.
* **Ratear pagamento de professores da turma/disciplina por Centro de Custo:** Para trabalhar distribuindo por centro de custo é necessário marcar este parâmetro e depois definir a origem do centro de custo pelo parâmetro "Origem do centro de custo".
* ****Associar evento RM Labore à disciplina:****O parâmetro “Associar evento RM Labore à disciplina” quando marcado irá utilizar o evento cadastrado na disciplina, durante o processo de “Associação dos eventos por disciplina” no TOTVS Folha de pagamento. Quando não marcado ela irá obedecer aos eventos cadastrados durante o “Agrupamento Salarial”. Tal parâmetro trabalha em conjunto com outro existente no folha de pagamento “agrupamento salarial por disciplina”.
* ****Turmas livres utilizam o centro de custo da disciplina da turma:**** Este parâmetro é um complemento do parâmetro "Origem do Centro de Custo", pois quando é uma turma livre - turma que não possui matriz aplicada - e o sistema está marcado para utilizar o centro de custo da matriz, o sistema não sabe de onde utilizar.Com a utilização do parâmetro “Turmas livres utilizam o centro de custo da disciplina da turma”, o sistema vai utilizar o centro de custo da turma/disciplina quando for turma livre.

### Parâmetros Folha 2/2

* **Utilizar controle de alteração de registro:** É utilizado quando o usuário deseja controlar quem realizou modificações nos cadastros que podem ser controlados.
  1. **Cadastros Controlados:** Selecionar qual o cadastro que terá o controle de alteração.
  2. **Enviar email na aprovação/reprovação do controle:** Se deseja ou não enviar um e-mail para aprovação/reprovação do controle.
