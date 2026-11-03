---
article_id: 4407018491031
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 67a781370ac6d59a0b6d2aa52d3a1987ece2d3ede1a50f6ce423b474a43821f6
fetched_at: '2026-06-28T22:38:43.918473+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Segunda devolução
  de Nota
type: support-article
updated_at: '2024-03-27T18:50:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407018491031-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Segunda-devolu%C3%A7%C3%A3o-de-Nota
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Cliente possui o seguinte cenário :

1) NF de Entrada;

2) Devolução no Pedido de Vendas;

Fornecedor não aceita a devolução e solicita uma nova nota Fiscal de Devolução. O que fazer ?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - todas as versões.  
  
**Solução**1) Se estiver dentro do prazo de cancelamento e não houver impedimento, excluir a NF de devolução realizada no Faturamento e emitir novamente a NF.

2) Se não houver a possibilidade de exclusão, entrar com uma nova NF normal (Documento de Entrada - MATA103) e realizar o retorno desta segunda entrada no faturamento.  
  
Porque a nova entrada de NF ?

O ciclo de devolução da primeira NF terminou. Houve uma entrada e uma devolução desta entrada em documento de saída.

A primeira entrada não poderá ser devolvida novamente, pois caso seja feito a devolução da primeira, duplicará todos os saldos e movimentações na devolução (duas devoluções no Faturamento para somente uma NF de Entrada)
