---
article_id: 360056359073
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: 1aaf937ca74ccf9f0feed41aaff811aba86aa7c593b4e042c9f16bb03d2ea22b
fetched_at: '2026-06-28T22:39:50.097999+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Inclusão de frete
  no cadastro de despesa
type: support-article
updated_at: '2022-04-27T20:53:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056359073-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Inclus%C3%A3o-de-frete-no-cadastro-de-despesa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**No cadastro de despesas, o frete foi excluído por engano sendo que o processo de embarque já foi finalizado. Porém ao tentar incluir novamente o sistema exibe uma mensagem de caráter impeditiva:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360092219674/mceclip0.png)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões  
  
**Solução**O valor da despesa que está sendo lançado em reais tem de bater com o valor do frete da capa do processo, da soma dos campos SW6->W6\_VLFRECC + SW6->W6\_VLFREPP, multiplicado pela taxa do frete SW6->W6\_TX\_FRET (aba 'Transporte' na rotina de manutenção de Desembaraço). Ou seja o valor que esta sendo informado em reais no cadastro despesas não bate com o que foi informado no capa do processo (Pasta Transporte na Manutenção do Desembaraço).
