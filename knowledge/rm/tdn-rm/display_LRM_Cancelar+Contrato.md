---
content_hash: ab2604868ce16b37673971772e4c49eb3f7635c5787e40a821ebe358dd1ba96c
fetched_at: '2026-06-29T00:09:33.423702+00:00'
page_id: '425459021'
product: rm
source: tdn-rm
title: Cancelar Contrato
type: documentation
url: https://tdn.totvs.com/display/LRM/Cancelar+Contrato
version: 6
---

---

O cancelamento de contrato pode ser executado através do processo **'Cancelar contrato'** disponível dentro da tela de visão de contratos ou dentro da própria tela do contrato.

Quando um contrato é **Cancelado**, o sistema não permite que mais nenhuma ação seja feita para o mesmo, porém mantem para efeito de histórico todas as informações contidas no contrato até o momento.

Assim, se o contrato já tiver sido contabilizado, os lançamentos contábeis referentes às contabilizações do contrato já realizadas até o momento não serão excluídos, porém, serão feitos automaticamente ajustes contábeis entre os valores contratados e não realizados. Para saber mais sobre este assunto .

As parcelas e bolsas existentes também serão mantidas, assim como os lançamentos financeiros e boletos das respectivas parcelas geradas, porem o usuário tem a possibilidade de cancelar neste momento os lançamentos financeiros em aberto e não vencidos. Para isto, durante a execução do processo, marque a opção *'Cancelar lançamentos em abertos e não vencidos'*. Neste momento pode-se informar ainda uma data a partir da qual esses lançamentos são cancelados.

A data de cancelamento do contrato, por default, será a data do sistema. Se desejar indicar outra data, informe-a conforme desejado.

**Observações:**

* Ao cancelar o contrato, quando também optamos por cancelar os lançamentos financeiros em abertos e não vencidos, o sistema verificará se os respectivos boletos já foram remetidos e/ou registrados nos bancos, e caso já tenham sido, o cancelamento destes lançamentos e do contrato *não* será permitido.  
  Para o cancelamento de lançamentos como estes, cujos boletos possuem status de remessa igual à ***'Remetido'*** ou ***'Registrado'*** possa ser realizado, o sistema verificará e aplicará as regras descritas para .   
  No final do processo de cancelamento de contrato será apresentado um LOG com informações sobre os contratos cancelados, assim como a relação de lançamentos cancelados e também dos boletos que tiveram a remessa cancelada.
* Contratos *cancelados* poderão ser excluídos, desde que não tenham contabilização, nem movimentos de notas ficais vinculados, nem lançamentos financeiros gerados. Se o contrato *cancelado* assim estiver, sem nenhum vínculo com outro sistema, a sua exclusão será permitida e neste caso o sistema excluirá automaticamente as suas parcelas não geradas.
* No processo de cancelamento do contrato as bolsas ativas presente no contrato serão inativas.
* Ao cancelar o contrato, a recorrência de pagamento com cartão de crédito será cancelada caso a adesão tenha sido feita. O cancelamento da recorrência será registrado em  com o motivo "Contrato cancelado".
