---
content_hash: 8c91fae95b65b814f13445ab51325735b847dc564f7ed0ed4749e9cf85eff32a
fetched_at: '2026-06-29T00:05:52.126724+00:00'
page_id: '1056934330'
product: rm
source: tdn-rm
title: Dados das faturas vinculadas (TPF)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1056934330
version: 1
---

### Voltar para [Layout único de integração da NFS-e com o TPF](https://tdn.totvs.com/pages/viewpage.action?pageId=1056143731)

| Nome | Pai | Tipo Elemento | Ocorrência | Descrição | Campo no RM | Observações |
| --- | --- | --- | --- | --- | --- | --- |
| faturas | **[rps](https://tdn.totvs.com/pages/viewpage.action?pageId=1056143860)** | G | 0-1 | Tag raiz que agrupará as faturas do documento. |  |  |
| fatura | faturas | G | 1-N | Tag raiz que conterá as informações sobre uma fatura do documento. |  |  |
| numero | fatura | E | 1-1 | Número da fatura do documento. | TMOV.NUMEROMOV | Numero do movimento |
| valor | fatura | E | 1-1 | Valor da fatura do documento. |  | Valor total do movimento |
