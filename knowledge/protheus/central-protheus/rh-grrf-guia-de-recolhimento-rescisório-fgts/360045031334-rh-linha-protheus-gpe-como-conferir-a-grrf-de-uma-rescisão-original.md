---
article_id: 360045031334
category: RH - GRRF (Guia de Recolhimento Rescisório - FGTS)
content_hash: c8f03b77890532c67f1b27066c08e0729e5c5063babd94fe6ded441946960863
fetched_at: '2026-06-28T22:43:32.390738+00:00'
product: protheus
section_id: 360010781714
source: central-protheus
title: RH - Linha Protheus - GPE - Como conferir a GRRF de uma rescisão original
type: support-article
updated_at: '2021-04-30T18:20:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045031334-RH-Linha-Protheus-GPE-Como-conferir-a-GRRF-de-uma-rescis%C3%A3o-original
---

**Ocorrência**Como conferir a GRRF de uma rescisão original?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão Pessoal - A partir da versão 12  
  
**Solução**Identifique dentro do cálculo as verbas com SIM para FGTS, para diagnosticarmos os identificadores de cálculo envolvidos. Na rescisão será apresentado os **Ids 0293 e 0294** a soma de todas as verbas que estão com SIM para FGTS.  
Para a geração da GRRF é separado os valores das verbas que pertencem a rescisão e Aviso prévio.  
  
**Rem. Mês. Resc.”  =** (Id 0293 + Id 0294) – (Id 0111 + Id 0115 + Id 0250 + id 0252 + id 0253 + id 0230 + Id 0231).  
  
**Cálculo Av. Prévio -** 0111 de Aviso Prévio, 0115 de 13º Sobre o Aviso Prévio, 0250 de Média sobre Aviso Prévio, 0252 Média de férias sobre aviso prévio, 0253 de Média de 13º salário sobre aviso prévio, 0230 férias sobre aviso prévio e 0231 1/3 férias sobre aviso prévio.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360062294294/mceclip0.png)  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360062294374/mceclip1.png)  
  
Memória de Cálculo:  
**Rem Mês Resc**  
213,13 + 84,71 + 282,36 + 710, 44 = **1290,64**  
  
**Aviso Prévio**  
1524,72 + 127,06 + 423,53 + 5082,39 = **7157,70**

Log de ocorrência da GRRF

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360062294614/mceclip2.png)

Validador GRRF

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360063186893/mceclip3.png)
