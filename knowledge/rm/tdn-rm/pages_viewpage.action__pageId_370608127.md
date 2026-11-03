---
content_hash: cf05e00ec25941131569c1d2e1b108388683cfc7014467bf8adc7a742715320e
fetched_at: '2026-06-29T00:09:00.915495+00:00'
page_id: '370608127'
product: rm
source: tdn-rm
title: Agilis - Totvs Gestão de Relacionamento com Cliente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=370608127
version: 57
---

Novidades

Novidades12.1.23Atenção

A partir da versão 12.1.23 o sistema permite a utilização do parâmetro " Atendente destino será o novo responsável pelo contato com o cliente" (Similar ao que já existe no avanço de etapas e repasse de atendimento).

Este parâmetro permite que o usuário que apropria - se de um atendimento que esta na fila possa ser ou não ser o contato direto do atendimento.

Exemplo:

Usuário ANTONIO criou um atendimento e ele é o contato do atendimento.

Ao avançar o atendimento para fila o sistema permite que outro usuário como o GDPRH apropriar- se do atendimento na ila habilitando um parâmetro que define se ele vai ser ou não não o responsável pelo contato.

11AtendimentosAtendimentos

1 – Visão geral.

Atendimentos são tarefas que seguem um determinado fluxo com várias etapas, passando por vários atendentes com instruções do que cada deve fazer para concluir determinada etapa, até sua conclusão.

2 - Pré-requisitos para criar atendimentos.

2.1 - O usuário logado deve estar associado a um atendente.

2.2 - O usuário logado deve ter permissão no perfil.

3 – Configurações disponíveis na parametrização dos atendimentos.

3.1 – Gerais.

É possível definir relatórios usados no processo de imprimir atendimentos, pode ser usado um relatório delphi ou .NET, cada um tem seu parâmetro específico para ser definido.

3.2 – Visão de atendimentos.

3.2.1 - É possível modificar os dados apresentados na visão de atendimentos, acrescentado novos campos mesmo de outras tabelas ou retirando alguns campos que não são obrigatórios, para isso, basta criar uma sentença SQL e defini-la no parâmetro “Consulta SQL a ser utilizada para recuperar os registros para a visão de atendimentos”, as seguintes regras devem ser respeitadas ao criar tal sentença SQL:

 - A clausula SELECT deve obrigatoriamente conter os campos abaixo:

CODLOCAL, CODCOLIGADA, CODATENDIMENTO, CODSTATUS, CODTAREFA, CODCOLIGPRD CODPRODUTO, CODATENDENTERESP, CODCOLIGADARESP, CODCOLIGADAALARME, CODATENDALARME, PRAZOLIMITE, CODCOLIGADARPR, CODRPR, ASSUNTOOC, CODITEMPRD, PRIORIDADE, FECHAMENTO

 - A clausula FROM deve obrigatoriamente conter a tabela HATENDIMENTOBASE.

3.2.2 – É possível definir algumas configurações de acesso a atendimentos na visão, assim, pode ser restringido a visualização de atendimentos por atendentes indevidos. Essa restrição pode ser feita por hierarquia de localidade, pode permitir que o atendente que abriu sempre visualize o atendimento ou que todos os atendentes que já foram responsáveis pelo atendimento, sempre possam visualiza-lo.

3.2.3 – É possível impedir que sejam cadastrados atendimentos para clientes que sejam fornecedores.

3.3 – Edição de atendimentos.

3.3.1 – É possível obrigar o preenchimento do campo “Solicitação” na abertura de atendimentos.

3.3.2 – É possível escolher se o campo “Número de série” deve ser apresentado na edição.

3.3.3 – É possível obrigar a escolha de um grupo e tipo de atendimento ou de um modelo de atendimento antes que a edição de um novo atendimento seja aberta, além de garantir o preenchimento desses campos, isso ajuda o usuário quando estiver criando atendimentos de tipos com muitas customizações (Isso será explicado melhor no tópico Tipos de atendimento).

3.3.4 – É possível bloquear a abertura de atendimentos para um ou vários tipos de clientes, os tipos de clientes disponíveis são: Aluno, Cliente, Pessoa, Professor, Prospect, Médico.

Tipo de Atendimento

1 – Tipos de atendimento.

1.1 – Visão geral.

O tipo de atendimento define todo o fluxo que o atendimento vai seguir, desde sua criação, até sua conclusão. Nele estão configuradas as etapas que esse atendimento terá, podem ser quantas o usuário criador desse tipo de atendimento necessitar, é definido também como essas etapas se ligam, desde a primeira, até a última e quais atendentes devem atuar em cada uma dessas etapas.

1.2 – Configurações.

1.2.1 – Modelo

