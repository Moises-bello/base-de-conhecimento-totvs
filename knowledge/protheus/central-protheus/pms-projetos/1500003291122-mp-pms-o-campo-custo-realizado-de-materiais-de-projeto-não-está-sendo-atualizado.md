---
article_id: 1500003291122
category: PMS - Projetos
content_hash: 6e2d8f39b154960b8b3dbbda283cad4cf56e3fad2c1ba71b8aedd3758829b46e
fetched_at: '2026-06-28T22:37:15.029366+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: MP - PMS - O campo custo realizado de materiais de projeto não está sendo atualizado.
type: support-article
updated_at: '2021-04-28T15:20:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003291122-MP-PMS-O-campo-custo-realizado-de-materiais-de-projeto-n%C3%A3o-est%C3%A1-sendo-atualizado
---

**Dúvida**O campo "**Custo Realizado**" não esta somando os custos realizados com materiais, tipo documento de entrada amarrado no projeto, porém, esta considerando apenas os custos com recurso e OP.   
  
**Ambiente**

Microsiga Protheus - todos os releases.

**Solução**

Avalie o cadastro de **TES (MATA080)**, verifique se o campo **F4\_BONIF** (**Bonificação**, aba outros) está como Sim, deixe-o como Não para gerar o custo...

Segue informações sobre o campo **F4\_BONIF**: Indica se o item da NF de compra é uma bonificação. O tratamento para cálculo do custo do item seguirá a seguinte regra:

- Se o conteúdo do campo for "**Sim**", *o custo do item será zerado*, caracterizando uma entrada por bonificação.

- Se o conteúdo do campo for "**Não**" ou  vazio, *o custo do item será calculado normalmente* seguindo as configurações do TES.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360104356793/mceclip0.png)

**Saiba mais sobre tratamento de custo no PMS:**

**[MP-PMS-Custos-de-Projetos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018868692-MP-PMS-Custos-de-Projetos)**

**[MP-PMS-CUSTO-STANDARD-DO-RECURSO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048564493-MP-PMS-CUSTO-STANDARD-DO-RECURSO)**

**[MP-PMS-MV-PMSCUST-](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039417114-MP-PMS-MV-PMSCUST-)**

**[MP-PMS-Como-calcular-o-Custo-Realizado-do-Projeto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044319034-MP-PMS-Como-calcular-o-Custo-Realizado-do-Projeto)**
