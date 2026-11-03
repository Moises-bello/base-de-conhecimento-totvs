---
article_id: 1500010342362
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 89526fb69faf10ba3fc4db61717baf3472fd5fd4cfb9aac49b7e692dad99a21b
fetched_at: '2026-06-28T22:39:56.266112+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - 1454 - Tributacao
  invalida. Para o regime de enquadramento Simples nacional o contribuinte deve a
  tributação H : Tributavel SN'
type: support-article
updated_at: '2025-07-14T21:42:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010342362-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-1454-Tributacao-invalida-Para-o-regime-de-enquadramento-Simples-nacional-o-contribuinte-deve-a-tributa%C3%A7%C3%A3o-H-Tributavel-SN
---

**Ocorrência**Ao realizar a transmissão de um RPS para o provedor DSFNET, ocorre a rejeição: *"1454 - Tributacao invalida. Para o regime de enquadramento Simples nacional o contribuinte deve a tributação H : Tributavel SN"*  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Causa**Essa rejeição é causada pelo fato da tag <Tributacao> estar sendo informada incorretamente quando o contribuinte se enquadra no Simples Nacional e há tributação de ISS.  
Segundo a própria rejeição da prefeitura orienta, deverá ser informada como: 'H - Tributável S.N.':  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500016429422/mceclip1.png)  
  
**Solução**Para correção, deverá verificar dois pontos para gerar a tag <Tributacao> = H:  
  
I. No Cadastro do TES, o campo **F4\_ISSST** deverá estar igual à **1** (Tributado Dentro do Município);  
II. Parâmetro **MV\_OPTSIMP = 1  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500016430882/mceclip3.png)**