Relatório para impressão de atendimentos: Relatório usado no processo de imprimir atendimentos, esse relatório terá prioridade caso algum esteja setado nos parâmetros gerais do sistema.

Atendimento modelo do tipo de atendimento: Um modelo de atendimento que irá preencher todos os campos do atendimento de acordo com esse modelo assim que esse tipo de atendimento for selecionado, o usuário é questionado no momento da seleção se ele deseja que valores já preenchidos sejam substituídos.

1.2.2 – Template de e-mail.

1.2.2.1 – Relatório para corpo de e-mail.

Abertura de atendimentos: Relatório usado no corpo dos emails enviados na abertura de atendimentos.

Repasse de atendimentos: Relatório usado no corpo dos emails enviados no repasse de atendimentos.

Concluído respondido: Relatório usado no corpo dos emails enviados na conclusão de atendimentos.

1.2.3 – Pesquisa de satisfação.

Layout da pesquisa de satisfação: Caso esse campo for preenchido, a pesquisa de satisfação padrão do sistema será substituída por esse layout selecionado (Mais detalhes no tópico Pesquisa de satisfação).

1.2.4 – Padrão de email.

Descrição padrão remetente: Caso esse campo for preenchido, o nome do remetente dos emails relativos a atendimentos que possuam esse tipo de atendimento, serão substituídos pelo valor preenchido, existe um parâmetro geral do sistema com essa mesma função, caso ambos estiverem preenchidos, esse terá a prioridade.

Endereço de email padrão do remetente: Caso esse campo for preenchido, o endereço de email do remetente dos emails relativos a atendimentos que possuam esse tipo de atendimento, serão substituídos pelo valor preenchido, existe um parâmetro geral do sistema com essa mesma função, caso ambos estiverem preenchidos, esse terá a prioridade.

Assunto padrão email: Caso esse campo for preenchido, o assunto dos emails relativos a atendimentos que possuam esse tipo de atendimento, serão substituídos pelo valor preenchido, existe um parâmetro geral do sistema com essa mesma função, caso ambos estiverem preenchidos, esse terá a prioridade.

1.3 – Anexo etapas.

1.3.1 – Visão geral.

Etapas são os passos que um atendimento passa até sua conclusão, várias configurações são possíveis em cada uma dessas etapas.

1.3.2 – Edição.

Tipo de repasse: Poder ser pra um atendente fixo, para um grupo, manter com o atendente atual ou fórmula, mais detalhes sobre fórmulas no tópico Repasse por fórmula.

Fórmula visual para executar instruções customizadas: O usuário seleciona uma fórmula visual que será executada ao final do processo de avanço para essa etapa.

Ação a ser realizada nessa etapa: O usuário seleciona uma ação que será executada no atendimento ao entrar nessa etapa, as opções disponíveis são: Concluir a responder, Concluído respondido, Concluído confirmado, Agendado a responder, Agendado respondido, Cancelar atendimento.

Sentença SQL: O usuário seleciona uma sentença SQL, cujo resultado será exibido em uma nova aba na edição do atendimento, quando o mesmo estiver nessa etapa.

Os emails de Repasse/Avanço de etapa devem utilizar o seguinte modelo: O usuário configura a prioridade que o sistema irá considerar ao decidir qual relatório será usado nos email de repasse e avanço de etapas.

Customização de campos da edição: É possível configurar se vários campos e parâmetros do tipo de atendimento, presentes na edição do atendimento, são obrigatórios, visíveis, necessários na etapa anterior, somente leitura, invisíveis no cliente online.

Ações bloqueadas: O usuário seleciona uma ou mais ações, que ele não deseja que sejam executadas no atendimento quando o ele estiver nessa etapa.

1.4 – Anexo fluxo de etapas.

1.4.1 – Visão geral.

O fluxo de etapas define como cada etapa ira se ligar a outra, além disso, o usuário pode definir algumas ações que podem ser realizadas.

1.4.2 – Edição.

O usuário seleciona uma determinada etapa, a próxima etapa e uma condição para que ocorra o avanço de etapas, essa condição, é um texto livre em que o usuário digita uma informação intuitiva que será usada no processo de avanço de etapas.

1.4.3 – Envio de e-mail.

Fórmula: Uma fórmula que deve retornar um ou mais endereços de e-mail que serão enviados durante a transição entre as duas etapas desse fluxo.

Endereço de e-mail: Campo livre onde o usuário pode setar um endereço fixo de e-mail que será enviado durante a transição entre as duas etapas desse fluxo.

Corpo do e-mail: O corpo do e-mail que será enviado durante a transição entre as duas etapas desse fluxo.

1.5 – Parâmetros do tipo de atendimento.

1.5.1 – Visão geral.

