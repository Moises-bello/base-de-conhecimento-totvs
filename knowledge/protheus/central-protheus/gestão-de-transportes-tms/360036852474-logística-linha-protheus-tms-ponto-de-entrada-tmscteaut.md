---
article_id: 360036852474
category: Gestão de Transportes (TMS)
content_hash: e02d0c4d6052f35d33076468ccefd51fce25765e02724672662886643c6e7c40
fetched_at: '2026-06-28T22:45:32.421615+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de Entrada TMSCTEAUT
type: support-article
updated_at: '2022-06-17T18:39:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036852474-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-Entrada-TMSCTEAUT
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:00:30 min**  
**Dúvida**Como implementar o ponto de entrada **TMSCTEAUT -  Status do Documento** ao **TSS - TOTVS Service SOA**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Este ponto de entrada está localizado na função **WsCteMnt**, responsável por solicitar o **Status do Documento** ao **TSS**.   
Segue exemplo do fonte:

* **Ponto de Entrada: TMSCTEAUT,**
* **Programa Fonte:** **SPEDNFE.PRX**
* **Sintaxe:**ExecBlock("TMSCTEAUT",.F.,.F.,{DT6->DT6\_FILDOC, DT6->DT6\_DOC, DT6->DT6\_SERIE, DT6->DT6\_SITCTE})

**Parâmetros**

|  |  |  |
| --- | --- | --- |
| **Nome** | **Tipo** | **Descrição** |
| DT6->DT6\_FILDOC | Caractere | Filial do Documento |
| DT6->DT6\_DOC | Caractere | Documento |
| DT6->DT6\_SERIE | Caractere | Série do Documento |
| DT6->DT6\_SITCTE | Caractere | Situação do CT-e - Conhecimento de Transporte Eletrônico |

**Exemplo fonte:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048132114/mceclip0.png)
