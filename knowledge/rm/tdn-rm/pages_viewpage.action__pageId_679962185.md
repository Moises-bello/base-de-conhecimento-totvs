---
content_hash: 07647aa7b76ad33d2c327346dbd8b417f864eef156a4dea30c62bab4f49085ab
fetched_at: '2026-06-29T00:11:17.388797+00:00'
page_id: '679962185'
product: rm
source: tdn-rm
title: Excluir Lote Contábil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=679962185
version: 7
---

A atividade Excluir Lote Contábil, permite excluir os lotes informados.

Os parâmetros necessários:

* **CodColigada:** Código da coligada.
* **CodLote:** Código do lote.
* **UsuarioLogado:** Usuário logado.
* **CodSistmaSolicitouExclusao:** Identifica o sistema que solicitou a exclusão do lote contábil.
* **ExcluiLancamentosLote:** Identifica se é para excluir o lançamentos do lote. Caso este campo não estiver informado e tenha lançamentos no lote será gerada um Exceção. É importante que ao solicitar a exclusão do lote e o mesmo tenha lançamento seja apresentado ao o usuário uma mensagem de confirmação.

Segue um exemplo com a atividade configurada.
