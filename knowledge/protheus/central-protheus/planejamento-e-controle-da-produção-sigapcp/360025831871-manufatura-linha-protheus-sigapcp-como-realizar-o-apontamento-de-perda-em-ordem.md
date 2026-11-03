---
article_id: 360025831871
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: f488c487dc56cd4f78230e1c8668bb46fde977567f57b7d317c70492aa74a005
fetched_at: '2026-06-28T22:42:42.044878+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: 'Manufatura - Linha Protheus - SIGAPCP - Como realizar o Apontamento de perda
  em Ordem de produção encerrada '
type: support-article
updated_at: '2024-04-23T17:29:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025831871-Manufatura-Linha-Protheus-SIGAPCP-Como-realizar-o-Apontamento-de-perda-em-Ordem-de-produ%C3%A7%C3%A3o-encerrada
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23004414744983)**Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como realizar o **Apontamento de perda - MATA685** em **Ordem de Produção - MATA650** encerrada?   
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Para realizar o apontamento de perda em ordem encerrada é necessário ativar o parâmetro **MV\_A685OPE - Indica se será permitido apontar perda de OP encerrada**.  
Quando o parâmetro estiver **N - Não**, o programa não irá permitir apontar, ficando com a validação atual. Quando o parâmetro estiver **S - Sim**, o programa irá permitir apontar, realizando uma requisição sem vínculo com a ordem de produção.   
Ao realizar o apontamento em ordens encerradas serão geradas uma **RE0 - requisição sem vínculo à ordem de produção**.
