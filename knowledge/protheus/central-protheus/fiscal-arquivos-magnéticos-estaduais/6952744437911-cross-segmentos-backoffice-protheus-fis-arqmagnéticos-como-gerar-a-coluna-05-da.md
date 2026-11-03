---
article_id: 6952744437911
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 6e66ff7e195ce36e25fc0f14718446a4bfd50b16375b603e8d6fafdd0f20475d
fetched_at: '2026-06-28T22:42:10.304433+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Como gerar a
  coluna 05 da DAPIMG?
type: support-article
updated_at: '2022-08-17T19:38:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6952744437911-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-a-coluna-05-da-DAPIMG
---

**Dúvida**Como gerar a coluna 05 da **DAPIMG**?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Livros Fiscais – A partir da versão 12  
  
**Solução**Configuração como gerar a **coluna 05** da **DAPIMG**.

Configure a **TES** **(Tabela SF4)**, através dos campos:

**Sit.Trib.ICM (F4\_SITTRIB)** = 40 - Isentas

O Valor considerado será gravado no campo **Vlr Isen ICM (FT\_ISENICM)**, na **tabela SFT.**
