---
article_id: 12712849650711
category: RH - Rescisão
content_hash: b75267aaff1df2176be68175a6c35d32ce501cc3e5989218d352113fb2615aa6
fetched_at: '2026-06-28T22:43:53.659649+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Por que relatório de médias emitido no cálculo
  da rescisão apresenta linha com descrição TOT DSR
type: support-article
updated_at: '2025-05-21T11:19:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12712849650711-RH-Linha-Protheus-GPE-Por-que-relat%C3%B3rio-de-m%C3%A9dias-emitido-no-c%C3%A1lculo-da-rescis%C3%A3o-apresenta-linha-com-descri%C3%A7%C3%A3o-TOT-DSR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18329499930135) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Por que relatório de médias emitido no cálculo da rescisão apresenta linha com descrição TOT DSR?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) -Gestão de Pessoal - A partir da Versão 12.1.17  
  
**Solução**O relatório de médias emitido no cálculo da rescisão apresenta linha com descrição TOT DSR devido configuração S043.

**S043**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12712806720791)

**Descrição do campo:**

|  |  |
| --- | --- |
| DSR Média Fer/13º/Av. Prévio: | Este campo define se deve ser calculado o DSR sobre as médias pagas em rescisão (Esta configuração é muito especifica do sindicato da categoria, portando mantem-se este campo com N). **Se este campo estiver com SIM, irá causar divergências entre o calculo da rescisão e o demonstrativo de médias.** |

**Exemplo de como fica em rescisão o calculo da média:**

**Relatório médias férias vencidas.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18329448599959)

**Rescisão**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18329486488343)

**168,08 + 32,32 = 200,40**

**Saiba mais**Para adquirir maior conhecimento acesse o *link* abaixo

<https://tdn.totvs.com/pages/releaseview.action?pageId=519190688>
