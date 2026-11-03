---
content_hash: a0d51523dc9f3a184b6db73e68056b5191784576b3b81bea75500e5296c8a888
fetched_at: '2026-06-29T00:09:37.863693+00:00'
page_id: '425459636'
product: rm
source: tdn-rm
title: Alarmar atendimentos
type: documentation
url: https://tdn.totvs.com/display/LRM/Alarmar+atendimentos
version: 3
---

**Alarmar atendimentos**   
O serviço de alarme é utilizado para alertar (via e-mail) ao superior imediato sobre a situação dos atendimentos de seus subordinados que estão com prazos vencidos. O serviço também destaca na tela de visão do atendente responsável os atendimentos em atraso.   
É um recurso extremamente útil nas avaliações de entregas em atraso que podem impactar no resultado final do projeto além de evitar que as solicitações (atendimentos) fiquem sem resposta ou ultrapassem a data limite. Facilitando assim a renegociação com clientes, dependências de terceiros, resolução de problemas e  tomadas de decisão e suas conseqüências (replanejamentos, alterações no cronograma, a alocação de mais recursos entre outros).  
O alarme é um pode ser executado de forma única ou recorrente:  
**Hora de execução (1ª execução)**  
Executar o processo uma única vez e imediatamente na data corrente.  
**Executar o processo uma única vez em uma data e hora especifica de acordo com a data e hora escolhida.**   
Essa opção vem com a data corrente do dia como padrão, sendo possível alterá-la.  
**Sob demanda**  
Repetir a execução.  
Para habilitar esta opção é necessário informar a data e hora para 1ª execução.  
Deseja executar o processo de forma recorrente onde será apresentado ao usuário as seguintes opções de recorrência:  
• Semanal - Todas as semanas no mesmo horário e no(s) dia(s) definido(s) pelo usuário.   
• Mensal - Todos os meses, no mesmo horário e no dia definido pelo usuário.  
• Diária - Diariamente, a cada intervalo (em horas) definido pelo usuário.  
   
O serviço de Alarme pode ser dividido em Alarme e Alarme Avançado:  
   
**Alarme**   
   
A parametrização é utilizada para configurar em quanto tempo o atendimento passará a ser considerado alarmado e envolve três características e três condições.  
• Status (Em Andamento, Agendado a responder, Agendado respondido, Concluído a responder, Concluído respondido, Despertado, Aguardando Terceiros, Concluído confirmado, Concluído automático, Cancelado).  
• Classificação (Cadastro aberto ao cliente);  
• Prioridade (Baixa, Normal, Alta, Urgente).  
O tempo pode ser definido em horas ou minutos.  
Condições:  
• Número de Horas/Minutos em aberto com o responsável atual: número de horas/minutos em que um atendimento com o status 'Em andamento' pode ficar com o mesmo atendente. Vencendo este prazo, o alarme será disparado.  
• Tempo máximo de resposta: número total de horas/minutos em que um atendimento pode ficar sem ser concluído (totalmente finalizada), ou seja, com status 'Em Andamento'.  
• Prazo Limite: se o campo prazo limite estiver preenchido no atendimento e o mesmo vencer, também será disparado o alarme.  
Para os atendimentos que atendam aos parâmetros de Status, Classificação, Prioridade e qualquer uma das condições, é gerado um alarme.  
Os atendimentos que forem repassados fora do horário de serviço do atendente não irão alarmar no mesmo dia, mesmo se atender aos parâmetros de configuração, porque o sistema checa o horário que o atendimento foi repassado e não gera o alarme. Este processo é realizado para o próximo dia útil.  
Exemplo  
Atendimento 'Em andamento' de classificação 'Solicitações em geral' e prioridade 'Normal' irá alarmar se o número de dias com o mesmo atendente ultrapassar 2 dias OU o número de dias para a conclusão ultrapassar 3 dias OU o prazo limite definido no atendimento estiver vencido.   
A parametrização seria como a abaixo:  
• Status: Em andamento.  
• Classificação: Solicitações em geral.  
• Prioridade: Normal.  
• Número de Horas/Minutos em aberto: 2 dias.  
• Tempo máximo: 3 dias.  
• Prazo Limite: sim (alarmar caso o prazo limite esteja vencido).  
Vale ressaltar que o sistema considera o tempo útil considerado para o alarme é igual a 8 horas diárias.  
O e-mail encaminhado para o chefe do atendente sobre os atendimentos alarmados possuem as informações:  
• Atendentes que tiveram seus atendimentos alarmados, quantidade de alarmes, número de alarmes dos subordinados, e os subordinados com mais alarmes.  
• Resumo dos atendimentos alarmados por atendente e chefe do atendente. Este resumo contém o código do atendimento, o cliente, classificação, prioridade, prazo limite e uma parte da solicitação.  
o sistema agrupa todos os atendimentos a alarmar para um determinado superior (todos os atendimentos de seus subordinados que tem atendimento a alarmar) e monta um único e-mail.  
Para cada atendimento será apresentado o código , informações sobre o atendente que abriu o atendimento (Código , Nome , Email , Ramal) , informações sobre o cliente do atendimentos (Código , Nome e Tipo do Cliente.) e outras informações relevantes do atendimento (Etapa  , Status , Classificação , Prioridade , Abertura , Prazo Limite , Solicitação).  
   
