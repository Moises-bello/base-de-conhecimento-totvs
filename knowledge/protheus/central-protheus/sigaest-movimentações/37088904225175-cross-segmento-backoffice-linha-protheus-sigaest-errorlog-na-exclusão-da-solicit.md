---
article_id: 37088904225175
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 6afd9e70c6274020e8d9454b9814ccdd81d9d2abac6087c27db7dee858ccb599
fetched_at: '2026-06-28T22:38:55.499589+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Error.Log na Exclusão
  da Solicitação ao Armazém com campo virtual
type: support-article
updated_at: '2025-12-17T14:14:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37088904225175-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Error-Log-na-Exclus%C3%A3o-da-Solicita%C3%A7%C3%A3o-ao-Armaz%C3%A9m-com-campo-virtual
---

Durante a exclusão de um item da solicitação ao armazém, um erro causado por um campo customizado com contexto virtual gerou comportamento inesperado no sistema. Foi implementado um tratamento para distinguir campos reais de virtuais, evitando novos erros. Recomenda-se atualizar o produto nas versões indicadas e realizar backup antes da atualização.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37088907921175) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Durante a tentativa de excluir um item da solicitação ao armazém, foi identificado um erro provocado por um campo customizado com um contexto virtual. Devido a isso, gerou-se um comportamento inesperado no sistema, impedindo a continuidade normal do processo.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) -Estoque/Custos - Todas as versões.  
  
**Solução**  
Efetuado um tratamento no trecho da gravação da alteração/exclusão do itens da solicitação ao armazém. Este tratamento identificará se o campo é de contexto real ou virtual antes do processamento, evitando que novos errorlogs desta natureza ocorra.

12.1.2210:<https://r.totvs.io/p/1225878>

12.1.2310:<https://r.totvs.io/p/1225879>

12.1.2410:<https://r.totvs.io/p/1225877>

 12.1.2510:<https://r.totvs.io/p/1225880>

**Issue TDN:** DMANMAT01-46642

É importante atualizar seu produto constantemente, mantendo-o sempre na última versão disponível no Portal de Clientes ([Central de Download](https://totvs.fluigidentity.com/cloudpass/SPInitPost/receiveSSORequest/zf0y84vo717g8hjx/xlglk8zqmzw44blf1442945918727)), a fim de contemplar todas as melhorias e correções disponibilizadas.  
  
Efetuar o Backup antes da atualização. Todos os procedimentos devem ser realizados primeiro em ambiente TESTE atualizado.

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
