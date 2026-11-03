---
article_id: 4415932583447
category: RH - Soluções para error.log
content_hash: 1920289edb5ba9f256573c03178412157e9aae199a1cd315f49265a7ee9eb59e
fetched_at: '2026-06-28T22:44:08.886852+00:00'
product: protheus
section_id: 115003853987
source: central-protheus
title: RH - Linha Protheus - GPE - Error log ao executar Schedule de Workflow de Férias
  - array out of bounds ( 0 of X )  on FSRH
type: support-article
updated_at: '2025-09-11T17:51:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415932583447-RH-Linha-Protheus-GPE-Error-log-ao-executar-Schedule-de-Workflow-de-F%C3%A9rias-array-out-of-bounds-0-of-X-on-FSRH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34873937152663) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao tentar realizar a execução do **Workflow de Férias**, através da rotina **GPEW030** cadastrado nos Agendamentos, é gerado ***error log***: "***array out of bounds (*** **0** ***of*** **1** ***)  on*** **FSRH(GPEW030.PRW)**".  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Causa**Este erro ocorre devido à desatualização do fonte **GPEW030.**  
  
**Solução  
1.** Aplicar o pacote conforme abaixo:  
Pacote de Expedição Contínua do RH:<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854>   
 **Saiba Mais:**  
Documentação técnica sobre a correção: <https://tdn.totvs.com/pages/releaseview.action?pageId=653841698>
