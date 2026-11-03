---
article_id: 360052000453
category: Escrita Fiscal - Impostos - ICMS
content_hash: a290824e79963867439dc08c1f7b14139bcadccb50461abd9b4102c2290835b0
fetched_at: '2026-06-28T22:39:25.587719+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Configuração do código
  de reflexo para ICMS desonerado base simples, ou seja quando não é calculado conforme
  resolução SEFAZ RJ 13/2019
type: support-article
updated_at: '2021-07-20T14:05:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052000453-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Configura%C3%A7%C3%A3o-do-c%C3%B3digo-de-reflexo-para-ICMS-desonerado-base-simples-ou-seja-quando-n%C3%A3o-%C3%A9-calculado-conforme-resolu%C3%A7%C3%A3o-SEFAZ-RJ-13-2019
---

**Dúvida**Configuração do código de reflexo para ICMS desonerado base simples, ou seja quando não é calculado conforme resolução SEFAZ RJ 13/2019.

Valor do ICMS desonerado = BCICMS\*Alíquota

**Ambiente**  
Microsiga Protheus – Livros Fiscais  – A partir da versão 12  
  
**Solução**

**MV\_DESONRJ**em branco

Configuração no TES:

F4\_ICM=Sim  
F4\_LFICM=Outros/Isento  
F4\_SITTRIB=de acordo com a operação

Na aba outros  
F4\_MOTICMS=9

Configuração Código de Reflexo (Rotina FISA072)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080302434/mceclip0.png)
