---
article_id: 360020593011
category: Contabilidade Gerencial - Relatórios Razões
content_hash: 2df667efddf06978e5c98c44074291bc267848f4d409336ceade35d5c522cfba
fetched_at: '2026-06-28T22:40:41.105351+00:00'
product: protheus
section_id: 1500001548782
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus  - SIGACTB CTBR404 Como o relatório
  demonstra os lançamentos de partida simples.
type: support-article
updated_at: '2022-06-10T23:20:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020593011-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBR404-Como-o-relat%C3%B3rio-demonstra-os-lan%C3%A7amentos-de-partida-simples
---

***Relatório Razão Plano Referencial (CTBR404)*** **Dúvida**Como o relatório demonstra os lançamentos de partida simples?  
   
 **Ambiente**Protheus – Contabilidade Gerencial – A partir da versão 11.80  
  
   
**Solução**

A coluna " Contra Partida" do relatório CTBR404 considera apenas lançamentos de partida dobrada  (CT2\_DC= 3), pois considera apenas 1 linha por movimento (CT2\_LINHA).

No caso de partida simples, o sistema demonstrará as operações a créditos, separadamente conforme a respectiva linha, exemplo:

![](https://totvssuporte.zendesk.com/attachments/token/cK5cEph6VSOsI0IaGaBRNK1Dw/?name=inline1070975823.png)

Na partida dobrada, caso não filtre uma conta referencial, o sistema irá trazer o lançamento de partida dobrada para as 2 contas referenciais relacionadas ao lançamento.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360016531491/mceclip0.png)

Importante!

Ao filtrar por conta referencial, o sistema irá demonstrar as linhas do lote que possuem essa referencial como amarração (CVD). Mesmo que esteja no mesmo lote se a conta contábil não tiver a respectiva amarração, não será demonstrada.

![](https://totvssuporte.zendesk.com/attachments/token/RS35bdcehwFfm9huTBcZ86a0o/?name=inline-981787177.png)
