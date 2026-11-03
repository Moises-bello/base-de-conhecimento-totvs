---
article_id: 360052699634
category: RH - Folha de Pagamento
content_hash: 7b7956f68c640f772a503fe5f0dfbc5dde1a98efb7079129c46c7d6490e9a5b9
fetched_at: '2026-06-28T22:44:13.428846+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como é tratada a verba de dedução INSS base IR
  férias (Id 0168) na folha do mês seguinte quando tem férias partidas com o parâmetro
  MV_DINSSFM = N
type: support-article
updated_at: '2025-08-22T18:48:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052699634-RH-Linha-Protheus-GPE-Como-%C3%A9-tratada-a-verba-de-dedu%C3%A7%C3%A3o-INSS-base-IR-f%C3%A9rias-Id-0168-na-folha-do-m%C3%AAs-seguinte-quando-tem-f%C3%A9rias-partidas-com-o-par%C3%A2metro-MV-DINSSFM-N
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26357785204503)** Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Como é tratada a verba de dedução INSS base IR férias (Id 0168) na folha do mês seguinte quando tem férias partidas com o parâmetro MV\_DINSSFM = N?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Inicialmente a verba de Dedução INSS Base IR Férias (Id 0168) transitava na folha do mês seguinte, quando tem férias partidas, para demonstrar o valor recolhido de INSS Férias do período. Porém, essa verba parou de ser apresentada no cálculo para não influenciar nas informações enviadas para a DIRF e E-social.

Pois por se tratar de IR devido, sua referência e data do fator gerador, o valor de INSS férias que consta nesse período da folha seguinte, já foi utilizada para a base de IR nas férias, então na folha seguinte não é utilizada mais.

Pois se for apresentado estaria duplicando a dedução e ficaria incorreto na DIRF e E-social.

**Saiba mais:**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
