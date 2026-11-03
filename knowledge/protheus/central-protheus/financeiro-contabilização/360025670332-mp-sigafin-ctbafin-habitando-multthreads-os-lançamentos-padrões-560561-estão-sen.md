---
article_id: 360025670332
category: Financeiro - Contabilização
content_hash: 681a3aa92cae96789dfb4aaf95f2906d00eecc969fa34e0c730a2d91131136c0
fetched_at: '2026-06-28T22:38:05.558084+00:00'
product: protheus
section_id: 1500001550502
source: central-protheus
title: MP - SIGAFIN - CTBAFIN - Habitando Multthreads os lançamentos padrões 560/561
  estão sendo gerados como Pré lançamentos
type: support-article
updated_at: '2021-04-28T15:56:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025670332-MP-SIGAFIN-CTBAFIN-Habitando-Multthreads-os-lan%C3%A7amentos-padr%C3%B5es-560-561-est%C3%A3o-sendo-gerados-como-Pr%C3%A9-lan%C3%A7amentos
---

**Dúvida**Habitando Multthreads os lançamentos padrões 560/561 estão sendo gerados como Pré lançamentos?  
  
 **Ambiente**Microsiga Protheus – Financeiro – CTBAFIN – A partir da versão 12  
  
**Solução  
CTBAFIN** - possibilita *Multthreads*  
Parâmetros configurados *Multthreads*

**MV\_CFINTHR**  
**MV\_AUTLCTO**  
**MV\_PRELAN**  
**MV\_CT105MS**  
  
Porém nos parâmetros da rotina existe a pergunta **Separa Por** - Período/Documento/Processo.  
Caso a pergunta **Separa Por**= Documento, o mesmo deve alterar o parâmetro.

**MV\_GPDOCTB = .T.** - Determina que os **LPs 560** e **561** sejam agrupados em um mesmo documento contábil quando a pergunta **Separa por** estiver por documento.  
  
**Importante:**Documentação do parâmetro  
 <http://tdn.totvs.com/pages/releaseview.action?pageId=272696341>   
  
Parâmetros da rotina **CTBAFIN**  
<http://tdn.totvs.com.br/pages/releaseview.action?pageId=271166213>

Explicação do conteúdo da pergunta separa por em relação aos LP's **560/561**  
<http://tdn.totvs.com/display/public/PROT/FIN0023_LPAD_contabilizacao_off_line_LP_560_561>
