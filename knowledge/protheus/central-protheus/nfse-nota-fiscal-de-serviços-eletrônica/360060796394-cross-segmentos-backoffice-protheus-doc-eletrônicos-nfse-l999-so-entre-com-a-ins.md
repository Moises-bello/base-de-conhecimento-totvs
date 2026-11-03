---
article_id: 360060796394
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 2e4e98049ff265cd9819d627c3df50e8bb7c45f47ec75e94eb9a80cd0b0266d1
fetched_at: '2026-06-28T22:39:57.535537+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - L999 - SO
  ENTRE COM A INSCRICAO PARA CONTRIBUINTES CADASTRADOS EM GOIANIA
type: support-article
updated_at: '2025-07-02T14:10:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060796394-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-L999-SO-ENTRE-COM-A-INSCRICAO-PARA-CONTRIBUINTES-CADASTRADOS-EM-GOIANIA
---

**Ocorrência**Ao realizar a transmissão de um RPS para a prefeitura de Goiânia é apresentado o erro: ***L999 - SO ENTRE COM A INSCRICAO PARA CONTRIBUINTES CADASTRADOS EM GOIANIA.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500002134061/mceclip0.png)***  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Causa**A rejeição ocorre pois está sendo informado a Inscrição Municipal no XML de um cliente/tomador não cadastrado internamente pela prefeitura.  
  
**Solução**Para correção deverá deixar no Cadastro do Cliente o campo **A1\_INSCRM** com conteúdo em branco.  
OU  
Caso a IM desse cliente já seja de Goiânia, deverá entrar em contato com a prefeitura para regularização e atualização da base de dados.
