---
article_id: 31232670267031
category: Avisos Automáticos
content_hash: 4ba03c16984d8842731b96b13409a9f8416040773c7077b0ac8d563d561d0f7b
fetched_at: '2026-06-28T22:46:40.515769+00:00'
product: rm
section_id: 31224122282519
source: central-rm
title: RH - RM - FOP - Como funciona o aviso automático Tipo 1 - Escala de Férias?
type: support-article
updated_at: '2025-04-08T18:06:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31232670267031-RH-RM-FOP-Como-funciona-o-aviso-autom%C3%A1tico-Tipo-1-Escala-de-F%C3%A9rias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31232670247959) Tempo aproximado para leitura: **00:02:16 min** **Dúvida**Como funciona o envio de avisos automáticos do tipo Escala de Férias?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**

Será enviado um aviso automático pelo RM toda vez que um (ou mais) funcionários estiverem para tirar férias (início de gozo próximo).

Este aviso tem como finalidade notificar os chefes da devida falta que aquele funcionário possa fazer e possivelmente, providenciar mudanças estruturais para minimizar o impacto (caso necessário). O número de dias de antecedência que será enviado o aviso é controlado pelo Nro. Dias Referência.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31232700321815)

No exemplo abaixo será considerada a data atual em **13/03/2025**, e a **data início de gozo** do colaborador é **14/03/2025** **(Férias marcadas).**

Neste cenário, o campo **Nro. Dias Ref.:** do Aviso Automático foi preenchido com o valor 1, nesse caso será enviado um dia antes do do início de gozo das férias.![](https://centraldeatendimento.totvs.com/hc/article_attachments/31232670251671)

Será enviado o e-mail informando o período de gozo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31232700323223)

**Importante**

Para executar a rotina automaticamente, deverá ser realizado o Agendamento de Job no ambiente conforme as orientações da documentação [Como agendar a execução de um processo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005088792-Framework-Linha-RM-Frame-Como-agendar-a-execu%C3%A7%C3%A3o-de-um-processo)
