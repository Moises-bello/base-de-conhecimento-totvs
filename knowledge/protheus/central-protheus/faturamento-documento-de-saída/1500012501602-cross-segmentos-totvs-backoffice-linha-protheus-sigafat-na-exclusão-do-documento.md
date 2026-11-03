---
article_id: 1500012501602
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: ac6deabdd783a3818ac7618a533c991f55cd7ed8f4810ee8f28b8f500a4ed915
fetched_at: '2026-06-28T22:38:45.081908+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: 'Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Na exclusão
  do documento de saída, aparece o Help: FA040BAIXA'
type: support-article
updated_at: '2023-01-31T12:12:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012501602-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Na-exclus%C3%A3o-do-documento-de-sa%C3%ADda-aparece-o-Help-FA040BAIXA
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: 00:03:00 min**

**Dúvida**Help FA040BAIXA na exclusão de nota fiscal de saída, como solucionar?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT (Faturamento) – A partir da versão 12.1.25  
  
**Solução**

O Help **FA040BAIXA** compara o valor baixado para o titulo (**E1\_VALOR - E1\_SALDO**), com o valor dos adiantamentos.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12062160329367)

1 - Achar o título gerado pela documento de saída, para isso, basta filtrar a tabela SE1 no campo "No. Titulo [E1\_NUM]" pela numeração da nota fiscal de saída.

2 - Nesse registro, verifique os campos "Vlr. Titulo [E1\_VALOR]" e "Saldo [E1\_SALDO]"

3 - Achar o registro gerado pelo adiantamento, para isso, basta filtrar a tabela FIE no campo "Pedido  [FIE\_PEDIDO]" pelo pedido de venda que originou o documento de saída e os títulos.

4 - Nesse registro, verificar o campo "Valor [FIE\_VALOR]".

* Se a subtração dos campos (E1\_VALOR - E1\_SALDO) do título, for diferente do valor (FIE\_VALOR) do adiantamento, o sistema apresenta o HELP e não deixa excluir.
* **Se a subtração dos campos (E1\_VALOR - E1\_SALDO) do título, for igual ao valor (FIE\_VALOR) do adiantamento, o sistema deixa excluir.**

**A solução é excluir todas as baixas referentes aos títulos gerados pelo documento de saída,** pois se a subtração está diferente é porque já houveram baixas no titulos, estornando as baixas dos títulos a subtração dos campos (E1\_VALOR - E1\_SALDO) fica idêntica ao valor do adiantamento (FIE\_VALOR) e é possível excluir o documento de saída.
