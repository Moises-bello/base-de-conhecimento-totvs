---
article_id: 360055738173
category: RH - Soluções para error.log
content_hash: ee21a6efc6bfe15d5fa030b0c8c47178366e8b848855a5ca0f93c8bdc70d1d6e
fetched_at: '2026-06-28T22:44:08.989057+00:00'
product: protheus
section_id: 115003853987
source: central-protheus
title: RH - Linha Protheus - PON - Error log ao realizar Apontamento de Marcações
  - variable does not exist LPORT1510 on P9FILTRAEVENTO
type: support-article
updated_at: '2025-08-04T14:01:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055738173-RH-Linha-Protheus-PON-Error-log-ao-realizar-Apontamento-de-Marca%C3%A7%C3%B5es-variable-does-not-exist-LPORT1510-on-P9FILTRAEVENTO
---

**Ocorrência**Ao efetuar o **Apontamento** de Marcações, gera *error log: **variable does not exist*** **LPORT1510** ***on P9FILTRAEVENTO*****Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Causa**O erro é apresentado devido à aplicação indevida de pacote para ambientes de Mercado Internacional e utilização de fonte com versão destinado ao Mercado Internacional.  
  
**Solução**Para solução do problema, favor seguir o passo a passo abaixo:  
**1.** Retornar o RPO antes da aplicação do pacote do Mercado Internacional (sufixo \_MI no nome do pacote);  
**2.** Atualizar o ambiente com o acumulado do RH para ambiente país Brasil, conforme link abaixo.   
<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854>   
  
**Informações complementares**  
Pacote de Expedição Contínua do eSocial: [https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051585234-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-acumulado-do-eSocial)  
Pacote de Expedição Contínua do Medicina e Segurança do Trabalho:<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057956773>
