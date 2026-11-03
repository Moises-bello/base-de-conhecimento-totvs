---
article_id: 1500003845262
category: Metrologia (SIGAQMT)
content_hash: d5ccf92c4ebfdda85c0d7b863bf787d68af500b0da081d349a57b511b8574bae
fetched_at: '2026-06-28T22:42:24.866734+00:00'
product: protheus
section_id: 360005876694
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQMT - QMTA140 - Padrões Secundários Não Encontrados
type: support-article
updated_at: '2021-12-23T18:47:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003845262-Manufatura-Linha-Protheus-SIGAQMT-QMTA140-Padr%C3%B5es-Secund%C3%A1rios-N%C3%A3o-Encontrados
---

***![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:00 min**  
**Ocorrência**No módulo **SIGAQMT - Metrologia**, ao realizar a calibração de um instrumento na rotina **QMTA140 - Medições** na aba **Inst. Utilizados** ocorre a mensagem **Padrões Secundários Não Encontrados**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Metrologia (SIGAQMT) - Todas as versões  
  
**Causa**Essa mensagem pode ocorrer em duas situações:

* Quando não existe padrão secundário relacionado à faixa utilizada no instrumento ou;
* Quando a data de validade da frequência de calibração do instrumento informado é maior do que a data base, ou seja, a data em que está sendo realizada a calibração do instrumento principal.

**Solução**Para solucionar esta mensagem, verifique:

* Se existe padrão secundário relacionado à faixa na rotina **QMTA040 - Faixas** em **Outras Ações/Padrões/Secundário**;
* Se a data de validade da frequência de calibração no campo **Val. Calibr.** da rotina **QMTA010 - Instrumentos** do instrumento que está sendo informado na aba **Inst. Utilizados** da rotina **QMTA140** é anterior à data base, data em que está sendo realizada a nova calibração.
