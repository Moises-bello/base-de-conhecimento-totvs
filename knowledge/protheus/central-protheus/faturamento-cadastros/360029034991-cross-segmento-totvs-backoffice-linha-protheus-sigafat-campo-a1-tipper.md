---
article_id: 360029034991
category: Faturamento - Cadastros
content_hash: 3ab9d79b76d37bab52f45727c34e22e82e3d305434c4f024aaee0b8f4e8ab4cf
fetched_at: '2026-06-28T22:38:35.352485+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT -Campo A1_TIPPER '
type: support-article
updated_at: '2023-03-20T19:47:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029034991-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Campo-A1-TIPPER
---

**Dúvida**

O que trata o campo A1\_TIPPER no cadastro de clientes (MATA030 e CRMA980)?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**

O campo **A1\_TIPPER** - Tipo de período, é um campo para informar o Tipo de Período para fechamento das duplicatas provisorias a serem efetivadas no sistema para os clientes periódicos.

O campo é tratado no Atendimento a Clientes  (Orcamento de Pecas e Servicos  e Venda de Pecas Balcao e Avaliacao do Resultado da Venda -   **OFIOM110** ) - Gestão de Concessionarias (SIGAPEC e SIGAOFI) e no Financeiro.

No módulo Financeiro, o campo é tratado em renegociação de títulos, substituição de título a receber de forma automática, segue abaixo documentações que tratam o campo em conjunto com o parâmetro **MV\_TIPPER** :

**[Renegociação de títulos a receber](http://tdn.totvs.com/pages/releaseview.action?pageId=126714886)**

**[Substituição de título a receber automática - Fina045](http://tdn.totvs.com/pages/releaseview.action?pageId=6070656)**

O módulo de Faturamento não faz uso deste campo, não sendo possível a sua demonstração de uso.

Desta forma, maiores informações de como utilizar o campo A1\_TIPPER, avalie as documentações de Financeiro e contate a equipe para averiguar o tratamento de títulos.

Caso utilize algum dos módulos de Concessionárias, entre em contato com a equipe de Automação Comercial para averiguar o uso do campo A1\_TIPPER no **SIGAPEC**. -Auto Peças.
