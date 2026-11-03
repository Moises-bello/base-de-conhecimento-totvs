---
article_id: 35190588599447
category: Reforma Tributária
content_hash: 830a5e83f4cf9c981e4e2cc691078d674266db299711cfd51b0346f4df80f78c
fetched_at: '2026-06-28T22:39:53.815523+00:00'
product: protheus
section_id: 34900856700439
source: central-protheus
title: 'Cross Segmentos - TSS - Reforma Tributária - 225 Rejeicao: Falha no Schema
  XML da NFe (Elemento: enviNFe/NFe[1]/infNFe/det[1]/vItem/)'
type: support-article
updated_at: '2025-11-27T14:29:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35190588599447-Cross-Segmentos-TSS-Reforma-Tribut%C3%A1ria-225-Rejeicao-Falha-no-Schema-XML-da-NFe-Elemento-enviNFe-NFe-1-infNFe-det-1-vItem
---

**Dúvida**  
Como corrigir o erro 225 Rejeicao: Falha no Schema XML da NFe (Elemento: enviNFe/NFe[1]/infNFe/det[1]/vItem/)

**Ambiente**  
Cross Segmentos - Backoffice Protheus - Todas as versões      
  
**Solução**  
Caso apresente o erro 225 Rejeicao: Falha no Schema XML da NFe (Elemento: enviNFe/NFe[1]/infNFe/det[1]/vItem/) ao emitir notas fiscais eletrônicas, Faça as atualizações da documentação abaixo:

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/33208366723607-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFE-Reforma-Tribut%C3%A1ria-Nota-T%C3%A9cnica-2025-002-v-1-10-v1-20-e-V1-30-IBS-CBS>

**Para montar a tag vItem em produção facultativa antes de 05/01/2026, precisa criar o parâmetro MV\_NT25002 = 10/11/2025 na tabela SPED000 do TSS para a entidade que deseja mandar IBS e CBS um produção**
