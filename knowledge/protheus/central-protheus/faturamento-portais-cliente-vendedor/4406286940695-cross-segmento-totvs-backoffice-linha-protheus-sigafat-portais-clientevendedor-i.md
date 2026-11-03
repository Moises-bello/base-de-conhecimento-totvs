---
article_id: 4406286940695
category: FATURAMENTO - PORTAIS (Cliente, Vendedor)
content_hash: 3c35c61d631bb3753d9dd94385447e6597baa976d6d8ab7f5bf6ac728b81cf0e
fetched_at: '2026-06-28T22:38:23.889232+00:00'
product: protheus
section_id: 1500001539321
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) -Sigafat - Portais (Cliente/Vendedor)-
  Inclusão de pedido no portal do Vendedor
type: support-article
updated_at: '2021-08-18T14:20:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406286940695-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Sigafat-Portais-Cliente-Vendedor-Inclus%C3%A3o-de-pedido-no-portal-do-Vendedor
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00min** **Dúvida**

Como incluir um pedido de venda no portal do vendedor?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) -Sigafat - Portais (Cliente/Vendedor) - Todas as versões

**Solução**

1-Acesse o portal do vendedor (**PWSV040**) com o usuário do portal cadastrado;

2-Acesse Vendas e Distribuição, Pedido de Vendas;

3-Clique no botão Incluir;

4-O pedido de venda do portal funcionará como o pedido de venda na retaguarda do ERP, pode se selecionar o cliente ou digitar diretamente no campo;

4.1 - Da mesma forma, selecionar a  condição de pagamento;

5- Nas versões anteriores, utilizava-se o botão Calcular para saber a totalização do pedido. Nas releases mais novas, o sistema já está ajustando automaticamente.

Caso não o faça, clique em Calcular.

6-Clique em Gravar para que seja gerado o pedido de venda.

![Pedido_portal_do_vendedor.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4406293685527/Pedido_portal_do_vendedor.gif)

Obs: Para pedido no portal, o produto precisa conter tes e preço de venda, para não gera o help ***PUTSALESORDER : AJUDA:A410VZ***

O pedido no portal não aceita referência de grade (**MATA550**) ou referência de indicador de produto (**MATA018**)como no pedido no ERP, o portal olha direto no cadastro do produto (**MATA010**) com a referência completa.

**Saiba mais: [PPVD0005\_Inclusão\_de\_Pedido\_no\_Portal\_do Vendedor](https://tdn.totvs.com/x/PPoDIQ)**
