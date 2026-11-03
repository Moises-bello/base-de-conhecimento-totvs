---
article_id: 21494389689111
category: MDT - PCMSO
content_hash: 57d12ec59ad7262ae0108d5e8769e7711c0cd5cdab151cf28b15658cf9d29aab
fetched_at: '2026-06-28T22:44:28.314868+00:00'
product: protheus
section_id: 360010945214
source: central-protheus
title: RH - Linha Protheus - MDT - Ao tentar incluir exames e acessar fornecedor de
  exames ocorre o error log Called from J98F3SA2(JURA098.PRW)
type: support-article
updated_at: '2025-09-03T14:16:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21494389689111-RH-Linha-Protheus-MDT-Ao-tentar-incluir-exames-e-acessar-fornecedor-de-exames-ocorre-o-error-log-Called-from-J98F3SA2-JURA098-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21494364336791) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Error log - Ao tentar incluir exames e acessar fornecedor de exames ocorre o error log Called from J98F3SA2(JURA098.PRW)  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Causa**Esse erro ocorre quando o campo Fornecedor na tabela TM5 - TM5\_FORNEC esta utilizando consulta padrão fora do padrão do modulo. Este campo busca a consulta padrão da tabela NGE.

O erro pode ser apresentado em cliente que migrarão a base de LOGIX para PROTHEUS e utilizam banco Informix.  
  
**Solução**Alterar via configurador o campo **Fornecedor - TM5\_FORNEC, com as consulta padrão correta NGE- Fornecedor**.

No configurador **SIGACFG> Base de dados> Dicionários> Base de dados > TM5 > TM5\_FORNEC**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/21494932347543)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/21494988098583)**

**Vá na aba : Opções e edite o campo Cons  Padrão para NGE:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21494932358167)  
  
**Saiba Mais**[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
