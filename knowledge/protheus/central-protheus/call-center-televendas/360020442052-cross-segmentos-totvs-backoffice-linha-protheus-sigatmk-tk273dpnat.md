---
article_id: 360020442052
category: Call Center - Televendas
content_hash: e3193c6f0c5937eebcae38936ecf002003c088d8960aada40801193edc5cc596
fetched_at: '2026-06-28T22:41:30.309793+00:00'
product: protheus
section_id: 1500001537121
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGATMK - TK273DPNAT
type: support-article
updated_at: '2022-06-22T18:59:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020442052-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-TK273DPNAT
---

**Ocorrência**

Ao incluir um atendimento televendas está gerando a mensagem: **Nofuncw - opção não disponível no protheus função: TK273DPNAT Called By Tk271INIT**

![erro_tk273dpnat.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360016679032/erro_tk273dpnat.jpg)  
  
**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGATMK- a partir da versão 11.  
  
**Causa**

O erro ocorre por falta da função **tk273dpnat** no RPO.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Valide se as rotina **TMKA273** / **TMKA273B** /  **TMKXFUNA** estão atualizadas com a data de 04.05.18, caso não esteja, efetue o download do pacote das rotinas: **<https://suporte.totvs.com/portal/p/10098/download?e=686858>**

2. Via TDS ou IDE, aplique o pacote para atualização do RPO;

3. Reinicie o smartlient e refaça o processo.

**OBS**: É recomendado que toda aplicação de pacote seja efetuada primeiro em ambiente de homologação, para validar o processo e posteriormente, aplicado no ambiente de produção.

Para aplicação de pacote requer que o analista detenha conhecimentos de estrutura de de ambiente Protheus.

Caso necessite de apoio para aplicação, acione a equipe de Frame Work.
