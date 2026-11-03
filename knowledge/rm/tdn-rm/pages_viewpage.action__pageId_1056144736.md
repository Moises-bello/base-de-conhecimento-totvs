---
content_hash: 08a7e2bc6984112fbe77bcc18606c22c5f2a35c5cf78d2cec4ea0eb81666ba08
fetched_at: '2026-06-29T00:05:52.084252+00:00'
page_id: '1056144736'
product: rm
source: tdn-rm
title: Totais das informações dos tributos PIS/COFINS Apurado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1056144736
version: 6
---

### Voltar para [Layout único de integração da NFS-e com o TSS](https://tdn.totvs.com/pages/viewpage.action?pageId=560652116)

| Nome | Pai | Tipo Elemento | Ocorrência | Descrição | Campo no RM | Observações |
| --- | --- | --- | --- | --- | --- | --- |
| piscofinsApu | [valores](https://tdn.totvs.com/pages/viewpage.action?pageId=560653837) | G | 0-1 | Totais das informações dos tributos PIS/COFINS Apurado |  | Este grupo é gerado apenas com as informações dos tributos PIS/COFINS não retidos. |
| CST | piscofinsApu | E | 0-1 | CST PIS/COFINS. | TTRBMOV.SITTRIBUTARIA |  |
| vBcPis | piscofinsApu | E | 0-1 | Base Cálculo PIS - apuração. | TTRBMOV.BASEDECALCULO |  |
| pAliqPis | piscofinsApu | E | 0-1 | Alíquota PIS.apuração | TTRBMOV.ALIQUOTA |  |
| vPis | piscofinsApu | E | 0-1 | Valor pis apuração | TTRBMOV.VALOR |  |
| vBcCofins | piscofinsApu | E | 0-1 | Base Cálculo Cofins- apuração. | TTRBMOV.BASEDECALCULO |  |
| pAliqCofins | piscofinsApu | E | 0-1 | Alíquota Cofins.apuração | TTRBMOV.ALIQUOTA |  |
| vCofins | piscofinsApu | E | 0-1 | Valor cofins apuração | TTRBMOV.VALOR |  |
