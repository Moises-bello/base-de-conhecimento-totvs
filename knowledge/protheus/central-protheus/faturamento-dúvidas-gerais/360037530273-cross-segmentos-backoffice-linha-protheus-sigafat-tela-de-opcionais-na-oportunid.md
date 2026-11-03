---
article_id: 360037530273
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 194c946e6b6c96d7db92674cc6b0ac263aeaf75873087b92ee60ba236c890429
fetched_at: '2026-06-28T22:38:28.742095+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) - SIGAFAT -Tela de opcionais
  na oportunidade de vendas
type: support-article
updated_at: '2023-07-13T13:32:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037530273-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFAT-Tela-de-opcionais-na-oportunidade-de-vendas
---

**Dúvida**

Foi configurado Opcionais de Produto e em rotinas como Pedido de Venda (**MATA410**) e Orçamento (**MATA415**) estão funcionando, mas na tela de Oportunidade não abre a janela para escolha dos opcionais. Como habilitar?

**Ambiente**

Cross Segmentos - Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Todas as versões

**Solução**

O conceito de uso da rotina de opcionais de produto foi efetuado para tratar apenas produtos para ordem de produção (**MATA650**),  orçamento de vendas e pedido vendas.

As rotinas de oportunidade de vendas (**FATA300**) ou proposta comercial (**FATA600**) não foram projetadas para tratar o uso de produtos com opcionais em sua estrutura, por isso, que não abre a tela de opcionais para a escolha de componentes de produto.  
  
Lembrando que o conceito de uso da rotina oportunidade de vendas é para gerar um inicio de uma negociação com o cliente associado a um orçamento de vendas ou proposta comercial, conforme a configuração do parâmetro **mv\_fatprop**, e somente com a aprovação da oportunidade gerar o pedido de vendas, finalizando da negociação.

Não se gera o pedido de vendas diretamente da oportunidade vendas e também, nada do que é cadastrado direto na oportunidade é levado para o orçamento de vendas ou proposta comercial, não fazendo sentido o uso do opcional de produto nesta fase da negociação, como o fluxo é contrário, ou seja, o produto deve ser informado no orçamento de vendas ou na proposta comercial, e após a gravação é que será levados os dados para a oportunidade de venda, faz mais sentido o uso de opcionais de produto.

O orçamento já trata opcional no padrão do produto, enquanto a proposta comercial possui um projeto de evolução de produto, onde já está sendo estudado por nossa equipe de desenvolvimento de produto , a sua  implementação em futuras versões.

Sabia mais: [FAT0066 Uso de Opcionais no Pedido de Vendas](https://tdn.totvs.com/display/public/PROT/FAT0066+Uso+de+Opcionais+no+Pedido+de+Vendas)
