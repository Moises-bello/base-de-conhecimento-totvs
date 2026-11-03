---
article_id: 360017731151
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 5f2a0cad3438e45b046f037a9aa019436ecf79477292c6a749ca7e2d3408df94
fetched_at: '2026-06-28T22:39:57.412501+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Emissão de
  uma nota fiscal de serviço sem tomador
type: support-article
updated_at: '2025-06-02T12:24:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017731151-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Emiss%C3%A3o-de-uma-nota-fiscal-de-servi%C3%A7o-sem-tomador
---

**Dúvida**Como emitir uma nota fiscal de serviço sem tomador?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**Para a emissão de uma nota fiscal de serviço sem tomador, ou seja, para que no XML do Protheus não sejam montadas as tags referentes ao tomador, basta deixar em branco os campos **A1\_CGC** e **A1\_NOME** no Cadastro do Cliente, assim o remessa será montado da seguinte maneira abaixo:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4420223148567/mceclip1.png)  
  
***Obs.: O envio do XML sem os dados do tomador depende exclusivamente do layout e da aprovação de cada município, por questões de regras específicas para cada prefeitura.***
