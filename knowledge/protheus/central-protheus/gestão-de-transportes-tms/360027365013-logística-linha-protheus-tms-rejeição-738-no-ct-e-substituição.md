---
article_id: 360027365013
category: Gestão de Transportes (TMS)
content_hash: 45ce044d8ce6202f3461c8283585ee640003e7856aa8b10e73212e6a8951fd3e
fetched_at: '2026-06-28T22:45:33.322177+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Rejeição 738 no CT-e Substituição
type: support-article
updated_at: '2022-06-14T20:30:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027365013-Log%C3%ADstica-Linha-Protheus-TMS-Rejei%C3%A7%C3%A3o-738-no-CT-e-Substitui%C3%A7%C3%A3o
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:30 min****Dúvida**Como avaliar a **Rejeição 738 - A indicação do tomador do CT-e - Conhecimento de Transporte Eletrônico de substituição deve ser igual a do CT-e substituído**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Ao receber a **Rejeição 738 - A indicação do tomador do CT-e de substituição deve ser igual a do CT-e substituído**, será necessário comparar o **arquivo XML do CT-e original com o CT-e de Substituição** e validar as informações abaixo:  
  
A ***tag*** **toma3**: correspondente ao tomador do serviço, podendo ser preenchida da seguinte forma:  
  
0-Remetente  
1-Expedidor  
2-Recebedor  
3-Destinatário  
  
Se no **arquivo *XML* do CT-e original estiver como 3-Destinatário**, ao realizar o **CT-e de Substituição a SEFAZ - Secretaria da Fazenda valida se o tomador é o mesmo**, caso seja enviado **no arquivo XML do CT-e de Substituição o tomador diferente,** será apresentada a rejeição **738 - A indicação do tomador do CT-e de substituição deve ser igual a do CT-e substituído**.  
  
**Exemplo:** Arquivo *XML* do **CT-e de Substituição**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042695393/mceclip2.png)

Toma3 = 3-Destinatário  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042695633/mceclip4.png)

Consultar o **CT-e** de origem no arquivo *XML* ou na **SEFAZ** e observar se o tomador é o mesmo:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041857394/mceclip5.png)

Dessa forma, será apresentada a **rejeição 738 - A indicação do tomador do CT-e de substituição deve ser igual a do CT-e substituído**.
