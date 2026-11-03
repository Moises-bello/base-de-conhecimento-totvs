---
article_id: 360023358131
category: Ativo Fixo - Ampliação
content_hash: cd258d30c24d903499f5bf4df2ff1255a6d9e56742abd1e118679312ce070b1b
fetched_at: '2026-06-28T22:41:58.170524+00:00'
product: protheus
section_id: 1500001535321
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA050 - O QUE CAUSA
  O HELP: ATF150AD?'
type: support-article
updated_at: '2023-11-20T16:04:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023358131-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA050-O-QUE-CAUSA-O-HELP-ATF150AD
---

**Dúvida**

O QUE CAUSA O HELP: *ATF150AD?*

***![](https://atendimento.totvs.com/attachments/token/Q90qagVOPwwOhHMaXg0ibnFvB/?name=image002.png)***

**Ambiente**Microsiga Protheus – Ativo Fixo – A partir da versão 11.80

**Solução**

 Configuração do parâmetro **MV\_ULTDEPR**, onde este deve possuir data final do mês anterior ao mês em que será executada a depreciação.  
  
Exemplo:  
  
Se a depreciação será aplicada em 31/12/20XX, o parâmetro **MV\_ULTDEPR** deve  conter a data para 20XX1130.

 Diante disso a operação só poderá ser realizada data posterior ao ultimo calculo de depreciação
