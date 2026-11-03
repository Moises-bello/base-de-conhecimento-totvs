---
article_id: 4408539014935
category: Escrita Fiscal - Impostos - ICMS
content_hash: bfaefecbde482c2ece8fcc06e7f0c901edf30cb0a2cca6c073ac267b48620ab6
fetched_at: '2026-06-28T22:39:24.204801+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como gravar os campos  CD2_VFCPDI
  e CD2_VFCPEF?
type: support-article
updated_at: '2021-09-15T11:18:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408539014935-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-gravar-os-campos-CD2-VFCPDI-e-CD2-VFCPEF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:05:00**min** **Dúvida**Como gravar os campos CD2\_VFCPDI e CD2\_VFCPEF ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**

Os campos serão gravados nas operações com calculo de  DIFERIMENTO, temos 7 opção conforme a TES

1) exemplo

**F4\_ICM:**Definido como SIM.

**F4\_ICMSDIF:**Definido como 1 

**F4\_PICMDIF:**Informar o Percentual de Diferimento: 33,33%

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408537914647/mceclip0.png)

CD2

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408538079383/mceclip1.png)

2) exemplo

**F4\_ICM:**Definido como SIM.

**F4\_ICMSDIF:**Definido como 3

**F4\_PICMDIF:**Informar o Percentual de Diferimento:33,33%

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408538119191/mceclip2.png)

CD2

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408538176023/mceclip3.png)

3) exemplo

**F4\_ICM:**Definido como SIM.

**F4\_ICMSDIF:**Definido como 4

**F4\_PICMDIF:**Informar o Percentual de Diferimento:50,00%

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408544034967/mceclip4.png)

CD2

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408538321047/mceclip5.png)

4) exemplo

**F4\_ICM:**Definido como SIM.

**F4\_ICMSDIF:**Definido como 5

**F4\_PICMDIF:**Informar o Percentual de Diferimento:50,00%

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408544161047/mceclip6.png)

CD2

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408538533015/mceclip7.png)

5) exemplo

**F4\_ICM:**Definido como SIM.

**F4\_ICMSDIF:**Definido como =6

**F4\_PICMDIF:**Informar o Percentual de Diferimento:33,33%

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408544315287/mceclip8.png)

CD2

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408544342039/mceclip9.png)

6) exemplo

**F4\_ICM:**Definido como SIM.

**F4\_ICMSDIF:**Definido como 7

**F4\_PICMDIF:**Informar o Percentual de Diferimento:33,33%

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408538824215/mceclip10.png)

CD2

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408544429719/mceclip11.png)

Os campos CD2\_VFCPDI, CD2\_VFCPEF e CD2\_VFCP (já existente) ficarão responsáveis por gravar os valores relativos ao FECP.

* O campo CD2\_VFCP fica responsável por gerar a tag <vFCP>, onde é gravado o Valor do ICMS relativo ao Fundo de Combate à Pobreza (FCP), considerando o valor do FCP Efetivo + o valor do FCP Diferido, ou seja, o valor total do FCP desconsiderando o possível valor diferido.
* O campo CD2\_VFCPDI fará a geração da tag <vFCPDif>, onde é gravado o Valor do ICMS relativo ao Fundo de Combate à Pobreza (FCP) diferido.
* Já o campo CD2\_VFCPEF fará a geração da tag <vFCPEfet>, onde é gravado o Valor do ICMS relativo ao Fundo de Combate à Pobreza (FCP) efetivo, ou seja, o valor total de FCP - o valor diferido de FCP.
