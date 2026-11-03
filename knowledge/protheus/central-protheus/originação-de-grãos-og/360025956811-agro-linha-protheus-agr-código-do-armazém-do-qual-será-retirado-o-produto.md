---
article_id: 360025956811
category: Originação de Grãos (OG)
content_hash: c0ee762fa6a4bdf32a10d745ad17e5263e0f5e052370b537dad8e49a1b3f6db8
fetched_at: '2026-06-28T22:45:37.529965+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Código do armazém do qual será retirado o produto
type: support-article
updated_at: '2025-06-24T11:53:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025956811-Agro-Linha-Protheus-AGR-C%C3%B3digo-do-armaz%C3%A9m-do-qual-ser%C3%A1-retirado-o-produto
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20176047654807)** Tempo aproximado para leitura: **00:00:30 min**  
**Ocorrência**Ao tentar confirmar um romaneio, na rotina **OGA250 - Romaneio com Pesagem**, é exibida a mensagem: **Ajuda: C6\_Local - Código do Armazém do qual será Retirado o Produto**.  
  
 **Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
 **Causa**Essa mensagem ocorre porque o tamanho do campo **NJJ\_CODPRO - Código do Produto** não está de acordo com os demais campos de Produto das outras tabelas.   
  
 **Solução**É necessário ajustar o tamanho do campo de acordo com o tamanho definido no campo **B1\_COD - Código**.
