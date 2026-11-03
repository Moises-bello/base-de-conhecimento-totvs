---
article_id: 1500009810462
category: Call Center - Telemarketing
content_hash: eb72b161661a6052d43dd29445bd01bb1e892cbc3b4c47eaaabfe5952f881f48
fetched_at: '2026-06-28T22:41:29.384246+00:00'
product: protheus
section_id: 1500001548162
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGATMK - Help TK061NAC8 no Atendimento
  Telemarketing
type: support-article
updated_at: '2024-04-29T13:09:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009810462-Cross-Segmentos-Backoffice-Protheus-SIGATMK-Help-TK061NAC8-no-Atendimento-Telemarketing
---

**Ocorrência**Ao informar o contato no Atendimento Telemarketing o sistema exibe o Help **TK061NAC8**.  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGATMK - A partir da release 12  
  
**Causa**O help **TK061NAC8** ocorre, ao informar um código de contato no atendimento de Telemarketing, quando o sistema não localiza nenhuma entidade vinculada à esse contato. O vínculo entre o Contato e a Entidade é feito através da tabela **AC8** do sistema.  
  
**Solução**Acesse o Cadastro do Cliente/Prospect que deseja incluir no atendimento, acesse "Outras Ações" e selecione a opção "Contato", verifique se o Contato que está selecionando no atendimento está vinculado.

Verifique também se o contato está ativo, acesse a rotina de "Contatos" (**TMKA070**) e, editando o contato que deseja informar no atendimento, verifique se o campo "Status" (**U5\_MSBLQL**) está com conteúdo "2-Ativo".
