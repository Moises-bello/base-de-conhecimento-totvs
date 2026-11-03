---
article_id: 17561737536151
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: b30541253739aa8c144f353dd8d04d7652c7fa0c3ea33ddc9940cf114e5f8339
fetched_at: '2026-06-28T22:38:42.500979+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) – SIGAFAT – Erro "Cannot insert
  duplicate key row in object 'dbo.SB2' with unique index 'SB2_UNQ'" no faturamento
type: support-article
updated_at: '2023-09-15T19:04:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17561737536151-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFAT-Erro-Cannot-insert-duplicate-key-row-in-object-dbo-SB2-with-unique-index-SB2-UNQ-no-faturamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17561753873815) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Ocorre o erro "Cannot insert duplicate key row in object 'dbo.SB2XXX' with unique index 'SB2XXX\_UNQ'" no faturamento, como resolver?  
  
**Ambiente**

Cross Segmentos - Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Todas as versões

**Solução**O erro está ocorrendo na verificação do fonte "FATXFUN" a existência da SB2 pelo índice 1.

O sistema cria para o produto na SB2 quando os campos "Produto (C6\_PRODUTO)" e "Armazém (C6\_LOCAL)" do pedido de venda, não são localizados na tabela SB2 (B2\_CODIGO e B2\_LOCAL).

1 - Certifique-se que os índices da tabela SB2 estão no padrão:

> ![](https://totvssuporte.zendesk.com/attachments/token/rqhMjLG8R5RrEOimrIkF7Fcqw/?name=image.png)

   
2 - Certifique-se que o campo X2\_UNICO (Tabela SX2) de chave primária da tabela SB2 é esse:

> ![](https://totvssuporte.zendesk.com/attachments/token/7FCxhpRMN39vW9VdRjnqx2wK9/?name=image.png)

    
3 - Avalie colocar o parâmetro MV\_FATTRAV com o valor "4"  
   
4 - Certifique-se que os campos filial (C6\_FILIAL), produto (C6\_PRODUTO) e armazém (C6\_LOCAL) da tabela SC6 existe os mesmos dados na tabela SB2: 

> B2\_FILIAL  |  B2\_COD  |  B2\_LOCAL

   
5 - Certifique-se que os pontos de entradas do processo estão inativos no momento

   
6 - Certifique-se que os campos "B1\_COD", "B2\_COD" e "C6\_PRODUTO" tem o mesmo tamanho no módulo configurador.
