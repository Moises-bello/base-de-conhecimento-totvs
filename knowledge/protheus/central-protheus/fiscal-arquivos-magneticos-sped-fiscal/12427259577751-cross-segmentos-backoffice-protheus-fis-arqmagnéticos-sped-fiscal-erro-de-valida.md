---
article_id: 12427259577751
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 05d644ccb80d2f3320981f8458c218f025e2321186c4388e54ada10d76402b4a
fetched_at: '2026-06-28T22:42:03.606648+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Sped Fiscal
  - Erro de validação registro C100 campo - 9 CHV_NFE. Obrigatório, se NFe. '
type: support-article
updated_at: '2023-02-15T13:57:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12427259577751-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Sped-Fiscal-Erro-de-valida%C3%A7%C3%A3o-registro-C100-campo-9-CHV-NFE-Obrigat%C3%B3rio-se-NFe
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como resolver o erro de validação que está no *print* abaixo?

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12427152102039)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**O erro em questão, ocorre porque a chave do documentos fiscal, indicado na linha criticada pelo validador, não está preenchida no **campo 9 CHV\_NFE** do **registro C100.**

Para que a informação seja levada ao **campo 9 do registro C100,** os campos **Chave NFe -  F3\_CHVNFE** e **Chave Nfe - FT\_CHVNFE,** nas tabelas **SF3 - Livros Fiscais** e **SFT - Livro Fiscal por Item de NF,** respectivamente, precisam estar preenchidos com a chave da nota fiscal em questão.

Para as notas de entrada, os campos na **SFT** e **SF3** são alimentados conforme informação manual informada no momento da escrituração do documento fiscal no campo **Chave NFE - F1\_CHVNFE.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12427289296407)**

Para as notas de saída, o campo é alimentado automaticamente, após transmissão da nota.
