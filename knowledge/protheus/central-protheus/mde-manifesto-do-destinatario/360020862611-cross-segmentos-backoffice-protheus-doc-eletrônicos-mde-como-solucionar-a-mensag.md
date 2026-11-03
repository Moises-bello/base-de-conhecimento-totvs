---
article_id: 360020862611
category: MDe - Manifesto do Destinatario
content_hash: 67e12d31c7e2f6eb829e29d2b1d8f879977d3d20450c6977ed68cad5cab24b40
fetched_at: '2026-06-28T22:40:09.247184+00:00'
product: protheus
section_id: 1500001549162
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - MDE - Como solucionar
  a mensagem 006 - Não é possível enviar o mesmo evento de Manifestação
type: support-article
updated_at: '2025-06-10T17:53:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020862611-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-MDE-Como-solucionar-a-mensagem-006-N%C3%A3o-%C3%A9-poss%C3%ADvel-enviar-o-mesmo-evento-de-Manifesta%C3%A7%C3%A3o
---

**Dúvida**

Como solucionar a mensagem ao manifestar:  **006 - Não é possível enviar o mesmo evento de Manifestação**

**Ambiente**

Cross Segmentos - Backoffice Protheus - Todas as versões   
  
**Solução**

Esta mensagem é apresentada ao tentar manifestar uma nota que já consta o mesmo evento na Sefaz, pois para a Sefaz pode ser realizada mais de uma manifestação desde que **sejam diferentes.**

Será necessário tentar manifestar uma nota por vez para saber qual apresenta esse retorno, após isso através da chave  realize a consulta no site da Sefaz, assim irá verificar se realmente já consta a manifestação dessa nota junto a Sefaz referente a essa operação.

Na tabela SPED154 é possível realizar um filtro pela chave da nota no campo NFE\_CHV e pelo evento TPEVENTO= 210200, 210210, 210220, 21040 haverá o campo PROTOCOLO preenchido com retorno do protocolo do envio do evento vinculado.

* **Os eventos da Sefaz para o manifesto do destinatário são:**

* **210200 Confirmação da operação**
* **210210 Ciência da operação**
* **210220 Desconhecimento da operação**
* **21040 Operação não realizada**

Caso queira enviar um novo evento deve ser diferente do já vinculado junto a Sefaz.
