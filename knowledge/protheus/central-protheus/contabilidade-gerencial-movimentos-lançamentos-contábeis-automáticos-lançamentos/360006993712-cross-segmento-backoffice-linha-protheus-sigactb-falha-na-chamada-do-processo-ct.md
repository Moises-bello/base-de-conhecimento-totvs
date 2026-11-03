---
article_id: 360006993712
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: b269cf8abfbe2d010a3f97512f4fa5eff663ca1ec6dd8a95bfb360635b6fd8aa
fetched_at: '2026-06-28T22:40:32.348875+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - FALHA NA CHAMADA DO
  PROCESSO  CTBA185_06
type: support-article
updated_at: '2021-12-07T11:44:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006993712-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-FALHA-NA-CHAMADA-DO-PROCESSO-CTBA185-06
---

**Ocorrência**

* Na exclusão de lançamentos, retorna mensagem de "Falha na chamada do processo ctba185\_06"
* LIBSERV:O Serviço de Schedule está desativado, verifique configuração.

**Ambiente**

Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12

**Solução**

Verifique  o parâmetro MV\_CTBSALD, que define qual a forma de atualização de saldos on-line.

Se esta configurado com a opção 2

Seu conteúdo pode ser:

* “1” atualização pelo processo 04 - P12\_04.SPS - CTB150 (Atualização de saldos on-line)
* “2” atualização pelo processo 06 – default - P12\_06.SPS - CTB185 (Atualização de saldos on-line por lote)

Segue links com mais  informações em relação ao parâmetro,  e saldos por fila para conhecimento.

<http://tdn.totvs.com/pages/releaseview.action?pageId=233748084>

<http://tdn.totvs.com/display/public/PROT/CTB113_REPROCESSAMENTO_SALDOS_POR_FILA_P12>
