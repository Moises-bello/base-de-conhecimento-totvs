---
article_id: 360060514153
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: 5ee7c0a65845f47a0cafa06c03d101e914b7dd6e6974ee25d69c9f2dd210b8cb
fetched_at: '2026-06-28T22:39:49.915722+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC -  CARGA SEM INFORMAÇÃO
  PELO DEPOSITÁRIO
type: support-article
updated_at: '2021-12-22T12:56:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060514153-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-CARGA-SEM-INFORMA%C3%87%C3%83O-PELO-DEPOSIT%C3%81RIO
---

**Dúvida**Como preencher a Presença de Carga "CARGA SEM INFORMAÇÃO PELO DEPOSITÁRIO"?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
  
**Solução**Para que sejam enviadas as informações corretamente, preencher no Desembaraço, aba Embarque.

- Informar no campo W6\_MAWB [Master] Somente o numero da Presença de carga - "Sem o CEMERCANTE31032008"

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099086794/mceclip0.png)

- Informar no campo W6\_PRCARGA [Presença de Carga] "CEMERCANTE31032008" - sem o numero da carga

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099087134/mceclip1.png)  
- Selecionar no campo W6\_TIPOCON [Tipo de Conhecimento]: 12 = HLB

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000221021/mceclip2.png)

- No campo W6\_IDENTVE [Embarcação] é para criar/usar um codigo existente com N.da Viagem e Bandeira (não informar um texto).

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000208582/mceclip3.png)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101322073/mceclip4.png)
