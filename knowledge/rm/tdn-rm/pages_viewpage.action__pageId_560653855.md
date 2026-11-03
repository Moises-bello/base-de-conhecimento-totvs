---
content_hash: c353eaea557586098046a2915f6b37fb10b33b606da4a604478f40c085a6e407
fetched_at: '2026-06-29T00:10:47.784759+00:00'
page_id: '560653855'
product: rm
source: tdn-rm
title: Informações sobre as parcelas de pagamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=560653855
version: 5
---

### Voltar para [Layout único de integração da NFS-e com o TSS](https://tdn.totvs.com/pages/viewpage.action?pageId=560652116)

| Nome | Pai | Tipo Elemento | Ocorrência | Descrição | Campo no RM | Observações |
| --- | --- | --- | --- | --- | --- | --- |
| pagamentos | [rps](https://tdn.totvs.com/pages/viewpage.action?pageId=1056143227) | G | 0-1 | Tag raiz que agrupará os pagamentos do documento. |  | Não será Gerado |
| pagamento | pagamentos | G | 1-N | Tag raiz que agrupará as informações sobre um pagamento do documento. |  | Não será Gerado |
| pagamento | pagamentos | G | 1-N | Tag raiz que agrupará as informações sobre um pagamento do documento. |  | Não será Gerado |
| parcela | pagamento | E | 1-1 | Número da parcela do pagamento. |  | Não será Gerado |
| dtvenc | pagamento | E | 1-1 | Data do vencimento do pagamento. Formato AAAA-MM-DD |  | Não será Gerado |
| valor | pagamento | E | 1-1 | Valor do pagamento. |  | Não será Gerado |
