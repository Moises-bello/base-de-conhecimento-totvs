---
article_id: 360045569873
category: RH - GRRF (Guia de Recolhimento Rescisório - FGTS)
content_hash: a74972e5a67aafa3730cde93e3f565d68ae0569cf1af0c243b0ab815ae4aa470
fetched_at: '2026-06-28T22:43:32.387068+00:00'
product: protheus
section_id: 360010781714
source: central-protheus
title: RH - Linha Protheus - GPE - Como conferir a GRRF da rescisão complementar por
  dissídio
type: support-article
updated_at: '2024-09-18T20:40:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045569873-RH-Linha-Protheus-GPE-Como-conferir-a-GRRF-da-rescis%C3%A3o-complementar-por-diss%C3%ADdio
---

**Ocorrência**Como conferir a GRRF da rescisão complementar por dissídio?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão Pessoal - A partir da versão 12  
  
**Solução**A GRRF (Guia de Recolhimento Rescisório do FGTS) da rescisão complementar tem por objetivo o recolhimento referente aos valores de Aviso Prévio e a Multa Rescisória.

Uma vez que a GRRF de rescisão complementar não permite recolhimento do FGTS do sobre a **remuneração do mês e remuneração de 13º salário**, será feito o recolhimento nesta Sefip com **código 650.**

Para conferência da GRRF de rescisão complementar separamos do cálculo efetuado as verbas com Identificadores referente a Aviso, das demais verbas:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360062284174/mceclip0.png)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360062285374/mceclip1.png)

Parâmetros de Geração

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360063181833/mceclip2.png)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360062285914/mceclip3.png)

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360063182173/mceclip5.png)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360063182233/mceclip6.png)

Log de Ocorrência da GRRF

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360062286234/mceclip7.png)

**VALOR FGTS**  (verbas 161/132) = 110,34 + 33,34 =  143,68 X 8% = **11,49** (base para recolhimento da multa dos 40%)  
**AV. PRÉVIO** (verbas 134/ 157) = 16,66 + 220,00 = **236,66**

Memória de cálculo  
**Valor FGTS** - Este campo é **composto por 8%** da soma dos Ids. **0337 e 0398** exceto os valores referentes ao Aviso Prévio, pois existe um campo especial para eles. Os Ids. de aviso que devem ser excluídos são: 0111 – Aviso Prévio, 0115 – 13º Sobre o Aviso, 0250 – Média Aviso Prévio, 0252 – Média Férias sobre aviso, 0253 – Média de 13º salário sobre aviso indenizado. Sendo assim, para compor este campo temos que fazer: **(0337 + 0398) – (0111 + 0115 + 0250 + 0252 + 0253) \* 8%= “Valor FGTS** **Av. Prévio** - Este campo é composto pelos Ids. relacionados ao aviso, ou seja, os mesmos que excluímos do campo anterior, são eles: **0111** – Aviso Prévio, **0115** – 13º Sobre o Aviso, **0250** – Média Aviso Prévio, **0252** – Média Férias sobre aviso, **0253** – Média de 13º salário sobre aviso indenizado.  
Sendo assim, para compor este campo temos que fazer: **0111 + 0115 + 0250 + 0252 + 0253 = “Av. Prévio”.**Importando no Validador da GRRF

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360063184093/mceclip8.png)
