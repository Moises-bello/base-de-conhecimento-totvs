---
article_id: 360052770613
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: a8588dfc7dc1e434c9d62dd35edf9ce80dc9fecb6fcb953c0c45bf6896af74ca
fetched_at: '2026-06-28T22:42:40.915234+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Bloqueio do apontamento de produção
  maior do que o previsto na abertura da OP
type: support-article
updated_at: '2022-09-09T18:10:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052770613-Manufatura-Linha-Protheus-SIGAPCP-Bloqueio-do-apontamento-de-produ%C3%A7%C3%A3o-maior-do-que-o-previsto-na-abertura-da-OP
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura**: 00:01:00 min  
  
Dúvida**Como fazer o bloqueio de um apontamento de produção com quantidade maior do que a prevista na abertura da **OP - Ordem de produção**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Para bloquear o apontamento de produção excedente, configure o parâmetro **MV\_GANHOPR** **- Utilizado para verificar se permite o conceito de Ganho de Produção na inclusão do apontamento de produção** para **.F.** e o parâmetro **MV\_PERCPRM - Percentual da quantidade das ordens de produção qual será permitido apontado a maior** para**0**, dessa forma o Sistema bloqueará o apontamento de produção excedente.  
  
**Saiba mais**Para mais detalhes sobre os parâmetros envolvidos consulte as documentações conforme os *links*:  
[Manufatura - Linha Protheus - SIGAPCP - Quais são os parâmetros referente ao ganho de produção e produção a maior](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026020913-MP-SIGAPCP-Quais-s%C3%A3o-os-par%C3%A2metros-referente-ao-ganho-de-produ%C3%A7%C3%A3o-e-produ%C3%A7%C3%A3o-a-maior)  
[Manufatura - Linha Protheus - SIGAPCP - Parametrização para produção excedente como ganho de produção](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026609853-MP-SIGAPCP-Parametriza%C3%A7%C3%A3o-para-produ%C3%A7%C3%A3o-excedente-como-ganho-de-produ%C3%A7%C3%A3o)
