---
article_id: 1500009773842
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 2c357dec649ebd345629777aa6b3c51ba002ee4ad02b80304e5d8863c8729b68
fetched_at: '2026-06-28T22:38:38.632023+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat - Usabilidade
  do botão rejeitar na análise de crédito
type: support-article
updated_at: '2021-08-24T20:43:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009773842-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Sigafat-Usabilidade-do-bot%C3%A3o-rejeitar-na-an%C3%A1lise-de-cr%C3%A9dito
---

**Dúvida**Qual a finalidade de uso do botão rejeitar na análise de credito (**MATA450**)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat- Todas as versões.  
  
**Solução**O botão rejeitar na tela de análise de crédito(**MATA450**) é para rejeitar aquela análise de pedido, assim, ao clicar no botão, o pedido ficará com status marrom de rejeitado:

![rejeitar_pedido_mata450.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500015403461/rejeitar_pedido_mata450.gif)

Nada impede de efetuar novamente a liberação manual, e posteriormente,  o liberar por crédito, se após a análise do cliente , verificar que o pedido pode ser aprovado por crédito.  
  
No browser do pedido, **mata410**, o status permanecerá como pedido liberado(amarelo), pois no browser do pedido a tabela visualizada é a **SC5**. e somente na tabela **SC9,** que já é o pedido liberado que é possível identificar se há bloqueio de crédito, através do campo **c9\_blcred.**

**Importante:**o botão rejeitar somente fará a rejeição do pedido posicionado, não tratará mais de um pedido como ocorre, com o botão liberar todos.

Caso seja necessário, na função Rejeitar existe o ponto de entrada **MTA450R**, que pode ser utilizado para efetuar algum tratamento diferente do padrão de sistema: **<https://tdn.totvs.com/x/lYVn>**

**SAIBA MAIS:**

**[MP-FAT-Como-identificar-e-liberar-bloqueios-do-Pedido-de-Vendas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014207291-MP-FAT-Como-identificar-e-liberar-bloqueios-do-Pedido-de-Vendas)**

**[MP-FAT-Pedido-de-Vendas-está-com-Bloqueio-de-Crédito-ou-de-Estoque-porém-na-rotina-de-Pedido-de-Vendas-demonstra-Status-Liberado-legenda-verde-](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019749211-MP-FAT-Pedido-de-Vendas-est%C3%A1-com-Bloqueio-de-Cr%C3%A9dito-ou-de-Estoque-por%C3%A9m-na-rotina-de-Pedido-de-Vendas-demonstra-Status-Liberado-legenda-verde-)**

**[MP-FAT-Bloqueios-gravados-na-tabela-SC9-nos-Pedidos-de-Venda](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017467652-MP-FAT-Bloqueios-gravados-na-tabela-SC9-nos-Pedidos-de-Venda)**
