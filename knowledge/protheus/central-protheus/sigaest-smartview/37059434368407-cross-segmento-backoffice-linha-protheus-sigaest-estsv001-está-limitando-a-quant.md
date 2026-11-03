---
article_id: 37059434368407
category: SIGAEST - SMARTVIEW
content_hash: 0fa4ff6e4bae76079b6e5eb2ded0536f6926e4662bbd3e93309beff3c0e08595
fetched_at: '2026-06-28T22:38:47.145896+00:00'
product: protheus
section_id: 16108365627287
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - ESTSV001 está limitando
  a quantidade da descrição do produto
type: support-article
updated_at: '2025-12-16T15:08:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37059434368407-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-ESTSV001-est%C3%A1-limitando-a-quantidade-da-descri%C3%A7%C3%A3o-do-produto
---

A descrição do produto gerada pelo objeto de negócio de Formação de Preços do Smartview no Protheus Release 12.1.2210 ou superior ultrapassa o limite de caracteres do campo 'Descrição' (B1\_DESC). O problema ocorre devido a erro na definição do campo, com soluções disponíveis para versões 12.1.2210, 12.1.2310, 12.1.2410 e 12.1.2510. Recomenda-se atualizar o sistema pela Central de Download e realizar backup antes da atualização.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37059434363543) Tempo aproximado para leitura: **00:01:00 min**  
  
**Ocorrência**  
A descrição do produto gerada pelo objeto de negócio de Formação de Preços do Smartview não respeita o limite de caracteres definido no campo 'Descrição' (B1\_DESC) para os componentes da estrutura de um produto.

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Protheus Release 12.1.2210 ou Superior.  
  
**Causa**  
Erro durante a definição do campo B1\_DESC.  
  
**Solução**  
12.1.2210:<https://r.totvs.io/p/1216601>

12.1.2310:<https://r.totvs.io/p/1216602>

12.1.2410:<https://r.totvs.io/p/1216600>

12.1.2510:<https://r.totvs.io/p/1216603>

Issue TDN: [DMANMAT01-46126](https://tdn.totvs.com/x/3AArOw)

É importante atualizar seu produto constantemente, mantendo-o sempre na última versão disponível no Portal de Clientes ([Central de Download](https://totvs.fluigidentity.com/cloudpass/SPInitPost/receiveSSORequest/zf0y84vo717g8hjx/xlglk8zqmzw44blf1442945918727)), a fim de contemplar todas as melhorias e correções disponibilizadas.

Efetuar o Backup antes da atualização. Todos os procedimentos devem ser realizados primeiro em ambiente TESTE atualizado.

**Saiba mais:**

[*Relação de SmartViews do Estoque (TDN)*](https://tdn.totvs.com/x/pwKQLg)

[*Clique aqui e veja mais artigos sobre Relatórios SmartView do Estoque Custos*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/16108365627287-SIGAEST-SMARTVIEW)
