---
article_id: 36319654061335
category: Financeiro - Novo Gestor Financeiro
content_hash: e53ccb572fff80198f0fb147de51ab5e2b51030bfbb0d66bb79d44eae10fee3d
fetched_at: '2026-06-28T22:37:41.374379+00:00'
product: protheus
section_id: 33830415324183
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - O JOB FINA711 pode ser
  desabilitado?
type: support-article
updated_at: '2025-11-13T20:43:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36319654061335-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-O-JOB-FINA711-pode-ser-desabilitado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36319644483351) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Após a descontinuidade da **Comunicação Bancária Online / via API (Contas a Receber) podemos desabilitar o JOB FINA711?**  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Financeiro - Todas as versões  
  
**Solução:**  
O **JOB FINA711** é responsável pela **atualização do dashboard do novo Gestor Financeiro**, permitindo também a **integração para transmissão de boletos via API**, utilizada na **geração de boletos e comprovantes**.  
   
É importante destacar que, **caso a rotina FINA710 seja utilizada**, o **JOB FINA711 deve permanecer ativo**, pois é ele quem mantém o dashboard atualizado.  
   
Reforçamos ainda que o **processo de transmissão do Contas a Receber (JOB FINA713)** será **descontinuado a partir de abril do próximo ano**. Entretanto, o **processo de Contas a Pagar continuará ativo**, utilizando o **mesmo dashboard (FINA710)**.  
   
Portanto, mesmo com a descontinuidade programada do Contas a Receber, **o JOB FINA711 deve permanecer habilitado** para garantir o funcionamento correto do módulo de **Contas a Pagar**.

**Saiba Mais**

[Prorrogação da Descontinuação da Comunicação Bancária Online / via API (Contas a Receber) do TOTVS Backoffice da Linha Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33180957342615-Prorroga%C3%A7%C3%A3o-da-Descontinua%C3%A7%C3%A3o-da-Comunica%C3%A7%C3%A3o-Banc%C3%A1ria-Online-via-API-Contas-a-Receber-do-TOTVS-Backoffice-da-Linha-Protheus)
