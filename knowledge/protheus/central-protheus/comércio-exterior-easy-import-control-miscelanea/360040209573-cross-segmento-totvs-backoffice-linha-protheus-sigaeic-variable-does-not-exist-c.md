---
article_id: 360040209573
category: Comércio Exterior - Easy Import Control - Miscelanea
content_hash: 5200f050b2234467f6b4378ed97331459171d7a039c748572509b184bca4790a
fetched_at: '2026-06-28T22:39:42.037632+00:00'
product: protheus
section_id: 1500001549702
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Variable does
  not exist CARQ on IN100CONTROL
type: support-article
updated_at: '2022-06-02T12:45:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040209573-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Variable-does-not-exist-CARQ-on-IN100CONTROL
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Variable does not exist CARQ on IN100CONTROL  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Easy Import Control - Todas as versões  
  
**Solução**

1 .Acesse o configurador, Ambiente - Cadastro - Parâmetros

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044308553/mceclip1.png)

2. Selecione a ![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043462814/mceclip2.png)e Procurar por:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043462874/mceclip3.png)

 3. Verifique as configuração dos parâmetros MV\_AVG0097,  caso esteja Habilitado 'T" *True*, será apresentado o error.log, Desabilite o parâmetro 'F' *False*, saia da rotina e acesse novamente e faça a integração.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360053598813/mceclip1.png)

Para correção do incidente foi aberta a Issue  DTRADE-3667, e a correção esta contemplada no pacote acumulado do Comex: [Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Pacote Acumulado Comex](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047332793)
