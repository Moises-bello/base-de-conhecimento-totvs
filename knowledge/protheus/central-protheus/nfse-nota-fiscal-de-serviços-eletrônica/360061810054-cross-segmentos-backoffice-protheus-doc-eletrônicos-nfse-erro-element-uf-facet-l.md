---
article_id: 360061810054
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: d5fbb8804cdb3550b0a879a494cb490befa36f0d83b02ec49f37a32641dc1cf8
fetched_at: '2026-06-28T22:39:57.421296+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Erro: Element
  ''uf'': [facet ''length''] The value has a lenght of ''0'','
type: support-article
updated_at: '2025-07-08T19:46:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061810054-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Erro-Element-uf-facet-length-The-value-has-a-lenght-of-0
---

**Ocorrência**Ao transmitir um RPS ocorre a falha de SCHEMA: ***Erro: Element 'uf': [facet 'length'] The Value has a lenght of '0', this differs from the allowed lenght of '2'.***  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003448201/mceclip0.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Causa**Essa falha de schema ocorre pela falta de informação na tag <UF>, isso podendo ser tanto no bloco do Prestador, quanto no do Tomador.  
  
**Solução**Para correção, deverá checar ambos os pontos citados acima:  
  
Prestador: Verificar no Cadastro da Filial (via Configurador ou APSDU) se os campos a seguir estão preenchidos: **M0\_ESTCOB** e **M0\_ESTENT**.   
  
Tomador: Verificar no Cadastro do Cliente se o campo **A1\_EST** está devidamente preenchido.
