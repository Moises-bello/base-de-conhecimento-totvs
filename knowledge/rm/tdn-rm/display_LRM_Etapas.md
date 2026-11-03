---
content_hash: 2f6bcc1250275a896db6f7762b37cd6bf6180bae4f9da5af5d3de4d090aeb4a0
fetched_at: '2026-06-29T00:09:36.786628+00:00'
page_id: '425459520'
product: rm
source: tdn-rm
title: Etapas
type: documentation
url: https://tdn.totvs.com/display/LRM/Etapas
version: 97
---

**Etapas**   
As etapas são fases que o atendimento possui juntamente com atividades que devem ser realizadas em cada uma delas, para que seja concluído o objetivo que originou a abertura do atendimento. As etapas podem ter um tempo de duração provável e sua ordem de criação deve ser parametrizada para facilitar sua visualização na tela de visão. Elas têm como cadastro Pai o Tipo de Atendimento e podem ser vinculadas a tipos de repasse, ações pré-determinadas, campos, fórmulas entre outros.  
A primeira etapa do fluxo deve ser marcada para que o processo seja utilizado com sucesso, do contrário nenhuma ação será realizada. A partir da versão 11.60, o fluxo pode ter várias primeiras etapas, visando que o mesmo tipo de atendimento possa ter diferentes pontos de entradas.  
   
**Entrada Padrão = Antiga Primeira Etapa de um Possível fluxo.**  
Serve para marcar qual é  a "primeira etapa oficial" do tipo de atendimento.  É de caráter obrigatório e somente uma etapa pode possuir esta flag marcada. Na tentativa de marcar mais de uma etapa como entrada padrão, o sistema emite uma mensagem de alerta informando que este procedimento não pode ser realizado.  
   
**Primeira Etapa de um possível fluxo = Já existente no sistema, mas seu funcionamento foi alterado.**  
Serve para marcar quais etapas do tipo de atendimento também servirão com pontos de entrada para o fluxo, sendo que várias etapas podem ser marcadas.  
Para os fluxos que possuam somente um ponto de entrada, o sistema apresentará durante o processo de avanço de etapas somente as informações relativas ao processo e para os fluxos que possuam vários pontos de entrada, o sistema apresentará uma lista de todos os pontos de entrada (entrada padrão e possíveis entradas) para que a escolha da etapa inicial seja realizada.  
Através deve processo, após contato com o cliente e confirmado que a solução atende a solicitação, a conclusão do atendimento pode ser feita. Com isto o sistema irá alterar o status do atendimento para concluído confirmado. Existe a particularidade em que se o cliente demorar mais que X dias (X = número de dias que pode ser configurado pelos parâmetros do sistema) para confirmar uma conclusão então o sistema coloca o atendimento como concluído automático. Caso o cliente não concorde com a solução, o atendimento pode ser colocado "Em Andamento" ou então este atendimento é concluído e novo atendimento(nova solicitação) é aberto.  
Exemplo: Existe a necessidade de alterar a unidade de trabalho do atendente, com isso haverá modificações nos dados do funcionário no sistema e inclusive informações referentes ao vale transporte. A mesma solicitação "Mudança de Unidade de Trabalho do Atendente " pode ser feita de duas formas:

1ª - O atendente solicita a troca de unidade.  
O pedido é aberto e será avaliado pelos supervisores podendo ser atendido ou não. O responsável pela análise irá averiguar sobre a necessidade da troca, o motivo e se a mesma não prejudicará no andamento dos processos da empresa.  
2ª - O supervisor solicita a troca de unidade do atendente.  
O supervisor verifica a necessidade de trocar o atendente de unidade por motivos estratégicos ou financeiros (redução de custos na empresa, por exemplo) e não há necessidade de avaliação. Os documentos necessários são enviados, a autorização é feita e a solicitação apenas aguarda liberação.  
   
  
   
Os tipos de repasses que podem ser encontrados na etapa são:

* **Atendente**: O atendimento será encaminhado ao atendente selecionado para dar continuidades nas tarefas, entretanto a Coligada, Localidade e o Atendente Inicial da Tarefa devem ser definidos.
* **Grupo**: O atendimento será encaminhado para um grupo de atendentes que também possui tipo de repasse pré-determinado (Para um atendente fixo do grupo, Por rodízio entre os Atendentes do Grupo, Para o Atendente do Grupo com Menor número de Atendimentos e Para uma fila).  
  Mostrar atendentes do grupo  
  No avanço de etapas, caso esta opção esteja marcada será possível selecionar o atendente e repassar o atendimento diretamente, caso o campo fique em branco o processo seguirá o fluxo normalmente.
