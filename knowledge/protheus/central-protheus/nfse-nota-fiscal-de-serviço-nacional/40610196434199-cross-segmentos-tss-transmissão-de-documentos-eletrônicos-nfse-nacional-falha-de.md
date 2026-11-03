---
article_id: 40610196434199
category: NFSE - Nota Fiscal de Serviço Nacional
content_hash: 646340050f60998a3e999003e1cd739cc0070b2092919b133adde044a87735ec
fetched_at: '2026-06-28T22:39:54.406933+00:00'
product: protheus
section_id: 33955617231639
source: central-protheus
title: 'Cross Segmentos - TSS Transmissão de Documentos Eletrônicos - NFSE Nacional
  - Falha de Schema: Element ''{http://www.sped.fazenda.gov.br/nfse}tpRetPisCofins'':
  [facet ''enumeration''] The value ''3'' is not an element of the set {''1'', ''2''}.'
type: support-article
updated_at: '2026-05-20T16:39:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40610196434199-Cross-Segmentos-TSS-Transmiss%C3%A3o-de-Documentos-Eletr%C3%B4nicos-NFSE-Nacional-Falha-de-Schema-Element-http-www-sped-fazenda-gov-br-nfse-tpRetPisCofins-facet-enumeration-The-value-3-is-not-an-element-of-the-set-1-2
---

**Ocorrência**  
Ao realizar a transmissão de uma nota, ocorre a falha de schema abaixo:  
  
**Element '{http://www.sped.fazenda.gov.br/nfse}tpRetPisCofins': [facet 'enumeration'] The value '3' is not an element of the set {'1', '2'}.**  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões  
  
**Causa**  
Isso ocorre pois a nota está sendo transmitida na versão de **layout antiga (1.00)**, a qual contempla apenas as opções 1 e 2 na tag tpRetPisCofins, ou seja, sem a NT 007. Portanto, deverá ser utilizada a **versão atual (1.01).**  
  
**Solução**  
Para correção deverá configurar o Wizard.cfg na rotina FISA022 da seguinte forma:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40610231673495)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40610231675415)  
  
Além disso, realizar as atualizações de schemas do TSS abaixo:  
- [Cross Segmentos - TSS Transmissão de Documentos Eletrônicos - Atualização dos SCHEMAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025103552-Cross-Segmentos-TSS-Transmiss%C3%A3o-de-Documentos-Eletr%C3%B4nicos-Atualiza%C3%A7%C3%A3o-dos-SCHEMAS)  
  
Por último, gerar uma nova nota do zero e transmiti-la.
