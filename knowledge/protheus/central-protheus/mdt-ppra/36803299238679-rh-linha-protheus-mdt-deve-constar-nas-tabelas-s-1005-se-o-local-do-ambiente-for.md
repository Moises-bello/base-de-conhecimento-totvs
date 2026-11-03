---
article_id: 36803299238679
category: MDT - PPRA
content_hash: 333639922f22e0566756e080fa1f6ae1594385c665550ab8be6717cb8a3d5367
fetched_at: '2026-06-28T22:44:27.223984+00:00'
product: protheus
section_id: 360010945454
source: central-protheus
title: RH - Linha Protheus - MDT -  Deve constar nas tabelas S-1005 se o local do
  ambiente for igual a 'Estabelecimento do próprio empregador'
type: support-article
updated_at: '2025-12-05T13:45:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36803299238679-RH-Linha-Protheus-MDT-Deve-constar-nas-tabelas-S-1005-se-o-local-do-ambiente-for-igual-a-Estabelecimento-do-pr%C3%B3prio-empregador
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36803299225367) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Ao incluir um ambiente físico com o campo **Loc. Amb**. igual a **3**(Prestação de Serviços em Terceiros), é apresentada a mensagem **"Deve constar nas tabelas S-1005 se o local do ambiente for igual a 'Estabelecimento do próprio empregador'".**  
  
**Ambiente**  
RH - Linha Protheus - MDT - Todas as versões  
  
**Causa**  
Existe no TAF evento S-1005 ou S-1000 com o mesmo número de inscrição informado na rotina de Ambiente Físico.  
  
**Solução**  
Quando o serviço a ser prestado ocorrer em empresas terceiras, não deve existir S-1005 ou S-1000 cadastrados no TAF com o mesmo número de inscrição, pois esses eventos são destinados exclusivamente a informar os dados da empresa contratante do funcionário.
