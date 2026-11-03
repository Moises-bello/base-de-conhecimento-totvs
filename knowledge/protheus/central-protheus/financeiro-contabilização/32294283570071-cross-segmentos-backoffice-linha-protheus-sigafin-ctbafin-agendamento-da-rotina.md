---
article_id: 32294283570071
category: Financeiro - Contabilização
content_hash: 7b5757276b2581644718df157b4900b62dd3c5c30b2c934204cd9d9168a56e99
fetched_at: '2026-06-28T22:38:05.321396+00:00'
product: protheus
section_id: 1500001550502
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBAFIN - Agendamento
  da rotina CTBAFIN via schedule
type: support-article
updated_at: '2025-05-22T16:54:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32294283570071-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBAFIN-Agendamento-da-rotina-CTBAFIN-via-schedule
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32294306514839) Tempo aproximado para leitura: **00****:05:00 min** **Dúvida**Como realizar o agendamento da rotina CTBAFIN via schedule?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da versão 12  
  
  
**Solução**

**Como efetuar o agendamento da rotina CTBAFIN - Rotina de contabilização off-line do Financeiro**

A rotina **CTBAFIN** está preparada para ser executada via **Schedule**.

Basta seguir os mesmos procedimentos para agendamento das demais rotinas do sistema, os quais estão descritos no seguinte link:  
[Schedule - Como agendar a execução de rotinas](https://tdn.totvs.com/pages/releaseview.action?pageId=271167961)

Ao informar a rotina **CTBAFIN** no campo **"Rotina"** em **Schedule > Agendamentos > Novo**, será aberta a tela de parâmetros da rotina **(caso não seja aberta, clique no botão "Parâmetros").**  
Os parâmetros são os mesmos que são apresentados ao acessar a rotina **CTBAFIN** via menu no módulo de **Financeiro > Miscelânea / Contábil / Contabilização Off-line.**

Adicionalmente, na configuração via **Schedule** a tela de parâmetros apresenta a aba **"Fórmulas"**. Nesta aba podem ser definidas fórmulas, que devem ser cadastradas, para que sejam retornados os valores dos parâmetros conforme desejado. Caso deseje utilizar fórmulas, deixe os parâmetros da aba **"Parâmetro"** em branco e utilize apenas as fórmulas.

A rotina será executada conforme configurado no **Schedule** para efetuar a contabilização das operações financeiras.

Segue exemplo de um cadastro deste agendamento.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32295026731415)

Saiba mais:

[Contabilização Offline - CTBAFIN - Financeiro - P12](https://tdn.totvs.com/pages/releaseview.action?pageId=497932563)

[Documentação Smart Schedule](https://tdn.totvs.com/display/public/framework/Schedule+Protheus)

[Lançamento padrão Financeiro](https://tdn.totvs.com/pages/releaseview.action?pageId=235585410)
