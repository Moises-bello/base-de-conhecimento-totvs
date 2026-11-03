---
article_id: 360016734171
category: Ativo Fixo - Tabelas, Parâmetros, Campos .Gatilho
content_hash: 47de2de03d609e7ce77179fd40757a23908b1850abeb5b7d0f99919204de5371
fetched_at: '2026-06-28T22:41:50.298486+00:00'
product: protheus
section_id: 1500001536201
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF -  STATUS dos Bens (ativo
  fixo)
type: support-article
updated_at: '2022-07-28T19:50:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016734171-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-STATUS-dos-Bens-ativo-fixo
---

**Dúvida**Qual a função do campo Status Bem?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Ativo Fixo A partir da versão 12  
  
  
**Solução**

Este campo permite determinar o status de um bem **no momento de sua inclusão**, que pode ser: 0 - Pendente de Classificação, 1 - Em uso,  2 e 3 - Bloqueado e 4 Transferência interna de filiais.

Ao informar - Bloqueado, o Sistema não permite as seguintes operações para este bem:

Cálculo da depreciação

Baixas (sem cálculo de depreciação)

Baixas (com cálculo de depreciação)

Baixas de Adiantamento

Transferências

Ampliação

Aquisição por Transferência

Depreciação Acelerada

Descálculo Mensal

Inventário

Ajuste de Inventário

**Importante:**

Para o bloqueio de operações de Inventário e Ajuste de Inventário é necessário que o parâmetro MV\_BLQINVE esteja com o conteúdo em 1.
