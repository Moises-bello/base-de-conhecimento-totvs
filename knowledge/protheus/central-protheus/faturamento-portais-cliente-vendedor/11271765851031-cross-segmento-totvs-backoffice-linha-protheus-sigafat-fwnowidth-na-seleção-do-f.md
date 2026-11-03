---
article_id: 11271765851031
category: FATURAMENTO - PORTAIS (Cliente, Vendedor)
content_hash: e0b33a75063af0588fda2b18cebe8ebe3ff5c38cdaf8a403ac3923db34960791
fetched_at: '2026-06-28T22:38:23.885015+00:00'
product: protheus
section_id: 1500001539321
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT-FWNOWIDTH na seleção
  do fornecedor no cadastro de usuário de portal
type: support-article
updated_at: '2022-12-28T14:29:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11271765851031-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-FWNOWIDTH-na-sele%C3%A7%C3%A3o-do-fornecedor-no-cadastro-de-usu%C3%A1rio-de-portal
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Ao selecionar o código do fornecedor no usuário de portal, gera o help: **FWNOWIDTH**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11271201726487)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões  
  
**Solução**

O help ocorre por que o campos **A2\_NOME** está com um tamanho maior que o campo **AI5\_NOMFOR**, gerando o conflito, por padrão o nome do fornecedor vem com 40 caracteres e o campo nome do fornecedor no cadastro de usuário de portal vem com 30 caracteres. Desta forma, para evitar o help ajuste ambos os campos com a mesma quantidade de caracteres, conforme o exemplo abaixo:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11271346306839)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11271397714327)
