---
article_id: 360017786011
category: Ativo Fixo - Baixa e Baixa de Adiantamento
content_hash: a63d4985a290fe42f5b836b94aef674689f29548857c31824b7026dae17947fa
fetched_at: '2026-06-28T22:41:55.540752+00:00'
product: protheus
section_id: 1500001535901
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA036 e ATFA030 -
  Baixas do Ativo (Migração)
type: support-article
updated_at: '2023-11-20T16:27:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017786011-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA036-e-ATFA030-Baixas-do-Ativo-Migra%C3%A7%C3%A3o
---

**Dúvida**

|  |
| --- |
| Ao migrar da release 11 com ambiente exclusivo para a release 12 com ambiente compartilhado, é relatado que o cancelamento da baixa de ativo não altera a legenda. |

**Ambiente**ATIVO FIXO – A partir da versão 11.80  
  
   
**Solução**Na versão 11 do Protheus com ambiente exclusivo o campo N3\_FILORIG não era preenchido, e este campo é usado como chave para a busca dos dados da baixa dos ativos na versão 12 com ambiente compartilhado, sendo assim, como o campo não está preenchido, não é encontrado o registro nas tabelas FN6 e FN7 para realizar o cancelamento da baixa, não alterando assim o status de baixa nestas respectivas tabelas.
