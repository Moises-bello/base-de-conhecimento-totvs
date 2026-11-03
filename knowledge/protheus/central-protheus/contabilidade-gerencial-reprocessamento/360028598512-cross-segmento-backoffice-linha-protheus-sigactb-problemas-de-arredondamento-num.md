---
article_id: 360028598512
category: Contabilidade Gerencial - Reprocessamento
content_hash: 917b54891605fae09e3a5db7caf793c53e0cf36b7d2a856457fe2de515622be4
fetched_at: '2026-06-28T22:40:41.985977+00:00'
product: protheus
section_id: 1500001548742
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - Problemas de arredondamento
  numérico Protheus 32bits
type: support-article
updated_at: '2022-06-20T19:57:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028598512-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Problemas-de-arredondamento-num%C3%A9rico-Protheus-32bits
---

**Ocorrência**Problema com arrendondamentos devido a uma condição interna do servidor de aplicação do **Protheus** **32 bits** para valores numéricos com muitas casas decimais.

**Ambiente**Protheus – Contabilidade Gerencial – A partir da versão 12.1.17

**Solução**Para trabalhar com uma precisão mais apurada de tais valores numéricos é imprescindível habilitar o parâmetro "*FloatingPointPrecise"*(deixando com o valor igual a 1). Este parâmetro deverá ser informado no arquivo de configurações do sistema (**appserver.ini**) dentro do seção**[General]**.
