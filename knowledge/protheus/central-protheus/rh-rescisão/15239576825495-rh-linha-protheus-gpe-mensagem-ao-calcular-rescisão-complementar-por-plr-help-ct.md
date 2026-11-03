---
article_id: 15239576825495
category: RH - Rescisão
content_hash: dbea387e68d929b79630e4af9b37f4b9a24b6e9c14cacc7930a9876a7a24d085
fetched_at: '2026-06-28T22:43:52.219904+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: 'RH - Linha Protheus - GPE - Mensagem ao calcular rescisão complementar por
  PLR: Help CTB105CC'
type: support-article
updated_at: '2024-10-04T14:58:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15239576825495-RH-Linha-Protheus-GPE-Mensagem-ao-calcular-rescis%C3%A3o-complementar-por-PLR-Help-CTB105CC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15239604405783) Tempo aproximado para leitura: **01:30 min** **Dúvida**Por que ao calcular rescisão complementar por PLR, rescisão só calcula uma verba e apresentam mensagem: Help CTB105CC - Problema: O campo RGB\_CC não pertence ao modelo?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15239378477719)  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.  
  
**Solução**A rescisão complementar por PLR apresenta a mensagem devido a configuração dos campos RR\_CC e RGB\_CC. Para o cálculo ocorrer corretamente, ambos devem estar em prioridade como Alterar.

Após edição dos campos em configurador SIGACFG, o módulo SIGAGPE deve ser reiniciado e acessar a rotina de rescisão.

**RGB\_CC**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15239505034903)

**RR\_CC**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15239513893783)

**Saiba mais**Para adquirir maior conhecimento acesse os *links* abaixo:

[RH - Linha Protheus - GPE - Como calcular PLR para funcionário desligado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115013033127-RH-Linha-Protheus-GPE-Como-calcular-PLR-para-funcion%C3%A1rio-desligado)
