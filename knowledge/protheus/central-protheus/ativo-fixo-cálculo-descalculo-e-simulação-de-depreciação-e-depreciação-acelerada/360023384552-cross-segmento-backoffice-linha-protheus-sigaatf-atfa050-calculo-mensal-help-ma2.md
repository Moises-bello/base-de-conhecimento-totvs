---
article_id: 360023384552
category: Ativo Fixo - Cálculo, Descalculo e Simulação de Depreciação e Depreciação
  acelerada
content_hash: 5b534c4b71904e6ce1bcfd01c56857d2f79ce51fbade3c07208f7b080ca46a0c
fetched_at: '2026-06-28T22:41:43.241419+00:00'
product: protheus
section_id: 1500001536401
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA050 - CALCULO MENSAL   HELP:
  MA280FLOCK'
type: support-article
updated_at: '2023-11-30T18:52:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023384552-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA050-CALCULO-MENSAL-HELP-MA280FLOCK
---

**Dúvida:**

**Na rotina *ATFA050 -* Calculo mensal (Depreciação) o que causa o HELP: MA280FLOCK?**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360021252452)

**Ambiente**  
Microsiga Protheus – Ativo Fixo – Todas as versões  
  
  
**Solução**

Nos Parâmetros da rotina, pergunta: **Abre Arq. Exclusivo? quando igual a 1 (sim)**

Indica se as tabelas relacionadas diretamente ao cálculo da depreciação/correção monetária serão abertas em modo exclusivo, **quando igual a 1 (sim)** a função Ma280Flock protege o uso exclusivo das tabelas envolvidas:

 If !( MA280FLock( IIf( lCtb, "CT1", "SI1" ) ) .And.;

MA280FLock("SN1") .And.;  
MA280FLock("SN2") .And.;  
MA280FLock("SN3") .And.;  
MA280FLock("SN4") .And.;  
MA280FLock("SN5") .And.;  
MA280FLock("SN6"))

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360021195011)
