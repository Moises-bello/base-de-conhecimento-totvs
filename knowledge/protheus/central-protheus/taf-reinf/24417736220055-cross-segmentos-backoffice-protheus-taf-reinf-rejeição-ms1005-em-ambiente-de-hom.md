---
article_id: 24417736220055
category: TAF - REINF
content_hash: 8a266fa0b502cd1148519ae4a1cc5d2d6ff307293b9ca6143f86bc3152b6a777
fetched_at: '2026-06-28T22:41:34.822852+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Rejeição MS1005 em ambiente
  de homologação.
type: support-article
updated_at: '2024-06-26T13:10:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24417736220055-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Rejei%C3%A7%C3%A3o-MS1005-em-ambiente-de-homologa%C3%A7%C3%A3o
---

**Ocorrência**No módulo TOTVS automação fiscal(TAF) ao transmitir um evento periódico é retornada a rejeição MS1005 em ambiente de homologação.

**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Automação Fiscal - Todas as versões.  
  
**Causa**

  O erro retornado pela RFB, ocorre porque já existe um R-1000 ativo na base de dados da RFB para o ambiente de homologação.

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1.  Exclua a apuração retornada inconsistente do R-1000.

[Cross Segmentos - Backoffice Protheus - TAF - REINF - Como excluir apuração inconsistente.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8549885209879-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-excluir-apura%C3%A7%C3%A3o-inconsistente?source=search)

2. No Painel REINF envie a solicitação de remoção do contribuinte.

![MS1005.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24417752058903)

3. Após o retorno autorizado da remoção do contribuinte, apure e transmita novamente o R-1000.
