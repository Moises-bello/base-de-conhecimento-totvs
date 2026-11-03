---
article_id: 4413866211735
category: SIGAEST - LEGAIS
content_hash: 9fb45e30a2333a65eb60ee2bb35fa28fd3efe76abcfb2378c53ba81ce32fa0ae
fetched_at: '2026-06-28T22:38:51.868703+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - SPEDFISCAL (Bloco
  K) - Error.log "insert duplicate key row in D3O"
type: support-article
updated_at: '2021-11-23T16:47:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413866211735-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-SPEDFISCAL-Bloco-K-Error-log-insert-duplicate-key-row-in-D3O
---

**Ocorrência**

Cannot insert duplicate key row in object 'dbo.D3O010' with unique index 'D3O010\_UNQ'. The duplicate key value is (000000, 202110, 000006 , 47295-24010 , 0).

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Causa**Ao executar a geração do bloco K gerando histórico igual a "Sim" onde existe OP de terceiros ocorre o erro de chave duplicada.  
  
**Solução**

Para corrigir, basta efetuar um ajuste no dicionário nas chaves primárias da tabela de históricos (D3O).

Como ajustes de dicionários somente estarão disponíveis em próximas releases, para correção em dicionário corrente será necessário solicitar apoio juntamente ao DBA responsável para ajuste na tabela SX2 alterando a chave única da tabela D3O para:

D3O\_FILIAL+D3O\_PERBLK+D3O\_CHAVE+DTOS(D3O\_DT\_CON)+D3O\_COD\_IT

**Saiba mais**

*[Clique aqui e veja mais artigos sobre Legais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538941-SIGAEST-LEGAIS)*
