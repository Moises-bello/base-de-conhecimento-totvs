---
article_id: 360019474452
category: Contabilidade Gerencial - Consolidação
content_hash: 955f81f7665dd8b7b5a9902b901f36029cedaec665f809cc2748bdc6d9fbe263
fetched_at: '2026-06-28T22:40:56.797395+00:00'
product: protheus
section_id: 1500001548562
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB CTBA220 CONSOLIDACAO
  GERAL, HELP: MA280FLOCK USO EXCLUSIVO ALIAS CT1'
type: support-article
updated_at: '2023-11-14T16:50:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019474452-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA220-CONSOLIDACAO-GERAL-HELP-MA280FLOCK-USO-EXCLUSIVO-ALIAS-CT1
---

**Dúvida**

**Ao processar a consolidação geral é gerada a mensagem:**

**HELP: MA280FLOCK**

**Problema: Não foi possível a abertura dos arquivos de forma exclusiva neste momento.**

**Contate o administrador do sistema. Alias: CT1**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015296592)  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Contabilidade Gerencial – Todas as versões  
  
  
**Solução:**

**Primeira pergunta da rotina (CTBA220):**

**"Limpa Consolidação= NÃO" o uso exclusivo não será obrigatório.**

Quando a consolidação é feita com a Pergunta "Limpa Consolidação= SIM"

Para manter a integridade do sistema, a função Ma280Flock protege o uso exclusivo das tabelas envolvidas:

MA280FLock("CT1") .And.;  
MA280FLock("CT2") .And.;  
MA280FLock("CQ0") .And.;  
MA280FLock("CQ1") .And.;  
MA280FLock("CQ2") .And.;  
MA280FLock("CQ3") .And.;  
MA280FLock("CQ4") .And.;  
MA280FLock("CQ5") .And.;  
MA280FLock("CQ6") .And.;  
MA280FLock("CQ7") .And.;  
MA280FLock("CTC") .And.;  
MA280FLock("CTD") .And.;  
MA280FLock("CTF") .And.;  
MA280FLock("CTH") .And.;  
MA280FLock("CTT") .And.;  
MA280FLock("CTZ") .And.;  
MA280FLock("CTK") .And.;  
MA280FLock("CV1") .And.;  
MA280FLock("CV2") .And.;  
MA280FLock("CV3") )

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015296812)
