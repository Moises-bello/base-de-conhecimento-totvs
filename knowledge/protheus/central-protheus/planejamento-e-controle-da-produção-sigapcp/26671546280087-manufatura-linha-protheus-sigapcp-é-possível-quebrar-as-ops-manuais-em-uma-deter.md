---
article_id: 26671546280087
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: b0c9a376e1dc967db7ebf88ea85120b6b7ae86d0e335c361cb6a447dab12a14f
fetched_at: '2026-06-28T22:42:42.218327+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - É possível quebrar as OPs manuais em
  uma determinada quantidade
type: support-article
updated_at: '2024-09-27T18:17:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26671546280087-Manufatura-Linha-Protheus-SIGAPCP-%C3%89-poss%C3%ADvel-quebrar-as-OPs-manuais-em-uma-determinada-quantidade
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26671514685719)**Tempo aproximado para leitura: **00:00:45 min  
  
Dúvida**É possível quebrar uma **OP - Ordem de produção** manual aberta através da rotina **MATA650 - Ordem de Produção** em uma determinada quantidade?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Não é possível quebrar a **OP**em uma determinada quantidade, considerando a informação dos campos **B1\_LE - Lote Econômico** e **B1\_LM - Lote Mínimo** para o produto, quando o parâmetro **MV\_QUEBROP- Define se as OPs serão quebradas de acordo com o lote econômico ou se será gerada apenas uma ordem de produto com quantidade total** está igual a **S**.  
  
Somente irá quebrar as **OPs Intermediárias**, não a **OP** pai. A **OP** pai será gerada de acordo com a quantidade informada em tela.
