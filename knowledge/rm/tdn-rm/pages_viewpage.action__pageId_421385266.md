---
content_hash: 70b503fd08d1c98fd77078449d041a9b0a1d8349f04f1f5294363bab63db46da
fetched_at: '2026-06-29T00:09:14.817902+00:00'
page_id: '421385266'
product: rm
source: tdn-rm
title: Excluir insumos não utilizados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385266
version: 2
---

---

São considerados insumos não utilizados no projeto, os insumos que não foram associados a nenhuma composição, tarefa ou contrato, insumos não apropriados e insumos que não estejam vinculados a requisições de materiais.

**Exclusão de insumos não utilizados:**

O sistema realizará as seguintes validações ao realizar exclusão de insumos não utilizados.

1- Não será permitida a exclusão:

* De insumos contratados;
* Se os insumos filhos de um insumo principal forem contratados;
* Para insumos detalhados que o insumo principal não tenha planejamento e nem esteja contratado.
* De insumos que não estão associados à composições e/ou tarefas, mas que estão apropriados, não ficam disponíveis para exclusão.
* De insumos que estão associados a uma tarefa e a mesma se encontra desativada ou com o valor cotado ativo, não ficam disponíveis para exclusão.
* Se o insumo principal já está planejado, não se permitirá a exclusão dos filhos, pois já houve detalhamento para um item planejado.

 2- Será permitida a exclusão:

* Se um filho for contratado e outros não e o insumo principal não estiver planejado, estes serão excluídos.
