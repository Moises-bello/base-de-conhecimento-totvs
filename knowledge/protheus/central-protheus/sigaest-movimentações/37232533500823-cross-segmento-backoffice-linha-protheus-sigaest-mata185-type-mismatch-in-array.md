---
article_id: 37232533500823
category: SIGAEST - MOVIMENTAÇÕES
content_hash: f6a9d8bd578136368d1ceaefc1a17a5172fed1f8fa06a690c9b983eb85875f50
fetched_at: '2026-06-28T22:38:56.907181+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA185 - type mismatch
  in array subscriptor - expected N->C on A241CDOC
type: support-article
updated_at: '2025-12-23T21:24:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37232533500823-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA185-type-mismatch-in-array-subscriptor-expected-N-C-on-A241CDOC
---

O sistema TOTVS Protheus corrigiu erros na rotina MATA185 que impediam a baixa de pré-requisições e atualizou o saldo do lote após estorno. As correções estão disponíveis nas versões 12.1.2210, 12.1.2310, 12.1.2410 e 12.1.2510. Recomenda-se atualizar o produto e realizar backup antes da atualização.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37232533485335) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Cenário 1

Na tentativa de realizar a baixa de a pré requisição de material na rotina MATA185, o sistema apresenta error.log impedindo a conclusão da baixa do documento.

Cenário 2

Ao estornar uma baixa de uma pré-requisição, foi identificado que o saldo do lote não era atualizado.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
Cenário 1

Foi implementado um tratamento no programa corrigindo o error.log em questão.

Além de outro tratamento para caso ocorra a substituição do número do documento por outro, o sistema informará qual o próximo número de documento encontrado.

Cenário 2

Implementada a correção para que o campo B8\_SALDO fosse atualizado corretamente após o estorno do movimento do lote.

12.1.2210:<https://r.totvs.io/p/1229305>

12.1.2310:<https://r.totvs.io/p/1229306>

 12.1.2410:<https://r.totvs.io/p/1229304>

12.1.2510:<https://r.totvs.io/p/1229308>

**Issue TDN:** DMANMAT01-46778  
   
É importante atualizar seu produto constantemente, mantendo-o sempre na última versão disponível no Portal de Clientes ([Central de Download](https://totvs.fluigidentity.com/cloudpass/SPInitPost/receiveSSORequest/zf0y84vo717g8hjx/xlglk8zqmzw44blf1442945918727)), a fim de contemplar todas as melhorias e correções disponibilizadas.  
  
Efetuar o Backup antes da atualização. Todos os procedimentos devem ser realizados primeiro em ambiente TESTE atualizado.

Saiba Mais:

[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
