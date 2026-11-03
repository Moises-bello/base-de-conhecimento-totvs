---
article_id: 38503932858903
category: SIGAACD - Automação e Coleta de Dados
content_hash: cf53a271d9b9580004d79ed0007b54c0bf045a936696bd47ab24ecf09bb00cb5
fetched_at: '2026-06-28T22:39:13.884727+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - VTACDMONIT - Conexão
  presa no coletor e travamento
type: support-article
updated_at: '2026-02-19T16:57:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38503932858903-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-VTACDMONIT-Conex%C3%A3o-presa-no-coletor-e-travamento
---

O artigo orienta sobre correção de conexão presa no coletor e travamento no SIGAACD na rotina VTACDMONIT  do  TOTVS Protheus, informando que foi implementada uma verificação para liberar a conexão caso o usuário não esteja utilizando o coletor. Recomenda-se manter o sistema atualizado e realizar procedimentos primeiro em ambiente de teste.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38503932843799) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Conexão presa no coletor e travamento no SIGAACD, como corrigir?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**  
Realizado alteração para verificar se o usuário ainda está utilizando o coletor, caso não esteja é liberado a conexão.

**12.1.2210**: <https://r.totvs.io/p/1206112>

**12.1.2310**: <https://r.totvs.io/p/1206113>

**12.1.2410**: <https://r.totvs.io/p/1206111>

**12.1.2510**: <https://r.totvs.io/p/1206114>

**Issue TDN:** DMANMAT01-45369

É importante atualizar seu produto constantemente, mantendo-o sempre na última versão disponível no Portal de Clientes ([Central de Download](https://totvs.fluigidentity.com/cloudpass/SPInitPost/receiveSSORequest/zf0y84vo717g8hjx/xlglk8zqmzw44blf1442945918727)), a fim de contemplar todas as melhorias e correções disponibilizadas.  
  
Efetuar o Backup antes da atualização. Todos os procedimentos devem ser realizados primeiro em ambiente TESTE atualizado.

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
