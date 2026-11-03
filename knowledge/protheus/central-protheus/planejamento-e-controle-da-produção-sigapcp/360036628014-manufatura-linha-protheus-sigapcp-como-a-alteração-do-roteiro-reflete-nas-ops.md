---
article_id: 360036628014
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 7bfb4400bbd4e9bf3ab4ee02d507c0c5800f9aed607b150915f43e4b94486ae1
fetched_at: '2026-06-28T22:42:41.060751+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Como a alteração do roteiro reflete
  nas OPs
type: support-article
updated_at: '2025-10-16T17:29:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036628014-Manufatura-Linha-Protheus-SIGAPCP-Como-a-altera%C3%A7%C3%A3o-do-roteiro-reflete-nas-OPs
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35682837166999)**Tempo aproximado para leitura:**00:01:00 min**  
**Dúvida**Ao editar o roteiro de operações, incluindo ou excluindo operações, como ocorre o reflexo dessa alteração para as **OP's - Ordens de Produção** já cadastradas?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**O comportamento depende do conteúdo do parâmetro **MV\_PCPATOR - Indica que as operações serão geradas individualmente na ordem de produção**. Quando possui o conteúdo **.T.** faz com a tabela **SHY - Operações x Ordem** seja preenchida com as operações do roteiro no momento da abertura da **OP**.  
No apontamento da **OP**, é validada a operação registrada nesta tabela, e ao alterar o roteiro de operações, através da rotina **PCPA124 - Processo Produtivo** pode ocorrer o ajuste na tabela **SHY** para as **OPs** ainda não apontadas, de acordo com a listagem de **OPs** em tela e confirmação do cliente no processo.  
Quando o parâmetro **MV\_PCPATOR** possui o conteúdo **.F.** a tabela **SHY** não é carregada com os dados do roteiro e as validações acontecem diretamente na tabela **SG2 - Roteiro de Operações**.
