---
content_hash: e712364ea58d0f1797aa4f3a3b478468ff734aa402e421daf8a34babe582bc13
fetched_at: '2026-06-29T00:11:17.374860+00:00'
page_id: '679962150'
product: rm
source: tdn-rm
title: Salvar Inclusão de Lote
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=679962150
version: 8
---

A atividade de Salvar Inclusão de Lote Contábil permite gravar os dados informados do lote. As principais propriedades existentes nela são:

* **Lote referenciado:** Faz referência a atividade em que foram informados os dados do lote. Essa é um propriedade obrigatória, pois para incluir o lançamento é necessário informa o lote.

* **Aplicação:** Sistema de origem.
* **CodColigada:** Código da coligada.
* **CodLote:** Código do lote. Essa propriedade deve receber um valor fixo (2020 por exemplo) ou deve estar associada a uma atividade que irá gerar o código do lote. Se o código não existir ele será criado.
* **CodUsuarioLogado:** Usuário logado.
* **Descrição:** Descrição do lote.
* **DataInicial:** Data inicial dos lançamentos que poderão fazer parte do lote.
* **DataFinal:** Data final dos lançamentos que poderão fazer parte do lote.
* **DigitarCapa:** Digitar Capa do Lote, permite limitar a data e o valor que o lote poderá receber. (Não se aplica no exemplo abaixo)
* **Valor:** Pode ser o somatório das partidas existentes no Lote, caso o parâmetro "Digitar capa de lote" seja informado, o campo definirá o valor máximo que o lote irá receber. (Não se aplica no exemplo abaixo)

Segue um exemplo com a atividade configurada.
