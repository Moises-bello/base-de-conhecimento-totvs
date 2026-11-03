---
content_hash: 4685d5e4ee56e11e3fd222303d3e98679bb0d4617a8bee6ef96af447cf02e08c
fetched_at: '2026-06-29T00:09:38.136046+00:00'
page_id: '425918497'
product: rm
source: tdn-rm
title: Registrar comparecimento em chamadas
type: documentation
url: https://tdn.totvs.com/display/LRM/Registrar+comparecimento+em+chamadas
version: 4
---

Este processo será executado a partir da visão de "processos seletivos". Ele deverá ser executado para que o sistema seja capaz de determinar o número de vagas disponíveis à medida que as chamadas forem realizadas. Por meio dele é possível que o usuário indique, dentre os convocados, quem realmente compareceu para ocupar a vaga a qual se candidatou.

Quando a integração com o RM Classis é utilizada para realização de matrículas, a execução desse processo torna-se desnecessária. O RM Classis possui meios próprios para atualizar o status de chamada dos candidatos na medida em que as matrículas forem efetivadas.

Na seqüência será apresentada uma lista com todos os candidatos da área ofertada e com o status "Em Chamada", "Compareceu à Chamada" e "Não Compareceu à Chamada". O usuário deverá, então, selecionar todos os candidatos que compareceram à chamada e deixar desmarcados os que não compareceram. Os que ficarem marcados terão seu status alterado para "Em Chamada" mesmo que já estejam nessa situação. De forma similar, os que ficarem desmarcados terão seu status alterado para "Não Compareceu à Chamada".

Após concluir o processo será exibido um Log. notificando o resultado do processamento.

**Pré-requisitos do processo:**

Deverão existir chamadas realizadas para uma ou mais áreas do processo seletivo em questão.

Observações:

Informações

Caso o processo seletivo utilize controle de vagas que permita candidatos excedentes, ao alterar o status de opção de um candidato para "Não compareceu a chamada", o primeiro candidato da lista de excedentes será alterado de excedente para inscrito, ou seja, para a quantidade de candidatos que tiverem o status de opção alterado para "Não compareceu a chamada" será liberado o número de inscrições para tornar o candidatos excedentes em inscritos conforme a quantidade de vagas liberadas.
