---
article_id: 360058187754
category: RH - Schedule (PONSCHEDULE)
content_hash: 642004de7d8ff327a57092f4fd6bc96c1a54bb740ae48769735154b9be16f3ec
fetched_at: '2026-06-28T22:44:42.657067+00:00'
product: protheus
section_id: 32419396129943
source: central-protheus
title: RH - Linha Protheus - PON -  Como cadastrar recorrência no agendamento de Leitura
  e Apontamento via Schedule
type: support-article
updated_at: '2025-06-13T18:46:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058187754-RH-Linha-Protheus-PON-Como-cadastrar-recorr%C3%AAncia-no-agendamento-de-Leitura-e-Apontamento-via-Schedule
---

**Dúvida**Como cadastrar recorrência no agendamento de Leitura e Apontamento via *Schedule*  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**Ao cadastrar a fórmula do U\_PONSCHEDULER no Configurador para leitura e apontamento de forma automática. há uma opção de recorrência e intervalo de recorrência.   
Nessa opção pode ser escolhido a recorrência que precisar para o *job "startar".*Exemplo:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098582374/mceclip0.png)​  
Nesse caso, cadastrei para todos os dias da semana, com intervalo de 04:00 entre uma e outra leitura, ou seja, com os seguintes horários de execução:  
00:00 - 04:00 - 08:00 - 12:00 - 16:00 - 20:00  
  
O Sistema vai tratar as marcações para ler corretamente, por causa da tabela RFB, pois o número de NSR das marcações posteriores sempre serão maiores que os já lidos.  
Segue uma documentação sobre a tabela RFB e sua funcionalidade:  
[Funcionalidade da tabela RFB e como controlar a leitura para que o NSR não ocasione erros no processo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016068372-MP-PON-Funcionalidade-da-tabela-RFB-e-como-controlar-a-leitura-para-que-o-NSR-n%C3%A3o-ocasione-erros-no-processo?source=search)
