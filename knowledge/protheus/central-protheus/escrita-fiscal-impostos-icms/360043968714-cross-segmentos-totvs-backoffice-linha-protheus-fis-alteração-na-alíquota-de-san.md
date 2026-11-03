---
article_id: 360043968714
category: Escrita Fiscal - Impostos - ICMS
content_hash: 8de4fba9575a83301d59a8a85e27af1b697818be17a4394192575c4b1342bb1f
fetched_at: '2026-06-28T22:39:24.133731+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Alteração na alíquota
  de Santa Catarina, conforme a lei 17.878/2019
type: support-article
updated_at: '2021-07-28T02:29:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043968714-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Altera%C3%A7%C3%A3o-na-al%C3%ADquota-de-Santa-Catarina-conforme-a-lei-17-878-2019
---

**Dúvida**

**MP-FIS-Alteração na alíquota de Santa Catarina, conforme a lei 17.878/2019**

Protheus-Fiscal – A partir da versão 11.80]  
  
**Solução**

A lei trata de alíquotas diferenciadas de ICMS que podem ser tratadas pelas funcionalidade padrões do sistema, via exceção fiscal.

Essa alteração deverá ser aplicada para contribuinte (revendedor/consumidor final) do ICMS com operações dentro do estado.

Exemplo de configuração para exceção fiscal:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060375153/mceclip0.png)

Para os demais clientes o sistema trata a alíquota padrão automaticamente pelo fonte MATXFIS que verifica os parâmetros: MV\_ESTICM e MV\_ICMPAD, considerando a alíquota interna do estado de 17%. 

-Para maiores informações sobre os parâmetros acesse o link:  
[https://tdn.totvs.com/pages/releaseview.action?pageId=240299174](https://www.google.com/url?q=https://tdn.totvs.com/pages/releaseview.action?pageId%3D240299174&sa=D&source=hangouts&ust=1583427050592000&usg=AFQjCNE-A06UxdDYeif_zjiDmCyosiz9eA)  
  
-Para maiores informações sobre a configuração da exceção fiscal:  
[https://tdn.totvs.com/pages/releaseview.action?pageId=269448119](https://www.google.com/url?q=https://tdn.totvs.com/pages/releaseview.action?pageId%3D269448119&sa=D&source=hangouts&ust=1583427050592000&usg=AFQjCNG6_Uv9Fncv1hoH3s8TkFDrTDD9TQ)
