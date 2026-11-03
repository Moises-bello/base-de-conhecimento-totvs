---
article_id: 360047143614
category: NFe - Nota Fiscal Eletrônica
content_hash: 32d8a95a7843b0a9de99b581efe2341a9e789ef93de96f7207a9cb302d38f6ac
fetched_at: '2026-06-28T22:40:03.561658+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  Como gerar a TAG  reboque
type: support-article
updated_at: '2025-07-03T12:12:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047143614-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-a-TAG-reboque
---

**Dúvida**Como gerar a TAG reboque ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

1- Para gerar a TAG Reboque de **nota de entrada**no documento de entrada além do campo ***F1\_PLACA do veículo*** na aba **informações adicionais** há os campos **Veículo 1, Veículo 2 e Veículo 3 para gerar as informações do Reboque.**

 Ao preencher o veículo 1 será gerada a TAG **<veicTransp>** e ao preencher o veículo 2 e veículo 3 será gerada a TAG **<reboque>**

![20210204_161624.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500002281922)

2 - Conforme o exemplo do XML abaixo foi preenchido apenas um reboque:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360068558774)

 3- Para gerar a TAG Reboque de **nota de** **saída** fazer o pedido de venda e gerar o Documento de saída, após isso ir na Rotina de Expedição **(Faturamento >> Atualizações >> Faturamento >> Expedição)**

4- Clicar no Botão Manutenção:

* **Informar Transportadora**
* **Veículo 1**
* **Veículo 2 = 1º Reboque**
* **Veículo 3 = 2º Reboque** (Se houver um segundo reboque)

![MDFe_reboque.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360101166414)

5- Conforme o exemplo do XML abaixo foi preenchido apenas um reboque:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360068558774)

* **Importante:**

* Para operações internas para gerar as TAGS**<veicTransp> e <reboque>**configurar o parâmetro **MV\_INTTRAN** = **.T.**

**Nome:** MV\_INTTRAN  
**Descrição:** Habilita a geração das tags <veicTransp> e <reboque>, em operações internas para NFESEFAZ.  
**Tipo:** Lógico  
**Conteúdo:** .F. - Não gera as TAGS .T. - Gera as TAGS

* Saiba mais:

No Danfe será impresso apenas o **veículo** principal conforme o print abaixo:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360069683373)
