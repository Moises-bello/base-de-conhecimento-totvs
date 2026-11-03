---
article_id: 12714829151767
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 0b4a98c1866a83ceac2f37df7be7a2cae6702a19960ac69b3e789dbe6120bc2a
fetched_at: '2026-06-28T22:37:22.851746+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Help " Quantidade "
  ao digitar uma quantidade na inclusão de uma Medição de Contrato
type: support-article
updated_at: '2023-02-27T14:34:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12714829151767-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Help-Quantidade-ao-digitar-uma-quantidade-na-inclus%C3%A3o-de-uma-Medi%C3%A7%C3%A3o-de-Contrato
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Ao realizar uma medição, ao digitar a Quantidade da medição ocorre o Help "Quantidade" :

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12714534808087)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões

**Solução**O Help "Quantidade" ao digitar o campo de quantidade em uma medição, ocorre normalmente quando é digitada uma quantidade maior que o saldo a medir existente para o referido item do contrato.

A mensagem normalmente ocorre quando na medição no campo de quantidade (CNE\_QUANT) a quantidade digitada é maior do que o contido na coluna "Saldo a Medir" do item da medição sendo que esse saldo a medir no item na tela de medição normalmente é o mesmo do saldo existente do item da planilha no contrato (CNB\_SLDMED) que é a quantidade do item do contrato "menos" a quantidade já medida deste item.

Conforme exemplo da imagem abaixo onde o "Saldo a Medir" é "3" e está se tentando informar uma  Quantidade "4" na medição, a mensagem ocorre:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12714636162583)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12714657618327)

***Saiba Mais:***

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
