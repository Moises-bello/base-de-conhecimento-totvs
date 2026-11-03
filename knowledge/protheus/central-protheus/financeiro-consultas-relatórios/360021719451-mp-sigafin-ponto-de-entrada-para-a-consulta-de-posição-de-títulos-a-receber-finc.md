---
article_id: 360021719451
category: Financeiro - Consultas / Relatórios
content_hash: ec2f710b1fc0b5f91949c40e664345a6b480cf5ee563c5cfcefeb6c1b3186641
fetched_at: '2026-06-28T22:37:58.391364+00:00'
product: protheus
section_id: 1500001539561
source: central-protheus
title: MP - SIGAFIN - Ponto de Entrada para a Consulta de Posição de Títulos a Receber
  - FINC040
type: support-article
updated_at: '2021-04-28T15:19:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021719451-MP-SIGAFIN-Ponto-de-Entrada-para-a-Consulta-de-Posi%C3%A7%C3%A3o-de-T%C3%ADtulos-a-Receber-FINC040
---

**Dúvida**Quais os pontos de entrada para a rotina FINC040?  
   
 **Ambiente**Protheus – Financeiro – Todas as versões  
  
   
**Solução**

FINC040 - ExecBlock("FC040FIL",.F.,.F.) - <http://tdn.totvs.com/pages/releaseview.action?pageId=6071267>;

FINC040 - ExecBlock("F040BOT",.F.,.F.) - Ponto de entrada para montar array com botões a serem apresentados na tela da consulta;

FINC040 - ExecBlock("FI040CPTN",.F.,.F.) - <http://tdn.totvs.com/pages/viewpage.action?pageId=89620900>;

FINC040 - ExecBlock("FI040MNCP",.F.,.F.,{aBrowse}) - <http://tdn.totvs.com/display/PROT/FI040MNCP+-+Manipula+as+colunas+do+aBrowse>;

FINC040 - ExecBlock("FI040TPCP",.F.,.F.,{aCampos}) - <http://tdn.totvs.com/pages/viewpage.action?pageId=89620917>;

FINC040 - FI040CMPO - <http://tdn.totvs.com/pages/viewpage.action?pageId=6071268>;

FINC040 - ExecBlock("F040FILTIT") - Validação para inclusão do titulo na tabela temporária  
FINC040 - ExecBlock("FI040GRCP",.F.,.F.) - <http://tdn.totvs.com/pages/viewpage.action?pageId=89620934>
