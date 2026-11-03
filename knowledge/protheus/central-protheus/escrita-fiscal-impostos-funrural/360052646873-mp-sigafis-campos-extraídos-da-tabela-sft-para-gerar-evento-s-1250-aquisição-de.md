---
article_id: 360052646873
category: Escrita Fiscal - Impostos - Funrural
content_hash: 92aae1e73e685bcad06c62f91e28368e8ef509be869ec2f2bfe2d50a8d19faa8
fetched_at: '2026-06-28T22:39:28.179003+00:00'
product: protheus
section_id: 1500001549822
source: central-protheus
title: MP - SIGAFIS - Campos extraídos da tabela SFT para gerar evento S-1250 - Aquisição
  de Produção Rural
type: support-article
updated_at: '2021-04-28T19:15:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052646873-MP-SIGAFIS-Campos-extra%C3%ADdos-da-tabela-SFT-para-gerar-evento-S-1250-Aquisi%C3%A7%C3%A3o-de-Produ%C3%A7%C3%A3o-Rural
---

**Dúvida**Quais os campos na tabela SFT são extraídos os valores do SENAR, GILRAT e INSS?  
   
 **Ambiente**Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

Seguem os campos da tabela SFT que são lidos pelo fonte do extrator fiscal para extração dos valores na tabela SFT e alimentar os dados no TAF para gerar o evento S-1250:  
  
GILRAT  
SFT->FT\_BASEFUN  
SFT->FT\_ALIQFUN  
SFT->FT\_VALFUN  
  
SENAR  
SFT->FT\_BSSENAR  
SFT->FT\_ALSENAR  
SFT->FT\_VLSENAR  
  
INSS  
SFT->FT\_BASEINS  
SFT->FT\_ALIQINS  
SFT->FT\_VALINS