Parâmetros do tipo de atendimento, são campos extras que o usuário pode criar e estarão disponíveis na edição de atendimentos desse tipo. Esses parâmetros, enriquecem muito as informações contidas no atendimento, uma vez que eles podem ser de vários tipos, inclusive podem ser baseados em uma consulta SQL, dessa forma possibilitando ao usuário, criar um campo em que o atendente seleciona um registro já existente no banco para ficar registrado no atendimento.

Processo avançar etapas

Visão geral.

O processo de avançar etapas, é acionado assim que todas as requisições da etapa atual forem realizadas, ele faz com que o atendimento passe para sua próxima etapa, geralmente com outro atendente responsável. Um avanço de etapa pode fazer o atendimento ir de uma determinada etapa para N outras, inclusive podendo voltar para uma etapa anterior de acordo com o fluxo criado.

Um atendimento é criado sem etapas, ou seja, ele ainda não está no fluxo, ao avançar etapa a primeira vez, normalmente só existe uma opção de primeira etapa, nesse caso é apresentada uma tela informativa, sem que o usuário possa selecionar um caminho para o fluxo seguir.

Já as demais etapas, o fluxo pode seguir vários caminhos diferentes, de acordo com o necessidade do usuário que criou o fluxo, nesse caso, o avanço de etapas exibe uma tela em que o usuário deve escolher uma condição de avanço de etapas (Definida no fluxo) que encaminha o atendimento para a etapa seguinte. Nesse ponto, o usuário também pode definir um motivo para o avanço de etapas, que é um campo informativo, e ele pode definir que atendente seguinte será o novo responsável pelo contato com o cliente.

