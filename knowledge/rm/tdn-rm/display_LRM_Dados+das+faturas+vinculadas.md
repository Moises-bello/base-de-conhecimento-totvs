---
content_hash: 27bf69ed6e45fa26a041fcd223e36567c99526468b1945d7739bcce3c69e2b40
fetched_at: '2026-06-29T00:10:47.780865+00:00'
page_id: '560653846'
product: rm
source: tdn-rm
title: Dados das faturas vinculadas
type: documentation
url: https://tdn.totvs.com/display/LRM/Dados+das+faturas+vinculadas
version: 5
---

### Voltar para [Layout único de integração da NFS-e com o TSS](https://tdn.totvs.com/pages/viewpage.action?pageId=560652116)

| Nome | Pai | Tipo Elemento | Ocorrência | Descrição | Campo no RM | Observações |
| --- | --- | --- | --- | --- | --- | --- |
| faturas | [rps](https://tdn.totvs.com/pages/viewpage.action?pageId=1056143227) | G | 0-1 | Tag raiz que agrupará as faturas do documento. |  |  |
| fatura | faturas | G | 1-N | Tag raiz que conterá as informações sobre uma fatura do documento. |  |  |
| numero | fatura | E | 1-1 | Número da fatura do documento. | TMOV.NUMEROMOV | Numero do movimento |
| valor | fatura | E | 1-1 | Valor da fatura do documento. |  | Valor total do movimento |
