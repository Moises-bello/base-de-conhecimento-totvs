---
content_hash: 6a0fe86115bfe79e387104948fcb50ef2dc2ed9219337e9bcebe8d7916eae34e
fetched_at: '2026-06-29T00:10:31.040271+00:00'
page_id: '520659357'
product: rm
source: tdn-rm
title: Aluguel Complementar - Cancelar Aluguel Complementar
type: documentation
url: https://tdn.totvs.com/display/LRM/Aluguel+Complementar+-+Cancelar+Aluguel+Complementar
version: 7
---

Este processo permite o usuário cancelar e excluir os lançamentos do aluguel complementar do contrato de locação. Esses lançamentos suscetíveis ao cancelamento são gerados através do processo .

Para acessar o processo abra Aluguel / Contrato de Locação / Processo Cancelar Aluguel Complementar.

O processo pode ser executado para vários contratos de locação, e para cada contrato o sistema realiza o cancelamento dos lançamentos de várias medições, conforme a competência parametrizada pelo usuário.

Na execução do processo, o usuário informa a competência inicial e final. Esta competência é cadastrada pelo usuário para cada medição. O sistema então irá cancelar e excluir os lançamentos referentes a essas medições dentro do período informado.

O cancelamento dos lançamentos somente será realizado se o lançamento não estiver sido baixado.

Observações

Em caso de necessidade de cancelamento do lançamento do aluguel complementar e a sua regeração com novos dados, o usuário deverá ir no cadastro de Medição, alterar qualquer campo editável na tela conforme desejado e salvar. O sistema irá solicitar uma confirmação de regeração do lançamento. Após a confirmação, o lançamento antigo será cancelado e excluído e o novo lançamento será criado e vinculado à medição. Este procedimento não é possível de ser realizado quando o lançamento estiver baixado.

Quando há geração de aluguel complementar mínimo, ao cancelar uma parcela o evento anual do valor complementar também será cancelado e seu status voltará para não integrado.
