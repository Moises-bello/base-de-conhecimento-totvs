---
article_id: 360057602534
category: RH - Rescisão
content_hash: 24bbd4b728965ea963701ebaedd1cdb866fade6d8733790def01ed6e9c6f2c3d
fetched_at: '2026-06-28T22:43:53.639895+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Por que o cálculo de rescisão aviso trabalhado
  não apresenta ID saldo de salário 0048
type: support-article
updated_at: '2025-05-07T21:17:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057602534-RH-Linha-Protheus-GPE-Por-que-o-c%C3%A1lculo-de-rescis%C3%A3o-aviso-trabalhado-n%C3%A3o-apresenta-ID-saldo-de-sal%C3%A1rio-0048
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19349482149527) Tempo aproximado para leitura: **00:01:30 min**

**Dúvida**Por que o cálculo de rescisão aviso trabalhado não apresenta ID saldo de salário 0048?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Para aviso trabalhado o sistema apresenta o valor dos dias trabalhados no ID 0112 (aviso prévio trabalhado), pois na Tabela S043 a coluna aviso prévio está configurado com T e a coluna Saldo de salário com N.

**Exemplo:**

**Tabela S043**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099970553)**

**Rescisão**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097692594)

Obs: Para rescisão aviso trabalhado apresentar verba saldo de salário ID 0048, em tabela S043 tipo de rescisão aviso trabalhado mantenha T em coluna aviso e S em saldo de salário.

**Saiba mais**Para adquirir maior conhecimento acesse o *link* abaixo:

[MP - GPE - Como cadastrar um novo tipo de rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004395831-MP-GPE-Como-cadastrar-um-novo-tipo-de-rescis%C3%A3o?source=search)

[RH - Linha Protheus - GPE - Como parametrizar o sistema para rescisão por acordo aviso trabalhado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059768093-RH-Linha-Protheus-GPE-Como-parametrizar-o-sistema-para-rescis%C3%A3o-por-acordo-aviso-trabalhado?source=search)
