---
article_id: 4408615826839
category: Metrologia (SIGAQMT)
content_hash: 2fdea06ae8bad52d9757eaee50a27df4fddfef12d0cf208086a397ba1d71309b
fetched_at: '2026-06-28T22:42:24.902575+00:00'
product: protheus
section_id: 360005876694
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQMT - Rotinas que alteram o status do instrumento
type: support-article
updated_at: '2021-09-15T16:38:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408615826839-Manufatura-Linha-Protheus-SIGAQMT-Rotinas-que-alteram-o-status-do-instrumento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:55 min** **Dúvida**Quais rotinas alteram o *status* do instrumento para **inativo**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Metrologia (SIGAQMT) - Todas as versões  
  
**Solução**

As rotinas abaixo fazem alteração do status do instrumento, no campo **QM2\_STATUS - Status** para Inativo, sendo este um procedimento padrão do Sistema:

* **QMTA010 - Instrumentos**: Ao alterar os dados de um instrumento já calibrado, e gerar uma nova revisão, a revisão anterior é inativada;
* **QMTA020 - Duplicação**: Processo de duplicação sempre inativa o instrumento informado como instrumento de origem;
* **QMTA030 - Famílias**: Processo de associações também altere o conteúdo do campo **QM2\_STATUS** para inativo;
* **QMTA140 - Calibrações**: Ao realizar a calibração do instrumento, também altera o conteúdo do campo **QM2\_STATUS**;
* **QMTA160 - Movimentação**: Movimentações de instrumentos também realiza essa alteração.
