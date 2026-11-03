---
content_hash: 8edb193015b3ee313ab1cae59698e740d3c8ebb28c8b070a94e87347d79024c7
fetched_at: '2026-06-29T00:09:28.118143+00:00'
page_id: '423938661'
product: rm
source: tdn-rm
title: Alteração do Campo "Tem Distribuição Gerencial"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938661
version: 5
---

Para que os valores lançados em determinadas contas contábeis possam ser rateados em contas gerenciais, no momento da inclusão das contas contábeis o campo *Rateio* deve ser marcado e, neste momento, um rateio padrão (default) pode ou não ser informado. O campo *Rateio* só fica disponível no momento da inclusão da conta. Depois que a conta já tiver sido incluída, o campo fica desabilitado, não sendo possível mais marcá-lo nem desmarcá-lo.

O processo **Alteração do campo 'Tem Distribuição Gerencial'** possibilita que a situação gerencial de determinadas contas contábeis possa ser alterada mesmo depois que estas contas já tenham sido incluídas.

Existem dois tipos de alterações disponíveis:

* Deixará de ter distribuição gerencial
* Passará a ter distribuição gerencial

Quando se usa o processo para passar a ter distribuição gerencial deve-se obrigatoriamente informar o rateio padrão (default), sempre fechando em 100%. Deve-se observar também que para contas contábeis globais somente contas gerenciais globais podem ser utilizadas.

Uma vez executado o processo para deixar de ter distribuição ou para passar a ter distribuição, o sistema altera automaticamente todos os lançamentos da base que estiverem utilizando tais contas, excluindo os rateios ou os incluindo automaticamente.
