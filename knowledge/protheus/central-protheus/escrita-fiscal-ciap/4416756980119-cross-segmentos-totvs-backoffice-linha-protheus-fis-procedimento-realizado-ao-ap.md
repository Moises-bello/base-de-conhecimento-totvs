---
article_id: 4416756980119
category: Escrita Fiscal - CIAP
content_hash: 5db850ac5fd19b0245b35d295741c39b0698bd81f55ecbef1212a5a69834c5b2
fetched_at: '2026-06-28T22:39:33.981439+00:00'
product: protheus
section_id: 1500001538561
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Procedimento Realizado
  ao Apresentar Alerta A906BAIXA
type: support-article
updated_at: '2021-12-22T16:34:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4416756980119-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Procedimento-Realizado-ao-Apresentar-Alerta-A906BAIXA
---

**Dúvida**Qual procedimento deve ser realizado ao apresentar alerta A906BAIXA?   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**

**CIAP já baixado ou com data do último movimento superior a data base****.**

Quando for apresentada a tela, verifique na tabela **Estorno Mensal CIAP (SFA)** qual a data da última apropriação realizada para o bem que precisa ser baixado.

Ocorre quando é solicitada a baixa de um bem que já sofreu apropriação com data superior a data base utilizada. **Exemplo**:

* **Base**: 19/04/2011
* **Última apropriação**: 30/04/2011

Nesse caso, o bem só pode ser baixado no mês seguinte ou após exclusão da apropriação ocorrida no período.
