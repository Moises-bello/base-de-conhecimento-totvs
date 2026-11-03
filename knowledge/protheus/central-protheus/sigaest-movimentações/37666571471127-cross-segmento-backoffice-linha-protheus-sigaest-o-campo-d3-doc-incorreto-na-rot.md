---
article_id: 37666571471127
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 742dde97d7e33e7d4c4b5891dd4bb5255400587e1589ec78248183ebc698ba07
fetched_at: '2026-06-28T22:38:57.233005+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - O campo D3_DOC incorreto
  na rotina de movimentação múltiplas e transferência múltiplas.
type: support-article
updated_at: '2026-01-14T13:41:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37666571471127-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-O-campo-D3-DOC-incorreto-na-rotina-de-movimenta%C3%A7%C3%A3o-m%C3%BAltiplas-e-transfer%C3%AAncia-m%C3%BAltiplas
---

A rotina MATA261, na função a261Inclui, foi ajustada para substituir a função NextNumero() pela A240NumDoc() ao preencher o campo D3\_DOC quando o documento não é informado.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37666587251095) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Foi identificado que a rotina MATA261, na função a261Inclui, utilizava a função **NextNumero()** para preencher o campo **D3\_DOC** quando o campo de documento não era informado durante a inclusão.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) -Estoque/Custos - Todas as versões.

**Solução**  
Realizado um ajuste na rotina para fazer a chamada da função A240NumDoc().

12.1.2310:<https://r.totvs.io/p/1233665>

12.1.2410:<https://r.totvs.io/p/1233666>

12.1.2510:<https://r.totvs.io/p/1233667>   
   
É importante atualizar seu produto constantemente, mantendo-o sempre na última versão disponível no Portal de Clientes ([Central de Download](https://totvs.fluigidentity.com/cloudpass/SPInitPost/receiveSSORequest/zf0y84vo717g8hjx/xlglk8zqmzw44blf1442945918727)), a fim de contemplar todas as melhorias e correções disponibilizadas.  
  
Efetuar o Backup antes da atualização. Todos os procedimentos devem ser realizados primeiro em ambiente TESTE atualizado.

**Issue TDN:** [DMANMAT01-47146](https://tdn.totvs.com/pages/releaseview.action?pageId=1032866991)

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
