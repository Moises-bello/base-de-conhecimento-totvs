---
article_id: 4410023002007
category: NFe - Nota Fiscal Eletrônica
content_hash: 3fa51f6cd1f754ab823f85816d038b78eaeda270b3f86a2d5f97ea4000dce64e
fetched_at: '2026-06-28T22:40:03.740051+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 029 : Falha de
  schema vFCPDif'
type: support-article
updated_at: '2021-10-04T18:54:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410023002007-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-029-Falha-de-schema-vFCPDif
---

**Dúvida**Como solucionar a falha de Schema referente a TAG vFCPDif ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

*1 - Ao gerar falha de Schema **referente ao vFCPDif** verifique se o seu XML gerou conforme o **exemplo abaixo:***

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410019368343/mceclip0.png)**

*2- Verifique se está atualizado todos **os fontes conforme o link abaixo:***

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Nota técnica 2020.005](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052495714)

*3- O conteúdo dessa **TAG é obrigatória vFCPDif** verifique qual opção do diferimento foi utilizado e usou as opções corretas:*

* Por isso, é necessário verificar se foi configurado corretamente no sistema a nota de diferimento:

* **No Protheus há 7 tipos de configuração de ICMS diferido conforme o link abaixo:**

<http://tdn.totvs.com/display/public/PROT/FIS0069_DIFERIMENTO_ICMS>

*4- Após isso, **exclua a nota e gere novamente.***

*5- Caso tenha que gerar o calculo, do **FECP com Diferimento** realizar o procedimento abaixo:*

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como gravar os campos CD2\_VFCPDI e CD2\_VFCPEF?](CROSS%20Segmentos%20-%20TOTVS%20Backoffice%20Linha%20Protheus%20-%20FIS%20-%20Como%20gravar%20os%20campos%20CD2_VFCPDI%20e%20CD2_VFCPEF?)

*6- Após isso, **exclua a nota e gere novamente.***