[Formulas Visuais](https://tdn.totvs.com/pages/viewpage.action?pageId=403746948)

Processo repassar atendimento

Visão geral.

O processo de repassar, faz com que o atendimento seja enviado para outro atendente responsável sem alterar sua etapa. O usuário seleciona o atendente ou grupo que deseja repassar, como no avanço de etapas, é possível definir que o próximo responsável seja o novo contato com o cliente. Um e-mail de repasse é enviado ao atendente que receberá o atendimento, para que ele fique ciente de que agora o mesmo está sob sua responsabilidade.

Processo concluir atendimento

Visão geral.

O processo de concluir atendimento, muda o status do mesmo para concluído, existem 3 etapas de conclusão, Concluir atendimento, que é usado quando o atendente finaliza sua atuação, Concluído respondido, que é usado pelo solicitando para confirma que concorda com a conclusão feita pelo atendente e Concluído confirmado, que é usado pelo atendente que concluiu inicialmente para finalizar em definitivo o atendimento. Para executar esse processo, é necessário que a conclusão do atendimento esteja preenchida.

Anexo apontamento

Visão geral.

No apontamento, o atendente pode registrar suas atividades nesse atendimento, ele deve definir o período, percentual concluído e tipo de atividade. É apresentado ao usuário uma visão de dados editável onde ele pode alterar ou acrescentar registros.

Também é possível acessar essa funcionalidade por fora de um atendimento

Nesse caso, serão exibidos os apontamentos do atendente logado em todos os atendimentos que ele apontou, ele também pode inserir apontamento para um atendimento especifico que tiver acesso dessa forma.

Anexo arquivos anexos ao atendimento

Visão geral.

O atendente pode anexar um ou mais arquivos ao atendimento, ele fica armazenado no banco de dados e pode ser posteriormente visualizado por qualquer pessoa com permissão pra isso. O tamanho de arquivos que pode ser anexado em um atendimento, pode ser limitado por atendimento, atendente ou ambos.

Parametrização para limitar tamanho do arquivo anexo ao atendimento:

Anexo histórico de repasses

Visão geral.

O histórico de repasses, recebe um registro sempre que o atendimento é passado para outro atendente responsável, isso pode ocorrer em um avanço de etapas ou em um repasse.

Anexo histórico de etapas

Visão geral.

O histórico de etapas, recebe um registro sempre que o atendimento alterar sua etapa atual, isso somente ocorre em um avanço de etapas. Vale observar que um avanço de etapas, pode alterar o atendente responsável e a etapa atual, nesse caso, é incluído um registro no histórico de repasses indicando a mudança de atendentes e outro no histórico de etapas indicando a mudança de etapa, em um repasse, somente o atendente responsável é alterado, portando, um registro é incluído somente no histórico de repasses.

Anexo pesquisa de satisfação

Visão geral.

A pesquisa de satisfação, é enviada ao solicitante do atendimento no momento em que acionar o processo de concluído respondido, o e-mail de conclusão enviado, terá um link para que o cliente acesse uma pesquisa de satisfação em que ele poderá responder um questionário indicando os pontos positivo e negativos da solução dada para o atendimento concluído.

É possível visualizar a resposta dada pelo cliente no anexo do atendimento.

Layout da pesquisa de satisfação

O layout da pesquisa de satisfação, permite que o usuário customize a pesquisa que será enviada ao usuário na conclusão do atendimento, para isso, ele seleciona um relatório que substituirá o texto padrão dessa pesquisa e também cria parâmetros, que funcionam de forma similar aos parâmetros do tipo de atendimento e irão substituir as perguntas padrões do sistema.

Pesquisa de atendimentos

Visão geral.

Na pesquisa de atendimentos, o usuário pode selecionar vários filtros para que sejam exibidos todos os atendimentos correspondentes e que o usuário tenha permissão de visualizar, o atendente pode visualizar todos os atendimentos cujo nível de acesso for menor ou igual ao nível de acesso do seu atendente, atendimentos que estiverem sob sua responsabilidade ou sob responsabilidade de um atendente chefiado por ele, mesmo podendo visualizar atendimentos pelo nível de acesso, um atendente só pode manipular atendimentos se ele for responsável ou chefe do responsável pelo atendimento.

Caso queira fazer uma pesquisa por valores dos parâmetros do tipo de atendimento, o usuário deve preencher os campos "Grupo de atendimento" e "Tipo de atendimento" da aba "Fluxo de etapas".

Ao fazer isso, a aba "Parâmetros" ira surgir com os parâmetros disponíveis no tipo de atendimento selecionado.

Atendimento modelo

Visão geral.

O atendimento do tipo modelo tem a finalidade de facilitar a abertura de atendimento, nele, o usuário pode inserir informações iniciais comuns a vários atendimentos que são abertos no dia a dia.

Criação de fórmulas

Para a criação de fórmulas que serão usadas pelo Agilis, alguns pontos importantes devem ser observados:

 - Qualquer sentença SQL usada em uma fórmula, deve obrigatoriamente possuir (NOLOCK) em todas tabelas.

 - Uma fórmula NUNCA deve usar a função AVANCARETAPAATENDIMENTO para avançar para ela mesmo, isso sempre ira causar erro.

 - Para fórmulas configuradas em Avanço de Etapa, NUNCA deve-se usar as funções REPASSARATENDIMENTO e REPASSARATENDPARAGRUPO. Essas funções são exclusivas para uso no serviço de 'Movimentar atendimentos por fórmulas' e o motivo disso é que em um avanço de etapas com fórmula, o sistema espera que a fórmula retorne pra ele o atendente ou grupo para o qual tal repasse deve ser feito, e usar essas funções faz com que o repasse ocorra fora do processo normal do sistema, o que pode trazer resultados incorretos.

 -  Para fórmulas configuradas em Avanço de Etapa, a função ALTERACAMPOSATENDIMENTO NUNCA deve ser utilizada para alterar código do atendente ou atendente responsável, pois isso pode fazer com que as regras do sistema para montar o histórico de etapas e repasse fiquem distorcidas.

Segue abaixo um modelo para adaptar uma fórmula que hoje usa as funções que não devem ser usadas, no modelo recomendado:

DECL ATENDENTE;//Inicio da formula  
...  
SETVAR(ATENDENTE, CONCATENA(COLIGADACORRENTE,5,';'));//Mesma linha do REPASSAR substituindo o 5 pelo primeiro argumento da função REPASSAR atual  
ENVIAEMAILREPASSE('', EMAILDESTINATARIO, '', ATENDENTE);//Essa linha somente é necessária caso o usuário deseje enviar o email de repasse para algum outro atendente além do de destino  
...  
RETURN ATENDENTE;//Fim da fórmula

Obs: Pode ser necessário retirar o RETURN da ultima linha dependendo da fórmula, o importante é que o retorno da fórmula acima seja '1;5'

2AtendentesAtendentes

Visão geral.

Atendentes são basicamente a forma do usuário criar ou interagir com um atendimento, ele sempre deve estar associado a um determinado usuário do sistema, dessa forma, quando um usuário loga no sistema e acessa o Agilis, todas as iterações desse usuário nos atendimentos será realizada por esse atendente associado, sendo essa a razão da necessidade primária de se ter um atendente associado ao usuário logado para manipular atendimentos.

Pré-requisito para criar atendentes

Ao criar um atendente, ele deve estar associado a uma pessoa do RH, o usuário da pessoa será o usuário associado ao atendente, também deve ser selecionada uma hierarquia e localidade.

A pessoa é um registro criado no sistema RH, mas tal cadastro pode ser acessado pelo atalho Pessoas criado no Agilis na aba Atendentes, o usuário exigido, deve ser setado dentro do cadastro da pessoa selecionada, ele não pode ser alterado ou selecionado diretamente dentro do cadastro de atendentes, ele apenas mostra o usuário relacionado a pessoa selecionada.

Motivos de inatividade

Visão geral.

O cadastro de motivo de inatividade, define uma ou mais atividade temporárias que o atendente pode estar exercendo no momento, muitas vezes é usado para definir uma ausência temporária em um período em que os atendimentos repassados pra ele devem ser encaminhados para o substituto, mas assim que ele voltar ao trabalho, esse status pode ser rapidamente mudado para um status ativo e ele voltaria a receber atendimentos normalmente.

3ServiçosServiços

Visão geral.

Serviços são um grupo de processos independentes de qualquer cadastro e que podem ser executados a qualquer momento para realizar determinada ação, todos os serviços podem ser agendados e parametrizados para executar em um intervalo de tempo, desde que o sistema esteja configurado para usar jobserver em 3 camadas, caso contrário, eles somente podem ser executados imediatamente.

Movimentar atendimentos por fórmula

Visão geral.

Esse serviço, executa uma determinada fórmula em cada um dos atendimentos retornados por uma sentença SQL escolhida pelo usuário. É normal que essa fórmula executada termine com a função REPASSARATENDIMENTO ou REPASSARATENDPARAGRUPO para que vários atendimentos possam ser repassados para várias pessoas diferentes de acordo com as regras definidas na fórmula, mas é possível aplicar qualquer outra função de fórmula que se adequar a necessidade do usuário.

Execução.

Na execução desse serviço, os seguintes campos devem ser preenchidos:

Código da sentença: Sentença SQL que lista os atendimentos aos quais aos quais determinada fórmula será executada, é exigido que nessa sentença, os campos que compõem a chave primária do atendimento estejam listados, esses campos são: CODCOLIGADA, CODLOCAL, CODATENDIMENTO. Caso o botão “Parâmetros” seja acionado, o usuário pode escolher valores para os parâmetros da sentença SQL, esses parâmetros, são definidos colocando “:” antes do campo na sentença SQL, exemplo, :CODCOLIGADA

Fórmula define grupo repasse: Fórmula que geralmente termina com as funções REPASSARATENDIMENTO ou REPASSARATENDPARAGRUPO, mas qualquer função de fórmula pode ser aplicada de acordo com a necessidade.

Gerar atendimentos por consultas SQL

Visão geral.

Esse serviço, gera novos atendimentos usando dados de determinada sentença SQL definida pelo usuário, essa sentença, pode trazer qualquer campo que o usuário necessitar, mas na execução do processo ele deve atribuir ao atendimento campos da sentença que sejam de tipos consistentes.

Execução.

Na execução desse serviço, os seguintes campos devem ser preenchidos:

Código da sentença: Sentença SQL que traz os dados que serão usados para gerar atendimento, será gerado um atendimento para cada registro retornado. Caso o botão “Parâmetros” seja acionado, o usuário pode escolher valores para os parâmetros da sentença SQL, esses parâmetros, são definidos colocando “:” antes do campo na sentença SQL, exemplo, :CODCOLIGADA

Assunto: Define o assunto do atendimento gerado, ele pode ser um assunto fixo ou usar algum campo pré-definido ou mesmo algum campo da sentença SQL do campo anterior, para isso deve ser acrescentado a TAG {0} e em seguida acionar o botão “Parâmetro” logo a direita, dessa forma, é possível definir qual campo da sentença SQL irá substituir a TAG na mesma posição em que ela foi colocada, caso necessite usar mais de um parâmetro, os seguintes devem seguir exatamente a ordem numérica seguinte, exemplo:

O atendente {0} solicita que seja resolvido o seguinte erro: “{1}” até o dia: {2}

O usuário pode acionar o botão “Parâmetros” para substituir a TAG {0} pelo campo NOME, a TAG {1} pelo campo MENSAGEMERRO e a TAG {2} pelo campo DATALIMITE, que no atendimento gerado o assunto ficaria:

O atendente João solicita que seja resolvido o seguinte erro: “Usuário inativo” até o dia: 02/10/2018

Solicitação: Vide Assunto acima, com a diferença de que será colocado na solicitação do atendimento.

Grupo de atendimento: Defino o grupo de cada atendimento gerado.

Tipo de atendimento: Define o tipo de atendimento de cada atendimento gerado.

Código da classificação: Define a classificação de cada atendimento gerado.

Atendente responsável: Define o atendente que será responsável por cada atendimento gerado, pode ser um atendente fixo, um grupo ou definido no avanço da primeira etapa, nesse caso, o fluxo de etapas do tipo selecionado irá definir o atendente responsável.

Coligada do cliente: Nesse campo, são listados todas as coligadas existentes na base para que uma seja selecionada, ela será a coligada do cliente de todos os atendimentos gerados.

Cliente do atendimento: Nesse campo, são listados todas as colunas retornadas pela sentença SQL selecionada no campo “Código da sentença” para que uma seja escolhida, esse será o cliente de todos os atendimento gerados.

Tipo do Cliente: Lista os tipos de cliente disponíveis para a abertura de atendimento, cada atendimento gerado terá esse tipo de cliente.

Importante: Os campos “Coligada do cliente”, “Cliente do atendimento” e “Tipo do Cliente” se referem ao mesmo cliente e devem ser consistentes, ou seja, o cliente escolhido, deve existir na coligada escolhida e pertencer ao tipo escolhido.

Coligada do Produto: Nesse campo, são listados todas as coligadas existentes na base para que uma seja selecionada, ela será a coligada do produto de todos os atendimentos gerados.

Produto do atendimento: Nesse campo, são listados todas as colunas retornadas pela sentença SQL selecionada no campo “Código da sentença” para que uma seja escolhida, esse será o produto de todos os atendimento gerados.

Importante: Os campos “Coligada do Produto” e “Produto do atendimento” se referem ao mesmo produto e devem ser consistentes, ou seja, o produto escolhido, deve existir na coligada escolhida.

Grupo de e-mails

Visão geral.

Trata-se de um cadastro para os serviços “Gerar atendimento por grupos de e-mail”, “Leitura de mailing” e “Inserir discussão/anexos a partir de e-mails” (Esses serviços serão detalhados em seguida). Cada registro, aponta para uma caixa postal de e-mail, quando qualquer um desses serviços é acionado, todo registro que tiver como finalidade ser usado no serviço em execução, terá sua caixa postal lida e o serviço executado para cada mensagem nela.

Importante: Todos os endereços de e-mails acessados dessa forma, devem estar configurados para permitir serem acessados por aplicativos externos.

Parametrização.

Nos parâmetros do CRM, no item “51.07 – Serviços” no subitem “Gerar atend por grupo de email”, devem ser gravados o endereço do servidor POP do e-mail que se deseja acessar e sua porta.

Edição.

Usuário: Define o usuário para acessar a caixa postal do e-mail, muitas vezes, o usuário será o endereço de e-mail completo.

Senha: Define a senha para acessar a caixa postal do e-mail, ela é armazenada criptografada e não é exibida na edição.

E-Mail: Define o endereço e e-mail completo a ser usado.

Finalidade da caixa postal (por alguns dos serviços do sistema): Define qual dos 3 serviços ligados a esse cadastro será executado para esse registro, as opções disponíveis são:

“Criação de atendimentos a partir dos e-mails da caixa postal” para o serviço “Gerar atendimento por grupos de e-mail”.

“Atualização do histórico do cliente a partir de resposta aos mailings do módulo de Marketing” para o serviço “Leitura de mailing”.

“Registro na discussão (do texto do e-mail) e inserção de arquivos anexos a partir de resposta aos e-mails de atendimentos” para o serviço “Inserir discussão/anexos a partir de e-mails”.

Atendimentos modelo: Define a coligada e o atendimento modelo que será usado nos atendimentos gerados.

Atendente responsável: Define o atendente que receberá os atendimentos gerados, ele pode ser um atendente fixo, um grupo de atendente ou definido no avanço da primeira etapa do fluxo definido no modelo selecionado.

Gerar atendimento por grupos de e-mail

Visão geral.

Esse serviço, gera um atendimento para cada mensagem na caixa de entrada do e-mail definido no cadastro de “Grupo de e-mails” que tiver sua finalidade definia como “Criação de atendimentos a partir dos e-mails da caixa postal”, o assunto do atendimento será o assunto do atendimento e a mensagem do corpo do e-mail será a solicitação, os arquivos anexos e imagens que estiverem direto no corpo, serão transformados em arquivos anexos ao atendimento.

Leitura de mailing

Visão geral.

Esse serviço lê as mensagens na caixa de entrada do e-mail definido no cadastro de “Grupo de e-mails” que tiver sua finalidade definida como “Atualização do histórico do cliente a partir de resposta aos mailings do módulo de Marketing”, o serviço irá buscar mensagens que foram respondidas por clientes que receberam propostas do módulo de marketing (mais detalhes sobre esse módulo mais adiante), e irá acrescentar essa mensagem no histórico desse cliente.

Inserir discussão/anexos a partir de e-mails

Visão geral.

Esse serviço lê as mensagens na caixa de entrada do e-mail definido no cadastro de “Grupo de e-mails” que tiver sua finalidade definida como “Registro na discussão (do texto do e-mail) e inserção de arquivos anexos a partir de resposta aos e-mails de atendimentos”, o serviço irá buscar mensagens que sejam respostas de e-mail enviados por determinado atendimento e incluir na discussão desse atendimento o corpo da mensagem que seria a resposta da pessoa que recebeu a mensagem sobre o atendimento.

Despertar atendimentos

Visão geral.

Esse serviço muda o status dos atendimentos agendados para despertado, isso é feito de acordo com o “Prazo limite” do atendimento e “Data em que os atendimentos deverá(ão) despertar” do processo de agendar atendimento.

Alertar chefias sobre agendamentos pendentes

Visão geral.

Esse serviço avalia a data de agendamento de atendimentos cujo status é 'Agendado a responder' e, de acordo com o número de dias (parametrizável) em que o atendimento se encontra neste status, envia um e-mail para chefe imediato do atendente responsável pelo atendimento.

Envio de e-mail

Visão geral.

Esse serviços dispara todos os e-mails do sistema, que até então ficavam armazenado na tabela HENVIAEMAIL, é normal que esse serviço seja agendado para ser executado repetidamente em curtos intervalos de tempo para que os e-mails sejam enviado o mais rápido possível.

4MarketingCampanha

Visão geral.

Campanha contém as informações necessárias para divulgar algum produto ou serviço e divulgá-lo para vários cliente por diferentes canais de comunicação.

Edição.

Título: Texto para identificar a campanha.

Objetivos: Texto livre com os principais objetivos da campanha.

Atendente: Um atendente que será responsável pela campanha.

Custo da campanha: Soma do valor total de todos os canais de divulgação usados.

Período previsto: Data de início e fim previsto para a campanha.

Status: Indica o status da campanha, que pode ser em andamento, pausada ou parada.

Descrição: Texto livre com uma descrição detalhada da campanha.

Anexo canais de divulgação

Visão geral.

Lista os canais de divulgação já cadastros que estão associado a essa campanha.

Edição.

Custo total: Custo do canal de divulgação cadastrado mais algum custo extra dele ser usado nessa campanha.

Período previsto: Data de início e fim previsto pra usar esse canal nessa campanha.

Canais de divulgação: Seleciona um canal de divulgação já cadastrado, detalhes sobre cadastro de canais de divulgação adiante.

Atendente: Atendente responsável por esse canal de divulgação nessa campanha.

Anexo clientes

Visão geral.

Lista os clientes já cadastrados que estão associados a essa campanha.

Edição.

Esse anexo não possui uma edição, clientes podem ser adicionados apenas pelo processo “Adicionar clientes”, mas detalhes sobre esse processo mais adiante.

Anexo discussão

Visão geral.

Lista as discussões inseridas nessa campanha, que são textos livres com informações adicionais que surgiram ao longo da campanha.

Edição.

Data: A data de inclusão da discussão, esse campo é preenchido automaticamente com a data do servidor sem que o usuário possa alterar.

Nome do atendente: Atendente associado ao usuário logado, esse campo é preenchido automaticamente sem que o usuário possa alterar.

Texto: Texto livre com a informação a ser acrescentada como discussão da campanha.

Anexo produtos

Visão geral.

Lista os produtos associados a essa campanha.

Edição.

Produto: Usuário seleciona um produto previamente cadastrado que será associado à campanha.

Anexo tipo de ação da campanha

Visão geral.

Lista os tipos de ação da campanha, que geralmente vem com um script de telemarketing que o operador deve seguir ao entrar em contato com o cliente.

Edição.

Tipo de ação: Usuário seleciona um tipo de ação previamente cadastrado.

Texto script: Texto livre com a possibilidade de formatação, é usado caso necessite de um script especifico para ser usado por essa ação nessa campanha.

Anexo relacionamento de cliente X atendente

Visão geral.

Esse anexo foge um pouco do padrão de um anexo TOTVS para facilitar sua usabilidade, ele apresenta um grid à direita com todos os clientes dessa campanha que ainda não foram atribuídos a nenhum atendente, e a esquerda apresenta os atendentes que estão configurados para aparecer no modulo de marketing, essa configuração é feita no próprio cadastro do atendente, cada atendente pode ser clicado em sua extremidade direita para que seja aberta uma caixa de detalhes logo abaixo dele, mostrando os clientes que esse atendente pode executar operações de telemarketing, detalhes sobre o processo de executar operação de telemarketing mais adiante. Para associar cliente a atendente, o usuário deve seguir os seguintes passos:

1) Marcar no grid à direita os clientes que deseja associar.

