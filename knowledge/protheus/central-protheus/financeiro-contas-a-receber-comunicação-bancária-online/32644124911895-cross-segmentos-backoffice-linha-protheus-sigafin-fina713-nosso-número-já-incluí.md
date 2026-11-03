---
article_id: 32644124911895
category: Financeiro - Contas a Receber - Comunicação Bancária Online
content_hash: 730a549ebc62a0d05afeece8973ce16cc6df3e55d3b224a81d0afeeebec8a425
fetched_at: '2026-06-28T22:37:49.229412+00:00'
product: protheus
section_id: 26656227629847
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA713 - Nosso Número
  já incluído anteriormente
type: support-article
updated_at: '2025-06-06T20:27:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32644124911895-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA713-Nosso-N%C3%BAmero-j%C3%A1-inclu%C3%ADdo-anteriormente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32644162536087) Tempo aproximado para leitura: **00****:03:00 min****Ocorrência**Na transmissão de boletos de cobrança ao tentar transmitir um boleto é apresentada a mensagem

Nosso Número já incluído anteriormente

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32644162536855)**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir do release 12.1.33

**Causa**

Este cenário ocorre quando o valor informado no campo **EE\_FAXATU** já está associado a outro título/boleto do mesmo banco.

**Solução**  
O número definido no campo **EE\_FAXATU**, nos parâmetros bancários, provavelmente já está vinculado a outro título identificado pelo campo **E1\_NUMBCO** do mesmo banco.

Outra possibilidade é que o título tenha sido registrado no banco com esse número, mas posteriormente excluído no sistema Protheus sem que a exclusão tenha sido refletida no Internet Banking.

Para resolver a situação, recomenda-se atualizar o campo **EE\_FAXATU** com uma numeração sequencialmente superior à atual.

**Exemplo:**  
Se o campo **EE\_FAXATU** estiver com o valor `000000000110`, utilizar um valor como `000000900150`.
