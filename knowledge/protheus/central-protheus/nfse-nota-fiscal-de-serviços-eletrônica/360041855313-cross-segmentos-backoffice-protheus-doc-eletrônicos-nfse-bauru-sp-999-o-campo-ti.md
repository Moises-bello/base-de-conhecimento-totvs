---
article_id: 360041855313
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 6a1c1aee998d6737a1cc885138e6dca1856b3afa319ef9bf96a8b38b3bd4df4d
fetched_at: '2026-06-28T22:39:56.315405+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Bauru-SP:
  999-O campo Tipo Tributação está inválido'
type: support-article
updated_at: '2025-07-14T21:39:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041855313-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Bauru-SP-999-O-campo-Tipo-Tributa%C3%A7%C3%A3o-est%C3%A1-inv%C3%A1lido
---

**Dúvida**Como informar no XML do RPS de Bauru-SP a tag SITUACAO, para solucionar a rejeição 999-O campo Tipo Tributação está inválido?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**Conforme [manual de integração webservice](https://www2.bauru.sp.gov.br/arquivos/arquivos_site/sec_financas/MANUAL_WS_NFE.pdf), a tag Situação possui as seguintes opções:  
tp – Tributada no prestador;   
tt – Tributada no tomador;  
is – Isenta;   
im – Imune  
  
Regra para Geração da tag:  
**tp – Tributada no prestador:**  
Campos F4\_ISSST=1 ou 2 e A1\_RECISS ou C5\_RECISS=2  
  
**tt – Tributada no tomador:**  
Campos F4\_ISSST=1 ou 2 e A1\_RECISS ou C5\_RECISS=1  
  
**is – Isenta:**  
Campo F4\_ISSST=3  
  
**im – Imune:**Campo F4\_ISSST=4, 5 ou 6.  
  
**Observação:**Caso tenha dúvidas sobre qual tributação informar, acione o fisco da prefeitura.
