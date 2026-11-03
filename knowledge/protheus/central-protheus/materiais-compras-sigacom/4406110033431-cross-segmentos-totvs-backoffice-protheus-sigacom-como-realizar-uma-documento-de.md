---
article_id: 4406110033431
category: Materiais - Compras (SIGACOM)
content_hash: 9e5dee0f42ffda33c4fdd50b04bc1b95af458799c00c4947758a046e4b284be7
fetched_at: '2026-06-28T22:41:16.034213+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como realizar uma Documento
  de Entrada para uma Filial diferente da filial do Pedido Compras ?
type: support-article
updated_at: '2021-08-11T13:29:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406110033431-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-realizar-uma-Documento-de-Entrada-para-uma-Filial-diferente-da-filial-do-Pedido-Compras
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:10:00 min** **Dúvida**Como realizar um Documento de Entrada para um Pedido em outra Filial ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Compras - Todas as versões  
  
**Solução**Para que se possa realizar uma Nota Fiscal de Entrada para uma Filial diferente da Filial em que o Pedido de Compras foi Cadastrado, a possibilidade existente é através da utilização do Campo "Filial p/ Entrega" do Pedido de Compras informando uma filial diferente da que o Pedido está sendo cadastrado.

Para se poder alterar o campo "Filial p/ Entrega" deve-se habilitar o parâmetro MV\_PCFILEN:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406109510295/mceclip0.png)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406109519255/mceclip1.png)

Com o Parâmetro habilitado pode-se informar uma filial diferente no campo "Filial p/ Entrega" da rotina de Pedido de Compras:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406109608983/mceclip3.png)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406109600407/mceclip2.png)

E ao Cadastrar um Documento de entrada para a Filial de Entrega informada no Pedido, o Pedido poderá ser vinculado à NF incluída:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406109701015/mceclip4.png)

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406109714711/mceclip5.png)

E confirmando a inclusão da NF, o Pedido incluído na Filial de Origem é baixado normalmente:

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406109853975/mceclip6.png)

***Saiba Mais :***

* [MP - SIGACOM - Qual o conceito do MV\_PCFILEN e sua interferência na numeração do Pedido de Compras?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022158251)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
