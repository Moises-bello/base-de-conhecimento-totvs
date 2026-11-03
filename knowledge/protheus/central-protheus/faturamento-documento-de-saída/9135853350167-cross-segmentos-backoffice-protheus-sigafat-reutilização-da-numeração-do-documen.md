---
article_id: 9135853350167
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 4595b853675b1f832baf4a5c73151c7185106bb5fc3ada2ab99aee1e06ed08d4
fetched_at: '2026-06-28T22:38:45.364124+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Reutilização da Numeração
  do Documento de Saída - Controle de Numeração pela SD9
type: support-article
updated_at: '2024-09-05T17:49:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9135853350167-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Reutiliza%C3%A7%C3%A3o-da-Numera%C3%A7%C3%A3o-do-Documento-de-Sa%C3%ADda-Controle-de-Numera%C3%A7%C3%A3o-pela-SD9
---

**Dúvida**Reutilização da Numeração do Documento de Saída - Controle de Numeração pela SD9  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.  
  
**Solução**Reutilização da Numeração do Documento de Saída - Controle de Numeração pela SD9, onde   
Criado o campo **D9\_DOCEXCL** para identificar as numerações da **Tabela** **SD9** que estão vagas, devido à exclusão de documentos. Essa numeração poderá ser utilizada apenas mediante a informação do número manualmente (**MV\_MUDANUM = T**).

O campo D9\_DOCEXCL o qual identifica as notas que estão disponíveis devido ao processo de exclusão, estas numerações apenas serão reutilizadas se o operador informar seu número e série especificamente no momento da geração do novo documento.

**Observação**: Esse processo só poderá ser utilizado caso a nota fiscal não tenha sido transmitida para o Sefaz.

O Tss possui trava para não permitir a transmissão de outra nota com mesma numeração.

Mais detalhes no TDN abaixo:

[14410169 DSERFAT-24963 DT Geração Documento Saída - SD9](https://tdn.totvs.com.br/pages/releaseview.action?pageId=698623839)

Saiba mais: [FAT0005 Reutilizar Numeração do Documento de Saída (Nota Fiscal)](https://tdn.totvs.com/pages/releaseview.action?pageId=225263579)

#
