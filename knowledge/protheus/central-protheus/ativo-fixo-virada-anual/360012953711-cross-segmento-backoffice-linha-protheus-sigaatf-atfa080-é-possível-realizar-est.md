---
article_id: 360012953711
category: Ativo Fixo - Virada Anual
content_hash: da134145a420f4eff4092fdb534978fe695c594fcb9368667ac79a5c56b6f75e
fetched_at: '2026-06-28T22:41:54.205028+00:00'
product: protheus
section_id: 1500001547482
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus -  SIGAATF - ATFA080 - É possível
  realizar estorno (correção) da rotina
type: support-article
updated_at: '2025-04-10T16:46:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012953711-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA080-%C3%89-poss%C3%ADvel-realizar-estorno-corre%C3%A7%C3%A3o-da-rotina
---

**Dúvida**  
É possível realizar estorno (correção) da rotina ATFA080?  
  
**Ambiente**  
Cross Segmento - Backoffice Linha Protheus  Ativo Fixo – A partir da versão 11.80  
  
  
**Solução**A rotina de Virada Anual não possui um estorno, neste caso será necessário voltar o backup da tabela SN5. Na virada anual a SN5 é reconstruída baseada nos saldos contidos na tabela **SN3** que sejam consistidos com os movimentos da tabela **SN4**.   
O processamento da rotina é irreversível, por isso é importante sempre ter um backup das tabelas.

**Veja Mais**

**<http://tdn.totvs.com/display/PROT/ATF0001+Rotina+Virada+Anual>**

**<http://tdn.totvs.com.br/pages/releaseview.action?pageId=271163111>**
