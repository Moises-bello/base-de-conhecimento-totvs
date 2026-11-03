---
article_id: 360024874813
category: Manutenção de Ativos (SIGAMNT)
content_hash: d1e3b1e5a23421deedfc2bd966cce3909b0f0f54f6a17d2a24968044ede3e55c
fetched_at: '2026-06-28T22:42:34.346603+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Preenchimento do campo Categoria do Bem
type: support-article
updated_at: '2021-09-10T20:35:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024874813-Manufatura-Linha-Protheus-MNT-Preenchimento-do-campo-Categoria-do-Bem
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:00:41 min**  
**Dúvida**Como funciona o preenchimento do campo **Categoria do Bem - T9\_CATBEM**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Todas as versões  
  
**Solução**Não é necessário informar o campo **Categoria do Bem**. Como estes cadastros são específicos, este campo é preenchido automaticamente, conforme o cadastro realizado:

* Quando realizado a inclusão de um bem pela rotina padrão de **Bens - MNTA080** a categoria do bem será igual a **1 – Bem**;
* Quando a inclusão for de **Veículo - MNTA084**, ele recebe a informação de categoria de bem igual a **2 – Frota integrada ao TMS** ou **4 – Frota não integrada ao TMS**.
* Quando incluído um **Pneu - MNTA083**, a categoria atribui a informação **3 – Pneus**.
