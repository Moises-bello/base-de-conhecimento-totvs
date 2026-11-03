---
article_id: 360034940353
category: UBA - Unidade de Beneficiamento de Algodão
content_hash: 772d67da1cc66e0545cf25f06e0032cd51430429f0a443061817c77d9f0fd3da
fetched_at: '2026-06-28T22:45:35.615430+00:00'
product: protheus
section_id: 360005717853
source: central-protheus
title: Agro - Linha Protheus - UBA - Mensagem de entidade não encontrada ao informar
  ordem de colheita
type: support-article
updated_at: '2025-06-18T20:10:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034940353-Agro-Linha-Protheus-UBA-Mensagem-de-entidade-n%C3%A3o-encontrada-ao-informar-ordem-de-colheita
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21881384169239)**Tempo aproximado para leitura: **00:00:30 min**  
 **Ocorrência**Na rotina **AGRA500 - Romaneio Unificado**, ao selecionar a ordem de colheita é exibida a mensagem: **Não foi encontrada a Entidade vinculada com a fazenda informada na Ordem de Colheita**.  
  
 **Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - UBA - Unidade de Beneficiamento de Algodão - Versão 12  
  
 **Causa**Essa mensagem é exibida porque a entidade informada não corresponde à ordem de colheita selecionada.  
  
 **Solução**Para que a mensagem não seja exibida e para que o processo seja retomado é necessário verificar na rotina**AGRA005 - Fazendas**qual é a entidade vinculada à fazenda utilizada na ordem de colheita.  
 Ao informar a entidade correspondente à fazenda da ordem de colheita o processo seguirá corretamente.
