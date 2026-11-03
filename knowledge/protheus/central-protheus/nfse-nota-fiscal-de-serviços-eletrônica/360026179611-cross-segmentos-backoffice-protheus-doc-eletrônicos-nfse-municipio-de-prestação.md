---
article_id: 360026179611
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: d76e18828e537243f3f4cb5520f9ed43624cd9201b15c1e0eaf31b2197822235
fetched_at: '2026-06-28T22:39:57.547689+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - Municipio
  de Prestação
type: support-article
updated_at: '2026-06-25T14:25:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026179611-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-Municipio-de-Presta%C3%A7%C3%A3o
---

**Dúvida**  
Onde informar o município de prestação?  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Solução**  
Ao transmitir uma nota fiscal de serviços, a tag município de prestação do XML por padrão é alimentada com o mesmo município do tomador.  
  
Se a prestação dos serviços ocorreu em um município diferente do tomador use os campos: **C5\_ESTPRES** e **C5\_MUNPRES** no Pedido de Vendas.  
  
Observação: Além disso, é de extrema importância a TES estar alinhada com o município de prestação, ou seja, F4\_ISSST (Legado) ou F4\_NATOPNF (Configurador de Tributos) estarem corretos.  
  
Exemplos:   
- Se município de prestação for dentro comparado ao município emissor: F4\_ISSST/F4\_NATOPNF = 1 - Dentro do Município;  
- Se município de prestação for fora comparado ao município emissor: F4\_ISSST/F4\_NATOPNF = 2 - Fora do Município.
