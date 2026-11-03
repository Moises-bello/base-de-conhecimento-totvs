---
article_id: 360036278633
category: MDT - Atendimento Médico
content_hash: 328ce1f4f25d7bc89f297b5b69397c66bca3ceb5195465aa0f1c4fab62b50a66
fetched_at: '2026-06-28T22:44:20.715030+00:00'
product: protheus
section_id: 360010945694
source: central-protheus
title: RH - Linha Protheus - MDT - eSocial - Integração entre MDT x GPE x TAF lançamentos
  de atestado com afastamentos sem data fim.
type: support-article
updated_at: '2024-07-30T20:29:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036278633-RH-Linha-Protheus-MDT-eSocial-Integra%C3%A7%C3%A3o-entre-MDT-x-GPE-x-TAF-lan%C3%A7amentos-de-atestado-com-afastamentos-sem-data-fim
---

**Dúvida**Como funciona os afastamentos com  os módulos GPE e TAF integrados com o modulo do MDT?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**1. Incluir um afastamento na rotina "Atestado Medico" (MDTA685)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046749194)  
2. Nas abas  "Afastamento" e "Outros"  preencher os campos necessários e confirme.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047614593)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047614773)

3 Nesta tela o sistema ira apresentar a mensagem integrado com o TAF. ![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046749554)

4. No modulo do GPE, na rotina de ausências (GPEA240), o funcionário ficará com status de afastado.

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047615613)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047615653)

5. No modulo TAF existirá um registro no evento S-2230 pendente de transmissão e sem data fim conforme inclusão do atestado medico.

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046750154)

Modulo TAF- (TAFA261).

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047615893)

6. Quando existir a data fim deverá alterar o mesmo registro no modulo do MDT, informar as datas fim em ambas as abas e confirme.

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047616293)

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046750474)

![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046750694)

7. Veja que no GPE o registro foi inserida sua data fim.

![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047616673)

8. No TAF criado um registro com status termino do afastamento pendente para transmissão.

![mceclip14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047616773)

**Saiba Mais**[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
