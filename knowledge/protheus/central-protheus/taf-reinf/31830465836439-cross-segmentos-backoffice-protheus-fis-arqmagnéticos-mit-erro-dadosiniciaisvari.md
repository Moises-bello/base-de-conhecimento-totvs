---
article_id: 31830465836439
category: TAF - REINF
content_hash: cb771a288c5b3137ed78fefe10841547eb669ddfa600d8582fd7bd368e4a3fb3
fetched_at: '2026-06-28T22:41:33.463158+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - MIT - Erro:
  -DadosIniciais.VariacoesMonetarias: campo obrigatório não informado.'
type: support-article
updated_at: '2025-05-02T18:49:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31830465836439-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-MIT-Erro-DadosIniciais-VariacoesMonetarias-campo-obrigat%C3%B3rio-n%C3%A3o-informado
---

**Ocorrência**MIT - Arquivo Json erro de validação: DadosIniciais.VariacoesMonetarias: campo obrigatório não informado.  
**Ambiente**TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - A partir da versão 12.1.2310  
  
**Causa**Esse incidente ocorre quando não é informado A **Variações Monetária** no cadastro campo **Ind.Rec. Rec** **CHD\_RECREC** na Rotina **TAFA372** - Parâmetros de Cálculo para geração do MIT.  
  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Rotina **TAFA372** - Parâmetros de Cálculo para geração do MIT.  
![recmit.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31830465825047)

MIT - Módulo de Integração de Tributos:

<https://tdn.totvs.com/pages/releaseview.action?pageId=904594705>

De\Para (TAGS do layout **MIT** x Campos **TAF**)

|  |  |  |  |
| --- | --- | --- | --- |
| DadosIniciais | 9 | VariacoesMonetarias | CHD\_RECREC |
