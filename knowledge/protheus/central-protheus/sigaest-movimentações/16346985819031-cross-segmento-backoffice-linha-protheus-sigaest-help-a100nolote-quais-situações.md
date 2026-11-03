---
article_id: 16346985819031
category: SIGAEST - MOVIMENTAÇÕES
content_hash: f913fc55183d5bfc91c06ca48c081a19a7914c3ef8c6e69d2f7aadf62d929522
fetched_at: '2026-06-28T22:38:55.548869+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - HELP A100NOLOTE -
  Quais situações que podem apresentar o HELP?
type: support-article
updated_at: '2023-10-23T14:53:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16346985819031-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-HELP-A100NOLOTE-Quais-situa%C3%A7%C3%B5es-que-podem-apresentar-o-HELP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16346962216215) Tempo aproximado para leitura: **00:04:00 min****Ocorrência**Ao excluir um Documento de Entrada (MATA103) o sistema apresenta o ***HELP A100NOLOTE***:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16347242474391)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Causa**

O help***A100NOLOTE*** é apresentado quando o saldo do Lote é menor que a quantidade da Nota Fiscal que está sendo excluída, isso pode ocorrer caso o Documento de Entrada tenha adicionado um saldo no Lote, porém esse saldo foi consumido por algum outro processo impossibilitando o estorno do saldo na exclusão do documento.

**Solução**

Verifique no ambiente os seguintes cenários:

1. Verificar se o lote esta empenhado para uma Ordem de Produção, nesse caso se o Documento de Entrada for excluído, não haverá saldo para atender à esta Ordem de Produção;

2. Verificar se o Lote esta Reservado para um Pedido de Vendas, isso pode ser verificado através dos campos "Lote" (C6\_LOTECTL) ou "Lote" (C9\_LOTECTL);

3. Verifique se o parâmetro MV\_LOTVENC esta igual a N e se o Lote esta com uma Data de Validade inferior a Data Base, ou seja, Lote Vencido não pode ser movimentado. Para esse cenário utilizar a rotina [MANUTENÇÃO DE LOTES (MATA390)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360030246893-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Rotina-MATA390-Manuten%C3%A7%C3%A3o-de-Lotes) e ajustar a Data de Validade para uma data superior.

4. Verificar se o produto consta com Saldo desbalanceado entre as tabelas de Lote. [Clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018463012-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR282-Parametriza%C3%A7%C3%A3o-para-identificar-diverg%C3%AAncia-de-saldos-entre-tabelas-SB2-X-SB8-X-SBF) e veja a FAQ com instruções sobre como avaliar.

***Saiba Mais:***  
*[Clique aqui e veja mais artigos sobre MOVIMENTAÇÕES no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