**Alarme Avançado**  
   
O Alarme Avançado é um complemento do Alarme. Através dele é possível parametrizar critérios variados, diferentemente dos fixos estipulados no primeiro alarme. O objetivo continua sendo alertar o supervisor imediato dos atendimentos que extrapolaram as datas de entregas ou limites.  
Essa  funcionalidade possui  como critérios para configuração, a quantidade de dias que o atendimento se encontra em uma determinada combinação de campos , onde esses campos serão os campos do atendimento (Obs. Exceto os campos de texto livre Assunto , Solicitação , Discussão , Solução) , incluindo os parâmetros (Obs: Exceto os parâmetros do tipo String e Texto).  
Dessa forma é disponibilizado ao administrador do sistema  maior flexibilidade para montar condições de alarme de acordo com os processos da empresa.  
Para  configurar a parametrização do alarme podem ser criados várias condições semelhantes considerando também o tempo. Para cadastrar basta indicar os campos:  
IDALARME – Preenchido automaticamente pelo sistema.  
DESCRIÇÃO – Descrição para o alarme.  
DIASEMABERTO - Número de Horas/Minutos em aberto com o responsável atual: número de horas/minutos em que um atendimento com o status 'Em andamento' pode ficar com o mesmo atendente. Vencendo este prazo, o alarme será disparado.  
PRAZOAUTORIZADO - número total de horas/minutos em que um atendimento pode ficar sem ser concluído (totalmente finalizada), ou seja, com status 'Em Andamento'.  
LIMITEVENCIDO - se o campo prazo limite estiver preenchido no atendimento e o mesmo vencer, também será disparado o alarme.  
Os campos Descrição ,  Dias em Aberto , Prazo Autorizado são de caráter obrigatório, por esse motivo a condição não é salva caso não seja preenchido corretamente.  
**(Botão) Definições do Alarme**  
Através deste botão é possível escolher os campos e seus respectivos valores para retornar os atendimentos que irão alarmar.  A coluna campo retorna campos visíveis na tela de atendimento, desde que não seja do tipo texto (como por exemplo: Assunto , Solicitação , Discussão , Solução , Parâmetros do tipo String e Texto).  
A inclusão de uma nova condição pelo menos um campo deverá ser escolhido, caso contrário uma mensagem de advertência será apresentada e na exclusão de registros, o sistema considera os campos que possuem dependência entre si.   
Ex.: Os campos da condição são: Grupo e Tipo de Atendimento. Ao excluir o grupo, automaticamente o tipo será deletado porque um depende do outro.  
Isto ocorrerá para os campos:  
Grupo de Atendimento - Tipo de Atendimento - Local de entrega . O tipo de atendimento irá influenciar nos parametros. Produto - Detalhe do Produto Código do Cliente - Contato do Cliente Representante - Contato do Representante  
Quaisquer alterações, o sistema apresenta mensagem de alerta solicitando confirmação para salvar ou cancelar a alteração, para que seja devidamente gravado.

Caso o usuário tente criar um critério sem sua respectiva dependência, uma mensagem é exibida informando sobre tal necessidade.

   
**E-mail de Atendimentos Alarmados**  
   
No TOTVS Aprovações e Atendimento, os atendimentos que não forem concluídos dentro de um período de tempo definido podem alarmar. Quando isso ocorre, um e-mail é enviado para o chefe do atendente que está com o atendimento em questão.  
   
Visando facilitar o controle e o gerenciamento por parte dos gestores, assim como a tomada de decisões, estão disponíveis no corpo do e-mail, informações referentes ao atendente e ao atendimento.   
   
Para o atendente alarmado constarão informações referentes ao código, o nome, o ramal e o e-mail.  
   
Para cada atendimento alarmado, além do código do mesmo, serão apresentadas informações sobre:

* o atendente que abriu o atendimento (código, nome, email, ramal)
* o cliente do atendimento (código, nome, tipo do cliente)
* o atendimento (etapa, status, classificação, prioridade, abertura, prazo limite, solicitação)  
     
  As informações contidas no corpo do e-mail serão as mesmas tanto para envio de e-mail HTML quanto para Texto.
