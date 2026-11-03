---
article_id: 37059208182423
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 45d14ce311921111bbc9260c95dc2d7a776f5f79a9a23da5eed46449e247611c
fetched_at: '2026-06-28T22:38:54.036427+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA103 não gera SD3
  com RE5 retornado de beneficiamento
type: support-article
updated_at: '2026-03-10T13:50:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37059208182423-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA103-n%C3%A3o-gera-SD3-com-RE5-retornado-de-beneficiamento
---

Ao realizar o retorno de produtos industrializados por terceiros via rotina MATA103, não estava sendo gerado o registro RE5 na tabela SD3 devido a problema de codificação. A correção foi implementada para que o movimento seja gerado corretamente nas versões 12.1.2210, 12.1.2310, 12.1.2410 e 12.1.2510 do TOTVS Protheus. Recomenda-se manter o sistema atualizado e realizar backup antes das atualizações.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37059215938839) Tempo aproximado para leitura: **00:01:00 min**  
  
**Ocorrência**  
Ao realizar o retorno de um produto industrializados por terceiros de beneficiamento através da rotina **MATA103**não está gerando registro **RE5**na tabela **SD3**.

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - A partir da release 12.1.2210  
  
**Causa**  
Problema de codificação para geração das funções na criação da RE5.  
  
**Solução**  
Realizamos o ajuste para que o movimento seja gerada corretamente.

12.1.2210:<https://r.totvs.io/p/1221637>

12.1.2310:<https://r.totvs.io/p/1221638>

12.1.2410:<https://r.totvs.io/p/1221636>

12.1.2510:<https://r.totvs.io/p/1221639>

É importante atualizar seu produto constantemente, mantendo-o sempre na última versão disponível no Portal de Clientes ([Central de Download](https://totvs.fluigidentity.com/cloudpass/SPInitPost/receiveSSORequest/zf0y84vo717g8hjx/xlglk8zqmzw44blf1442945918727)), a fim de contemplar todas as melhorias e correções disponibilizadas.

Efetuar o Backup antes da atualização. Todos os procedimentos devem ser realizados primeiro em ambiente TESTE atualizado.

**Saiba Mais**:

[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
