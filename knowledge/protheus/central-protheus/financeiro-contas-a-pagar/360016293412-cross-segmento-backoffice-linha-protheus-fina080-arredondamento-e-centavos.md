---
article_id: 360016293412
category: Financeiro - Contas a Pagar
content_hash: ef1e5ecfba15c9c5ab42a8b667dc47f3270357b24e97ad6a28a7c383974d51a8
fetched_at: '2026-06-28T22:38:07.192766+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - FINA080 - Arredondamento e Centavos '
type: support-article
updated_at: '2021-08-26T20:30:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016293412-Cross-Segmento-Backoffice-Linha-Protheus-FINA080-Arredondamento-e-Centavos
---

**Ocorrência**Ao efetuar baixa de títulos gerados pelo módulo de **Compras**, retendo os impostos de **PCC** na baixa e no módulo **Financeiro** estiver apresentando uma diferença de **Centavos,** a ocorrênciaestá no **arredondamento**.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – Financeiro – A partir da versão 12  
  
**Causa**Quando os parâmetros abaixo estiver com **o conteúdo = . F.**:

**MV\_RNDPIS**

**MV\_RNDCOF**

**MV\_RNDCSL**

**Solução**Para realizar a correção, se faz necessário alterar três parâmetros de **arredondamento** que deve ser preenchido com **conteúdo =. T.** no módulo **Configurador**, Parâmetros, seguem os parâmetros:

**MV\_RNDPIS**

**MV\_RNDCOF**

**MV\_RNDCSL**
