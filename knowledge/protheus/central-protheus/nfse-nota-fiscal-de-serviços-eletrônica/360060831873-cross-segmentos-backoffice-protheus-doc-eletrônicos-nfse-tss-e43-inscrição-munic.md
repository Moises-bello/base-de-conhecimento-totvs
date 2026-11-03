---
article_id: 360060831873
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 8bdd1af7cf16cbce9be16267615018a19b374dcffd937c7c0f6be5e58ac7740c
fetched_at: '2026-06-28T22:39:58.569832+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - TSS: E43
  - Inscrição Municipal do prestador não encontrada na base de dados do município
  (Americana)'
type: support-article
updated_at: '2021-10-06T19:03:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060831873-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-TSS-E43-Inscri%C3%A7%C3%A3o-Municipal-do-prestador-n%C3%A3o-encontrada-na-base-de-dados-do-munic%C3%ADpio-Americana
---

**Ocorrência**Ao realizar a transmissão de um RPS para a prefeitura de Americana ocorre a rejeição:   
**E43 - Inscrição Municipal do prestador não encontrada na base de dados do município.**  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Causa**Esse problema ocorre quando a prefeitura não possui os dados desse contribuinte cadastrado na base de dados interna.  
  
**Solução**Nesse caso deverá entrar em contato com a prefeitura e solicitar as devidas liberações para **transmissões via Web Services** (tanto em Homologação quanto Produção).  
  
Observações:  
Verificar se os dados da filial (CNPJ x IM) estão corretos no cabeçalho do lote da tabela SPED053, campo **XML\_LOTE,** exemplo:

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000558202/mceclip0.png)**

Caso estejam incorretos, deverão ser corrigidos os dados no Cadastro da Filial e refazer o Wizard.cfg por completo para as informações serem atualizadas nas tabelas do TSS.
