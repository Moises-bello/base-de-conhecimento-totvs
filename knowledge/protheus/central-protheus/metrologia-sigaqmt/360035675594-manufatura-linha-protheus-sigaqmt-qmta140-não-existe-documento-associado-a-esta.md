---
article_id: 360035675594
category: Metrologia (SIGAQMT)
content_hash: 134824e4f6c7d12eaefe054f40bdd04b58c5b72e402d6f50c1a6be9debc70b72
fetched_at: '2026-06-28T22:42:24.855719+00:00'
product: protheus
section_id: 360005876694
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQMT - QMTA140 - Não existe documento associado
  a esta Calibração
type: support-article
updated_at: '2021-08-10T18:45:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035675594-Manufatura-Linha-Protheus-SIGAQMT-QMTA140-N%C3%A3o-existe-documento-associado-a-esta-Calibra%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:15 min**  
**Ocorrência**No módulo **SIGAQMT - Metrologia**, ao tentar visualizar o documento na rotina **QMTA140 - Medições** ocorre a mensagem **Nao existe documento associado a esta Calibracao**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Metrologia (SIGAQMT) - Todas as versões  
  
**Causa**Essa mensagem ocorre na opção **Visual.Docto** da rotina **QMTA140** quando o instrumento selecionado não está relacionado à um documento e pode ocorrer em todas as rotinas que possuem a opção **Visual.Docto**, assim como nas rotinas **QMTA010 - Instrumentos** e **QMTA140**.  
  
**Solução**Para relacionar um instrumento à um documento deverá:

* cadastre um procedimento de medição na rotina **QMTA052 - Procedimento Medição** e informe um documento no campo **Cod. Docto**;
* relacione uma família à este procedimento de medição na rotina **QMTA030 - Família de Instrumentos**;
* no cadastro de instrumento da rotina **QMTA010**, relacione esta família;
* e na rotina de **QMTA140**, realize a calibração do instrumento para então em **Outras Ações/Visual. Docto**, visualizar o documento relacionado.
