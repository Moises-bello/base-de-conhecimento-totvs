---
article_id: 360036212274
category: Call Center - Telecobrança
content_hash: 739e5d1d7af5913e7fe960d2a825752550a63ba2a8055cd9a0254a0e447d3b9f
fetched_at: '2026-06-28T22:41:28.654121+00:00'
product: protheus
section_id: 1500001548222
source: central-protheus
title: 'Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGATMK- Help: TMKEXCSK1'
type: support-article
updated_at: '2022-06-22T17:14:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036212274-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Help-TMKEXCSK1
---

**Ocorrência**

Ao tentar acessar simultaneamente as rotinas**Seleção de títulos** (TMKA180), **Pré-Atendimento** (TMKA280), **Quitação de Cobrança** (TMKA290) e**Transferência de Cobrança** (TMKA300), utilizando empresas diferentes, o sistema exibe a mensagem “**Esta rotina não poderá ser utilizada enquanto houver algum processo de cobrança em execução**”, não permitindo o acesso as rotinas.

**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGATMK-A partir da versão 12.  
  
**Causa**

A rotina: **TMKA180** é necessário estar exclusiva quando for realizar o processo, mesmo que  exista mais de um usuário acessando em empresas ou filais diferentes.   
  
**Solução**

Realizado ajuste nas rotinas **Seleção de títulos**, **Pré-Atendimento**, **Quitação de Cobrança** e **Transferência de Cobrança** para que considere a Empresa ao efetivar o bloqueio de acesso, quando utilizado em ambientes com Gestão de Empresas.

**Função :**

**TMKA180** - Seleção de Titulo

**TMKA280** - Pré-Atendimento

**TMKA290** - Quitação de Cobrança

**TMKA300** - Transferência de Cobrança

O pacote pode ser acessado no endereço:

**12.1.23:<https://suporte.totvs.com/portal/p/10098/download?e=759602> ; 12.1.17:<https://suporte.totvs.com/portal/p/10098/download?e=759601> ;**
