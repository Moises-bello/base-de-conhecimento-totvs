---
article_id: 6191185162775
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: ab0e0166982122be934070021033f190cf58a6ec56d46e7344252ed02e03a8a8
fetched_at: '2026-06-28T22:38:38.353061+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAFAT - Help: A455NOCQ'
type: support-article
updated_at: '2023-10-30T12:07:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6191185162775-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFAT-Help-A455NOCQ
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18649919655191) Tempo aproximado para leitura: **00:03:00 min****

**Ocorrência**

Ao tentar realizar uma **Devolução de Documento de Entrada** ou uma **Liberação de Estoque**, o sistema gera  amensagem de Help: **A455NOCQ | Não é permitida a liberação de estoque manual de produtos bloqueados no CQ.**

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Faturamento - Todas as versões.  
  
**Causa**

O Help é apresentado quando está configurado o "Controle de Qualidade" (CQ) no ambiente (Para saber mais sobre o tema veja: [Baixas do CQ - MATA175](https://youtu.be/wCxQnZfhe-U?si=xuqFH83xDsmfOhLI)).

Quando o produto encontra-se no Armazém de Controle de Qualidade (Valide o parâmetro MV\_CQ), ou quando o produto foi Rejeitado no controle de qualidade (Rotina "Baixas do CQ" (MATA175)), o sistema não pode realizar a movimentação do Saldo, por isso impede a devolução ou a liberação do estoque desse produto.

 Apenas quando o produto for **Aprovado**, saindo do armazém de qualidade para outro armazém, ele ficará disponível para movimentação.

Quando o produto é **rejeitado**, ele **só pode ser devolvido** ao fornecedor através de uma nota de devolução.

**Solução**

Para que o help não ocorra, valide todo o processo no exemplo abaixo e forma de efetuar a liberação:

**1.**  Siga as orientações do vídeo: [SIGAEST Baixas do CQ - MATA175;](https://youtu.be/wCxQnZfhe-U?si=M8Rkff5q3jv5WQI0)  
**2.** Realizando o Estorno da Rejeição e a transferência do Produto para um armazém padrão;  
**3.** Após o ajuste será possível prosseguir com a Devolução / Liberação de Estoque do Produto.

**Saiba mais:**

[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT -Pedido de Venda com status indevido de bloqueado (ou indevidamente liberado) por Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115004164287-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Pedido-de-Venda-com-status-indevido-de-bloqueado-ou-indevidamente-liberado-por-Estoque?source=search)

[Clique aqui e veja mais artigos sobre Pedidos de Venda no Faturamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550322-FATURAMENTO-PEDIDO-DE-VENDAS)
