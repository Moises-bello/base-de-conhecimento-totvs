---
article_id: 26266136563479
category: Financeiro
content_hash: c53793b3db4c12958005d3e0f5cb568ee0b4f89d420c5a90949790d45205e3f6
fetched_at: '2026-06-28T22:38:03.188550+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA914 - Via Schedule
type: support-article
updated_at: '2024-09-10T20:47:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26266136563479-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA914-Via-Schedule
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26266136533911) Tempo aproximado para leitura: **01:00 min** **Dúvida**É possível utilizar as rotinas abaixo via Schedule?

**FINA914** - Importação  
**FINA916** - Conciliação de Vendas  
**FINA918** - Conciliação de Pagamentos  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Financeiro - Todas as versões  
  
**Solução**Sobre inclusão das rotinas **FINA914** (Wizard de importação), **FINA916** (Conciliador de Vendas) e **FINA918** (Conciliador de Pagamentos) via Schedule, não será possível, pois, conforme documentação abaixo, para ser possível configurar os parâmetros no agendamento via Schedule, a rotina precisa ter a função "SchedDef()", e essas rotinas não têm.  
  
Como agendar rotinas via Schedule:  
https://tdn.totvs.com/pages/releaseview.action?pageId=271167961  
  
SchedDef()  
https://tdn.totvs.com/pages/releaseview.action?pageId=36800166

**Saiba Mais**

**[FINA914 - Importação](https://tdn.totvs.com/pages/releaseview.action?pageId=655440482)**

**[FINA916 - Conciliação de Vendas](https://tdn.totvs.com/pages/releaseview.action?pageId=655196878)**

**[FINA918 - Conciliação de Pagamentos](https://tdn.totvs.com/pages/releaseview.action?pageId=655196877)**
