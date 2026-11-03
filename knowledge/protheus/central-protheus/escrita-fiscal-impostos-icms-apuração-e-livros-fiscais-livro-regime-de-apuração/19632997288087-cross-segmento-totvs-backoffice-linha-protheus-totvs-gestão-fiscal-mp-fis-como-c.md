---
article_id: 19632997288087
category: Escrita Fiscal - Impostos - ICMS - Apuração e Livros Fiscais - Livro - Regime
  de Apuração
content_hash: 6b683e29f0cff6436efd6ab6cce028a324b6eea486c8e238bb3b1153272c1d50
fetched_at: '2026-06-28T22:39:22.127129+00:00'
product: protheus
section_id: 1500001538681
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal -
  MP FIS Como corrigir o valor da linha 016 - Informações Complementares?
type: support-article
updated_at: '2024-03-28T14:34:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19632997288087-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-TOTVS-Gest%C3%A3o-Fiscal-MP-FIS-Como-corrigir-o-valor-da-linha-016-Informa%C3%A7%C3%B5es-Complementares
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19632981901591) Tempo aproximado para leitura: 03:00**min** **Dúvida**Como corrigir o valor da linha 016 - Informações Complementares?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**A linha 016 - da Aba Informações complementares é gravada das notas fiscais com calculo de diferencial de aliquotas

Configuração da TES

Calcula icms = sim

L fiscal icms = outros

Sit trib icm = 90

Calc dif icm = sim

Calc difal = não

Mat consumo = sim

O valor do diferencial de aliquota é calculado e lançado no campo F3\_ICMSCOM

Ocorrendo se o valor da linha 016 não bater com a soma do F3\_ICMSCOM, verificar os parametros abaixo:

Para o estado de SP

MV\_ART117 = .F.

Para todos os estados

MV\_PARICMS = .F.

Para a geração da GNRE / Titulo verificar o parametro

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22398459670423)
