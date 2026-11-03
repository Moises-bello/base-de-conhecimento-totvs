---
article_id: 1500003943201
category: Inspeção de Processos (SIGAQIP)
content_hash: 5909c5c65b01137991f9994406537ff3dec690f202e0ef22319bb91ccd51087f
fetched_at: '2026-06-28T22:42:25.768152+00:00'
product: protheus
section_id: 360005906153
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIP - Help QA_CPOOBR exibido na rotina QIPA010
type: support-article
updated_at: '2021-10-01T13:13:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003943201-Manufatura-Linha-Protheus-SIGAQIP-Help-QA-CPOOBR-exibido-na-rotina-QIPA010
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:00 min**  
**Ocorrência**No módulo **SIGAQIP - Inspeção de Processos**, ao relacionar um ensaio para a especificação, ocorre o *help* **QA\_CPOOBR**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Processos (SIGAQIP) - Versão 12  
  
**Causa**O *help* **QA\_CPOOBR** ocorre quando o ensaio utilizado na especificação é do tipo calculado, e neste caso, é obrigatório informar a fórmula no campo **Fórmula** da rotina **QIPA010 - Especificação do Produto**.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Verifique na rotina **QIPA020 - Ensaios** se o ensaio está definido como **D-Digitado** ou **C-Calculado.** Esta informação consta no campo **Resultado** desta rotina;  
2. Para ensaio do tipo **C-Calculado** é obrigatório informar a fórmula a ser utilizada no campo **Fórmula** da rotina **QIPA010**.  
  
**Saiba mais**  
Para mais informações referente à montagem da fórmula, consulte o [Help On-Line](https://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/qipa010_formulas.htm).
