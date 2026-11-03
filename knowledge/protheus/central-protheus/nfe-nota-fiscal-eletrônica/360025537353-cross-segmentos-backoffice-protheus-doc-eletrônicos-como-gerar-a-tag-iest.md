---
article_id: 360025537353
category: NFe - Nota Fiscal Eletrônica
content_hash: 02eeac1199ec69f30e058553e3ea31814621bb576bfae87bd62e47c77034a655
fetched_at: '2026-06-28T22:40:03.575491+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  Como gerar a TAG
  IEST
type: support-article
updated_at: '2024-11-06T13:52:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025537353-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-a-TAG-IEST
---

**Dúvida**Como gerar a TAG IEST ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.27

Cross Segmentos - TSS - a partir da versão 12

**Solução**

1. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /** **Cadastros / Parâmetros** clicar em **editar**

**MV\_SUBTRIB** **Exemplo:** MG1111111111111/RS11111111111111/

![](https://centraldeatendimento.totvs.com/hc/article_attachments/12840114445079)

2. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /** **Cadastros / Parâmetros** clicar em **editar**  Observação: O **parâmetro** no configurador **MV\_STNIEUF "não"** pode ser preenchido estados de origem e destino do parâmetro.  **Exemplo:** SPSP/SPMG/SPPR.  Caso esteja o estado de **origem** e de **destino** nesse parâmetro MV\_STNIEUF retire. 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/12840167912087)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/12840147807511)

3. O parâmetro **MV\_COMBPET** deve ser utilizado quando **não houver calculo de ICMS-ST.**

Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /** **Cadastros / Parâmetros** clicar em **editar MV\_COMBPET = .T.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/12840200936855)**

4. Para gerar a ***Tag IEST,*** pode ser configurado também conforme o link abaixo:  
  
*[Clique Aqui](http://tdn.totvs.com/pages/releaseview.action?pageId=225951368)*

Caso haja a necessidade de gerar a tag IEST para o cliente entrega verifique a informação abaixo:

<https://tdn.totvs.com/pages/viewpage.action?pageId=883064237>

* ***Saiba mais:***

Será necessário, informar na TAG IEST um **IE diferente do emitente e do destinatário.**

A TAG é apenas para **operações interestaduais para operações internas**não é gerada.

Há apenas uma **exceção** para emitentes da **UF do PR** para **operações internas.**

* Conforme o **parecer da consultoria tributária** da TOTVS no link abaixo:

[Clique Aqui](%20http://tdn.totvs.com/pages/releaseview.action?pageId=497460058%20)

Para nota de devolução a TAG ***IEST não é gerada no XML:***

* Conforme o **parecer da consultoria tributária** da TOTVS no link abaixo:

[Clique Aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=437261045)

Para cliente de entrega referente a TAG ***IEST deve ser gerada conforme o parecer abaixo:***

* Conforme o **parecer da consultoria tributária** da TOTVS no link abaixo:

[Clique Aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=223934099)
