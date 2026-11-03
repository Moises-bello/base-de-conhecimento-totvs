---
article_id: 360059756013
category: RH - FGTS / SEFIP
content_hash: 4bfa3ffa8493cab6cd349072877120b719d251fd8a89cd023ca657ccdf7c0a55
fetched_at: '2026-06-28T22:43:41.410214+00:00'
product: protheus
section_id: 360003115651
source: central-protheus
title: 'RH - Linha Protheus - GPE - Erro Sefip 300405 e/ou 300411 - Categoria do Trabalhador
  incompatível com o Código de Recolhimento/FPAS informados, como resolver '
type: support-article
updated_at: '2021-07-17T03:18:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059756013-RH-Linha-Protheus-GPE-Erro-Sefip-300405-e-ou-300411-Categoria-do-Trabalhador-incompat%C3%ADvel-com-o-C%C3%B3digo-de-Recolhimento-FPAS-informados-como-resolver
---

**Ocorrência**Ao importar o arquivo SEFIP.RE gerado no Protheus, o validador do programa SEFIP apresenta o seguinte erro 300405 e/ou 300411 - Categoria do Trabalhador incompatível com o Código de Recolhimento/FPAS informados.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Causa**- O campo com categoria do trabalhador deve ser compatível com o FPAS da empresa/código de recolhimento.  
  
**Solução****1**. Verificar se o **"FPAS"** indicado no **Cadastro de Empresa** esta correto, e **se é compatível** com a categoria dos funcionários. **Via Configurador**. modulo SIGACFG.

**2.**Verificar se o **"Código de Recolhimento"** informado nos **parâmetros de geração** do arquivo SEFIP.RE no modulo SIGAGPE esta correto, e **se é compatível** com a categoria dos Funcionários.

**3.** Verificar se a **"Categoria do funcionário"** informada no **Cadastro do Funcionário** aba **"Funcionais"** esta correta, e **se é compatível** Com **FPAS/código de recolhimento.**

**Saiba mais:  <https://tdn.totvs.com/display/public/PROT/FGTS>**
