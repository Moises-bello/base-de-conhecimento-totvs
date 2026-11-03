---
article_id: 360056083013
category: NFe - Nota Fiscal Eletrônica
content_hash: 044f109038bef0782e9e7cd66b89205e303d48b9cb08f6c4a2fea66ecc5b75ab
fetched_at: '2026-06-28T22:40:00.280752+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  Alterando a modalidade
  de contingência para todas as entidade '
type: support-article
updated_at: '2021-08-18T13:48:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056083013--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Alterando-a-modalidade-de-conting%C3%AAncia-para-todas-as-entidade
---

**Dúvida**

Ao mudar a contingência de uma filial, está alterando  para todas as entidades.  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Ao mudar para uma modalidade de contingência em **Parâmetros -> NFe -> Modalidade** de uma filial, o sistema também está alterando a modalidade para outras filiais de forma indevida, por meio do parâmetro MV\_MODALID na tabela do TSS SPED000.  
  
Caso isso ocorra, de forma paliativa, filtre pelo parâmetro MV\_MODALID na tabela do TSS SPED000 e reconfigure para 1 (modalidade normal) a filial/entidade onde ocorreu a troca indevida.

* Segue link com a **RPO do TSS atualizado:**

[MP - TSS - Atualização do Repositório (RPO) do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981)

**\*Importante:** Fazer um backup do rpo do TSS antes da atualização. Ao aplicar "aceitar somente os fontes mais recentes".
