---
article_id: 360041164333
category: Originação de Grãos (OG)
content_hash: 6efbb3c46b7db5b269cbeed33ab4ba3bd2f71be572ba6bb0ee3aaf227eeb5fdc
fetched_at: '2026-06-28T22:45:39.375071+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: 'Agro - Linha Protheus - AGR - Erro ao usar a balança: MSSETPORTNAME Array
  out of Bounds MATXFUNA'
type: support-article
updated_at: '2025-10-28T13:10:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041164333-Agro-Linha-Protheus-AGR-Erro-ao-usar-a-balan%C3%A7a-MSSETPORTNAME-Array-out-of-Bounds-MATXFUNA
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20325047963927)**Tempo aproximado para leitura: **00:00:50 min**  
**Ocorrência**Ao tentar confirmar romaneio com pesagem está apresentando o erro **Array out of bounds [1] of [0] on MSSETPORTNAME(MATXFUNA.PRX)**.  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Causa**Esse erro ocorre quando no cadastro de **Usuário x Balança** - **AGRA770**, o campo **Modalidade** está preenchido como **2 - Ambas**, ou seja, **Manual** e **Automático**.

![MATXF.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/7301445245079)

**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

* Foram realizadas correções nessa função **SmartClient** disponível no **Portal do Cliente** no *link*: [SmartClient - 17.3.0.11 - Lobo Guara](https://tdn.totvs.com.br/display/tec/SmartClient+-+17.3.0.11+-+Lobo+Guara)
