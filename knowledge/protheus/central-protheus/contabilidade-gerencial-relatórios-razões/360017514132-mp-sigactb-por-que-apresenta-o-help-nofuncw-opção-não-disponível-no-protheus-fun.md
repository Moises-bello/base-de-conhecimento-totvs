---
article_id: 360017514132
category: Contabilidade Gerencial - Relatórios Razões
content_hash: 169c28635cc31495a635f802e756822a3abdc0afc0a77ccd723040f3cb7e14f2
fetched_at: '2026-06-28T22:40:41.169722+00:00'
product: protheus
section_id: 1500001548782
source: central-protheus
title: 'MP - SIGACTB - POR QUE APRESENTA O HELP: NOFUNCW  - Opção não disponível no
  Protheus Função CONR230 ?'
type: support-article
updated_at: '2021-04-28T22:12:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017514132-MP-SIGACTB-POR-QUE-APRESENTA-O-HELP-NOFUNCW-Op%C3%A7%C3%A3o-n%C3%A3o-dispon%C3%ADvel-no-Protheus-Fun%C3%A7%C3%A3o-CONR230
---

**Ocorrência**

Ao selecionar a opção centro de custo (relatórios) apresenta:

**HELP: NOFUNCW**  - Opção não disponível no Protheus Função **CONR230**  
   
 **Ambiente**Microsiga Protheus  – Contabilidade Gerencial  – A partir da versão 11.80  
  
   
**Solução**

A rotina ***CONR230***, pertence a o modulo **SIGACON (CONTABILIDADE)** que foi descontinuado. No módulo ***SIGACTB (CONTABILIDADE GERENCIAL)***, a rotina responsável pelo relatório de Listagem de Centro de Custo temos o ***CTBR020***, e  Razão Contábil por Centro de Custo - *CTBR440*

Verifique se rotina esta disponível em seu menu do módulo SIGACTB, caso não esteja, realize a troca do menu.

<http://tdn.totvs.com/pages/releaseview.action?pageId=271164329>
