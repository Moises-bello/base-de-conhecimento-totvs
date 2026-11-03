---
article_id: 23081711200023
category: Faturamento - Cadastros
content_hash: 8b528591dc806835779e77326dcfcdff552e45758c7d02354ce5ea5e3fb46910
fetched_at: '2026-06-28T22:38:35.453807+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Envio de e-mail automático
  (por Schedule) em relatórios do Faturamento
type: support-article
updated_at: '2024-04-26T17:23:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23081711200023-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Envio-de-e-mail-autom%C3%A1tico-por-Schedule-em-relat%C3%B3rios-do-Faturamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23081726250903) Tempo aproximado para leitura: **00:02:30 min** **Dúvida**Como realizar o envio de e-mail automático (por Schedule) em relatórios do Faturamento?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**1 - Configure o envio de emails por autenticação.

> Se precisar de apoio nessa parte, oriento que contate a Equipe Framework!

 

2 - Vá no Configurador > Ambiente > Schedule > Realize a inclusão do agendamento:

![](https://totvssuporte.zendesk.com/attachments/token/JJh6ERoB59QgPuolJdpy7dWoa/?name=image.png)

3 - Realize um JOB no Schedule assim do nome técnico do relatório desejado (no exemplo é MATR020), com a recorrência desejada, informando no campo "Email" o email configurado no passo 1:

> ![](https://totvssuporte.zendesk.com/attachments/token/GE6mfupLFuk4YLEBGvhMz3h9U/?name=image.png)![](https://totvssuporte.zendesk.com/attachments/token/oaVxMmsK1lotCR228HVcctoRH/?name=image.png)

   
4 - Ative o Agent e o Schedule no Configurador

> Se precisar de apoio nessa parte, oriento que contate a Equipe Framework!

### 

Resultado no email configurado no passo 1, com a recorrência programada disparará um email de tempos em tempos após a iniciação do passo 4:

> ![](https://totvssuporte.zendesk.com/attachments/token/su3cgw2ZIV9kE4C6sls2ys2Ty/?name=image.png)
