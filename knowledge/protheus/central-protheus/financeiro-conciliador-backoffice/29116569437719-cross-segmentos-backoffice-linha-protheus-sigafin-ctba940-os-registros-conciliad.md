---
article_id: 29116569437719
category: Financeiro - Conciliador Backoffice
content_hash: db27c85578ccded0703ea624c36a32a5df18be8a9031ba3a7ce24e82606d7c52
fetched_at: '2026-06-28T22:37:47.214841+00:00'
product: protheus
section_id: 30769054561431
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940 - Os registros
  conciliados na rotina anterior, aparecem na rotina CTBA940, como não conciliados
type: support-article
updated_at: '2025-09-11T18:17:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29116569437719-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-Os-registros-conciliados-na-rotina-anterior-aparecem-na-rotina-CTBA940-como-n%C3%A3o-conciliados
---

**Dúvida**Os registros conciliados na rotina anterior, aparecem na rotina CTBA940, como não conciliados.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da release 12.2310  
  
**Solução**

No padrão, as conciliações realizadas nas rotinas legadas **FINA380/FINA473** não serão apresentadas como conciliadas no novo mecanismo. Isso ocorre porque, além dos campos **E5\_RECONC** e **FK5\_DTCONC**, a rotina **CTBA940** exige que os registros estejam devidamente gravados nas novas tabelas **QLB/QLC** e **QLD**.

Destacamos, ainda, que mesmo com o preenchimento dos campos **\_MSUIDT** por meio do **WizardUUID**, o comportamento permanecerá inalterado. Nesses casos, os dados serão exibidos na aba **“Não encontrados”** da rotina **CTBA940**, ainda que já tenham sido conciliados na rotina anterior, sendo necessário conciliar novamente.

Para consultas referentes às conciliações realizadas nas rotinas anteriores, recomendamos a utilização do relatório de **Extrato Bancário** disponível no **SmartView**.

Segue também artigo de referência sobre como desconciliar registros conciliados na rotina legado.

[Cross Segmentos - Backoffice Linha Protheus - CTBA940 - Como desconciliar o que foi conciliado pela antiga rotina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/28949343147031-Cross-Segmentos-Backoffice-Linha-Protheus-CTBA940-Como-desconciliar-o-que-foi-conciliado-pela-antiga-rotina)
