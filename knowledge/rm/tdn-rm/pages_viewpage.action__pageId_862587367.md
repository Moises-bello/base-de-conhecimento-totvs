---
content_hash: 8c95d1c2890c586354b619da207874ae36de8160fe3f3b6cfbf9f5c3f00425c7
fetched_at: '2026-06-29T00:11:55.591907+00:00'
page_id: '862587367'
product: rm
source: tdn-rm
title: Contratos de Venda - Processo - Atualizar Histórico Ficha Financeira
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=862587367
version: 4
---

Utilize a ferramenta ***Atualizar Histórico Ficha Financeira*** para corrigir cenários em que a [Ficha Financeira](https://tdn.totvs.com/pages/viewpage.action?pageId=528923958) apresenta valores inconsistentes.

Este processo ajusta o histórico das parcelas do financeiro, da venda selecionada, que tenham a data do log superior à data da da última baixa e que, por possuírem esta característica, fazem com que os valores apresentados na Ficha Financeira possam ficar incorretos, em relação à realidade da venda.

Ao executar este processo, o sistema criará um job service e ao final da execução do mesmo, é possível de se consultar o log da execução do mesmo.
