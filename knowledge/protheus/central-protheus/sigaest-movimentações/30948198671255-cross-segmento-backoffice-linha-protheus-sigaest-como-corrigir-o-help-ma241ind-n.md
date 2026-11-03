---
article_id: 30948198671255
category: SIGAEST - MOVIMENTAÇÕES
content_hash: da945f3f526dcc0064075ef7244117d0558567110106cacfdba2317b4e03ff93
fetched_at: '2026-06-28T22:38:54.374500+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como corrigir o HELP
  MA241IND na rotina Movimentação Interna?
type: support-article
updated_at: '2025-03-26T19:54:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30948198671255-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-corrigir-o-HELP-MA241IND-na-rotina-Movimenta%C3%A7%C3%A3o-Interna
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30948220566295) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Ao fazer uma movimentação interna, com um produto indireto(**B1\_APROPRI**) preenchido informando um OP ocorre o HELP ***MA241IND***, como corrigir?    
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**Produto de apropriação indireta não se usa OP. O conceito de produtos de apropriação indireta é única e exclusivamente para delegar o saldo requisitado para o armazém de processo (MV\_LOCPROC).   
  
Se o seu produto vai direto ser requisitado para uma OP, conceitualmente ele não pode ser de apropriação indireta (B1\_APROPRI = I).  
  
Para entender mais sobre o conceito de produto de apropriação indireta, recomendo a leitura desta documentação:

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Conceito e usabilidade de Apropriação Indireta (MV\_LOCPROC)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020688571-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Conceito-e-usabilidade-de-Apropria%C3%A7%C3%A3o-Indireta-MV-LOCPROC)

**Saiba Mais:**

[Clique aqui e acesse mais artigos sobre Movimentação no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
