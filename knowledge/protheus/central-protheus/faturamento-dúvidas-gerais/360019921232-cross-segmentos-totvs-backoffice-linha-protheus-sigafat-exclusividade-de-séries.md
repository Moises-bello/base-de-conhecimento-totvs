---
article_id: 360019921232
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 891050529614412fb24731365c6fb7f79e8ea8068e0dd3f131d5e2e4c1141690
fetched_at: '2026-06-28T22:38:29.974073+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Exclusividade
  de Séries por Filial
type: support-article
updated_at: '2022-02-03T21:32:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019921232-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Exclusividade-de-S%C3%A9ries-por-Filial
---

**Dúvida**

Como tratar a exclusividade de séries por filial?  
  
**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**

O controle de numeração no Protheus pode ser realizado de três formas (de acordo com a configuração do parâmetro MV\_TPNRNFS), porém o controle de Séries sempre será via SX5.

Se a SX5 e seus registros forem **compartilhados**, então as séries estarão disponíveis para todas as Filiais.

Se o Faturamento for exclusivo, ou seja, os registros na tabela SF2 possuam o campo de Filial preenchido, é natural que a organização opte por séries **exclusivas**, onde cada Filial possui sua série e, consequentemente, uma sequência de numeração individual.

Para trabalhar com **séries exclusivas**, acesse o link abaixo, e veja as informações no tópico "**Exclusividade de Séries por filial"**: **[Ajuste de Controle de Numeração automática para Documento de Saída](http://tdn.totvs.com/pages/viewpage.action?pageId=329024579)**
