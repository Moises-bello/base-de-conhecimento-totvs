---
article_id: 19263805517719
category: RH - FGTS / SEFIP
content_hash: 8d49d9e4b3a02065725838ad8f5e640f2574aed300d8b79ea024f67f2cf65416
fetched_at: '2026-06-28T22:43:41.274775+00:00'
product: protheus
section_id: 360003115651
source: central-protheus
title: RH - Linha Protheus - GPE - Erro Sefip 130384 - Categoria do Trabalhador Inválida
type: support-article
updated_at: '2025-08-07T13:25:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19263805517719-RH-Linha-Protheus-GPE-Erro-Sefip-130384-Categoria-do-Trabalhador-Inv%C3%A1lida
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19263790816791) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Como resolver o Erro Sefip 130384 - Categoria do Trabalhador Inválida?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**O erro de validação no programa SEFIP é apresentado quando o campo Categ.Sefip, no cadastro do funcionário, aba funcionais está preenchido de forma incorreta.

O campo deve ser preenchido com duas posições e uma categoria válida da Sefip, exemplo: "01"  
Caminho rotina Funcionários **>Atualizações >Funcionários >Funcionários**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19263851743767)

**OBS:** Caso seja necessário efetuar a alteração do campo, como trata-se de um campo em que o sistema grava histórico de alterações na tabela SR9, é necessário que no momento da alteração do campo a **data base do sistema esteja com a mesma data da competência da geração da SEFIP**, **caso contrário irá gravar uma data futura e não será considerada a alteração para geração**. 

**Saiba mais**

[RH - FGTS/SEFIP](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003115651-RH-FGTS-SEFIP)
