---
article_id: 360028345292
category: Faturamento - Cadastros
content_hash: 723ec1587926eabb91a1690c587a424bff9a23baa1940c7cedd3f02095b30224
fetched_at: '2026-06-28T22:38:35.306167+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Help MA030TEMBA
type: support-article
updated_at: '2023-04-20T12:59:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028345292-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Help-MA030TEMBA
---

**Ocorrência**

É apresentado Help **MA030TEMBA** (*cliente não poderá ser excluído.* - *verifique os equipamentos da base instalada existentes para este cliente*) ao tentar excluir o cadastro de cliente.  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.  
  
**Causa**

O help ocorre pois encontrou algum contrato/oportunidade(orçamento) vinculado na base de atendimento.

**Solução**

Verifique a tabela **AA3** se tem algum contrato/oportunidade(orçamento) vinculado ao cliente que esta tentando excluir.

Caso tenha exclua primeiro o contrato/oportunidade(orçamento) e depois exclua o cliente.
