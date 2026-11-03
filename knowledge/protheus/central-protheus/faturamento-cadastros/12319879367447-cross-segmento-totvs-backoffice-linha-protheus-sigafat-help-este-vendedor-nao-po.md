---
article_id: 12319879367447
category: Faturamento - Cadastros
content_hash: aad89ce588ceb3e221b6d39ba8507e9ff0034df32dbeba65c0f82406b1bdced8
fetched_at: '2026-06-28T22:38:36.588187+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Help: "Este
  vendedor nao pode ser excluido pois está inserido na estrutura de negócio".'
type: support-article
updated_at: '2023-05-10T18:46:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12319879367447-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Help-Este-vendedor-nao-pode-ser-excluido-pois-est%C3%A1-inserido-na-estrutura-de-neg%C3%B3cio
---

**Dúvida**

Ao tentar excluir um vendedor na rotina MATA040 (Cadastro de Vendedor) apresenta

Help: "Este vendedor não pode ser excluído pois está inserido na estrutura de negócio".

Como proceder?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**

A mensagem ocorre quando o vendedor não pode ser excluído na rotina "Vendedores" (MATA040), pois está configurado na "Estrutura de Negócio" (CRMA240) do módulo SIGACRM (74).

Para saber o que é e para que serve a Estrutura de Negócios, consulte: [Estrutura de Negócio no módulo de CRM](https://tdn.totvs.com/x/hWlrE)

Nesse caso, o vendedor deverá ser excluído da estrutura de negócios para somente depois ser feita a exclusão do cadastro do vendedor.
