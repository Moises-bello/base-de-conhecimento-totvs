---
article_id: 37224276790551
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 8a973aec87b5202f96e65fba0b7552c27a427e64a05d4838bb104b47ccc91fce
fetched_at: '2026-06-28T22:38:58.406798+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Travamentos na MATA241
  apresenta o Help D3DOCP como corrigir?
type: support-article
updated_at: '2025-12-23T16:32:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37224276790551-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Travamentos-na-MATA241-apresenta-o-Help-D3DOCP-como-corrigir
---

O travamento no arquivo SX5 durante movimentações internas no TOTVS Protheus causa lentidão e bloqueio para usuários simultâneos. A solução foi alterar a rotina para atualizar o sequencial da chave antes de gerar o LOCK dos registros. Recomenda-se manter o sistema atualizado e realizar backup antes de atualizar.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37224292310935) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
O travamento no arquivo SX5 durante a inclusão de movimentações internas está impactando diretamente a performance e a usabilidade da rotina, gerando lentidão e, em alguns casos, causando o travamento das operações de outros usuários que tentam acessar o mesmo processo simultaneamente. Impedindo a conclusão do processo seja realizada sem que a anterior tenha finalizada.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
Alterado o comportamento da rotina, para que a atualização do sequencial da chave (SX5) do D3DOC seja realizada antes de gerar o LOCK dos registros para a movimentação de estoque.

12.1.2210:<https://r.totvs.io/p/1229699>

12.1.2310:<https://r.totvs.io/p/1229700>

12.1.2410:<https://r.totvs.io/p/1229698>

12.1.2510:<https://r.totvs.io/p/1229701>

**Issue TDN:** DMANMAT01-46655  
   
É importante atualizar seu produto constantemente, mantendo-o sempre na última versão disponível no Portal de Clientes ([Central de Download](https://totvs.fluigidentity.com/cloudpass/SPInitPost/receiveSSORequest/zf0y84vo717g8hjx/xlglk8zqmzw44blf1442945918727)), a fim de contemplar todas as melhorias e correções disponibilizadas.  
  
Efetuar o Backup antes da atualização. Todos os procedimentos devem ser realizados primeiro em ambiente TESTE atualizado.

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
