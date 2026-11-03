---
article_id: 360051693134
category: RH - Cadastros
content_hash: 70fb50ce14191338318934ea682c438e098d4537828cbbbb51df37cff8115a61
fetched_at: '2026-06-28T22:44:52.927091+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Como utilizar a funcionalidade do contador de DSR
  no Ponto Eletrônico
type: support-article
updated_at: '2025-06-16T18:13:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051693134-RH-Linha-Protheus-PON-Como-utilizar-a-funcionalidade-do-contador-de-DSR-no-Ponto-Eletr%C3%B4nico
---

**Dúvida**Como utilizar a funcionalidade do contador de DSR no Ponto Eletrônico?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**Para realizar o desconto de DSR em verba de DIAS e não Horas, é necessário fazer o cadastro e vínculo do evento contador de DSR conforme exemplo abaixo:  
  
1 - no evento de desconto de DSR que possui ID de ponto, não deve existir verba de folha e o código do evento contador já deve ser vinculado:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360082017754/mceclip0.png)  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360082017814/mceclip1.png)  
  
2 - no evento contador, deve existir a verba do tipo DIA vinculada:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360082017874/mceclip2.png)  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360082017934/mceclip3.png)  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083157173/mceclip4.png)  
  
  
Desta forma, quando for realizado o cálculo mensal, o sistema mostrará nos Lançamentos de Resultados do funcionário a verba e o lançamento em dias.
