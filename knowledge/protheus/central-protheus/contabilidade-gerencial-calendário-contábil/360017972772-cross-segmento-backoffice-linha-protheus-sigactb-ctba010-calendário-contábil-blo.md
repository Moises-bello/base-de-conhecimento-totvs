---
article_id: 360017972772
category: Contabilidade Gerencial - Calendário Contábil
content_hash: a68996a073891b14d71a304990b1e9fea156da61d49f8fbded5bede04cc6096e
fetched_at: '2026-06-28T22:41:03.403463+00:00'
product: protheus
section_id: 1500001537301
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA010: Calendário
  contábil bloqueado gerando lançamento com saldo tipo 9'
type: support-article
updated_at: '2023-11-10T16:19:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017972772-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA010-Calend%C3%A1rio-cont%C3%A1bil-bloqueado-gerando-lan%C3%A7amento-com-saldo-tipo-9
---

**Dúvida**Calendário contábil bloqueado gerando lançamento com saldo tipo 9

**Ambiente**Protheus – Contabilidade Gerencial – A partir da versão 11.80  
  
   
**Solução**

Existe um conceito no sistema onde o parâmetro MV\_ALTLCTO, quando configurado com “N”, Permite com que a contabilização ocorra, porém altera automaticamente o saldo do tipo 1(real) para o tipo 9 (pré-lançamento).

Desta forma fica a critério do contabilista, efetivar o lançamento posteriormente avaliando se abre o calendário contábil do mês bloqueado ou se faz a Inclusão do lançamento no próximo mês com status aberto.

**Importante:** Mesmo estando o parâmetro MV\_PRELAN com "N", e o parâmetro MV\_ALTLCTO estiver como "N", sera gerado o lançamento como pre-lançamento.
