---
article_id: 360004941852
category: NFe - Nota Fiscal Eletrônica
content_hash: 9649e1d228c899bcd3259841f1c57d0fdd2082305a350a3db53651705397f9d3
fetched_at: '2026-06-28T22:39:59.944614+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como destacar
  o IPI na devolução na TAG  vOutro  ou vIPIDevol'
type: support-article
updated_at: '2023-12-01T20:09:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004941852--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-destacar-o-IPI-na-devolu%C3%A7%C3%A3o-na-TAG-vOutro-ou-vIPIDevol
---

**Dúvida**Como destacar o IPI na devolução na TAG vOutro ou vIPIDevol ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

1. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /** **Cadastros / Parâmetros** clicar em **incluir** e informar criar **MV\_IPIOUT e MV\_EIPIOUT** funcionarão em conjunto com os parâmetros **MV\_IPIDEV e MV\_EIPIDEV**, respectivamente.

![](https://tdn.totvs.com/download/attachments/517119820/image2019-10-9_10-5-48.png?version=1&modificationDate=1570626349043&api=v2) ![](https://tdn.totvs.com/download/attachments/517119820/image2019-10-11_15-23-42.png?version=1&modificationDate=1570818225397&api=v2)

![](https://tdn.totvs.com/download/attachments/517119820/image2019-10-9_10-10-14.png?version=1&modificationDate=1570626614597&api=v2)  ![](https://tdn.totvs.com/download/attachments/517119820/image2019-10-11_15-29-11.png?version=1&modificationDate=1570818579257&api=v2)

* Há um boletim do desenvolvimento **no link abaixo:**

*[Clique aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=517119820)*

2. Os **parâmetros** abaixo são utilizados para possibilitar o envio do valor do IPI nas tags **<vOutro>, <vIPI> ou <vIPIDevol>** quando a operação se tratar de uma devolução de compra, conforme tabela abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049577373)

Ambos precisam estar preenchidos

MV\_IPIDEV = .T. e MV\_IPIOUT = .T. gera a tag vOutro

MV\_IPIDEV = .T. e MV\_IPIOUT = .F. gera a tag vIPI

MV\_IPIDEV = .F. e MV\_IPIOUT = .T. gera a tag vIPIDevol

MV\_IPIDEV = .F. e MV\_IPIOUT = .F. gera a tag vIPIDevol

3. **Os parâmetros abaixo são utilizados para possibilitar o envio do valor do IPI nas tags <vOutro>,  <vIPI> ou <vIPIDevol> quando a operação se tratar de uma devolução de venda, conforme tabela abaixo:**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048676854)

Ambos precisam estar preenchidos

MV\_EIPIDEV = .T. e MV\_EIPIOUT = .T. gera a tag vOutro

MV\_EIPIDEV = .T. e MV\_EIPIOUT = .F. gera a tag vIPI

MV\_EIPIDEV = .F. e MV\_EIPIOUT = .T. gera a tag vIPIDevol

MV\_EIPIDEV = .F. e MV\_EIPIOUT = .F. gera a tag vIPIDevol

* **Saiba mais:**

**Apenas a TAG FINNFE = 4 ( CFOP que tenha finalidade de devolução),**será gerada o IPI na TAG **vIPIDevol ou Voutro.**

[Nota Técnica 2016.002 - v 1.61 (publicada em 10/09/2018)](https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=zfWxcJtOf98=)

**Página 51**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360086470733)**

* Para **FINNFE = 1 (CFOP sem finalidade de devolução)** será gerado apenas na **Voutro.**

**Criação do parâmetro MV\_IPIOUTB**

a.**Criação do parâmetro MV\_IPIOUTB**

|  |  |
| --- | --- |
| **Nome** | MV\_IPIOUTB |
| **Tipo** | Lógico |
| **Descrição** | Para nota de devolução tipo B :  T-valor do IPI na tag vOutro, caso MV\_IPIBENE=T  F-valor do IPI na tag vIPIDevol, caso MV\_IPIBENE=T |
| **Valor** **Padrão** | .F. |

![](https://tdn.totvs.com/download/attachments/551428239/image2020-6-9_10-21-10.png?version=1&modificationDate=1591708870833&api=v2) ![](https://tdn.totvs.com/download/attachments/551428239/image2020-6-9_10-22-25.png?version=1&modificationDate=1591708945970&api=v2)

## **01. EXEMPLO DE UTILIZAÇÃO**

O parâmetro criado MV\_IPIOUTB funcionará em conjunto com o parâmetro MV\_IPIBENE.

MV\_IPIOUTB - utilizado para possibilitar o envio do valor do IPI na tag <vOutro> quando a operação se tratar de uma devolução de beneficiamento, conforme tabela abaixo:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077264053)

**TIPO = "B" DEVOLUÇÃO BENEFICIAMENTO**

* **Parâmetro MV\_IPIBENE**= Para notas de devolução.

**.F.**  -> Será destacado na TAG VIPI na devolução

**.T.** -> Será destacado na TAG vIPIDevol

**TIPO = "B" DEVOLUÇÃO BENEFICIAMENTO**

* **Parâmetro MV\_IPIBENE**= Para notas de devolução.

**.F.**  -> Será destacado na TAG VIPI na devolução.

**TIPO = "B" DEVOLUÇÃO BENEFICIAMENTO**

* **Parâmetro MV\_IPIBENE**= Para notas de devolução.

**.T.** -> Será destacado na TAG vIPIDevol

* **Saiba mais:**

**Há o parecer da consultoria tributária** do link abaixo**, no qual informa** em quais casos devem ser destacados **o IPI na TAG vIPIDevol ou vOutro:**

<https://tdn.totvs.com/pages/releaseview.action?pageId=396362395>

Na Devolução ao ser destacado na **vIPIDevol** será destacado apenas em informações complementares o valor do IPI, pois não houve alteração do layout do **Danfe para inclusão da nova TAG.**
