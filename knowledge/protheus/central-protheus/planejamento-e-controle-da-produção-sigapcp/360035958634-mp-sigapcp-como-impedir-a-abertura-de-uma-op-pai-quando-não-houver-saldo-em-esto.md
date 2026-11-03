---
article_id: 360035958634
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 93f2df99182e15280f636daa88ccd33207a4b49a979f7794d782b036076b7944
fetched_at: '2026-06-28T22:42:47.159955+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: MP - SIGAPCP - Como impedir a abertura de uma OP pai quando não houver saldo
  em estoque
type: support-article
updated_at: '2020-01-31T18:11:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035958634-MP-SIGAPCP-Como-impedir-a-abertura-de-uma-OP-pai-quando-n%C3%A3o-houver-saldo-em-estoque
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:00:35 min**  
 **Dúvida**Como impedir a abertura de um **OP pai - Ordem de Produção**quando não houver saldo em estoque?  
  
**Ambiente**Microsiga Protheus - Planejamento e Controle da Produção - Versão 12  
  
**Solução**Ao abrir uma **OP pai**o Sistema não valida se existe estoque dos componentes da estrutura em quantidade suficiente para a necessidade, a **OP pai** e os empenhos serão gerados independente da posição do estoque.  
No caso de desejar implementar essa validação, recomendamos o uso do ponto de entrada**[MA650TOK](https://tdn.totvs.com/x/sOpc)**
