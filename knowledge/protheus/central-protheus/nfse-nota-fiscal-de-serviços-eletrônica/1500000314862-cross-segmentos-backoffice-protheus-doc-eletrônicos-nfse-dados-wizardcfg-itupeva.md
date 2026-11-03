---
article_id: 1500000314862
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 146a972891abe8f78243968fb2d66542c33c97a7c4791a8ca37ee15c63e490f2
fetched_at: '2026-06-28T22:39:56.427800+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Dados Wizard.cfg
  (Itupeva)
type: support-article
updated_at: '2025-07-08T20:08:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000314862-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Dados-Wizard-cfg-Itupeva
---

**Dúvida**O que deverá ser preenchido em cada campo do Wizard.cfg para a prefeitura de Itupeva-SP?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099219314/mceclip0.png)  
  
Os campos acima deverão ser preenchidos da seguinte maneira:  
  
**Nome de Usuário:** NOME DE USUÁRIO WEB SERVICES (DISPONIBILIZADO PELA PREFEITURA) **Senha:** SENHA WEB SERVICES (DISPONIBILIZADA PELA PREFEITURA) **Seq. Registro:** INSCRIÇÃO WEB SERVICES (DISPONIBILIZADA PELA PREFEITURA) **Cod. Validação:** MESMO CONTEÚDO DO CAMPO SENHA  
  
Esses dados serão gravados na tabela SPED000 da entidade no TSS da seguinte maneira:  
  
Campos                     Parâmetros  
Nome de Usuário      MV\_NFSEUSER  
Senha                        MV\_NFSPASS  
Cod. Validação          MV\_AUTORIZ  
Seq. Registro             MV\_CHVAUTE
