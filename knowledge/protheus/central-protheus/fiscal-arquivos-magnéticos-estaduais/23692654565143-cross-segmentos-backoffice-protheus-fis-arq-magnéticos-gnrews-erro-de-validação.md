---
article_id: 23692654565143
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: fdfbeab457b087c08737b076ec0c271d943d69084193e5044e50d88011378284
fetched_at: '2026-06-28T22:42:09.193685+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - GNREWS - Erro
  de validação 263 "CAMPO: DATAPAGAMENTO - DESCRICAO: DATA INVALIDA"'
type: support-article
updated_at: '2024-06-21T16:59:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23692654565143-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-GNREWS-Erro-de-valida%C3%A7%C3%A3o-263-CAMPO-DATAPAGAMENTO-DESCRICAO-DATA-INVALIDA
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23692665692567) Tempo aproximado para leitura: **00:02:00****Ocorrência**

Ao transmitir a **GNRE WS** pela rotina **FISA095** acontece erro de validação:

**263 "CAMPO: DATAPAGAMENTO - DESCRICAO: DATA INVALIDA":**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23692654530327)

**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Todas as versões

**Causa**Conteúdo incorreto no campo **F6\_DTPAGTO** da **Guia de Recolhimento** (**MATA960**).

**Solução**Configure na **Guia** o campo **F6\_DTPAGTO** **(data de pagamento)** com data igual ou maior que a data atual.

***Print**:*

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23692654535447)

Após isso, realize novos testes.
