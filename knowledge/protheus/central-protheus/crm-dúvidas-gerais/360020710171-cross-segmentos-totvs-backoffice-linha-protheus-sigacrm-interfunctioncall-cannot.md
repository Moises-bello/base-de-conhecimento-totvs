---
article_id: 360020710171
category: CRM - Dúvidas Gerais
content_hash: 21e6aa8067dee72c4b5ef0dc825735d666450f1c7b9ee96d2a45b2c2e15dc674
fetched_at: '2026-06-28T22:40:27.526654+00:00'
product: protheus
section_id: 1500001538021
source: central-protheus
title: 'Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGACRM  -InterFunctionCall:
  cannot find function FT600VPROD'
type: support-article
updated_at: '2022-06-22T19:44:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020710171-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGACRM-InterFunctionCall-cannot-find-function-FT600VPROD
---

**Ocorrência**

Ao gerar uma proposta no **CRM** é apresentado o erro: **InterFunctionCall**: **cannot find function FT600VPROD**  
  
**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGACRM - a partir da release 12.1.17.  
  
**Causa**

A função **FT600VPROD** não encontra-se na lista de funções do RPO.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Efetue o download do pacote do fonte **fatv600a**: **<https://suporte.totvs.com/portal/p/10098/download?e=653437>**;  
2. Via TDS ou IDE, aplique o pacote para atualização do RPO;  
3. Reinicie o smartlient e refaça o processo.

**OBS**: É recomendado que toda aplicação de pacote seja efetuada primeiro em ambiente de homologação, para validar o processo e posteriormente, aplicado no ambiente de produção.

Para aplicação de pacote requer que o analista detenha conhecimentos de estrutura de de ambiente Protheus.

Caso necessite de apoio para aplicação, acione a equipe de Frame Work.
