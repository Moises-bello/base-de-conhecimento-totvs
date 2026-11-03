---
article_id: 15129412292375
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: a981cb85587488a41828eac2d97bb4089819486c30d72b67314e8528bde1a187
fetched_at: '2026-06-28T22:38:42.518604+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) – SIGAFAT – Preço (C6_PRCVEN)
  do item na devolução de compras diferente da nota fiscal de entrada
type: support-article
updated_at: '2025-10-23T18:55:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15129412292375-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFAT-Pre%C3%A7o-C6-PRCVEN-do-item-na-devolu%C3%A7%C3%A3o-de-compras-diferente-da-nota-fiscal-de-entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15255225432855) Tempo aproximado para leitura: **00:01:30 min**

**Dúvida**

Alterei o preço de venda (C6\_PRCVEN) e não consigo salvar o pedido de vendas de devolução, o valor do item está diferente da entrada, o que fazer?

**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Todas as versões

**Solução**

Ao devolver um documento de entrada, o preço correto vem automaticamente ao escolher a nota fiscal de origem. O preço ao retornar o pedido de vendas, é pego da entrada, no campo "D1\_VUNIT".

Comportamento caso o documento de entrada NÃO tenha descontos:

* (D1\_VUNIT) → (C6\_PRUNIT)
* (D1\_VUNIT) → (C6\_PRCVEN)

Comportamento caso o documento de entrada tenha descontos:

* (D1\_VUNIT) → (C6\_PRUNIT)
* (D1\_VUNIT - D1\_VALDESC) → (C6\_PRCVEN)
* (D1\_VALDESC) → (C6\_VALDESC)

**OBSERVAÇÃO:** Na devolução, altera-se a quantidade (C6\_QTDVEN), o preço gatilhado no campo "C6\_PRCVEN" deve ser mantido.

**O preço de venda no pedido de venda de devolução, CASO TENHA DESCONTOS deve já conter o desconto da entrada, ficando diferente do documento de entrada exemplo:**

**(1)** Entrada:

* Preço do item na entrada: R$100 (D1\_VUNIT)
* Desconto do item na entrada: 10% (D1\_VALDESC)

**(2)** Ao devolver o pedido de venda, o preço gatilhado (que deve ser usado) é:

* Preço do item no retorno: R$90 (C6\_PRCVEN) [diferente porém correto pois o desconto age sobre]
* Desconto do item no retorno: R$10 (C6\_VALDESC)
* Preço do item no retorno: R$100 (C6\_PRUNIT)

**O preço idêntico a entrada, na devolução, permanece no campo de preço de lista [C6\_PRUNIT] para sair na DANFE idêntico a entrada.**

Quando há desconto e o preço de venda fica diferente da entrada e o mesmo é alterado para ficar idêntico ao preço da entrada, pode gerar os erros **"A410TOTDPRC"** e **"A410TOTAL"**.

Esse comportamento ocorre pois no faturamento (SIGAFAT) o desconto é aplicado sobre o preço de venda [C6\_PRCVEN], e o no módulo de compras (SIGACOM) o desconto é aplicado sem alterar o preço de entrada.

Exemplo de nota fiscal de entrada e pedidos de venda do tipo devolução de compras **COM** descontos:

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/15255499144599)![](https://centraldeatendimento.totvs.com/hc/article_attachments/15255489518359)**

Exemplo de nota fiscal de entrada e pedidos de venda do tipo devolução de compras **SEM** descontos:

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/15255512472471)![](https://centraldeatendimento.totvs.com/hc/article_attachments/15255426707991)**

**Saiba mais:**

* **Help: A410TOTDPRC:**[Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT (Faturamento) - Helps A410TOTAL e A410TOTDPRC no Faturamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007798262-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Faturamento-Helps-A410TOTAL-e-A410TOTDPRC-no-Faturamento)
* **Descontos no Faturamento (SIGAFAT):**[FAT0035 Descontos no Pedido de Venda](https://tdn.totvs.com/x/KE1tDQ)
* **Vídeo tutorial (Descontos):** [How To | MP - SIGAFAT - Descontos no processo de venda](https://youtu.be/JwG34Vyv3qQ)
