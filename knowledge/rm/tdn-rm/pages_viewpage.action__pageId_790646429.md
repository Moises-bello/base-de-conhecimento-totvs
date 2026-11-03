---
content_hash: 89f7bb95a1618979d43ebc9a545691a063e70fecba6186e18e2885e7b940364b
fetched_at: '2026-06-29T00:11:39.898825+00:00'
page_id: '790646429'
product: rm
source: tdn-rm
title: DT - Geração de Encargo - Férias em Dobro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=790646429
version: 4
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS - Folha de Pagamento |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Geração de Encargos |
| País: | Brasil |
| Ticket: | [15582699](https://totvssuporte.zendesk.com/agent/tickets/15582699 "View ticket on the Zendesk portal") [16020708](https://totvssuporte.zendesk.com/agent/tickets/16020708 "View ticket on the Zendesk portal") [16014240](https://totvssuporte.zendesk.com/agent/tickets/16014240 "View ticket on the Zendesk portal") [16883009](https://totvssuporte.zendesk.com/agent/tickets/16883009 "View ticket on the Zendesk portal") [17184597](https://totvssuporte.zendesk.com/agent/tickets/17184597 "View ticket on the Zendesk portal") |
| Story: | [DRHCALCRM-3425](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-3425) |

## **02. SITUAÇÃO/REQUISITO**

Ao gerar o Encargo de provisões de férias quando o funcionário teve férias em dobro e recebeu a mesma, o sistema está calculando o encargo de FGTS e INSS sobre o valor das férias em dobro, conforme legislação, as férias em dobro não tem incidência de INSS e FGTS.

## **03. SOLUÇÃO**

Anteriormente não existia a provisão de férias em dobro separado e com isso não abatia esse valor nos encargos 5 - Provisão de FGTS de férias e 6 - Provisão de encargos de férias. 

Atualmente foi feito o tratamento para abater as férias em dobro nos encargos 5 - Provisão de FGTS de férias e 6 - Provisão de encargos de férias.

## **04.****ASSUNTOS RELACIONADOS**

* Criado documento de referência com exemplos

  + [Exemplos para regra de cálculo dos encargos 5 - Provisão de FGTS de férias e 6 - Provisão de encargos de férias](https://tdn.totvs.com.br/pages/viewpage.action?pageId=790646098)
* Inserido link nos TDNs relacionados abaixo:

  + [Geração de Encargos](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452718264)
  + [Contabilização - Parâmetros](https://tdn.totvs.com.br/pages/releaseview.action?pageId=519715154)
  + [Encargos - Folha de Pagamento](https://tdn.totvs.com.br/display/public/LRM/Encargos+-+Folha+de+Pagamento)
