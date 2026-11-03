---
content_hash: 92b2d66f1eafd566ed3923a5bbe85abc2aadd342fce32b8fa8111a36b5420440
fetched_at: '2026-06-29T00:11:17.383920+00:00'
page_id: '679962178'
product: rm
source: tdn-rm
title: Bloquear Lote Contábil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=679962178
version: 6
---

A atividade Bloquear Lote Contábil, bloqueia o lote informando para a edição do mesmo, evitando que outro usuário possa acessá-lo.

Os Parâmetros necessários:

* **CodColigada:** Código da coligada.
* **CodLote:** Código do lote contábil.
* **CodUsuario:** Código do Usuário logado.
* **MotivoBloqueio:** Descrição do Motivo do bloqueio.
* **TipoBloqueio:** Seleciona  o tipo de bloqueio a ser efetuado:
  + Não Identificado.
  + Processo Agrupamento Lançamento.
  + Processo Integração Lote.
  + Processo Bloqueio Lote.
  + Processo Rateio Gerencial.
  + Processo Renumeração Lançamento.
  + Processo Recalculo Diferença.
  + Processo Distribuição Gerencial.
  + Processo Desfazer Agrupamento.
* **VerficaLanLote:** Identifica se é para analisar os lançamentos do lote.

Segue um exemplo com a atividade configurada.
