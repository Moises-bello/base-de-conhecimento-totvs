---
content_hash: 22bea614cd7508ab01c8ff90828547f60565b348ab8d6bf0eeec1f6859151ffc
fetched_at: '2026-06-29T00:05:52.131296+00:00'
page_id: '1056934821'
product: rm
source: tdn-rm
title: Informações sobre as parcelas de pagamento (TPF)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1056934821
version: 1
---

### Voltar para [Layout único de integração da NFS-e com o TPF](https://tdn.totvs.com/pages/viewpage.action?pageId=1056143731)

| Nome | Pai | Tipo Elemento | Ocorrência | Descrição | Campo no RM | Observações |
| --- | --- | --- | --- | --- | --- | --- |
| pagamentos | **[rps](https://tdn.totvs.com/pages/viewpage.action?pageId=1056143860)** | G | 0-1 | Tag raiz que agrupará os pagamentos do documento. |  | Não será Gerado |
| pagamento | pagamentos | G | 1-N | Tag raiz que agrupará as informações sobre um pagamento do documento. |  | Não será Gerado |
| pagamento | pagamentos | G | 1-N | Tag raiz que agrupará as informações sobre um pagamento do documento. |  | Não será Gerado |
| parcela | pagamento | E | 1-1 | Número da parcela do pagamento. |  | Não será Gerado |
| dtvenc | pagamento | E | 1-1 | Data do vencimento do pagamento. Formato AAAA-MM-DD |  | Não será Gerado |
| valor | pagamento | E | 1-1 | Valor do pagamento. |  | Não será Gerado |
