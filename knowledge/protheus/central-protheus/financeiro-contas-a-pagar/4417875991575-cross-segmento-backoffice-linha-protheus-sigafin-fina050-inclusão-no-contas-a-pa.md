---
article_id: 4417875991575
category: Financeiro - Contas a Pagar
content_hash: cd471515238efa4cc401ca97422edd89ddfdc5a6d9bddbbedbaca3e3e1e30ed5
fetched_at: '2026-06-28T22:38:08.217469+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA050 - Inclusão no
  Contas a Pagar  HELP F050VLDAPR
type: support-article
updated_at: '2023-01-25T22:33:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4417875991575-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA050-Inclus%C3%A3o-no-Contas-a-Pagar-HELP-F050VLDAPR
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:02:00 min****Ocorrência:**No módulo Financeiro FINA050 ao incluir titulo no Contas a Pagar ao finalizar da a mensagem HELP F050VLDAPR

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4417875640343/mceclip0.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA050  - Todas as versões

**Causa**O parâmetro MV\_FINCTAL esta com conteúdo = 2, e nesse caso o sistema exige que campo **cod aprov**. seja preenchido.

**Solução**O parâmetro **MV\_FINCTAL,** existe opção para liberação de movimentos com base no formato de liberação simples ou alçada.  
1=Liberação Simples   
2=Alçada

**Importante**Com o parâmetro **MV\_FINCTAL** habilitado o controle de alçada, se faz necessário o preenchimento do aprovador (**E2\_CODAPRO**).  
  
**Saiba mais**[Cross Segmento BackOffice Linha Protheus - Como parametrizar os cadastros para que os títulos a pagar necessite de aprovação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024732031-Cross-Segmento-BackOffice-Linha-Protheus-Como-parametrizar-os-cadastros-para-que-os-t%C3%ADtulos-a-pagar-necessite-de-aprova%C3%A7%C3%A3o?source=search)
