---
article_id: 38824453140887
category: SIGAACD - Automação e Coleta de Dados
content_hash: 387152e2f2b24c5d857bf604ccf69175b105c0a4f98381c34ec815f1fcca48b4
fetched_at: '2026-06-28T22:39:13.788459+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Qual licença utilizar
  no coletor TELNET do SIGAACD?
type: support-article
updated_at: '2026-03-05T14:39:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38824453140887-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Qual-licen%C3%A7a-utilizar-no-coletor-TELNET-do-SIGAACD
---

As licenças necessárias para usar o TELNET do ACD no Protheus são TOTVS FULL, TOTVS T e TOTVS I. Ao acessar as rotinas ACDV020, ACDV023 e ACDV025, ocorre consumo de licenças do Intera Manufatura devido ao apontamento de produção do módulo PCP via Telnet.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38824464144023) Tempo aproximado para leitura: 00**:**01:00 min  
  
**Dúvida**  
Qual licença é necessária para utilização do coletor  **TELNET do SIGAACD (Automação e Coleta de Dados)** no Protheus?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**  
As licenças para o uso do **TELNET do SIGAACD** são:

* TOTVS **FULL**
* TOTVS **T**
* TOTVS **I**

**Observação:**

Ao acessar as rotinas **ACDV020**, **ACDV023** e **ACDV025**, são executadas rotinas automáticas de **apontamento de produção do módulo PCP**, que são programadas para utilização via **Telnet**.

Devido a essa característica, durante a execução dessas rotinas ocorre o **consumo de licenças do Intera Manufatura**.

Rotinas relacionadas:

* **ACDV020** – Apontamentos Simples (**MATA250**)
* **ACDV023** – Produção PCP Mod I (**MATA680**)
* **ACDV025** – Produção PCP Mod II (**MATA681**)

**Saiba mais:**

[Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Qual licença utilizar no aplicativo Meu Coletor de Dados?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411627803415-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Qual-licen%C3%A7a-utilizar-no-aplicativo-Meu-Coletor-de-Dados)

[*Clique aqui e veja mais artigos sobre Automação e Coleta de Dados*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
