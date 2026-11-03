---
article_id: 360053893993
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 9c935ae23e8aa7895fd70ee3e1ada31dca61c0297639b58fd22232eac88d4e90
fetched_at: '2026-06-28T22:38:28.668253+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - SIGAFAT -Uso
  do B1_ALTER no módulo de Faturamento
type: support-article
updated_at: '2023-07-20T18:35:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053893993-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-SIGAFAT-Uso-do-B1-ALTER-no-m%C3%B3dulo-de-Faturamento
---

**Dúvida**

Efetuado um pedido de vendas (**MATA410**) com um produto sem estoque, mas que tem uma configuração de produto  alternativo vinculado e que possui estoque, porém, quando libero o pedido de vendas, ele fica bloqueado por estoque , o sistema não devia  usar o produto alternativo como segunda opção para  liberar o estoque ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - Todas as versões.  
  
**Solução**

O faturamento utiliza sempre o ***produto principal*** no processo, não há configuração para que considere produto alternativo na liberação de estoque, por isso gera bloqueio por falta de saldo.   
  
O conceito de uso de produto alternativo, com o uso campo **B1\_ALTER**  é indicar um produto alternativo somente na impressão das solicitações de compras ou consultas de material.  
  
Caso queira alterar o produto informado é necessário efetuar o processo manualmente, clicando no botão alterar e selecionando o produto no qual deseja vender.  
  
Para o caso de  customização no processo, pode se utilizar o ponto de entrada referente a validação da linha do pedido de venda ou para refazer a liberação de estoque:

**M410LIOK** - Validação de linha de **pedido**  
**<https://tdn.totvs.com/pages/releaseview.action?pageId=6784149>**  
  
**M410RLIB** - Refaz liberações de estoque  
**<https://tdn.totvs.com/pages/releaseview.action?pageId=6784153>**  
  
**Obs. *Com relação a melhoria e evolução de produto, foi efetuada a solicitação [DSERFAT-8560](https://jiraproducao.totvs.com.br/browse/DSERFAT-8560), o parecer final da equipe é que neste momento a solicitação não será produtizada, todavia está  armazenada em nosso banco de idéias para análise em roadmaps de releases futuros.***
