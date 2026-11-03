---
article_id: 360026180971
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 1727ddb0837e2847eaee90fd286f8ebe78b02e8deeecbb7509ac1e75fb70ad71
fetched_at: '2026-06-28T22:39:56.457866+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Discriminação
  dos serviços NFSE
type: support-article
updated_at: '2025-06-25T14:24:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026180971-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Discrimina%C3%A7%C3%A3o-dos-servi%C3%A7os-NFSE
---

**Dúvida**  
Como realizar a parametrização para gerar a Discriminação dos Serviços?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**Através do parâmetro **MV\_NFESERV** é definido por onde será considerada a Discriminação, podendo ter duas opções (1 ou 2), seguem:  
  
**1** – Para que a descrição do serviço prestado, a ser enviado no arquivo xml para a prefeitura, seja composta pelo Pedido de Vendas (C5\_MENNOTA) + descrição da tabela 60 (X5\_DESCRI) de acordo com o B1\_CODISS.

**2** – Para que a descrição do serviço prestado, a ser enviado no arquivo xml para a prefeitura, seja composta apenas pela descrição da tabela 60 (X5\_DESCRI) de acordo com o B1\_CODISS.

Portanto com base na configuração desse parâmetro, deverá informar a discriminação dos serviços no C5\_MENNOTA e/ou X5\_DESCRI de acordo com o B1\_CODISS.  
  
**Na necessidade de enviar no XML apenas o texto contido no 'C5\_MENNOTA', mantenha MV\_NFESERV = 1 e MV\_NFEDESC = .T.**
