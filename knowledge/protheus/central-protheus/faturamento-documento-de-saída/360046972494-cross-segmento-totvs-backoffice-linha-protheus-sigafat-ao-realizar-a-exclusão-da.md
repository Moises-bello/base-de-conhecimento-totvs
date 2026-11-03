---
article_id: 360046972494
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 8ecd38def33054d175b9f88938d8097d27731fc5e547f55726f04eff0055914e
fetched_at: '2026-06-28T22:38:43.848920+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ao realizar
  a exclusão da nota de serviços, o sistema apresenta uma tela solicitando preenchimento
  do Processo Administrativo: Help A926PROCOBR'
type: support-article
updated_at: '2023-09-18T17:37:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046972494-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ao-realizar-a-exclus%C3%A3o-da-nota-de-servi%C3%A7os-o-sistema-apresenta-uma-tela-solicitando-preenchimento-do-Processo-Administrativo-Help-A926PROCOBR
---

**Ocorrência**

Ao realizar a **exclusão** da **nota de serviços**, o sistema apresenta uma tela solicitando **preenchimento** do **Processo Administrativo**:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099975154)

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Causa**

Ao realizar a exclusão da nota de serviços, pode ocorrer algumas situações como:

* Já **ultrapassou** a **data limite de exclusão**;
* Está dentro do prazo, porém o **título** de **ISS** já está com **vencimento expirado**;
* O ISS não está expirado, o **parâmetro MV\_VLDSBT**= .T. e a **nota** esta **sem substituta**.

**Solução**

A **nota substituta e/ou o processo administrativo** é exigido por **algumas prefeituras** em casos de **cancelamento** de notas que **geraram ISS** e este já esta **vencido**:

1. Caso o **ISS** seja **devido**, é necessário a emissão da **nota substituta** ou verificar com sua Assessoria Contábil a forma de emissão do **Processo Administrativo**;

2. Caso o **ISS** seja **indevido**, é necessário **alterar** a **data** de **vencimento** (**E2\_VENCREA**) no **Contas a Pagar (FINA750)** para uma **data igual ou superior** à data base (**data atual**).

**Saiba mais**: [FAT0150 - Exclusão Notas Serviço (MATA521A) - Processo Administrativo ISS](https://tdn.totvs.com/pages/viewpage.action?pageId=267797581)
