---
article_id: 4414865424535
category: PMS - Projetos
content_hash: 176ee04737725ad4fa20205fc3b54a9fc4d1179e6296f8bc05032e51e3ebb5de
fetched_at: '2026-06-28T22:37:14.843978+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - PMS - Os campos C1_PROJET
  e C1_TAREFA não estão sendo preenchido na abertura da SC
type: support-article
updated_at: '2021-12-03T19:17:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414865424535-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-PMS-Os-campos-C1-PROJET-e-C1-TAREFA-n%C3%A3o-est%C3%A3o-sendo-preenchido-na-abertura-da-SC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Duvida**Os campos **C1\_PROJET** e **C1\_TAREFA** não estão sendo preenchido na abertura da Solicitação de Compra, visto que a amarração com a tabela **AFG**, e **AFJ** estão sendo registradas normalmente.  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Gestão de Projetos PMS - Todas as versões  
  
**Solução**Os campos **C1\_PROJET** e **C1\_TAREFA** realmente não preenche de forma automática, estes campos são informativos caso queira utiliza-los deve informar manual.  
Quando gera um solicitação de compras através do módulo PMS, deve integrar o projeto/edt/tarefa na tabela **AFG**, que se encontra em ações relacionadas Projetos na rotina **MATA110**. 

**Saiba Mais**Documentação com o processo para gerar SC  
[MP-PMS-Gerar Solicitação de Compras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000583528-MP-PMS-Gerar-Solicita%C3%A7%C3%A3o-de-Compras?source=search)
