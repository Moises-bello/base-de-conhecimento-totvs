---
article_id: 33711308215703
category: Financeiro - Contabilização
content_hash: b2e976da58aa12d4b3c172bf512599db3408c4b1e7244f773409f518dda2cfb8
fetched_at: '2026-06-28T22:38:05.214267+00:00'
product: protheus
section_id: 1500001550502
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBAFIN - Diferença
  entre contabilização online  e offline
type: support-article
updated_at: '2025-07-25T13:01:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33711308215703-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBAFIN-Diferen%C3%A7a-entre-contabiliza%C3%A7%C3%A3o-online-e-offline
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33711308208791) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Qual é a diferença entre a contabilização online e a contabilização offline?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – Todas as Releases  
  
**Solução**  
Com a LP previamente cadastrada, é possível realizar a contabilização no modo **offline e online**. No caso da contabilização offline, os processos são executados normalmente e, após sua conclusão, a contabilização é realizada por meio da rotina **CTBAFIN**, que gera os lançamentos contábeis correspondentes a todos os processos executados.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33711586650903)

Para a contabilização no modo **online**, é necessário, na própria rotina de origem, acessar o atalho **F12** e habilitar o parâmetro **Contabiliza Online** para **"Sim"**. Com isso, o processo é executado e, ao ser finalizado, é apresentada automaticamente a tela de contabilização com os dados que serão encaminhados ao módulo contábil.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33711586652695)

Ressaltamos que **nem todas as LPs são compatíveis com a contabilização online ou offline**. Recomenda-se a consulta da documentação abaixo, onde constam as LPs disponíveis e os respectivos processos que suportam cada modalidade de contabilização.

[Documentação LPs - Lançamento padrão financeiro](https://tdn.totvs.com/pages/releaseview.action?pageId=235585410)

**Saiba mais**

[Contabilização Offline - CTBAFIN - Financeiro - P12](https://tdn.totvs.com/pages/releaseview.action?pageId=497932563)
