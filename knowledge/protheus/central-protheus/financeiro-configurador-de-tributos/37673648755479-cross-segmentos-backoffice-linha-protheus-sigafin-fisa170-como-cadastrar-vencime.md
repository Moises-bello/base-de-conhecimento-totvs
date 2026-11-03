---
article_id: 37673648755479
category: Financeiro - Configurador de Tributos
content_hash: bed90236787e222709ca3cbcd8dc43ac11d772c299519b3387870971ce38d2ae
fetched_at: '2026-06-28T22:37:46.193468+00:00'
product: protheus
section_id: 30946086151959
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FISA170 - Como cadastrar
  vencimento para quinzena subsequente?
type: support-article
updated_at: '2026-01-14T17:59:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37673648755479-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FISA170-Como-cadastrar-vencimento-para-quinzena-subsequente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37673679386007) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Como cadastrar vencimento para quinzena subsequente pelo configurador de tributos?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.2210  
  
**Solução**

**Importante**  
Para realizar este cadastro é necessário que o dicionário esteja atualizado, possuindo o campo **FKP\_DIAQUI (Dia Quinzena)** e o **FKP\_PRDVCT (Periodo Vct.)**tenha a opçõão 3 - Quinzenal.

Atualização de dicionário disponibilizada a partir da expedição de novembro/2025  
  
**REGRAS**

* Não será possível antecipar ou postergar o vencimento, será sempre considerado o ultimo ou primeiro dia util dentro da quinzena determinada.
* A data base para vencimento será utilizada apenas para vencimento de tributos com fato gerador na emissão, sempre que o tributo for gerado na baixa a data a ser considerada será a data em que a baixa esta sendo efetivada.
* Para definir se será na quinzena subsequente ou em mais quinzenas a frente pode ser utlizado o campo **Qtd. Periodos**, informar 1 para a quinzena subsequente, 2 para 2 quiznenas subsequentes ou mais caso necessário.

**1.1** Para esse cenário, crie a **regra de vencimento** considerando os campos indicados a seguir:

**Preenchimento dos campos**:  
Dia Vencto. = 0  
Tipo Vencto. = 2- Periodico   
Periodo Vct = 3 - Quinzenal   
Qtd. Periodo = 1  
Dia Quinzena = 2 - Ultimo dia útil

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37673679388183)

Após esse cadastro vincular a **Regra de Vencimento** na **Regra Financeira**  
  
Segue um exemplo pratico   
  
Se o pagamento for realizado entre 01/01 e 15/01 → recolhimento da retenção até 30/01  
Se o pagamento for realizado entre 16/01 e 31/01 → recolhimento da retenção até 13/02.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37673648737559)  
  
**Saiba mais:**

[Como cadastrar vencimento para quinzena subsequente?](https://tdn.totvs.com/pages/viewpage.action?pageId=1010811200)  
[Financeiro - Configurador de Tributos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/30946086151959-Financeiro-Configurador-de-Tributos)
