---
article_id: 4405821660823
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 3985c749beb806de6c415c10043d8c62d56f12fcf77b08a767741858a6ffa838
fetched_at: '2026-06-28T22:42:11.688747+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - GNRE WS - ERRO
  217 - Campo: Documento origem [item: 1] - descrição: O DOCUMENTO DE ORIGEM INFORMADO
  NÃO É USADO PELA RECEITA INFORMADA NA UF FAVORECIDA'
type: support-article
updated_at: '2022-08-17T19:30:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405821660823-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-GNRE-WS-ERRO-217-Campo-Documento-origem-item-1-descri%C3%A7%C3%A3o-O-DOCUMENTO-DE-ORIGEM-INFORMADO-N%C3%83O-%C3%89-USADO-PELA-RECEITA-INFORMADA-NA-UF-FAVORECIDA
---

**Ocorrência****GNRE WS** - Como corrigir o **ERRO 217 - Campo: Documento origem [item: 1] - descrição: O DOCUMENTO DE ORIGEM INFORMADO NÃO É USADO PELA RECEITA INFORMADA NA UF FAVORECIDA** na transmissão da **GNREWS.**  
**Ambiente**TOTVS Backoffice (**Linha Protheus**) - Livros Fiscais - A partir da versão **12.1.25.**  
  
**Causa**Esse incidente ocorre, pois os campos **F6\_TIPOGNU e F6\_DOCORIG** estão preenchidos de forma errada na Guia de recolhimento (Rotina **MATA960** - tabela **SF6**).  
  
**Solução**

Altere o preenchimento dos campos na guia (rotina **MATA960**), e realize a transmissão da guia novamente..  
  
**EXEMPLO de preenchimento:**  
<http://www.gnre.pe.gov.br/gnre/portal/automacao.jsp#>

Campos na Guia Rotina MATA960, exemplo para a UF de **SC** e código de receita **100102** deverá ser informado **F6\_DOCORIG = 1 ou 2**  e **F6\_TIPOGNU = 22**  
  
  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405821307927/mceclip0.png)  
Guia de recolhimento:  
  
​  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405821382807/mceclip1.png)  
  
  
Segue abaixo documentação e **Ponto de entrada** para automatização e preenchimento dos campos **F6\_TIPOGNU  e F6\_DOCORIG**:  
  
[MP - FIS - GNRE WS - Preencher campos F6\_TIPOGNU e F6\_DOCORIG de forma automática](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057390193-MP-FIS-GNRE-WS-Preencher-campos-F6-TIPOGNU-e-F6-DOCORIG-de-forma-autom%C3%A1tica?source=search)
