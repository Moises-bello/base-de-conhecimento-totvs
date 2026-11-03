---
article_id: 21456776323223
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: dab9a00906c3ca16ea490c237156acf588565a411c9d7add3c71cfc8d35b1a6d
fetched_at: '2026-06-28T22:42:05.063463+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  - Cannot find method FWSX1UTIL:EXISTPERGUNTE on SETQUEBRA(FISR101.PRW)
type: support-article
updated_at: '2024-02-20T12:24:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21456776323223-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Cannot-find-method-FWSX1UTIL-EXISTPERGUNTE-on-SETQUEBRA-FISR101-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21456754179095) Tempo aproximado para leitura: **00:01:00H**

**Ocorrência** **Errorlog** ao gerar o relatório de conferência do **EFD Contribuições** (FISR101)

**Cannot find method FWSX1UTIL:EXISTPERGUNTE on SETQUEBRA(FISR101.PRW) 01/02/2024 01:41:21 line : 1892**

**Ambiente**  
Cross Segmento - TOTVS Backoffice (**Linha Protheus**) -  A partir da versão **12.1.25**  
  
**Causa**Esse incidente ocorre, pois a versão da **LIB** do sistema está anterior a versão desejada **20230918**.  
  
**Solução**

Efetue a aplicação da última **LIB** disponível conforme link abaixo:

<https://suporte.totvs.com/portal/p/10098/download#000006/368/TFLIB/>

Após aplicação da LIB, deverá ser gerado um novo relatório de conferência do período selecionado.
