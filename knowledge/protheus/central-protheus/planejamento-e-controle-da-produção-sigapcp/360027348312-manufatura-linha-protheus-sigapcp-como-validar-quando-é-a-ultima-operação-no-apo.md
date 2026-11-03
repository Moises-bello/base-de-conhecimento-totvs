---
article_id: 360027348312
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 32c96403d3a97f6bb4c86d0d004d578b243728891ff9a67595f33f60c86b7305
fetched_at: '2026-06-28T22:42:42.058553+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: 'Manufatura - Linha Protheus - SIGAPCP - Como validar quando é a ultima operação
  no apontamento '
type: support-article
updated_at: '2023-08-15T11:15:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027348312-Manufatura-Linha-Protheus-SIGAPCP-Como-validar-quando-%C3%A9-a-ultima-opera%C3%A7%C3%A3o-no-apontamento
---

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:00:45 min****Dúvida**Como validar quando é a ultima operação no apontamento realizado pela rotina **MATA681 - Produção PCP MOD 2**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Para que o Sistema valide qual é a ultima operação no apontamento é necessário ativar o parâmetro **MV\_VLDOPER - Indica se deve validar as operações no apontamento de produção PCP MOD 2**. Caso contrário, o Sistema apresenta uma mensagem ao usuário, em cada apontamento, questionando se é a última operação. Se informar que é a ultima operação, então a **OP - Ordem de produção** é encerrada.
