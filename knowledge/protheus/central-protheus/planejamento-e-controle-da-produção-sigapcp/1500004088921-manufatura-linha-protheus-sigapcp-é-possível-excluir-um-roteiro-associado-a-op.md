---
article_id: 1500004088921
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 9efce3ee57b60d183dca9623f8eecdba6c3bda6dff31ea06539b59a1d555d3d9
fetched_at: '2026-06-28T22:42:42.209684+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - É possível excluir um roteiro associado
  a OP
type: support-article
updated_at: '2021-08-25T18:21:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004088921-Manufatura-Linha-Protheus-SIGAPCP-%C3%89-poss%C3%ADvel-excluir-um-roteiro-associado-a-OP
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:00:50 min  
  
Dúvida**É possível excluir um **roteiro** associado a **OP - Ordem de Produção**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**  
O Sistema não permite que um **roteiro** seja excluído quando está associado a uma **OP**, porém se o parâmetro **MV\_PCPATOR - Indica que as operações serão geradas individualmente na ordem de produção** estiver ativo e desse modo as **operações** do **roteiro** forem copiadas para a tabela **SHY - Operações x Ordem** no momento da abertura da **OP**, será possível excluir o **roteiro**.  
  
**Importante**Será possível excluir o **roteiro** somente para novas **OPs**, para os registros já existentes não será possível excluir o **roteiro**.  
  
**Saiba mais**  
Na documentação [Manufatura - Linha Protheus - SIGAPCP - Como a alteração do roteiro reflete nas OPs](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036628014-MP-SIGAPCP-Como-a-altera%C3%A7%C3%A3o-do-roteiro-reflete-nas-OPs) mostra o comportamento do parâmetro **MV\_PCPATOR.**
