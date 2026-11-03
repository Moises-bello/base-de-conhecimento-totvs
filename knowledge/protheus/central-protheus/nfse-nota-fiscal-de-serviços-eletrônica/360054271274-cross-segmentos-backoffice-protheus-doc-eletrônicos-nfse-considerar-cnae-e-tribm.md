---
article_id: 360054271274
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 3fdf26d3afa0f7af4d81bfc3591915d28b9c5a160a2fb8ecbc540a0aaa327e86
fetched_at: '2026-06-28T22:39:56.401333+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Considerar
  CNAE e TRIBMUN da tabela SF3
type: support-article
updated_at: '2025-07-14T21:14:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054271274-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Considerar-CNAE-e-TRIBMUN-da-tabela-SF3
---

**Dúvida**Como considerar o CNAE e TRIBMUN da tabela SF3, sem verificar a origem cadastral?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**Para essa situação é necessário configurar o parâmetro **MV\_ENVSF3** com conteúdo = **.T.**  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091688354)  
  
**IMPORTANTE**Essa configuração se aplica ao rdmake NFSEXMLENV igual ou superior a data de 11 de agosto de 2020:  
- [Download do Rdmake - NFSE: NFSEXMLENV](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061699513-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Atualiza%C3%A7%C3%A3o-rdmake-NFSEXMLENV)
