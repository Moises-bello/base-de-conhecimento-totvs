---
article_id: 4408442782231
category: Financeiro - Comissão
content_hash: 96b482d5aa688f9a8309fca5087a62b012a4f78165c1d46e917102f2d1143a87
fetched_at: '2026-06-28T22:37:50.758032+00:00'
product: protheus
section_id: 26655771327895
source: central-protheus
title: Cross Segmento Backoffice Linha Protheus - SIGAFIN - FINA440 - Qual a diferença
  entre comissão online e offline
type: support-article
updated_at: '2026-03-04T11:55:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408442782231-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA440-Qual-a-diferen%C3%A7a-entre-comiss%C3%A3o-online-e-offline
---

**Dúvida**  
Qual é a diferença entre comissão online e offline?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
Para a definição do tipo de comissão a ser utilizada pelo sistema, é imprescindível a correta configuração do parâmetro **MV\_TPCOMIS**, o qual poderá ser ajustado conforme as opções abaixo.

No cadastro do vendedor, a forma de geração da comissão é determinada por meio dos campos **%Pg na Emiss (Emissão)** e **%Pg na Baix (Baixa)**. Nesses campos, é possível estabelecer a distribuição do percentual da comissão, conforme a regra de negócio adotada pela empresa, tais como:

* 100% na emissão;
* 100% na baixa;
* 50% na emissão e 50% na baixa;
* ou qualquer outra combinação que totalize 100%.

No exemplo a seguir, a configuração está definida com **100% na baixa**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30770609829911)

**Comissão online**

Ao gerar o título com o parâmetro **MV\_TPCOMIS = O**, a comissão será gerada automaticamente, de acordo com o percentual configurado no cadastro do vendedor, seja na emissão ou na baixa.

**Comissão Offline**

O parâmetro deverá ser configurado como **MV\_TPCOMIS = B**, situação em que o cálculo da comissão não ocorrerá de forma automática, sendo necessário realizar o processamento em lote por meio da execução da rotina de **Recálculo de Comissão (FINA440).**

**Saiba mais**

[Recálculo de Comissões (FINA440 - SIGAFIN)](https://tdn.totvs.com/pages/releaseview.action?pageId=312162528)

[Financeiro - Comissão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/26655771327895-Financeiro-Comiss%C3%A3o)
