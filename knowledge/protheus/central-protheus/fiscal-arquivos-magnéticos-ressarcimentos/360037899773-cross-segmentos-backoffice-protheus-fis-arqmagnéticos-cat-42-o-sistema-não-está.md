---
article_id: 360037899773
category: Fiscal Arquivos Magnéticos - Ressarcimentos
content_hash: 8ff556f64c724d64866a7c711f9bf418920c803a07a1a8c2f3899909bdbaa676
fetched_at: '2026-06-28T22:42:12.685820+00:00'
product: protheus
section_id: 1500001546642
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - CAT 42 - O sistema
  não está considerando o saldo inicial lançado manualmente na rotina.
type: support-article
updated_at: '2022-08-18T17:55:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037899773-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-CAT-42-O-sistema-n%C3%A3o-est%C3%A1-considerando-o-saldo-inicial-lan%C3%A7ado-manualmente-na-rotina
---

**Ocorrência**O sistema não está considerando o saldo inicial lançado manualmente na rotina através da opção "**Saldos Iniciais**".

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049021914/mceclip1.png)  
   
 **Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
   
 **Causa**   
 Esse incidente ocorre, pois a lançamento do saldo inicial foi realizado no período incorreto (dezembro de 2018).  
   
 **Solução**  
 Para solucionar essa ocorrência, realize os seguintes passos:  
  
 1. Verifique se o lançamento do saldo foi realizado no período correto. Se o período que será apurado é Janeiro de 2019, então, a data do lançamento manual do saldo inicial deverá obrigatoriamente ser Janeiro de 2019 e não dezembro de 2018;

2. Caso o lançamento de fato tenha sido realizado no período errado, realize a exclusão do mesmo e inclua um novo lançamento preenchendo o campo "Ano/Mês" (**campo F2V\_ANOMES**) com a data correta, 2019/01.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049022894/mceclip2.png)
