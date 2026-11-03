---
content_hash: 62983c90cc97b077748c59e4b230e983636723f00619bcbfc53e42d94c917ad8
fetched_at: '2026-06-29T00:11:17.377344+00:00'
page_id: '679962162'
product: rm
source: tdn-rm
title: Estornar Lançamento Contábil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=679962162
version: 8
---

A atividade Estorno Lançamento Contábil permite estornar os dados de acordo com os campos informados. As principais propriedades existentes nela são:

* **CodColigada:** Código da coligada.
* **IdOperacao (Obrigatório):** Id de operação da contabilização.
* **EstornarSempre:** Estornar Lançamentos mesmo se estiverem no Lote ZERO.
* **CodLoteEstorno:** Código do lote de Estorno. Essa propriedade deve receber um valor fixo (2020 por exemplo) ou deve estar associada a uma atividade que irá gerar o código do lote. Se o código não existir ele será criado.
* **CodUsuario:** Usuário logado.
* **DataEstorno:** Data do Estorno.
* **Complemento:** Complemento a ser informado nas Partidas do Estorno.
* **DescricaoLanEstorno:** Descrição do lançamento de Estorno.
* **UsarComplementoPartidaParaEstorno:** Indica se o serviço de estorno contábil deverá considerar o complemento da partida contábil no lançamento de estorno.
* **UsarCodHistPartidaParaEstorno:** Indica se o serviço de estorno contábil deverá considerar o código do histórico da partida contábil no lançamento de estorno.
* **CodHistPartidaParaEstorno:** Código do histórico informado para a partida de estorno. (Esta propriedade será considerada somente se a propriedade "UsarCodHistPartidaParaEstorno" estiver como true).

Segue um exemplo com a atividade configurada.
