---
article_id: 28949343147031
category: Financeiro - Conciliador Backoffice
content_hash: 376e6037d2cf04491427f92c7f2b0b866332f52f38385c12cc5260a8af4baa21
fetched_at: '2026-06-28T22:37:47.057614+00:00'
product: protheus
section_id: 30769054561431
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - CTBA940 - Como desconciliar o
  que foi conciliado pela antiga rotina
type: support-article
updated_at: '2025-07-02T11:37:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28949343147031-Cross-Segmentos-Backoffice-Linha-Protheus-CTBA940-Como-desconciliar-o-que-foi-conciliado-pela-antiga-rotina
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28949373933335) Tempo aproximado para leitura: **00****:05 min**

**Dúvida**  
Como desconciliar o que foi conciliado pela antiga rotina?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Solução**

Os registros que já foram conciliados não precisam ser incluídos na nova rotina. Conforme descrito na documentação, é necessário definir uma data limite que marque o início da conciliação nesse novo processo.

Entretanto, caso seja indispensável incluir registros já conciliados na rotina anterior, é possível seguir o procedimento de atualização das informações através do [WIZARD WIZARDUUID](https://centraldeatendimento.totvs.com/hc/pt-br/articles/29106222860567-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-WIZARD-de-configura%C3%A7%C3%A3o-do-Novo-Conciliador-Backoffice) do novo conciliador.

Contudo, esses registros serão listados na aba "Dados não encontrados" e deverão ser conciliados novamente para passarem a constar na nova rotina e depois realizar o "Cancelamento do Match".

**Saiba mais**

[FAQ - Conciliador BackOffice - Conciliação Bancária Automática e Manual](https://tdn.totvs.com/pages/viewpage.action?pageId=773512408)
