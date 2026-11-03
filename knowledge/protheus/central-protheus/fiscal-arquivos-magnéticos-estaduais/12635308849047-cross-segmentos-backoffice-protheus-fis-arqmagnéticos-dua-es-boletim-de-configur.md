---
article_id: 12635308849047
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 4056e03bc68fac1b772dd841ece8bbde3f221d4e004be71cfe0f3af068c38232
fetched_at: '2026-06-28T22:42:10.856456+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - DUA ES - Boletim
  de configuração para transmitir e imprimir as guias de recolhimento de Espirito
  Santo- ES
type: support-article
updated_at: '2024-06-14T12:37:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12635308849047-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-DUA-ES-Boletim-de-configura%C3%A7%C3%A3o-para-transmitir-e-imprimir-as-guias-de-recolhimento-de-Espirito-Santo-ES
---

**Dúvida** **DUA ES** - Como transmitir e imprimir as guias de recolhimento para **Espirito Santo - ES**?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Livros Fiscais – Todas as versões.  
  
**Solução**

A **UF** de **ES** não aderiu programa nacional da **GNREWS**, porém **ES** tem um *web service* próprio, com isso, no sistema é possível transmitir a **ES** pela rotina **FISA095**, pois no momento da transmissão o sistema automaticamente faz a transmissão para **ES**.

Para essa **UF** basta configurar a **UF** nos parâmetros na rotina conforme boletins abaixo:  
   
1. Crie os campos necessários e configure o sistema para atender  **GNRE/DUA- ES**:  
<https://tdn.totvs.com/pages/releaseview.action?pageId=621784438>  
   
2. Configure a **UF ES** nos parâmetros rotina **GNREWS** (**FISA095**)   
<https://tdn.totvs.com/display/public/PROT/GNREWS+-+Guia+Nacional+de+Recolhimento+de+Tributos+Estaduais+via+Webservice>

3. Para as guias de **ES**, use para transmissão APENAS o ambiente de Produção da GNRE e a versão 1.0 :

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13821986080407)

**OBS.** Para **UF Espirito Santo (ES)** só é valido o ambiente de Produção da GNRE e a versão 1.0 (demais UFs contemplam só a versão 2.0 e os ambientes Produção e Homologação da **GNREWS**.
