---
article_id: 22761126701975
category: Materiais - Compras (SIGACOM)
content_hash: 6798f278afa60fde63a85aff3790de5864c5be0ec3e907096e9250d8bf6b4ff2
fetched_at: '2026-06-28T22:41:10.487678+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: ' Documentações Notícias Cross Segmentos - Totvs Backoffice Protheus - SIGACOM
  - MATA121 - Como o sistema controla o saldo que falta para receber do pedido de
  compra?'
type: support-article
updated_at: '2024-04-12T14:54:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22761126701975--Documenta%C3%A7%C3%B5es-Not%C3%ADcias-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-MATA121-Como-o-sistema-controla-o-saldo-que-falta-para-receber-do-pedido-de-compra
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22761126669975) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**Como o sistema controla o saldo que falta para receber do pedido de compra?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - Todas as versões  
  
**Solução**

O Pedido de Compra é finalizado pela quantidade e não pelo valor. O campo C7\_QUJE é o responsável por encerrar o pedido após a entrada da nota. Ou seja, quando o documento de entrada é incluído, o sistema preenche o campo C7\_QUJE com a quantidade digitada no D1\_QUANT. Se essa quantidade do C7\_QUJE for igual ao C7\_QUANT, o saldo desse pedido é consumido e o item do Pedido é considerado como atendido.

Por exemplo, quando o pedido de compra possui a quantidade 1, mas o fornecedor envia notas com valores diferentes do total do pedido, o processo sugerido é o seguinte: incluir a nota vinculando-a ao pedido de compras, porém fracionando a quantidade. Por exemplo, você tem um PC com quantidade 1 e valor R$ 1.000,00. Por algum motivo, seu fornecedor emite uma nota com quantidade 1 e valor de R$ 600,00. No documento de entrada, a quantidade, ao invés de ser 1, deverá ser proporcional ao valor de R$ 600,00, ou seja, 0,60. Assim, ficará pendente uma quantidade de 0,40 e um valor de R$ 400,00. Quando seu fornecedor enviar outra nota e você a incluir no sistema, ao vincular ao PC, será apresentado apenas o saldo a ser recebido: a quantidade de 0,40 e o valor de R$ 400,00. Isso ocorre porque, de acordo com a quantidade preenchida no C7\_QUJE com a entrada da primeira nota, o sistema calcula o valor pendente a ser recebido.

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
