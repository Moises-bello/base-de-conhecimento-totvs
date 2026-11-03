---
article_id: 360038352734
category: Materiais - Compras (SIGACOM)
content_hash: 7350c0ff5e61f301b6540e3bf636e7e05c71af6eb4791368078d99dba08718e4
fetched_at: '2026-06-28T22:41:14.189980+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Aposentadoria especial
  Tela apresentada sem o grid para incluir os percentuais da aposentadoria
type: support-article
updated_at: '2022-05-16T21:11:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038352734-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Aposentadoria-especial-Tela-apresentada-sem-o-grid-para-incluir-os-percentuais-da-aposentadoria
---

**Ocorrência**No módulo de Compras, ao abrir a opção de de **Aposentadoria Especial,** o **grid** é apresentado cortada não permitindo informar os percentuais respectivos.

![](https://p23.zdusercontent.com/attachment/888110/2LEGa4IBm7dkkODmhjlXAURNw?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..eMeSijJKDaBoxDItLJmP_Q.HCGPa8-K7x6mTqMPCJc4v5dbHoNAaDjBtlnLf_Gb-LuBQKYfTBRACbnUuZTMYEcDa41i6gpwqZllqfea3M7TQmOOyV-jUJuNClWzCNqMyhwWjNPYBN-shWBfv6YTpxnm2pPQgVFbNGBdIdRisunCuMuQ80DtmvM-tTSlf1XlsnudcyDo4Kl5pAJrL52De-D_dOMma57FOsm1rFb4kjDIe73CEgHwJSup_Lly7mG0e5rDQd26zmniU4XRZqk79xZdtP1kUguwCJ-Lo-6EYdaMNQ.u2jsdQV0wiRWx1HI2nQ_FA)

**Ambiente**Protheus– Compras – A partir da versão 12.1.17

**Causa**Esse incidente ocorre, pois a parametrização do sistema no configurador não esta marcada para o módulo que esta acessando, desta forma mesmo havendo a **tabela** **DHP** a grid não será mostrada.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acessar o configurador opção base de dados ;  
2. Acessar na tabela DHP os campos: **DHP\_FAIXA1, DHP\_FAIXA2, DHP\_FAIXA3**;  
3. Na aba de MÓDULOS selecionar os módulos da qual a grid poderá ser apresentada e salvar.
