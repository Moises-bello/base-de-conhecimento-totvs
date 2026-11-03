---
article_id: 360033697254
category: Financeiro - Contas a Pagar
content_hash: 377b488fc74e0aa2e93d6b9a38cf926abffcade04de19fd86084afbc9f4585b6
fetched_at: '2026-06-28T22:38:09.927521+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: 'MP - SIGAFIN - FINA665 - Conferência de Solicitação de Viagens '
type: support-article
updated_at: '2021-04-28T15:18:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033697254-MP-SIGAFIN-FINA665-Confer%C3%AAncia-de-Solicita%C3%A7%C3%A3o-de-Viagens
---

**Ocorrência**  
 No módulo **Financeiro**, ao tentar realizar a **Conferência da solicitação** é apresentada o Help:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043367874/mceclip0.png)  
   
 **Ambiente**  
Microsiga Protheus - Financeiro - FINA665 - A partir da versão 11.80  
   
 **Causa**   
 Esse incidente ocorre, pois a parametrização do sistema está incorreta para o **Gestor para Conferência** e **Aprovação do processo**.  
   
 **Solução**  
 Para solucionar essa ocorrência, realize os seguintes passos:  
 1. Na Rotina **FINA691** ( Wizard de Configuração).  
2. Clique em **Avançar**  
 3. No campo **Cód. de Usuários de Dpto. de Viagens** incluir o código de usuário do Protheus.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043368174/mceclip1.png)

Realize novamente o processo de conferência para aprovação.
