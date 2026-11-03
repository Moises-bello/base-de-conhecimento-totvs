---
article_id: 360052656313
category: RH - Dissídio
content_hash: 519ff3a3ee73947bdd178891787caf9c5f7f29609a74fb9835ef47b34fae286a
fetched_at: '2026-06-28T22:43:43.523732+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - Como calcular INSS outras entidades (terceiros)
  em dissídio retroativo quando houve mudança de percentual
type: support-article
updated_at: '2021-04-30T00:10:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052656313-RH-Linha-Protheus-GPE-Como-calcular-INSS-outras-entidades-terceiros-em-diss%C3%ADdio-retroativo-quando-houve-mudan%C3%A7a-de-percentual
---

**Dúvida**Como calcular INSS outras entidades (terceiros) em dissídio retroativo quando houve mudança de percentual?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Crie linha na Tabela S038, contendo o percentual INSS outras entidades (terceiros) da folha de pagamento referente ao dissídio retroativo e linha contendo o percentual atual.

**Exemplo:**

**Tabela S038**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360082894914/mceclip0.png)**

No exemplo acima na tabela S038 foi criada linha para o mês 06.2020 com o percentual 5,88 e linha com o campo em branco mês \ ano contendo o percentual 4,55.

No cálculo do dissídio retroativo, o sistema irá considerar para cálculo das diferenças outras entidades no mês 06.2020 o percentual de 5,88 e aos demais meses o percentual de 4,55.
