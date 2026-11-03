---
article_id: 360021619811
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 6185f63b3f98fc65d86630d557960b4e50a023f85eb762568ad5290eb93e1ee6
fetched_at: '2026-06-28T22:39:57.436880+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - Falha de
  schema: The ''Discriminacao'' element is invalid'
type: support-article
updated_at: '2025-07-18T14:53:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021619811-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-Falha-de-schema-The-Discriminacao-element-is-invalid
---

**Dúvida**Como corrigir a falha de schema na transmissão de uma NFSE: '**XML não compatível com Schema. The 'Discriminacao' element is invalid'**?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**A Falha de Schema está ocorrendo pois a discriminação do serviço não está sendo informada no XML.  
  
Atualmente as principais possibilidades de informar a Discriminação de Serviços são:  
  
**Notas de Saída:**  
- *Através do C5\_MENNOTA (Pedido de Vendas) e/ou X5\_DESCRI (Descrição do Código de Serviço)*  
Detalhes: [Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - Discriminação do Serviço](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026180971-MP-NFSE-Discrimina%C3%A7%C3%A3o-do-Servi%C3%A7o)  
  
- *Campo customizado na SC5 (através de um campo MEMO)*  
Detalhes: [Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - Discriminação de serviço com mais de 250 caracteres](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012315132-MP-NFSE-Discrimina%C3%A7%C3%A3o-de-servi%C3%A7o-com-mais-de-250-caracteres)

**Notas de Entrada (NFTS):**- Detalhes: [Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - Discriminação dos serviços NFTS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044468273-MP-NFSE-Discrimina%C3%A7%C3%A3o-dos-servi%C3%A7os-NFTS)
