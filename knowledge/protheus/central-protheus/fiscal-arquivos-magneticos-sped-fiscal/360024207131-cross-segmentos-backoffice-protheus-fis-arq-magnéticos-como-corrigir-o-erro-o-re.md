---
article_id: 360024207131
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: dbdc9774a73472d909976fea539287f6998c4f1a74235cdbb6edb43e84010caa
fetched_at: '2026-06-28T22:42:00.901659+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Como corrigir
  o erro "O Registro deve ser informado para a(s) UF(s) de origem" no registro E300
type: support-article
updated_at: '2025-02-11T20:57:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024207131-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-corrigir-o-erro-O-Registro-deve-ser-informado-para-a-s-UF-s-de-origem-no-registro-E300
---

**Dúvida**Como corrigir o erro "O registro deve ser informado para a(s) UF(s) de origem" no registro E300?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360022172452/mceclip0.png)  
  
  
**Ambiente**Microsiga Protheus – Livros Fiscais – A partir da versão 11.80  
  
   
**Solução**1- Para corrigir o erro de validação "O Registro deve ser informado para a(s) UF(s) de origem" no registro E300, informe a UF de origem no parâmetro **MV\_SUBTRIB** conforme demonstrado:

No exemplo abaixo, a UF de origem é SP (**MV\_ESTADO** = SP).  
  
![E300.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360022174772/E300.gif)  
  
  
2- Após a correção do parâmetro **MV\_SUBTRIB**, gere novamente o arquivo do Sped Fiscal.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360022167031/mceclip1.png)
