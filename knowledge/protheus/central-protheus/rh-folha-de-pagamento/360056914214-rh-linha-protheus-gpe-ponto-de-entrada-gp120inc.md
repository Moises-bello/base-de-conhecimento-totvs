---
article_id: 360056914214
category: RH - Folha de Pagamento
content_hash: 5d688ba43317f4ed441d7d256c8903165049c2bb6738688d1c8aca975254c7f2
fetched_at: '2026-06-28T22:44:17.152847+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: 'RH - Linha Protheus - GPE - Ponto de entrada GP120INC '
type: support-article
updated_at: '2024-09-12T17:36:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056914214-RH-Linha-Protheus-GPE-Ponto-de-entrada-GP120INC
---

**Dúvida**Criação do ponto de entrada GP120INC para gravar campos do usuário na tabela SRD.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Os campos de usuário deverão ser criados somente na tabela SRD.

**Exemplo**:

*User function* GP120INC

SRD->RD\_XTESTE1 := "TESTE 1"  
SRD->RD\_XTESTE2 := "TESTE 2"

*Return*
