---
content_hash: b55c52211503c8f3973a39401971b85130c3217a1da572cb0d540d0cb78c83e0
fetched_at: '2026-06-29T00:11:45.775061+00:00'
page_id: '821574786'
product: rm
source: tdn-rm
title: DT - S-2500 - Grau de Exposição de Agentes Nocivos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=821574786
version: 3
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | **RM** |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento - eSocial |
| Função: | eSocial - S-2500 - Grau de Exposição de Agentes Nocivos |
| País: | Brasil |
| Ticket: | [Ticket #18832899](https://totvssuporte.zendesk.com/agent/tickets/18832899 "View ticket on the Zendesk portal") |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-8814](https://jiraproducao.totvs.com.br/browse/DRHROTRM-8814) |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2302.257
* 12.1.2306.216
* 12.1.2310.148

## **03.** **SITUAÇÃO/REQUISITO**

O objetivo deste documento é fornecer informações sobre a atualização do S-2500 no grupo Grau de Exposição a Agentes Nocivos. 

A tag '**grauExp** ' do campo '**infoAgNocivo** ' passa a ser impressa mesmo quando não houver sido informado os códigos de categoria, considerados obrigatórios, e também quando a matrícula tiver sido preenchida e o indContr for igual a 'Sim' no cadastro do processo trabalhista.

## **04. SOLUÇÃO**

Ajuste na geração do evento S-2500 para imprimir o grupo infoAgNocivo quando a categoria do funcionário não é preenchida no cadastro do processo trabalhista.
