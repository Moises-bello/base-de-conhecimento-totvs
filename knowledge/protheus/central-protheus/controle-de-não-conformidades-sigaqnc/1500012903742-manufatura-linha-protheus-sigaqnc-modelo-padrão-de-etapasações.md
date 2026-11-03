---
article_id: 1500012903742
category: Controle de Não Conformidades (SIGAQNC)
content_hash: 1510c923192862021dd36263c3cefeac424ee94ec0b12fe9418ba44fa0f16019
fetched_at: '2026-06-28T22:42:27.993904+00:00'
product: protheus
section_id: 360005876654
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQNC - Modelo padrão de etapas/ações
type: support-article
updated_at: '2021-06-02T16:53:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012903742-Manufatura-Linha-Protheus-SIGAQNC-Modelo-padr%C3%A3o-de-etapas-a%C3%A7%C3%B5es
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:00 min**  
**Dúvida**É possível definir um modelo padrão de etapas/ações que serão utilizadas no plano de ação?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) – Controle de Não Conformidades (SIGAQNC) – Todas as versões  
  
**Solução**Sim, é possível definir um modelo padrão de etapas ou ações que serão utilizadas no plano de ação.  
Para definir este modelo, realize os seguintes passos:

1. O modelo deve ser cadastrado na rotina **QNCA080 - Modelo de Passos** **e Etapas** e em **Outras Ações/Pas/ETA** definir quais são as etapas utilizadas neste modelo. As etapas devem estar previamente cadastradas na rotina **QNCA110 - Cadastro de Etapas/Passos** para que possam ser relacionadas na rotina **QNCA080**;
2. Após este cadastro é possível relacionar este modelo por meio do campo **QI3\_MODELO - Modelo/Grupo** na rotina **QNCA040 - Cadastro de Plano de Ação**. Desta forma, ao acessar a opção **Outras Ações/Ação/Etap** desta rotina, as etapas relacionadas ao modelo estarão relacionadas com este plano.