2) Clicar com o mouse em qualquer ponto do grid, arrastar para o atendente ao qual deseja associar os atendentes marcados no passo 1 e soltar.

3) Com isso, os clientes sumirão do grid a direita e aparecerão na caixa de detalhas que aparece abaixo do atendente quando sua extremidade direita é clicada.

Para desassociar cliente de atendente, o usuário deve seguir os seguintes passos:

1) Marcar os clientes que deseja desassociar na caixa de detalhes do atendente.

2) Clicar com o mouse em qualquer ponto da caixa de detalhes, arrastar para um ícone de lixeira que aparece na parte inferior da lista de atendentes e soltar.

3) Com isso, os clientes sumirão da caixa de detalhes do atendente e retornarão para o grid a direita, estando dessa forma disponíveis para associação com outro atendente.

Anexo histórico de inserção de clientes

Visão geral.

Lista todas as inserções de clientes realizadas nessa campanha e como tais inserções foram realizadas.

Edição.

Não é possível inserir registro nesse anexo, mas é possível visualizar na edição, quais clientes foram incluídos e qual método foi usado pra isso, detalhes mais adiante no processo de adicionar clientes.

Processo adicionar clientes

Visão geral.

Esse processo lista todos os clientes de todos os tipos disponíveis para que o usuário selecione os que deseja inserir na campanha, o grid que exibe os cliente, além do recurso de filtro que é padrão em todas as telas, ele também pode ser preenchido usando uma sentença SQL cadastrada, ou mesmo digitando a sentença diretamente em um edito de texto que fica escondido na parte superior da tela e pode ser acessado clicando em “Sentença SQL personalizada”, é possível também selecionar uma sentença SQL e clicar em “Editar sentença” para que ela seja copiada na “Sentença SQL personalizada” para que o usuário possa incluir os campos exigidos e ela então possa ser executada, os campos exigidos em ambos os casos, são:

