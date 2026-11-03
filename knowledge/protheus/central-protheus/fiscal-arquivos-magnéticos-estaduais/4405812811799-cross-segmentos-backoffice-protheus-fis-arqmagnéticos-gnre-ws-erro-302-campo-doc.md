---
article_id: 4405812811799
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: d3c2a6042f77209f5e7d8c35daf12521716982cf0d6b6d333d7b3b5f41da962d
fetched_at: '2026-06-28T22:42:11.693109+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - GNRE WS - ERRO
  302 - Campo: Documento origem [item: 1] - descrição: valor do documento de origem
  invalido para o tipo informado'
type: support-article
updated_at: '2022-08-17T19:31:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405812811799-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-GNRE-WS-ERRO-302-Campo-Documento-origem-item-1-descri%C3%A7%C3%A3o-valor-do-documento-de-origem-invalido-para-o-tipo-informado
---

**Ocorrência****GNRE WS** - Como corrigir o **ERRO 302 - Campo: Documento origem [item: 1] - descrição: valor do documento de origem invalido para o tipo informado** na transmissão da **GNREWS.**  
**Ambiente**TOTVS Backoffice (Linha Protheus) - Livros Fiscais - A partir da versão **12.1.25**.  
  
**Causa**Esse incidente ocorre, pois os campos **F6\_TIPOGNU e F6\_DOCORIG** estão preenchidos de forma errada na Guia de recolhimento (Rotina **MATA960** - tabela **SF6**).  
  
**Solução**Altere o preenchimento dos campos na guia (rotina **MATA960**), e realize a transmissão da guia novamente..  
  
**EXEMPLO de preenchimento:**  
<http://www.gnre.pe.gov.br/gnre/portal/automacao.jsp#>

Campos na Guia Rotina MATA960, exemplo para a UF de **SC** e código de receita **100102** deverá ser informado **F6\_DOCORIG = 1 ou 2**  e **F6\_TIPOGNU = 22**  
  
  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405821307927/mceclip0.png)  
Guia de recolhimento:  
  
​  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405821382807/mceclip1.png)  
  
  
Segue abaixo documentação e **Ponto de entrada** para automatização e preenchimento dos campos **F6\_TIPOGNU  e F6\_DOCORIG**:  
  
[MP - FIS - GNRE WS - Preencher campos F6\_TIPOGNU e F6\_DOCORIG de forma automática](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057390193-MP-FIS-GNRE-WS-Preencher-campos-F6-TIPOGNU-e-F6-DOCORIG-de-forma-autom%C3%A1tica?source=search)
