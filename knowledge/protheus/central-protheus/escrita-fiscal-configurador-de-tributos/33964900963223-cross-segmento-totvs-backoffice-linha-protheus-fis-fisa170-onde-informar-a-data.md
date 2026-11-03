---
article_id: 33964900963223
category: Escrita Fiscal - Configurador de Tributos
content_hash: c0994103caa86df4fedeb06c1ad8d742be8919531e4d95ee3af05e6aa95e6b6d
fetched_at: '2026-06-28T22:39:17.525116+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - FISA170 - Onde informar
  a data de vigência da regra criada no Configurador de Tributos?
type: support-article
updated_at: '2025-08-06T12:51:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33964900963223-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Onde-informar-a-data-de-vig%C3%AAncia-da-regra-criada-no-Configurador-de-Tributos
---

**Dúvida**  
Onde informar a data de vigência da regra criada no Configurador de Tributos?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - a partir da release 12.1.2210  
  
**Solução**  
Segue abaixo o campo da rotina do Configurador de Tributos (FISA170) onde é determinado a data de vigência e se necessário, a data de encerramento da regra criada.

* Cadastros
* Regra de Cálculo - Documentos Fiscais

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33964921967895)

A regra criada na rotina será aplicada apenas quando a data de vigência for igual ou posterior à data de início, e desde que não haja uma data final informada.