COLIGADA, CODIGO, TIPO e NOME

Os campos deve ser de tipos consistentes, mas pode ser usada um alias em qualquer campo para que tenham exatamente o nome exigido.

Também é possível adicionar clientes diretamente de um grupo de clientes cadastrado.

Operações de telemarketing

Visão geral.

Essa funcionalidade é acessível pela aba “Meus atendimentos”, ela é usada pelo operador de telemarketing.

Ele entrará em contado com os clientes atribuídos a ele pelo anexo “relacionamento de cliente X atendente” visto anteriormente.

Esse processo lista em uma caixa a esquerda os filtros mais comuns, “Clientes não atuados”, “Clientes agendados” e “Clientes concluídos”, assim que algum desses filtros é clicado, os registros correspondentes são exibidos no grid a direita. Para usar essa funcionalidade, o usuário deve acessar o processo “Executar operação de telemarketing” que será detalhado adiante, e registrar nele como foi o contato com o cliente.

Processo executar operação de telemarketing

Visão geral.

Esse é o principal processo da funcionalidade de operações de telemarketing, ele irá guiar o atendente na ação de telemarketing que ele fará ao cliente e também registrará dados importantes desse contato.

Execução.

O atendente terá acesso ao nome, nome fantasia e telefone do cliente, caso seja necessário, ele pode acionar o botão “Mostrar informações estratégicas” para ver informações mais detalhadas desse cliente, ele então seleciona o tipo de ação que será realizado e o script de telemarketing que ele deve seguir já será exibido no campo “Script de telemarketing”, finalizado o contato, o atendente irá selecionar uma das opções cadastradas para o “Retorno do cliente”, caso o contato não tiver sido possível, o atendente marca a opção “Não houve contato com o cliente” e seleciona uma opção cadastrada para o “Motivo da falta de contato”, ele então decide se deve ou não agendar um novo contato com esse cliente marcando a opção “Agendar novo contato com cliente”, escolhendo uma data pra tal agendamento, o atendente pode também agendar um novo contato mesmo que esse contato tenha sido bem sucedido caso achar necessário ou caso o cliente solicite, o campo “Conversa” é um texto livre onde o atendente registra os detalhes do contato que ele achar necessário. Ao executar o processo, o registro irá passa a ser exibido no filtro “Clientes agendados” ou “Clientes concluídos” de acordo com as opções escolhidas pelo atendente.

Processo vinculação de cliente

Visão geral.

Esse processo tem a mesma funcionalidade do anexo de campanha “relacionamento de cliente X atendente”, com a diferença que o cliente será acrescentado para o atendente associado ao usuário logado atuar, esse processo é usado caso o próprio atendente de telemarketing tenha autonomia para incluir um cliente para sua atuação.

Execução.

O atendente seleciona uma campanha que será usada para a ação, o tipo de cliente, e o cliente do tipo selecionado, ao executar, esse cliente será exibido no filtro “Clientes não atuados”, caso o atendente de telemarketing tenha permissão para isso, ele pode inclusive cadastrar um novo cliente dentro da própria caixa de seleção de cliente desse processo.
