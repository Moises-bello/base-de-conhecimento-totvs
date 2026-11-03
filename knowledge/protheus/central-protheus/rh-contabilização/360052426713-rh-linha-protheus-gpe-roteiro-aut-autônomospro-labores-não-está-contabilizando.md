---
article_id: 360052426713
category: RH - Contabilização
content_hash: f62e4b3e39b4e32c8549fb379ec3acc79044f8d8f71bb1688ecd00a90039de3a
fetched_at: '2026-06-28T22:43:46.157783+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: RH - Linha Protheus - GPE - Roteiro AUT (autônomos/pro labores) não está contabilizando
type: support-article
updated_at: '2021-06-07T13:24:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052426713-RH-Linha-Protheus-GPE-Roteiro-AUT-aut%C3%B4nomos-pro-labores-n%C3%A3o-est%C3%A1-contabilizando
---

**Dúvida**Após cálculo, o roteiro AUT (autônomos/pro labores) não está contabilizando.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
1. Acesse Atualizações -> Definições de Cálculo -> Roteiros de Cálculo;

2. Selecione o roteiro AUT (Autonomos e Pro Labores) e busque o campo "Contabiliza?"(SRY\_CONTAB), configurando como "SIM":  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360081887074/mceclip0.png)  
  
3. Após essa alteração, selecione "Salvar", saia da rotina e refaça o processo de contabilização.
