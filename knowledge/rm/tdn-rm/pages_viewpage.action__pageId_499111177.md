---
content_hash: 8edf1945de334738dfa718c689b82997453ec159dee96519747dbd5bdb3c16ac
fetched_at: '2026-06-29T00:10:22.792841+00:00'
page_id: '499111177'
product: rm
source: tdn-rm
title: Incluir Lote Contábil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=499111177
version: 13
---

A atividade Incluir Lote Contábil permite informar os dados do lote. As principais propriedades existentes nela são:

* **Aplicação:** Sistema de origem.
* **CodColigada:** Código da coligada.
* **CodLote:** Código do lote. Essa propriedade deve receber um valor fixo (2020 por exemplo) ou deve estar associada a uma atividade que irá gerar o código do lote. Se o código não existir ele será criado.
* **CodUsuarioLogado:** Usuário logado.
* **DataInicial:** Data inicial dos lançamentos que poderão fazer parte do lote.
* **DataFinal:** Data final dos lançamentos que poderão fazer parte do lote.
* **Descrição:** Descrição do lote.
* **DigitarCapa:** Digitar capa de lote permite limitar a data e o valor que o lote poderá receber. (Não se aplica no exemplo abaixo)
* **Valor:** Pode ser o somatório das partidas existentes nele ou caso o parâmetro "Digitar capa de lote" for informado, o campo definirá o valor máximo que o lote irá receber. (Não se aplica no exemplo abaixo)

Observação: O funcionamento dessa atividade depende da correta configuração do fluxo. Para incluir um lote é necessário a inclusão de ao menos um lançamento e partida.

Segue um exemplo com a atividade configurada.
