---
article_id: 360062279353
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 99ac0d1abd00028624c7117be3ba9049805be987c50ebed8e3e3de4aeb1e0f31
fetched_at: '2026-06-28T22:38:58.630190+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: MP - SIGAEST - Na Transferencia entre Filiais, mesmo preenchendo o campo Observação
  NNT_OBS não está saindo na Nota Fiscal
type: support-article
updated_at: '2021-04-28T15:45:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062279353-MP-SIGAEST-Na-Transferencia-entre-Filiais-mesmo-preenchendo-o-campo-Observa%C3%A7%C3%A3o-NNT-OBS-n%C3%A3o-est%C3%A1-saindo-na-Nota-Fiscal
---

**Dúvida**

Ao fazer Transferência entre Filiais (MATA311) preenchendo a Observação no campo NNT\_OBS, ela não está saindo na Nota Fiscal de Saída. O que fazer para que seja preenchida a observação na NF de Saída?

**Ambiente**Microsiga Protheus - Estoque - A partir da versão 12.1.23

**Solução**Na rotina de Transferência entre Filiais - MATA311, o campo Observação (NNT\_OBS) possui apenas caráter de informação interna do sistema, este não tem correlação com a Observação que seria emitida e impressa na Danfe de saída. O módulo de Estoque no Protheus padrão não faz com que o campo NNT\_OBS conste na observação da Danfe. Desta forma uma recomendação é avaliar juntamente ao time do Protheus SPED a possibilidade de inserção da Observação diretamente na emissão da Nota Fiscal.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
