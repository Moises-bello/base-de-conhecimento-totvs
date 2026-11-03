---
article_id: 360057390193
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 2c0cbbe6e4dc4c4c8fca5cab016a28ada342d9d40f4069dd290b6af108bb4424
fetched_at: '2026-06-28T22:42:11.716888+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - GNRE WS - Preencher
  campos F6_TIPOGNU e F6_DOCORIG de forma automática
type: support-article
updated_at: '2024-09-27T13:09:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057390193-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-GNRE-WS-Preencher-campos-F6-TIPOGNU-e-F6-DOCORIG-de-forma-autom%C3%A1tica
---

**Dúvida****GNRE WS** - Como preencher novos campos **F6\_TIPOGNU** e **F6\_DOCORIG** da guia de recolhimento para rotina **GNREWS** para versão **2.0 da** **GNRE?**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (**Linha Protheus**) - Arquivos Magnéticos (**SIGAFIS**) - Arquivos Magnéticos - **GNREWS** - A partir da versão 12.1.23.  
  
**Solução**

Foram incluídos os campos no cadastro da **Guia de Recolhimento (SF6)**:

**Tipo Doc. UF** **(F6\_TIPOGNU)**: Informe qual o tipo de documento deve ser carregado no parâmetro tipo da tag **<documentoOrigem>.**

**Tag Doc. Ori (F6\_DOCORIG)**: Informe qual o conteúdo da tag **<documentoOrigem>**, as opções são **1 - Número do Documento** **Fiscal** ou **2 - Chave do Documento Fiscal**.

Essas informações devem respeitar a tabela de **Documentos de Origem**contida no **portal GNRE**:  
  
![](https://tdn.totvs.com/download/attachments/562476911/image2020-9-10_17-11-55.png?version=1&modificationDate=1599769203983&api=v2)

**\* Para preencher os campos de forma automática** foi disponibilizado o Ponto de Entrada **MA960GREC** conforme link e pacote abaixo:

<https://tdn.totvs.com/pages/releaseview.action?pageId=607040232>

 

Segue também:

**Boletim da rotina :**  
[https://tdn.totvs.com/display/public/PROT/FIS0039+GNRE+WS+Guia+Nacional+de+Recolhimento+via+Web+Service.](https://tdn.totvs.com/display/public/PROT/GNREWS+-+Guia+Nacional+de+Recolhimento+de+Tributos+Estaduais+via+Webservice)

**Artigos complementares:**

[MP - FIS - GNRE WS - Atualização da versão 2.0 da rotina GNREWS (FISA095)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009135981-MP-FIS-GNRE-WS-Atualiza%C3%A7%C3%A3o-da-vers%C3%A3o-2-0-da-rotina-GNREWS-FISA095-?source=search)
