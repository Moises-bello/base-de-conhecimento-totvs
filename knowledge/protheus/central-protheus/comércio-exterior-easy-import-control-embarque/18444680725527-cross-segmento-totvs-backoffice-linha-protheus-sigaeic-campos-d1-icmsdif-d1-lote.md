---
article_id: 18444680725527
category: Comércio Exterior - Easy Import Control - Embarque
content_hash: f19e4cfb4463d461ec0b55c210861255a615ccd71f90434d9b175079002faa98
fetched_at: '2026-06-28T22:39:48.808270+00:00'
product: protheus
section_id: 1500001538381
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Campos "D1_ICMSDIF",
  "D1_LOTECTL" e "D1_DTVALID" não estão sendo preenchidos ao gerar uma Pré-Nota de
  Entrada.
type: support-article
updated_at: '2024-02-28T17:31:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18444680725527-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Campos-D1-ICMSDIF-D1-LOTECTL-e-D1-DTVALID-n%C3%A3o-est%C3%A3o-sendo-preenchidos-ao-gerar-uma-Pr%C3%A9-Nota-de-Entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18444668156823) Tempo aproximado para leitura: **03:00 min****Dúvida**Na rotina "**EICDI154 - Recebimento de Importação**", ao gerar uma Pré-Nota de Entrada, os campos ICMS Diferido (**D1\_ICMSDIF**), Lote **(D1\_LOTECTL)** e Data de Validade do Lote **(D1\_DTVALID)** não estão sendo preenchidos com as informações enviadas pelo SIGAEIC.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control*- a partir da versão12.1.33  
 **Solução**Os campos pertencem a rotinas do Módulo de Compras em que os mesmos não estão marcados como **"Usado"** para o módulo de Importação **(SIGAEIC)**, desta forma, ao efetuar a geração da nota fiscal, as informações não são gravadas na tabela de Itens da Nota **(SD1)**. Foram feitos os ajustes no dicionário de dados "**SX3**" para que os campos referente ao ICMS Diferido **(D1\_ICMSDIF**), Lote **(D1\_LOTECTL)** e Data de Validade do Lote **(D1\_DTVALID)** sejam considerados como Usados para o **SIGAEIC**.

**Saiba mais:**

[Ajuste de Campos Usados para a Importação na geração de Nota Fiscal](https://tdn.totvs.com/pages/releaseview.action?pageId=734369140)

[Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Controle de lote MV\_LOTEEIC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037038934-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Controle-de-lote-MV-LOTEEIC)

[Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Rejeição 525: CFOP de Importação e não informado dados da DI](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026403192-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Rejei%C3%A7%C3%A3o-525-CFOP-de-Importa%C3%A7%C3%A3o-e-n%C3%A3o-informado-dados-da-DI)
