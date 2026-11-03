---
content_hash: cf175bf30e828714307bb88954d98ae0ac768d2c548188b032d818908e9b887a
fetched_at: '2026-06-29T00:09:38.108364+00:00'
page_id: '425918479'
product: rm
source: tdn-rm
title: Envio de Email
type: documentation
url: https://tdn.totvs.com/display/LRM/Envio+de+Email
version: 1
---

**Envio de Email**   
O serviço de "Envio de E-mail" permite encaminhar os e-mails de acompanhamento durante a execução de ações no sistema, como por exemplo, Repasse Atendimento, Avançar Etapa, Cancelar Atendimento, Conclusão, entre outros.   
O formato do e-mail pode ser configurado através dos Parâmetros do RM Agilis (Opções | Parâmetros | RM Agilis | Parâmetros de Controle | Enviar e-mails de notificações no formato texto) sendo: Texto (marcando a opção) ou HTML (desmarcando a opção).  
Este serviço funciona transformando os registros da tabela responsável em e-mails de acordo com uma determinada periodicidade. Os e-mails enviados com sucesso têm seu registro apagado na tabela e são encaminhados aos seus destinatários e os registros que apresentaram erros são mantidos para que possam ser processados posteriormente. Este procedimento terá o prazo de trinta dias, após este período os registros serão excluídos da tabela. Os logs de "envio" ou "falha do envio" dos e-mails são gravados no Gerenciador de JOBS.  
É possível controlar quando este serviço será executado:  
Hora de execução (1ª execução)  
Agora = Executa o processo uma única vez e imediatamente na data corrente.  
Executar em = Executa o processo uma única vez e na data e hora especificada. Essa opção possui como padrão a data corrente do dia sendo possível alterá-la.  
Sob demanda = Executa o processo de acordo com o recebimento dos e-mails.  
Repetir a execução  
Deve ser utilizada quando houver a necessidade de executar o processo de forma recorrente. Ela apresenta as seguintes opções:  
• Semanal - Todas as semanas no mesmo horário e no(s) dia(s) de acordo com o definido.   
• Mensal - Todos os meses, no mesmo horário e no(s) dia(s) de acordo com o definido.  
• Diário - Diariamente, a cada intervalo (em horas) de acordo com o definido.  
**Observação**  
Para habilitar esta opção é necessário que a Hora da execução (1ª execução) esteja marcada como "Executar em".