* **Fórmula**: O atendimento será repassado para um atendente ou um grupo de atendentes de acordo com a elaboração da fórmula.   
  Para que o atendimento seja repassado para um atendente à fórmula deve retornar o número da coligada e o código do atendente separado por ponto e vírgula (entre aspas duplas, conforme o exemplo abaixo:  
  Ex.: "1; 9" - onde 1 é o código da coligada e 9 é o código do atendente.  
  Para que o atendimento seja repassado para um grupo de pessoas a fórmula deve retornar o código do grupo de atendentes entre aspas, conforme o exemplo abaixo:  
  Ex. "4"- onde 4 é o código do grupo do atendente.

          É possível usar sentenças SQL do sistema em fórmula para diversos fins, seja recuperar um campo de outra tabela para usar no atendimento, ou buscar alguma informação externa para decidir que fluxo o atendimento deve seguir, isso é feito com as funções de fórmula EXECSQL e RESULTSQL, mas é importante destacar que é possível ainda usar o resultado de outra fórmula para filtrar uma sentença SQL, isso é especialmente útil para recuperar informação de tabelas que se relacionam com o atendimento de alguma forma, segue abaixo os passos de um exemplo de como buscar informações do movimento associado a um atendimento usando esse recurso:

1 - Criar 3 fórmulas, uma para cada campo chave da tabela de atendimento

2 - Criar um sentença SQL que utilize essas fórmulas, a anotação para isso é :FRM\_COIGODAFORMULA, para usar por exemplo a fórmula que retorna o código do atendimento previamente criada, seria :FRM\_CODATEND, segue abaixo um exemplo da SQL que busca dados do atendimento usando essas fórmula:

3 - Agora podemos usar nossa SQL em qualquer fórmula de algum atendimento que estiver relacionado a um movimento da seguinte forma:

A fórmula **AVANCARETAPAATENDIMENTO** retorna o valor **-8888** ao ser executada. Esse valor é importante pois é o que indica ao sistema que houve um avanço de etapa na fórmula.

Para garantir que uma fórmula retorne esse valor, ela deve estar no seguinte formato:

1 - Primeira linha da formula:

DECL RESULT;

2 - Linha em que está o avanço de etapa:

SETVAR(RESULT, AVANCARETAPAATENDIMENTO(VALOR\_ETAPA));

3 - Última linha da fórmula:

RESULT;

Segue abaixo um exemplo completo:

Observem que após testar, o resultado apresenta o valor esperado.

**Importante**: Seguem algumas recomendações quanto ao uso de fórmula no avanço de etapas

* Uma fórmula NUNCA deve usar a função AVANCARETAPAATENDIMENTO para avançar para ela mesmo, isso sempre ira causar erro.
* Para fórmulas configuradas em Avanço de Etapa, a função ALTERACAMPOSATENDIMENTO NUNCA deve ser utilizada para alterar código do atendente ou atendente responsável, pois isso pode fazer com que as regras do sistema para montar o histórico de etapas e repasse fiquem distorcidas.
* Para fórmulas configuradas em Avanço de Etapa, não é recomendado usar as funções REPASSARATENDIMENTO e REPASSARATENDPARAGRUPO. Essas funções foram projetadas para uso no serviço de 'Movimentar atendimentos por fórmulas' e o motivo disso é que em um avanço de etapas com fórmula, o sistema espera que a fórmula retorne pra ele o atendente ou grupo para o qual tal repasse deve ser feito, e usar essas funções faz com que o repasse ocorra fora do processo normal do sistema, o que pode trazer resultados incorretos especialmente nos históricos de etapas e repasses.

Segue abaixo um modelo para adaptar uma fórmula que hoje usa as funções que não devem ser usadas, no modelo recomendado:

DECL ATENDENTE;//Inicio da formula  
...  
SETVAR(ATENDENTE, CONCATENA(COLIGADACORRENTE,5,';'));//Mesma linha do REPASSAR substituindo o 5 pelo primeiro argumento da função REPASSAR atual  
ENVIAEMAILREPASSE('', EMAILDESTINATARIO, '', ATENDENTE);//Essa linha somente é necessária caso o usuário deseje enviar o email de repasse para algum outro atendente além do de destino  
...  
RETURN ATENDENTE;//Fim da fórmula

Obs: Pode ser necessário retirar o RETURN da ultima linha dependendo da fórmula, o importante é que o retorno da fórmula acima seja '1;5'

* **Manter com atendente atual**: Todas as outras opções são desabilitadas e o atendimento continua com o mesmo atendente que estava ao entrar nessa etapa.  
  **Template de E-mail:** têm por objetivo permitir que particularidades de cada tipo de atendimento seja tratado com precisão e maior controle do tráfego de informações que são enviadas no e-mail. Relatórios personalizados podem ser utilizados para apresentar as informações necessárias. Esta funcionalidade trabalha em conjunto à parametrização geral do sistema e respeita as regras:  
    
  E-mail de Repasse/Avançar Etapa:

* Etapa do Tipo de Atendimento: Busca o modelo de e-mail da próxima etapa.
* Tipo do Atendimento: Busca o modelo de e-mail do tipo de atendimento que a etapa pertence.
* Parâmetros do Agilis/Fixo: Busca o modelo de e-mail dos parâmetros gerais do sistema, caso não esteja preenchido busca do modelo fixo do sistema.

**Fórmula Visual para Executar Instruções Customizadas:**

A fórmula visual é uma funcionalidade global que permite customizar instruções (como por exemplo: envio de e-mails, com ou sem dados do atendimento, criação de lançamentos entre outros). O atendimento executa as instruções quando atingir a etapa especificada, mas todas as ações já existentes continuam sendo executadas normalmente (ações do atendimento, envio de e-mail, histórico de repasse etc).

Todas as validações de regras sobre os processos devem ser realizados para que ação seja realizada corretamente.

**Campos Obrigatórios**  
   
Os campos selecionados devem ser preenchidos na etapa atual do atendimento para que o mesmo possa  avançar para a próxima etapa, ou seja, o preenchimento dos campos obrigatórios é uma condição obrigatória. Para todas as etapas que necessitarem de campos obrigatórios as configurações devem ser realizadas.  
**Campos Invisíveis**  
São campos do atendimento que se tornarão invisíveis, ou seja, ficarão ocultos. Quando o atendimento avança para uma determinada etapa, o sistema verifica na etapa em questão se existe algum campo selecionado para não ser exibido, caso exista, o campo não será visualizado até o momento que o atendimento avance para a próxima etapa.  
Os campos invisíveis são agrupados nas etapas de acordo com aba que pertence e caso todos os campos estiverem marcados, a guia não será apresentada no atendimento. Lembrando que o sistema realiza o tratamento para os campos que são obrigatórios. Vale ressaltar que se em alguma etapa não for selecionado nenhum campo, o avanço do atendimento para essa etapa será realizado sem a que o sistema oculte nenhum campo.

**Campos Necessários da Etapa Anterior**  
São campos que devem ser preenchidos na etapa atual do atendimento para que o mesmo avance para a próxima. Caso alguma etapa não esteja com campos selecionados, o avanço do atendimento para essa etapa será realizado sem a cobrança de preenchimento de campo.

**Campos Invisíveis - Cliente Online**  
   
O controle da visibilidade dos parâmetros do atendimento no Módulo de Cliente Online ocorre de forma independente aos parâmetros comuns (Aba Campos Invisíveis), ou seja, a configuração dos Campos Invisíveis não interfere na parametrização dos Campos Invisíveis Cliente Online e vice-versa. Para o restante dos campos Somente Leitura, Obrigatório, Necessário da Etapa Anterior,  o atendimento e o Módulo de Cliente Online irão continuar compartilhando o mesmo local de configuração no tipo de atendimento.  
Os parâmetros do atendimento se tornarão invisíveis, ficarão ocultos em determinada etapa. Quando o atendimento sofre o avanço de etapa, o sistema verifica na etapa em questão se existe algum campo selecionado para não ser exibido, caso exista, o campo não será visualizado até o momento que o atendimento avance para a próxima etapa.

**Ações Bloqueadas**

São ações que podem ser bloqueadas em cada etapa, aumentando assim o poder de personalização de um fluxo, segue abaixo as opções possíveis:

**Configurações do aplicativo Minhas Aprovações**

**Notificar o responsável da etapa**

A partir da versão 12.1.33, estando a URL de configuração do App devidamente informada, sempre que o aprovador receber uma tarefa/atendimento para analisar, será enviada uma notificação no seu dispositivo conforme destacado abaixo:

As opções de notificações podem ser definidas no TOTVS Aprovações e Atendimento, por tipo de atendimento ou por etapa (tela abaixo) e nos dispositivos onde o App for instalado.

Por default esse parametro sempre será marcado para notificar.

Esse parametro pode ser habilitado no tipo de atendimento para todas as etapas , ou pode ser definido na própria etapa que só fica habilitada quando a opção de notificar em todas as etapas nao esteja informada.

Quando estiver habilitado no tipo de atendimento fica desabilitado na etapa.

É importante ressaltar que o sistema não notificará se o avanço for para conclusão do atendimento.

Caso o aparelho do usuário nao esteja com a permissão de notificação habilitada, ao clicar no sininho irá perguntar se deseja liberar permissão.

Para definir o número de dias que deverá manter as notificações no banco, acesse os [parâmetros do TOTVS Aprovaççoes e Atendimento>Atendimento.](https://tdn.totvs.com/pages/viewpage.action?pageId=425458824)

**Template do WhatsApp:**

Esse campo Template do WhatsApp é informado quando é habilitado o parâmetro "Disponível no WhatsApp" no cadastro de Tipo de Atendimento.

Para utilizar essa aprovação/reprovação via whatszapp é necessário contratar e configurar  o Worknow como intermediário veja os detalhes em: <https://worknow.com.br/store/>

Após a contratação e configuração do Worknow informa-se o template a ser utilizado na integração na etapa do atendimento no campo template do whatsapp.
