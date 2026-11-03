---
article_id: 115001428008
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: b182ba49c076bb0473bca418134c96bac9e26b8e70770d9c9ef757647b41e0cb
fetched_at: '2026-06-28T22:38:28.724770+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: 'Cross Segmentos -  TOTVS Backoffice (Linha Protheus) - SIGAFAT - Open index
  error: CFF'
type: support-article
updated_at: '2021-11-03T12:17:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115001428008-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Open-index-error-CFF
---

**Dúvida**

Ao tentar excluir um Documento de Saída (**MATA521**), ocorre o erro: **Open index error: CFF**  
  
**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - a partir da versão 12.  
  
**Causa**

O problema ocorre por falta ou por inconsistência no índice da tabela **CFF**.

**Solução**

No pacote de acumulados do módulo fiscal, fica disponível o dicionário diferencial, é necessário atualizar seu ambiente com esse dicionário e executar o UPDDISTR (**[Atualizador de dicionário e base de dados - UPDDISTR](https://tdn.totvs.com/x/nJLYCg)**), a tabela CFF pertence ao módulo fiscal e este procedimento deve corrigir/criar o índice e os campos dela.

Lembrando que o procedimento deve ser realizado por analista especialista no processo e validado primeiramente em ambiente de homologação. Caso o procedimento não tenha efeito na correção do problema, acione o time de Suporte ao módulo Fiscal.
