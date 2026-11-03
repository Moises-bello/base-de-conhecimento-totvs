---
article_id: 360051854113
category: Escrita Fiscal - Impostos - Simples Nacional
content_hash: 1ec5f586933dd052c291f94ef0045fc0a96fa54ffcc1d7e987fc4f5e50676e8b
fetched_at: '2026-06-28T22:39:37.579436+00:00'
product: protheus
section_id: 1500001538461
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como calcular ICMS
  ST sem calcular ICMS próprio para fornecedor Simples Nacional?
type: support-article
updated_at: '2023-11-16T20:39:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051854113-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-calcular-ICMS-ST-sem-calcular-ICMS-pr%C3%B3prio-para-fornecedor-Simples-Nacional
---

**Dúvida**

Como calcular ICMS ST sem calcular ICMS próprio para fornecedor Simples Nacional?  
  
**Ambiente**Protheus - Fiscal – A partir da versão 11.80  
  
**Solução :**

**1. Cadastro do Fornecedor**

Aba > outros> campo Opt Simp Nac  ( A2\_SIMPNAC )**= Sim**

**2. Cadastro da TES**

**Calcula ICM (F4\_ICM)=** Não **L Fisc ICMS (F4\_LFICM)=** Outros  **Agrega valor (F4\_AGREG)=** Sim

**AGREGA SOLID** = SIM

**Sit trib ICM (F4\_SITTRIB)=** Vazio

**ICMS s/ ST (F4\_ICMSST)=** Vazio

**Marg Solid (F4\_MKPSOL)=** Vazio

**LF ICMS-ST (F4\_LFICMSST)=** Não

**DED ICM ST** = VAZIO

**3. Evidencia**

41% MVA no produto > aba imposto > Solid.Entr.

12% credito de ICMS próprio abatido no valor do ICMS ST

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079660834)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080741513)
