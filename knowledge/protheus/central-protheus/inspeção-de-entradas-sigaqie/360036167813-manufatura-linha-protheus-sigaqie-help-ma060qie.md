---
article_id: 360036167813
category: Inspeção de Entradas (SIGAQIE)
content_hash: ca942338a1b5c690f2add632c1219341cf421feb3d6379cccdb07312a7824d71
fetched_at: '2026-06-28T22:42:27.005980+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - Help MA060QIE
type: support-article
updated_at: '2021-08-06T14:46:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036167813-Manufatura-Linha-Protheus-SIGAQIE-Help-MA060QIE
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:00:45 min**  
**Ocorrência**No módulo **SIGAQIE - Inspeção de Entradas**, ao tentar alterar o relacionamento entre produto x fornecedor na rotina **MATA061 - Atualização Produto x Fornecedor** é apresentado o *help* **MA060QIE**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Versão 12  
  
**Causa**O *help* **MA060QIE** ocorre quando os campos **Situação** **- A5\_SITU**, **Fab/Rev/Perm - A5\_FABREV** e/ou **Tempo Limite - A5\_TEMPLIM** não estão preenchidos no cadastro da rotina **MATA061**. Estes campos são de preenchimento obrigatório na integração com o módulo de Inspeção de Entradas.  
  
**Solução**Para solucionar essa ocorrência é necessário informar os campos citados acima.
