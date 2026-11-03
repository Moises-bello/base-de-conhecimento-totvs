---
article_id: 4413978579223
category: Financeiro - Contas a Pagar - Dirf
content_hash: c9f3a96b6ab515e3af6c8c25d7884c7de19d0ac50fa916273e6fe447b59a816f
fetched_at: '2026-06-28T22:38:10.700134+00:00'
product: protheus
section_id: 1500001550482
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA050 - Qual a gravação
  correta dos campos no Financeiro para geração da DIRF
type: support-article
updated_at: '2024-07-26T19:54:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413978579223-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA050-Qual-a-grava%C3%A7%C3%A3o-correta-dos-campos-no-Financeiro-para-gera%C3%A7%C3%A3o-da-DIRF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25200671994391) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Qual a gravação correta dos campos no Financeiro para geração da DIRF?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões  
  
**Solução**

De que forma o título do tipo **NF** (título ORIGINAL) devem estar gravados?  
Campo **Gera Dirf** (**E2\_DIRF**) o conteúdo deve ser **2-Não** após a geração do imposto, na inclusão do título o campo é gravado como 1-Sim.  
Campo **Código de retenção** (**E2\_CODRET**), deve estar preenchido.  
Campo **Título Pai** (**E2\_TITPAI**), deve estar em branco.  
  
De que forma os títulos do tipo **TX** (título de imposto) devem estar gravados?  
Campo **Gera Dirf** (**E2\_DIRF**) o conteúdo deve ser **1**.  
Campo **Código de retenção** (**E2\_CODRET**), deve estar preenchido.  
Campo **Título Pai** (**E2\_TITPAI**), deve estar preenchido com os dados do título principal (prefixo+número+parcela+tipo+fornecedor+loja)  
  
No cadastro de **Fornecedor**, o campo **CGC/CPF** (**A2\_CGC**) tem que estar preenchido com o **CNPJ/CPF** do **Fornecedor** e o Tipo (**A2\_TIPO**) igual a F - **Pessoa Física**, J - **Jurídica** ou X-**Outros para fornecedor exterior**.

**Saiba Mais**

[Cadastro de Sócio SCP - FINA994](https://tdn.totvs.com/pages/releaseview.action?pageId=527846378)

[Informações sobre a DIRF?](https://tdn.totvs.com/pages/releaseview.action?pageId=43549271)
