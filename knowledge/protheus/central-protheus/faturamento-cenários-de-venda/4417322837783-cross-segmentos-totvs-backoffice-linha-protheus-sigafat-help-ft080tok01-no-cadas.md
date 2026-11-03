---
article_id: 4417322837783
category: Faturamento - Cenários de Venda
content_hash: b41b660ee7ff8f3ea500eea59cf07b5e8ea9b0abfe930a7261e98b444f92d3e8
fetched_at: '2026-06-28T22:38:34.110677+00:00'
product: protheus
section_id: 1500001550382
source: central-protheus
title: 'Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Help: FT080TOK01
  no cadastro de Regras de Desconto (FATA080)'
type: support-article
updated_at: '2022-12-12T14:59:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4417322837783-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Help-FT080TOK01-no-cadastro-de-Regras-de-Desconto-FATA080
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao realizar o cadastro de uma Regra de Desconto (FATA080) o sistema não permite salvar o registro e apresenta o help **FT080TOK01**: "Regra de desconto já cadastrada anteriormente. Cod. Regra: X"  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões  
  
**Causa**Isso ocorre quando se tenta cadastrar duas regras que se conflitam, ou seja, uma regra determina que o produto X de ter 5% de desconto, por exemplo, caso tente cadastrar uma nova regra que indique que esse mesmo produto X deve ter 7% de desconto, as duas regras entram em conflito e o sistema não permite o cadastro.  
  
**Solução**Altere a regra que o sistema indica no Help ou modifique algum dado da regra que esta cadastrando para que não entre em conflito com as demais:

![FT080TOK01.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/4417349540631/FT080TOK01.jpg)

**Saiba mais**: [Regras de Desconto (FATA080)](https://tdn.totvs.com/x/dQ5dDg)
