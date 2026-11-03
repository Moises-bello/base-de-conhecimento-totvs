---
article_id: 360024056492
category: Faturamento - Cenários de Venda
content_hash: 198d33c081e39c5aea46c24d60cdfabc00ff55fa1a89cacf751b6ae068c10aea
fetched_at: '2026-06-28T22:38:33.928382+00:00'
product: protheus
section_id: 1500001550382
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ao incluir o
  mesmo item mais de uma vez na tabela de preço, apresenta o Help Uniqueline
type: support-article
updated_at: '2023-01-31T12:40:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024056492-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ao-incluir-o-mesmo-item-mais-de-uma-vez-na-tabela-de-pre%C3%A7o-apresenta-o-Help-Uniqueline
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Ao incluir o mesmo item mais de uma vez na tabela de preço, apresenta o **Help Uniqueline**, como resolver?   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – Faturamento – A partir da versão 11.80  
  
**Solução**O **Help Uniqueline** é reproduzido se incluir o mesmo produto com a mesma data de vigência.  
Observe, que em meu teste o produto SEMENTES esta em duplicidade com a data vigência de 01/02/2018 e ele apresenta o Help:  
![h1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360022307871/h1.png)​  
  
Se a data de vigência for diferente ele permite os dois itens:  
![h2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360022307891/h2.png)​  
  
Eu consigo incluir mais de uma linha do mesmo produto?  
A resposta é por vigência de preço: ou seja posso ter dois produtos cadastrados na tabela de preço sendo que sua data de vigência for diferente assim como seu preço de venda. Para que o sistema pegue um valor a partir da primeira vigência vencida e quando chegar na data de vigência do outro item começara a pegar o valor do 2 item com preço diferente. Esse processo e utilizado para fazer promoções relâmpagos ou semanais na tabela de preço do sistema.

**Saiba Mais:**  
Caso realmente não possa deixar que os usuários incluam o mesmo produto mais de uma vez. Pode utilizar o ponto de entrada a seguir:

**OM010LOK: <http://tdn.totvs.com/pages/releaseview.action?pageId=6091274>**

Valida a linha dos itens, podendo contar validação própria dentro do ponto de entrada para atender alguma necessidade especifica.
