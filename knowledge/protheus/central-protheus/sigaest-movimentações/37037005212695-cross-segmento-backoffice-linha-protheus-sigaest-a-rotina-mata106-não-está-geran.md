---
article_id: 37037005212695
category: SIGAEST - MOVIMENTAÇÕES
content_hash: f05c54a60dfe62a38db44d75c23f07c3ac98428f946ad4916a51a282df963806
fetched_at: '2026-06-28T22:38:54.259925+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - A rotina MATA106 não
  está gerando Solicitação de compras na filial correta.
type: support-article
updated_at: '2025-12-17T12:24:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37037005212695-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-A-rotina-MATA106-n%C3%A3o-est%C3%A1-gerando-Solicita%C3%A7%C3%A3o-de-compras-na-filial-correta
---

Foi corrigido um erro no TOTVS Protheus em que a Solicitação de Compras gerada a partir de uma Pré-Requisição usava a filial errada (01) em vez da filial de origem da Solicitação ao Armazém (02). Agora, o sistema considera corretamente a filial onde a solicitação foi criada, respeitando compartilhamento entre filiais, unidade de negócio e empresa.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37036963952023) Tempo aproximado para leitura: **01:00:00 min**  
  
**Dúvida**  
Ao criar uma Solicitação ao Armazém numa filial (02), sem saldo disponível ao produto requisitado, e posteriormente gerar a Pré-Requisição a partir da filial 01 com o parâmetro “Gera Sol. Compras/Aut. Entrega?” configurado como SIM, o sistema gera a Solicitação de Compras de forma incorreta para a filial 01, em vez da filial 02, que é a origem do documento da Solicitação ao Armazém. Esse comportamento faz com que todo o processo subsequente (requisição, compra e movimentação de estoque) seja direcionado à filial 01, onde não existe a SA nem a necessidade real do item.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
Corrigimos o processo da inclusão da Solicitação de Compras para considerar a filial de origem do documento (Solicitação ao Armazém).  
Com essa correção, o sistema passa a utilizar a filial onde a Solicitação ao Armazém foi gravada, considerando também o modo de compartilhamento entre filiais, unidade de negócio e empresa da tabela SC1 (Solicitação de Compras).

12.1.2210:<https://r.totvs.io/p/1220129>

12.1.2310:<https://r.totvs.io/p/1220130>

12.1.2410:<https://r.totvs.io/p/1220128>

12.1.2510:<https://r.totvs.io/p/1220131>

**Issue TDN:** DMANMAT01-46277

É importante atualizar seu produto constantemente, mantendo-o sempre na última versão disponível no Portal de Clientes ([Central de Download](https://totvs.fluigidentity.com/cloudpass/SPInitPost/receiveSSORequest/zf0y84vo717g8hjx/xlglk8zqmzw44blf1442945918727)), a fim de contemplar todas as melhorias e correções disponibilizadas.

Efetuar o Backup antes da atualização. Todos os procedimentos devem ser realizados primeiro em ambiente TESTE atualizado.

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
