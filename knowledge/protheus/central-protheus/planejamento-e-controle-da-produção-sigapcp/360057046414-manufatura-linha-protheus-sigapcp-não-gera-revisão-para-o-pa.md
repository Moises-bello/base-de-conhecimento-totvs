---
article_id: 360057046414
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 7b1487e56d9887b0466af9e33fb1dcbd13f51acb9445a74faa116ab61ee3d010
fetched_at: '2026-06-28T22:42:44.591488+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Não gera revisão para o PA
type: support-article
updated_at: '2025-03-19T14:31:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057046414-Manufatura-Linha-Protheus-SIGAPCP-N%C3%A3o-gera-revis%C3%A3o-para-o-PA
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30763081880471)***Tempo aproximado para leitura: **00:01:10 min**  
**Dúvida**Por que ao **alterar/incluir/excluir** um componente, no **PCPA200 - Estrutura**, de um **PI - Produto Intermediário** não é gerada a revisão para o **PA - Produto Acabado**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Porque ao realizar a **alteração/inclusão/exclusão** de um **componente** que está abaixo de um **PI** o Sistema irá gerar a revisão para o **PI**. Ou seja, o Sistema irá gerar a revisão para o produto onde os componentes que estão diretamente relacionados.  
  
**Exemplo:**  
\_\_\_\_\_\_\_PA\_\_\_\_\_\_\_  
|                       |  
PI                   MP1  
|  
MP2  
  
Ao realizar a alteração da quantidade, por exemplo, do **MP2** será gerado a revisão para o **PI** e não para o **PA**.  
  
**Importante**  
Para que seja gerada a revisão automaticamente é necessário que o controle de revisão**MV\_REVAUT -** **Indica se o controle de revisões será controlado automaticamente** esteja ativo.
