---
article_id: 360028706172
category: Ativo Fixo - Ativo X ICMS / CIAP, Impostos, Seguro, Frete
content_hash: 1f75f2d0dcb728a3b15d86dea59d47ed186a746bafc92ddfc6cdd7bea5b37741
fetched_at: '2026-06-28T22:41:56.178532+00:00'
product: protheus
section_id: 1500001546982
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - CIAP - CREDITOS DE ICMS
  NO ATIVO FIXO PERMANENTE
type: support-article
updated_at: '2023-08-11T14:10:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028706172-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-CIAP-CREDITOS-DE-ICMS-NO-ATIVO-FIXO-PERMANENTE
---

**Dúvida**Geração do ICMS no ativo (N3\_ICMSAPR)

**Ambiente**Protheus - Ativo fixo – A partir da versão 11.80  
  
**Solução**

Para tratar o CIAP estão disponíveis os campos  SN1, SN3, N1\_CODCIAP, N1\_ICMSAPR e N3\_BXICMS, no modulo Ativo Fixo.  
Estes campos permitem a integração com o modulo de Compras através da TES.

Na TES as perguntas 'Atualiza Ativo' e 'L.FISC. CIAP' devem ser respondidas com 'Sim'.  
Na inclusão de notas fiscais de entrada, utilizando esta TES, o Compras gera bens no Ativo com algumas informações. Para complementar estas informações, deve-se entrar no modulo Ativo e Classificar os ativos oriundos do modulo Compras. Após a Classificação, o ativo está pronto para iniciar as depreciações.  
No campo N1\_ICMSAPR está o valor total do ICMS a apropriar. No campo N3\_BXICMS está o valor de ICMS apropriado na baixa do bem.
