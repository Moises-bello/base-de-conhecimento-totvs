---
article_id: 360046283014
category: Escrita Fiscal - Impostos - ISS
content_hash: baee0b033cde5784d4e77f2fa3b50ed970982ac304d3821c6bab6859f84d0913
fetched_at: '2026-06-28T22:39:35.197899+00:00'
product: protheus
section_id: 1500001549762
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como aplicar desconto
  condicional e incondicional com ISS
type: support-article
updated_at: '2021-06-15T13:11:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046283014-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-aplicar-desconto-condicional-e-incondicional-com-ISS
---

**Dúvida**  
Aplicação de desconto condicional e incondicional com cálculo de ISS.  
  
**Ambiente**Protheus – Faturamento – A partir da versão 12.1.17  
  
**Solução**Desconto incondicional:

Emissa NFse com **desconto Incondicional**  
Vlr Servico = R$ 1000,00  
Desconto Condicionado = $ 150,00  
Base ISS = $ 850,00  
Vlr Liquido - $ 850,00

Utilize o campo no TES Desc. ISS (F4\_DESCISS) como sim:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360067134693/mceclip0.png)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360067134733/mceclip1.png)

Observe que a base de cálculo do ISS deduziu o desconto incondicional.  
  
Desconto condicional:

Vlr Servico = R$ 1000,00  
Desconto Condicionado = $ 150,00  
Base ISS = $ 1000,00  
Vlr Liquido - $ 850,00

Utilize no TES o campo Desc. Condici (F4\_DESCOND):

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360067134933/mceclip2.png)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360066072394/mceclip3.png)

Observe que a base do ISS foi mantida com o valor total do serviço, mesmo aplicando o desconto.

**Importante:** Nas duas situações, utilizar o campo C6\_VALDESC aplicando o valor do desconto. Após prepara a nota de saída o campo D2\_DESCON será populado.
