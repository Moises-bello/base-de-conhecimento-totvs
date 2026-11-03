---
article_id: 27001964687767
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 659aad09e5135340e4ae22170ca64ca916ea729778824cddff639355c3627f19
fetched_at: '2026-06-28T22:37:22.913183+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Help CNNOTADEV1 ao
  realizar uma Nota de Devolução na rotina de Documento de Entrada
type: support-article
updated_at: '2024-10-11T14:47:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27001964687767-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Help-CNNOTADEV1-ao-realizar-uma-Nota-de-Devolu%C3%A7%C3%A3o-na-rotina-de-Documento-de-Entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27001948310039) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Ao realizar na roita de Documento de Entrada uma Devolução de uma NF de Saído ocorre o Help CNNOTADEV1 da imagem abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27001948312215)

**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões

**Solução**

A mensagem de Help ***CNNOTEDEV1*** que pode ocorrer ao incluir um Doc. de Entrada de Devolução de uma NF de Saída, está relacionada à quando o Contrato que originou o Pedido de Vendas da NF de Saída para a qual está sendo feita a devolução não pode mais ser movimentado, e assim não será feita a devolução do saldo no Contrato dessa devolução da Nota.

O processo na rotina Documento de Entrada de Devolução da NF de Saida ocorre normalmente sem problemas, porém o que não ocorre é apenas o retorno do saldo para o Contrato do SIGAGCT que originou o Pedido de Vendas da NF de Saida que está sendo devolvida, devido ao Contrato não poder mais ser movimentado.

Isto acontece para quando o Contrato em questão no SIGAGCT está com os Status de *"Cancelado"*, *"Sol. Finalização"* e *"Finalizado"* ou também quando se trata de um Contrato de Integração com os Módulos de *Gestão de Conras Públicas (SIGAGCP)* ou de *Gestão de Serviços (SIGATEC)*.

***Saiba Mais:***

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
