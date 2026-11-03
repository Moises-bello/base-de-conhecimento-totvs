---
article_id: 5066808513559
category: Metrologia (SIGAQMT)
content_hash: 2e031cec6358fc5584a431d642134446c45f3c3e0be7e8992010ac1a0ae245b4
fetched_at: '2026-06-28T22:42:24.883742+00:00'
product: protheus
section_id: 360005876694
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQMT - QMTR130 - Não há dados a serem exibidos
type: support-article
updated_at: '2022-03-28T13:42:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5066808513559-Manufatura-Linha-Protheus-SIGAQMT-QMTR130-N%C3%A3o-h%C3%A1-dados-a-serem-exibidos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:40 min** **Ocorrência**No módulo **SIGAQMT - Metrologia**, ao tentar listar o relatório **QMTR130 - Disponibilidade** é exibida a mensagem **Não há dados a serem exibidos**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Metrologia (SIGAQMT) - Todas as versões  
  
**Causa**Essa mensagem ocorre quando o instrumento selecionado para listagem não possui determinadas informações preenchidas.  
 **Solução**O relatório somente irá listar os dados caso o instrumento em questão esteja com o campo **QM2\_NHORDI - No. Horas/Dias** preenchido no **QMTR010 - Cadastro do Instrumento** e o campo **QM6\_TOTHOR - Tot. Horas** informado quando realizada a calibração na rotina **QMTR140 - Medições**.
