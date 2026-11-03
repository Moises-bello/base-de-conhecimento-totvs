---
article_id: 18949056512791
category: Inspeção de Processos (SIGAQIP)
content_hash: 0d12be7e93e6605fb00a8db0653e6f0c279121bf9a796a88e0384e2e155317ea
fetched_at: '2026-06-28T22:42:25.838113+00:00'
product: protheus
section_id: 360005906153
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIP - MATA650 - Mensagem Imprime Plano Inspeção
type: support-article
updated_at: '2024-05-27T16:31:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18949056512791-Manufatura-Linha-Protheus-SIGAQIP-MATA650-Mensagem-Imprime-Plano-Inspe%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18949041634071) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**No módulo **SIGAPCP - Planejamento e Controle da Produção**, quando existe integração com o módulo **SIGAQIP - Inspeção de Processos**, após incluir a **OP - Ordem de Produção** é apresentada a mensagem **Imprime Pl Inspeção**. É possível desativar a exibição desta mensagem e a integração continuar ativa?  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Processos (SIGAQIP) - Todas as versões  
  
**Causa**Essa mensagem ocorre quando o parâmetro **MV\_QPIMPPL - Imprime a Ficha de Produto? Uso após a inclusão da ordem de** **Produção** está ativo.  
  
**Solução**Para que a mensagem não seja exibida, o conteúdo do parâmetro **MV\_QPIMPPL** deve ser alterado para **N-Não**. Desta forma, além da mensagem também não será impresso o relatório.
