---
article_id: 360027616251
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: f4d893f3de90488f2aa72b355865238d57633e851a3a570e74c71ecd95266a8f
fetched_at: '2026-06-28T22:42:43.496567+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Item opcional vencido está aparecendo
  ao abrir uma OP
type: support-article
updated_at: '2022-08-02T17:28:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027616251-Manufatura-Linha-Protheus-SIGAPCP-Item-opcional-vencido-est%C3%A1-aparecendo-ao-abrir-uma-OP
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:00:50 min** **Dúvida**Por que o item opcional vencido está aparecendo ao abrir uma **OP - Ordem de Produção**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**O grupo de opcionais é cadastrado no **MATA256 - Opcionais** e associado ao produto na estrutura no **MATA200 - Estrutura**. Então se o produto estiver **vencido**, **bloqueado** ou **fora de revisão** na estrutura o opcional é apresentado como vencido ao tentar abrir uma **OP**.  
  
Na rotina **MATA650 - Ordem de Produção** é consistido da seguinte forma:

1. Se **todos** os opcionais estiverem vencidos, a tela é aberta, mas não é necessário selecionar nenhum item e ao clicar em **OK**, a tela é fechada normalmente.
2. Se ao menos um opcional estiver dentro da validade, a tela é aberta da mesma forma, mas o programa obriga selecionar pelo menos um opcional.
