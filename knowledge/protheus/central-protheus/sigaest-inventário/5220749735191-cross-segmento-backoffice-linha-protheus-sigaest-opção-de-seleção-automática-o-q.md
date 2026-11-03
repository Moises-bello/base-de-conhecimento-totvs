---
article_id: 5220749735191
category: SIGAEST - INVENTÁRIO
content_hash: e7d8a721b7445bdaf6e697af926aefe6be2a73375866c19a1466ebd24d19a63c
fetched_at: '2026-06-28T22:38:50.437842+00:00'
product: protheus
section_id: 1500001538961
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Opção de Seleção automática
  o que ocorre quando consta apenas 1 contagem?
type: support-article
updated_at: '2022-04-04T19:44:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5220749735191-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Op%C3%A7%C3%A3o-de-Sele%C3%A7%C3%A3o-autom%C3%A1tica-o-que-ocorre-quando-consta-apenas-1-contagem
---

**Dúvida**Com o MV\_CONTINV = T qual o comportamento padrão da rotina MATA270 ao Selecionar automaticamente as contagens de inventário e constar apenas 1 contagem?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

Nesse cenário de exemplo abaixo, foi digitado no Armazém 01 apenas 1 contagem para o produto 542:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5220985882775/mceclip0.png)

Após selecionar a opção de Seleção Automática parametrizar com a data de seleção automática:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5222147783191/mceclip1.png)

Dessa forma, é considerado a contagem única automaticamente. Veja o resultado abaixo.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5222304480023/mceclip2.png)

**Esse comportamento é padrão na rotina. Mesmo que não tenha uma outra contagem o sistema entende que deve selecionar a contagem única automaticamente. Permitindo dessa forma que efetue inventário com apenas uma contagem e com o parâmetro MV\_CONTINV habilitado.**

**Saiba Mais:**  
*[Clique aqui e veja mais artigos sobre Inventario no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538961-SIGAEST-INVENT%C3%81RIO)*
