---
article_id: 360018769492
category: Escrita Fiscal - Impostos - ICMS
content_hash: 44d7b74bb9a1e09962432b0387100e85a32ff44de19aa0ffd6f38d131f0ccf26
fetched_at: '2026-06-28T22:39:26.054882+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: 'MP - FIS - Parâmetro MV_SUBTRIB com Limite Excedido '
type: support-article
updated_at: '2021-04-29T18:56:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018769492-MP-FIS-Par%C3%A2metro-MV-SUBTRIB-com-Limite-Excedido
---

**Dúvida**

Estamos informando no parâmetro MV\_SUBTRIB as IE´s, porém chegamos ao limite do parâmetro e precisamos colocar outros estados.   
  
Como proceder para que possamos configurar no Protheus as novas inscrições?  
  
  
**Ambiente**  
Protheus – Fiscal – A partir da versão 11.80  
  
  
**Solução**Caso o parâmetro MV\_SUBTRIB não seja suficiente para detalhar todas as Inscrições Estaduais da empresa, deverão ser criados parâmetros com nome MV\_SUBTRI e final numérico sequencial para acrescentar as demais inscrições. Exemplo: MV\_SUBTRI2, MV\_SUBTRI3, etc.

O parâmetro MV\_SUBTRIB deve ser configurado a UF + Inscrição Estadual separados por barra conforme exemplo abaixo:   
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360095923334/mceclip0.png)  
  
Maiores informações, acessar o boletim técnico contido no link abaixo:

<http://tdn.totvs.com/pages/releaseview.action?pageId=185738490>
