---
article_id: 360060835993
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 6c00b285cebb1a6eacda1c223d68be7d267b47d3786b8cf98e04f6060d74e272
fetched_at: '2026-06-28T22:39:56.438298+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Declaração
  Plano Saúde (DPS) - Prefeitura São Paulo (NFSE e NFTS)
type: support-article
updated_at: '2025-07-08T20:07:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060835993-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Declara%C3%A7%C3%A3o-Plano-Sa%C3%BAde-DPS-Prefeitura-S%C3%A3o-Paulo-NFSE-e-NFTS
---

**Dúvida**Como é parametrizado no sistema o tipo de nota Declaração Plano Saúde (DPS) para a Prefeitura São Paulo?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**Através de um parecer da consultoria tributária ([detalhes aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=142811812)), para **transmissões via Web Services,** o XML precisará destacar as tags referentes aos **Dados de Intermediário**, se enquadrando em uma DPS. Para isso deverá ser utilizada as configurações abaixo:  
- [MP - NFSE - Intermediário de Serviços](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025205112--MP-NFSE-Intermedi%C3%A1rio-de-Servi%C3%A7os?source=search)  
  
Uma vez transmitidas essas notas, a prefeitura possui um menu para acesso a informações da DPS.

![](https://totvssuporte.zendesk.com/attachments/token/Qt6ZMbb9yRasmS6F7hpm55TqV/?name=inline768705888.png)  
  
Link: <https://nfe.prefeitura.sp.gov.br/login.aspx>
