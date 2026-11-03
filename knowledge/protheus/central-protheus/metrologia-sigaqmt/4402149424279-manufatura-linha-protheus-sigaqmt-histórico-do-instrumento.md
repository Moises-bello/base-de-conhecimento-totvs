---
article_id: 4402149424279
category: Metrologia (SIGAQMT)
content_hash: 00eb0efc5a170ad92cbaa20263eb09219c7715106b95d8779ef72eb3158711ce
fetched_at: '2026-06-28T22:42:24.804237+00:00'
product: protheus
section_id: 360005876694
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQMT - Histórico do instrumento
type: support-article
updated_at: '2021-06-08T13:16:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402149424279-Manufatura-Linha-Protheus-SIGAQMT-Hist%C3%B3rico-do-instrumento
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:00:45 min**  
**Dúvida**Em qual tabela e campo é registrado o histórico do instrumento registrado em **Outras Ações/Textos/Históricos** da rotina **QMTA010 - Instrumentos**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Metrologia (SIGAQMT) - Versão 12  
  
**Solução**O histórico do instrumento é registrado na tabela **QA2 - Textos Gerais do Módulo Qualidade**, no campo **QA2\_TEXTO - Linha**. Este campo permite a inclusão de um texto de até 75 caracteres.  
Cada linha inserida no histórico é registrada na tabela **QA2** com um sequencial diferente, ou seja, cada linha permite até 75 caracteres.  
O relacionamento da tabela **QA2** com o instrumento é feito por meio do campo **QA2\_CHAVE - Chave** e **QM2\_CHAVE - Chave**.
