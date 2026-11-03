---
article_id: 360058691433
category: CRM - Dúvidas Gerais
content_hash: b8a32adee4f1b04c368198117241b4973e988ba39100529e6c017fe92a1e8c1e
fetched_at: '2026-06-28T22:40:27.543089+00:00'
product: protheus
section_id: 1500001538021
source: central-protheus
title: MP-CRM-Ao inserir um tes na proposta comercial gera o Help Ajuda - Regbloq
type: support-article
updated_at: '2021-04-28T14:49:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058691433-MP-CRM-Ao-inserir-um-tes-na-proposta-comercial-gera-o-Help-Ajuda-Regbloq
---

**Dúvida**

Ao inserir um TES na proposta comercial gera o Help Ajuda - Regbloq.  
  
**Ambiente**

Microsiga Protheus - todas as versões.  
  
**Solução**

O Help ocorre desta maneira:

AJUDA:REGBLOQ  
Este registro está bloqueado para uso.  
SF4-Tipos de Entrada e Saída

Como a geração da Proposta Comercial (Fata600), acaba gerando um Orçamento de Vendas (MATA415)de forma complementar, vinculado a proposta, é necessário que se preencha o  parâmetro **MV\_TESSAI** um TES (MATA080) não bloqueado ou que será utilizado na proposta , desta forma, o help deixará de ocorrer.
