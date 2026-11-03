---
article_id: 360028966351
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: f4bb4dbeeb42b5a0a0b17a2878cf21ac9a92392103c22ea21292678e099c100f
fetched_at: '2026-06-28T22:39:58.620105+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Valor da
  Fatura no XML
type: support-article
updated_at: '2025-06-10T17:45:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028966351-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Valor-da-Fatura-no-XML
---

**Dúvida**O valor da fatura no XML está bruto e deveria ser líquido, pois para algumas prefeituras essa diferença causa rejeição da nota.  
Qual o procedimento para que o valor da fatura seja igual ao valor liquido da nota?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**Deverá habilitar o parâmetro MV\_DUPLLIQ=T através do Configurador (SIGACFG).   
Dessa forma a fatura no XML será gerada com o valor liquido da nota.
