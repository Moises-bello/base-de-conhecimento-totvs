---
content_hash: 422f19c57679efe51bb458456838d6a2023e5897321e5076c0e301b450e34c38
fetched_at: '2026-06-29T00:10:50.639480+00:00'
page_id: '562470315'
product: rm
source: tdn-rm
title: Configuração do ambiente da NFS-e (CfgAmbNfse001)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=562470315
version: 6
---

A NFS-e enviada pelo RM é integrada com o TSS e então transmitida para o ambiente da prefeitura. Contudo algumas prefeitura exigem configurações especificas de autenticação para realizar a autorização da NFS-e.

Durante a integração entre RM x TSS estas configurações são transmitidas ao TSS através do serviço CfgAmbNfse001 conforme documentação do TSS: 

Para facilitar o entendimento desta integração disponibilizamos abaixo um mapeamento de campos do RM com os campos do serviço do TSS

|  |  |  |
| --- | --- | --- |
| **Campos dos parâmetros da Filial** | **Campos do Serviço CFGAMBNFSE001** | **Parâmetro TSS (SPED000)** |
| TPARFILIAL.LOGINPREFEITURA | LOGIN | MV\_NFSUSER |
| TPARFILIAL.SENHAPREFEITURA | PASS | MV\_NFSPASS |
| TPARFILIAL.AUTORIZACAOPREFEITURA | CHAVEAUTENTICACAO | MV\_CHVAUTE |
| TPARFILIAL.CLIENTID | CLIENTID | MV\_CLIENID |
| TPARFILIAL.CLIENTSECRET | CLIENTSECRET | MV\_CLIENSC |
| Para Florianópolis será gerado a partir do campo TPARFILIAL.AUTO­RIZACAOPREFEITURA  Para Londrina será gerado com a Inscrição municipal da Filial  Para Batatais será gerado a partir do campo TPARFILIAL.SENHAPREFEITURA  Para Itupeva será gerado a partir do campo TPARFILIAL.SENHAPREFEITURA | AUTORIZACAO | MV\_AUTORIZ |
