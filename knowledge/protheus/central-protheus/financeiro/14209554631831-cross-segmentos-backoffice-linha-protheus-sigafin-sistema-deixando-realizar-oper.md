---
article_id: 14209554631831
category: Financeiro
content_hash: 2ae21e814a7b28b9b983f656188f6dba9c5ee284b7881f0847f848340763e89f
fetched_at: '2026-06-28T22:38:01.007845+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Sistema deixando realizar
  operações de inclusão e baixa de títulos mesmo com calendário contábil bloqueado
  e não apresentando o Help: CTBBLOQ'
type: support-article
updated_at: '2025-11-26T17:52:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14209554631831-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Sistema-deixando-realizar-opera%C3%A7%C3%B5es-de-inclus%C3%A3o-e-baixa-de-t%C3%ADtulos-mesmo-com-calend%C3%A1rio-cont%C3%A1bil-bloqueado-e-n%C3%A3o-apresentando-o-Help-CTBBLOQ
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32753322307095) Tempo aproximado para leitura: **00:20:00 min**  
  
**Dúvida**  
Mesmo com Calendário Contábil Bloqueado é possível excluir títulos do Financeiro?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Financeiro - Todas as versões  
  
**Solução**  
Além de estar com o calendário bloqueado no período em questão, é **obrigatório** estar com o parâmetro com o conteúdo

**MV\_BXDTFIN = 2**

Dessa forma, no momento da inclusão ou baixa de títulos no módulo financeiro, a operação será bloqueada e a seguinte mensagem será exibida (exemplo):

Help: CTBBLOQ   
Problema: Calendário Contábil Bloqueado. Verfique o processo.  
Filial: Período: 01/09/2025 / 30/09/2025

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36604310981143)

**Exemplo:**

**Logado no sistema no ano de 2024**

Vamos supor que fiz uma compensação pela rotina "FINA330 compensação contas a receber" no ano 2024 contabilizando a operação pelo lançamento padrão LP 596, que registrou a contabilização na tabela CT2 ou na rotina "CTBA102 - Lançamento Contábil Automático"

E fiz o procedimento de bloqueio do calendário contábil do ano 2024 seguindo os processos da documentação

[CTBA010 - Calendário contábil bloqueado ou fechado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006722952-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA010-Calend%C3%A1rio-cont%C3%A1bil-bloqueado-ou-fechado)

**Logado no sistema  no ano de 2025 (**onde o ano de 2025 não está com o calendário contábil bloqueado, somente o ano de 2024**)**

Na rotina "FINA330 compensação contas a receber"

**a)** Caso eu faça o "**estorno / cancelamento**" da compensação, o sistema irá deixar o estorno ser realizado (sem efetuar nenhum tipo de bloqueio), já que a contabilização está ocorrendo em data logada, ano de 2025.

**b)** Caso eu faça o "**exclusão**" da compensação, o sistema irá bloquear a operação de exclusão apresentando o Help abaixo:

"CTBBLOQ  - Problema: Calendário Contábil Bloqueado. Verifique o processo."

Esse bloqueio/Help somente irá ter efeito caso o parâmetro esteja com o conteúdo **MV\_BXDTFIN = 2**

Caso o parâmetro esteja com o conteúdo **MV\_BXDTFIN = 1** a exclusão será realizada sem nenhum tipo de bloqueio

Saiba mais:

[SIGAFIN - Qual a funcionalidade do Bloqueio por Processo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/25977474343959-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Qual-a-funcionalidade-do-Bloqueio-por-Processo)

[FINA070 - Com o calendário contábil bloqueado está sendo possível realizar baixas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14154912852247-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA070-Com-o-calend%C3%A1rio-cont%C3%A1bil-bloqueado-est%C3%A1-sendo-poss%C3%ADvel-realizar-baixas)
