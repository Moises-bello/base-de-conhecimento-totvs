---
content_hash: 5383d8fda960e21983a1ff7aa0192d2c95f5895265149a11c6d2e7560ba05594
fetched_at: '2026-06-28T21:35:17.714972+00:00'
page_id: '126714186'
product: fluig
source: tdn-fluig
title: Eventos Iniciais
type: documentation
url: https://tdn.totvs.com/display/fluig/Eventos+Iniciais
version: 11
---

# Evento Inicial de processo comum

É o tradicional evento que indica o inicio do processo. Ao selecionar este tipo de inicio de processo os usuários que tiverem a permissão para iniciar este processo poderão iniciar o mesmo através da tela de abertura de solicitações do Fluig. As permissões são definidas através do mecanismo de atribuição desta atividade. Para processos definidos como públicos qualquer usuário poderá abrir solicitações neste processo. Embora essa atividade inicial possa ser em conjunto com outros tipos de atividade inicial o fluig aceitará apenas uma única instância de objeto de início comum por diagrama.

# Evento inicial condicional

Este evento permite que uma nova solicitação workflow seja criada toda vez que um script condicional retornar verdadeiro em uma determinada faixa de tempo. Será necessário configurar um usuário de integração que será o usuário utilizado para abrir as solicitações. Ao liberar um processo que contenha um evento inicial condicional será criado no fluig uma atividade no agendador de tarefas que ficará a cargo da execução periódica do script condicional bem como da criação da solicitação caso as condições do script condicional sejam verdadeiras.

Mais detalhes sob como funciona e exemplos de uso podem ser encontrados no [artigo dedicado a](http://tdn.totvs.com/display/fluig/Scripts+Condicionais)[scripts condicionais](http://tdn.totvs.com/display/fluig/Scripts+Condicionais)[.](http://tdn.totvs.com/display/fluig/Scripts+Condicionais)

# Evento inicial de sinal

Este evento inicial deverá ser configurado para monitorar a emissão de determinado sinal . Quando o sinal que este evento estiver monitorando fora emitido por alguma atividade emissora de sinais uma nova solicitação workflow será aberta. Será necessário configurar um usuário de integração que será o usuário utilizado para abrir as solicitações. É possível utilizar mais de uma atividade inicial de sinal para monitorar a emissão de diferentes sinais . Contudo em um cenário de monitoramento de multiplos sinais é recomendado que seja utilizado o evento inicial múltiplo ou o evento inicial paralelo.

# Evento inicial temporizador

Permite a criação de solicitações workflow em uma determinada faixa de tempo. Será necessário configurar um usuário de integração que será o usuário utilizado para abrir as solicitações. Ao liberar um processo que contenha um evento inicial temporizador será criado no fluig uma atividade no agendador de tarefas que ficará a cargo da criação de solicitações periódicas para o processo.

ATENÇÃO

A tecnologia utilizada para a temporização das atividades reinicia seus contadores de tempo a partir de um determinado período definido pelo próprio tipo de tempo utilizado para definir o gatilho. Isso significa que não se pode utilizar períodos de tempo acima de 24 horas para se temporizar por horas, ou um período acima de 31 dias para se temporizar por dia. O contador reinicia toda 24 horas ou todo começo do mês. Isso também significa que ao se colocar um período de dias, como por exemplo 8 dias, o período irá reiniciar no dia primeiro e começará a contar a partir de então. Para mais informações: <http://quartz-scheduler.org/documentation/quartz-2.1.x/cookbook/BiDailyTrigger>.

 

# Evento inicial múltiplo

Permite iniciar uma solicitação workflow analisando periodicamente um conjunto de condições para que uma solicitação workflow seja aberta. Essas condições podem incluem um ou mais scripts condicionais bem como um ou mais sinais a serem monitorados. Caso algum script condicional tenha suas condições atendidas ou um dos sinais tenha sido emitido será aberta uma solicitação workflow para aquele processo. Será necessário configurar um usuário de integração que será o usuário utilizado para abrir as solicitações. Ao liberar um processo que contenha um evento inicial múltiplo será criado no fluig uma atividade no agendador de tarefas que ficará a cargo do monitoramento de sinais e scripts condicionais relacionados a esta atividade, bem como da abertura das solicitações caso uma das condições relacionadas se torne verdadeira.
