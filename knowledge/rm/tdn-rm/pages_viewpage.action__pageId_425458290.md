---
content_hash: 79b7bc4be435d6ebbb4382820318ec3233eca593fce93c66103d42cb3194fc9b
fetched_at: '2026-06-29T00:09:29.804759+00:00'
page_id: '425458290'
product: rm
source: tdn-rm
title: Alterar forma de inscrição do candidato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458290
version: 4
---

Este processo será executado a partir da visão de "inscrição dos candidatos". Toda inscrição possui uma forma de inscrição e um lançamento gerado. Com este processo será possível alterar a forma do candidato. Ao executar o processo os campos abaixo deverão ser informados:

* Forma de inscrição: informe a nova forma de inscrição. Nas opções não poderá aparecer forma de inscrição atual do candidato.
* Motivo: Informe o motivo pelo qual a inscrição teve sua forma de inscrição alterada para utilização do histórico de alteração de forma de inscrição.

Para inscrição com lançamento não cancelado no RM Fluxus, o processo tentará realizar o cancelamento do mesmo. Será possível cancelar lançamento somente em aberto, ou seja, não baixado. Será permitido alterar a forma de inscrição somente após este cancelamento. Assim que este processo for executado, a inscrição do candidato estará com a nova forma de inscrição.

Se a nova "Forma de inscrição" escolhida possuir 100% de desconto e a área de interesse ofertada possuir a opção "Incide desconto" marcada, então o status da inscrição passará a ser "Candidato (inscrição confirmada)".  Se não, o novo lançamento gerado será com valor maior que zero e o status da inscrição passará a ser "Inscrito (pendente de confirmação)".

Se o status de inscrição do candidato estiver como excedente (controle de vagas), a alteração de forma de inscrição será feita, caso exista taxa de inscrição e descontos, será gravado o desconto da forma de inscrição para que no momento que o candidato excedente ganhar uma vaga o lançamento seja gerado com os valores corretos.

**Pré - requisitos do processo**:

1. O processo seletivo para o qual a inscrição foi realizada deverá ter mais de uma forma de inscrição.
2. As formas de inscrição disponíveis deverão estar no período de inscrição.
