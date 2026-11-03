---
article_id: 360055510534
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 07604af9c32105d7a966504efd4cca74a5af05bca1964bf9b6ac7c0e7fea2b11
fetched_at: '2026-06-28T22:39:57.335841+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - E156 - CNPJ
  DO PRESTADOR NAO AUTORIZADO A EMITIR NFS-E
type: support-article
updated_at: '2025-07-08T19:56:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055510534-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-E156-CNPJ-DO-PRESTADOR-NAO-AUTORIZADO-A-EMITIR-NFS-E
---

**Dúvida**Ao transmitir um RPS para prefeituras que trabalham com o provedor GINFES, ocorre a rejeição abaixo:  
E156 - CNPJ DO PRESTADOR NAO AUTORIZADO A EMITIR NFS-E  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**Essa rejeição ocorre quando o CNPJ do contribuinte não está liberado na prefeitura para emissão de notas via webservice.  
Dessa forma, orientamos a entrar em contato com a prefeitura solicitando essa liberação, para ambiente de homologação e produção.  
  
**Importante:** Verificar se o CNPJ do prestador está correto no XML, caso seja necessário alguma alteração, deve ser feita no cadastro da empresa/filial.  
  
**Observação:** Para identificar se o município usa o provedor GINFES, clique em [Municípios Homologados](https://tdn.totvs.com/pages/releaseview.action?pageId=4814340) e verifique a coluna **Provedor.**
