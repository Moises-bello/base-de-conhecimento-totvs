---
article_id: 360028749311
category: ADVPL - Rotina Automática
content_hash: 191cf52a16ee77d313676ee532efd4ef7a03f405b078bb2e36c7a74c08cfde6c
fetched_at: '2026-06-28T22:40:25.065972+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Tabela de preço
  via execauto
type: support-article
updated_at: '2022-06-21T17:25:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028749311-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Tabela-de-pre%C3%A7o-via-execauto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Ao gerar pedido de venda via execauto, o sistema não respeita a tabela de preço.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus – ADVPL – A partir da versão 12  
  
**Solução**Para que a rotina automática  **MATA410,** considere o valor da tabela de preço, é necessário que realize um posicionamento na tabela **DA1,** e traga o preço de venda configurado para o produto que vai ser incluído no pedido de venda**.** Com os dados da tabela de vendas posicionada, você deve realizar o calulo (**Q****uantidade \* Preço de venda).**Embora você esteja informando a tabela de preço no array correspondente ao cabeçalho, a execauto vai considerar sempre os valores que você informar no array correspondente aos itens.
