---
content_hash: 3fed17cceda3957e8493783e8bfda67665ef96d33a1af57a2f28fcbbb3691674
fetched_at: '2026-06-29T00:09:37.201969+00:00'
page_id: '425459575'
product: rm
source: tdn-rm
title: Atendimentos do usuário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459575
version: 7
---

**Atendimento**

---

Este tópico de menu permite visualizar os atendimentos do atendente logado, através da Visão de Atendimentos.   
Além de visualizar os atendimentos do atendente logado, essa tela permite que sejam exibidos atendimentos de outros atendentes.   
Para visualizar os atendimentos de outro atendente digite no campo "Atendimentos de" o código do atendente que deseja perquisar. Caso não saiba o código do atendente, o sistema permite que o mesmo seja localizado pelo nome ou outras informações.  
Na abertura dos atendimentos, qualquer tipo de cliente pode ser utilizado (Prospect, Suspect, Aluno, Professor, Cliente ou Pessoa), mas também é possível parametrizar para que apenas determinados tipos de cliente possam abrir atendimentos.   
O tipo de atendimento é utilizado para classificar o atendimento (definindo etapas e o fluxo de etapas) e validar o caminho que ele percorrerá no sistema. Ele deve estar vinculado a um grupo de atendimentos que engloba atendimentos que possuam características semelhantes.  
Com o parâmetro "Obriga selecionar tipo ou modelo de atendimento na abertura de atendimento" marcado nas configurações gerais, o sistema não permite que atendimentos sejam abertos sem selecionar o tipo ou modelo. Estes estão disponibilizados no canto esquerdo da tela de visão de atendimentos. A abertura do atendimento é realizada respeitando as configurações da primeira etapa do tipo de atendimento ou preenchendo os campos da edição do atendimento conforme o modelo escolhido.  
Os tipos de atendimentos serão carregados de acordo com o perfil do usuário e todos os modelos da coligada serão apresentados.

**Atendimentos de passaram de ontem para hoje pelo atendente selecionado**

* Quando você clica nesse ícone, o sistema traz como resultado os atendimentos que passaram pelo atendente logado do dia anterior até o atual.
* O objetivo desse recurso é permitir que o atendente consiga visualizar de forma mais rápida os atendimentos que ele trabalhou no dia anterior e no dia atual para apontar o tempo gasto de trabalho nos mesmos.   
    
  **Lista a relação de todos os atendimentos já abertos pelo cliente do atendimento atual**  
   Ao clicar neste ícone, O sistema traz uma relação com todos os atendimentos abertos pelo cliente do atendimento atual. Esta funcionalidade utiliza o mesmo mecanismo de pesquisa de atendimentos, isto é, internamente o sistema passará para a pesquisa de atendimentos o código do cliente do atendimento atual e a partir deste código de cliente o motor da pesquisa se encarregará de efetuar a busca na base de dados e apresentará, em uma nova tela de visão de atendimentos, os atendimentos já abertos pelo cliente.  
    
  **Atendimento na Fila**
* Foi adicionado na visão de atendimento um botão para mostrar os atendimentos que estão na fila.   
  Ao pressionar o botão, ele ficará pressionado e todos os atendimentos que estão relacionados com o grupo daquele atendente serão mostrados na visão de atendimento. Se pressionar o botão novamente, a visão voltará ao normal mostrando os dados de acordo com o filtro selecionado.   
  O botão trabalhará em conjunto de acordo com o filtro selecionado. Caso o filtro selecionado seja TODOS, serão mostrados TODOS os atendimentos cujo atendente responsável seja o atendente corrente + os atendimentos que estão na fila. Caso o filtro seja PENDENTES será mostrados todos os atendimentos pendentes do atendente corrente + os atendimentos que estão na fila. Será assim para qualquer filtro selecionado.   
  É utilizando o mesmo conceito do tipo de repasse na opção grupo de atendente, será criada uma "fila" onde certo atendimento, depois de colocado nela ficará disponível para os atendentes do grupo. Enquanto ninguém pegar esse atendimento sobre sua responsabilidade esse atendimento não poderá sofre nenhuma ação. Um processo deverá ser executado permitindo que o atendente se torne responsável daquele atendimento. Com o atendimento sobre sua responsabilidade o atendente poderá efetuar as operações normais de um atendimento (Repassar, Avançar Etapa, Agendar, etc).    
    
  **Solicitação de Atendimento através do RM Classis**  
  Integração CRM/TOTVS Aprovações e Atendimento X Educacional  
  A integração possibilita o aluno acompanhar, através do Portal do Educacional, os atendimentos abertos durante todos os períodos letivos. Esta funcionalidade permite maior interação com os sistemas gerando comodidade durante todo processo de duração da ocorrência.   
  Desenvolvimento/Procedimentos  
  1. Incluir Solicitação de Atendimento através do Classis.  
  Acesse: Atendimentos / Solicitação de Atendimento através do RM Classis.  
  2. Preencher Seleção de Contexto:  
  • Incluir Nível de Ensino para ser utilizado dentro dos serviços da área Educacional. • Definir Valores de Contexto através da validação das configurações atuais que vão ser utilizadas em todo o sistema. • Informar a Descrição do Processo (Optativo).   
  3. Parametrizar os Dados do Atendimento:  
  • Incluir Grupo de Atendimento. • Incluir Tipo de Atendimento.  
  4. Parametrizar os Dados do Aluno:  
  • Validar Período Letivo (Por default o sistema busca o período informado como corrente). • Informar o aluno. • Incluir o Contrato no Período Letivo. • Incluir a Matrícula do Período Letivo.  
  5. Preencher as informações do  atendimento: • Dados da Solicitação: Nome , Localidade (Obrigatório), Justificativa (Obrigatório). • Descrição: Informações complementares. • Descrição Detalhada: Informações complementares. • Procedimentos: Informações complementares. • Aceite: Informações complementares.   
  Descrição do Processo  
  • Após efetuar as parametrizações citadas acima, execute o processo.  
  • Verifique o atendimento.  
  •  Acesse:   
                 Anexo | Informações do Aluno  
                 Anexo| Informações Estratégicas | Anexos | Informações do Aluno  
  Verifique os dados extras relacionados ao aluno informado na ocorrência.  
  • Nos anexos, o ícone   é apresentado com o objetivo de destacar o período letivo no qual o atendimento foi aberto. Obs.: O aluno pode estar matriculado em vários períodos diferentes.  
    
  Informações Adicionais:
* As configurações necessárias para o funcionamento da integração devem ser parametrizadas no RM Classis:  
  Secretaria | Integração CRM | Configurações:  
  • Tipo de Atendimento  
  Opções | Parâmetros | Totvs Educacional | Integração | Atendimento:  
  • Parametrizar = Atendimento Geral 1                          Atendimento Geral 2                                            
  As solicitações de atendimentos através do Classis podem ser verificadas via Web, o que facilita o acompanhamento e a abertura de atendimentos de qualquer lugar que possua acesso a internet.  
    
  **Atenção**  
  Colocar um atendimento na fila irá envolver as seguintes alterações no sistema:  
  Alteração na funcionalidade "Grupo de Atendente" incluindo a nova opção "fila".   
  Alteração do processo "Repassar Atendimento" para que seja possível repassar um atendimento para um "Grupo de Atendente" com tipo de repasse "Para uma fila".  
  Alteração na visão de atendimento para que seja possível ver os atendimentos na fila.  
  Criar um processo para que seja possível se apropriar dos atendimentos que estejam na fila.  
  Foi adicionada na pesquisa de atendimento uma nova opção para mostrar todos os atendimentos que estão em alguma fila e uma nova opção quando se seleciona um atendente, permitindo mostrar os atendimentos da fila de um atendente especifico.  
  Apresentar o Assunto do atendimento:
* Foi incluído o campo assunto na tela de visão de atendimento, assim o usuário poderá utilizá-lo de acordo com o desejável, podendo agrupar os seus atendimentos pelo assunto ou não.   
    
  Avançar Etapas  
  O botão Avançar Etapas na tela de visão de atendimentos facilita a execução da tarefa. Através deste recurso é possível visualizar e efetuar o preenchimento dos campos obrigatórios/necessários na tela de avanço de etapas. Lembrando que o sistema alerta quando os mesmos estão vazios, evitando a necessidade de editar a ocorrência.   
  + **Observação:**  
    A tela de **visão de atendimentos** pode ser personalizada de acordo com o tipo de atendente ou com os parâmetros do sistema (Parâmetros>Totvs Aprovações e Atendimento>Atendimentos>Visão de Atendimentos), através de uma sentença SQL previamente cadastrada. Esse parâmetro vale apenas para personalização da tela no sistema e não se aplica ao App Minha Aprovações. Caso não esteja parametrizado com nenhuma sentença SQL, a visão será apresentada conforme padrão.  
  Através desta tela é possível controlar:

 **Atendimento – Identificação**  
 Esta pasta permite editar os dados de identificação dos atendimentos, do aplicativo e do contato.  
Abaixo é mostrada a descrição dos campos presentes nesta pasta e o procedimento correto para preenchê-los.  
 Opções da caixa Família do Atendimento:  
   
Atendimento   
Número criado automaticamente pelo sistema após salvar um novo atendimento. É único. Deve sempre ser informado ao cliente para que ele possa acompanhar a evolução do atendimento.  
Prazo limite final   
Você pode definir um prazo limite (agendar) para a resolução do atendimento (após clicar no botão Agendado (a responder) Ao definir este prazo, todas as pessoas envolvidas no processo do atendimento (os atendentes anteriores e aquele responsável pelo contato com o cliente) receberão um e-mail informando este prazo.   
Categoria Individual   
Selecione a categoria individual. As categorias individuais são visíveis a todos os usuários, para classificar seus atendimentos.  
Grupo de Atendimento   
No cadastro de um novo atendimento, pode ser definido se o mesmo seguirá um fluxo de tarefas pré-definido.   
Para que o atendimento siga um fluxo de tarefas, é necessário que seja definido no cadastro do mesmo, qual o grupo de atendimentos ele vai fazer parte.   
Selecione neste campo o grupo de atendimento que a ocorrência em questão pertencerá.   
Este campo ficará habilitado apenas quando for cadastrado um novo atendimento, na edição do mesmo não é possível o preenchimento ou alteração deste campo.   
Tipo de Atendimento  
Para que o atendimento siga um fluxo de tarefas é necessário também que seja definido qual o tipo de atendimento ele vai ser. Para cada tipo, são definidos tarefas e o fluxo delas.   
O atendimento poderá ser repassado automaticamente para um atendente que é responsável por uma tarefa e após a conclusão desta tarefa o atendimento pode ser repassado novamente para outro atendente, ou não, isso vai depender se ele for responsável pela próxima tarefa também.   
Todas essas informações são cadastradas no tipo de atendimento.   
Selecione neste campo o tipo de atendimento que a ocorrência em questão vai ser.   
O cadastro do tipo de atendimento é feito em: Cadastros | Atendimentos | Tipos de Atendimentos.   
Este campo ficará habilitado apenas quando for cadastrado um novo atendimento, na edição do mesmo não é possível o preenchimento ou alteração deste campo.   
Código de Classificação   
Este campo permite classificar os atendimentos. Tal classificação é importantíssima para que as outras pessoas envolvidas na resolução possam saber a origem do problema. Veja opções abaixo. As opções estão posicionadas em ordem alfabética para facilitar a escolha da mesma.  
  
**Atenção!**  
 Veja abaixo a forma correta de utilizar cada opção para classificar os atendimentos:  
A Classificar  
Atribuído automaticamente pelo sistema para atendimentos novos, manuais ou automáticos. Sempre que tentar salvar um atendimento com esta classificação, será emitido um aviso ao usuário para que a mude. Caso contrário, o alarme disparará a cada 2 dias.   
BUG  
Quando o motivo/solicitação do atendimento for resolvido com uma nova versão do aplicativo.   
Implementação:  
Sempre que o sistema não possuir recurso para atender à solicitação do cliente.   
Dúvida  
Para os questionamentos sobre os aplicativos (se existir no aplicativo um recurso para solucionar o questionamento efetuado pelo cliente), ou seja, sempre que não for um erro (BUG) ou uma Implementação. Também deverão ser classificados como dúvida os erros não simulados pelos técnicos.   
Cancelado  
Para cancelar uma ocorrência.   
Instalação do Aplicativo  
Quando for solicitado ao Departamento de Suporte, no caso dos aplicativos DOS, ou ao Departamento de Implantação, no caso dos aplicativos RM, a instalação do sistema. É utilizado pelo Departamento Comercial, quando o cliente adquire a licença de uso.   
Assuntos não relacionados aos aplicativos

Quando ocorrerem problemas de ambiente (rede, banco de dados, configurações de equipamentos: memória, config, autoexec etc), solicitação de senha, arquivo Aponta e informações sobre o código da ultima versão lançada.   
Versão/Senha/Aponta

Quando o cliente solicita soluções referentes às versões liberadas, senhas e problemas com o arquivo Aponta.   
Elaboração de relatórios

Para solicitações referentes à geração de relatórios específicos da situação da empresa.   
RUNTIME

Para solicitações referentes às mensagens emitidas pelo sistema e que são específicas do compilador (Ex.: Pascal). Para cada número de Runtime informado existe uma relação com a solução do problema.  
RECLAMAÇÃO 0800/INTERNET

Atendimentos ao cliente através do número 0800 ou pelo site da TOTVS, através de e-mail. Utilizado pelo Departamento de Marketing.   
Restaurar Backup/CORPORE

Solicitações de restauração de Backup's de bases CORPORE para simulações de problemas na base de dados do cliente.  
Visita técnica

Utilizado para solicitações que só podem ser resolvidas com uma visita do técnico atendente ao cliente, para solução In House. Normalmente, transcreve-se o Relatório de Atendimento Técnico (RAT) no atendimento.  
BUG/SGBD

Solicitações devido a problemas no Sistema de Gerenciamento de Banco de Dados.   
LIBERAÇÃO DE VERSÃO/FTP:

Solicitação de disponibilidade de versões e/ou bases no FTP. Utilizado pelo Departamento Administrativo.   
GERAÇÃO DE MÍDIA/CD

Solicitação de geração de CD's ou mídias.   
Alarmes

Status para o atendimento gerado pelo sistema para o chefe do atendente quando vence o prazo para a resolução de um atendimento específico (dispara o alarme).   
Documentação

Status para o atendimento gerado para os documentadores solicitando verificação na Ajuda do aplicativo.   
Comercial (uso do Depto. Comercial):

Uso exclusivo do Departamento Comercial.   
Homologação

Utilizado pelos homologadores para informar os problemas encontrados durante os testes dos aplicativos.   
Dica

Status para o atendimento requisitando o cadastro de uma nova dica ou pelo atendimento gerado quando é solicitada uma nova dica a partir da solução de um atendimento (clicando no ícone Requisição de Nova Dica).   
Melhorias Futuras

Utilizado para atendimentos que se referem a sugestões de aperfeiçoamento dos produtos, originadas internamente ou dos clientes, e que deverão ficar registradas sem data limite e/ou sem versão de liberação. Após classificar o atendimento com esse status, clique no botão "Aguardando Terceiros" e preencha a justificativa como "Analisando Proposta". O atendimento ficará entre os que estão aguardando terceiros na Árvore de Atendimentos da Visão de Atendimentos.  
Prioridade  
Selecione a prioridade do atendimento.  
**Atenção**

Veja abaixo a forma correta de utilizar cada opção para classificar a prioridade dos atendimentos:

* Baixa: Utilizado quando o problema não impede a operação do sistema e pode esperar um prazo mais longo para a solução.
* Normal: para problemas que possuem uma solução alternativa, não impedindo a operação do sistema. Podem esperar um prazo determinado sem gerar maiores transtornos ao cliente.
* Alta: utilizado quando existe uma solução alternativa que contorna o problema mas não é operacional, requerendo grande esforço para o cliente. A solução definitiva deverá ser implementada em curto prazo.
* Urgente: necessita de solução imediata pois o cliente está parado e não existe uma solução para contornar o problema.   
    
  Categoria Geral  
  Selecione a categoria geral. As categorias gerais são visíveis a todos os usuários, para classificar seus atendimentos.  
  Produto  
  Selecione o nome do aplicativo.   
  Detalhe do Produto  
  Selecione o módulo onde está localizado o problema relatado pelo cliente.  
  Cliente  
  Um atendimento pode ter como cliente os registros dos seguintes cadastros: Cliente / Fornecedor, Prospect / Suspect, Pessoa, Aluno ou Professor. A pesquisa para localizar o cliente pode ser realizada através do lookup informando os filtros de acordo com a real necessidade da organização, de forma rápida e precisa devido a possibilidade de realizar combinações de campos para resultados melhores, como por exemplo, por tipo de cliente e nome ou CPF/CNPJ.  
   No caso do cadastro de Cliente / Fornecedor, se o parâmetro "Não permitir cadastrar atendimentos para fornecedores" do CRM/TOTVS Aprovações e Atendimento estiver marcado, então a apresentação dos clientes será filtrada para não mostrar cliente que são fornecedores.   
  No cadastro de Prospect/Suspect, se o registro estiver com a opção "Inativo" marcada, também não será apresentado no lookup de cliente. Digite o código identificador do cliente e pressione a tecla TAB para que o sistema preencha com o respectivo nome (razão social). Ou, então, digite o nome do cliente (razão social), o sistema apresentará automaticamente, o código identificador do cliente.   
  Contato do cliente  
  O sistema exibe a tela de visão de cadastro do contato do cliente. Basta clicar duas vezes no nome para preencher o campo.   
  Para conseguir alterar ou excluir um contato com o cliente a seguinte regra deverá ser obedecida:
* O atendimento NÃO pode estar fechado/concluído e
* O atendente deve ser o responsável pelo contato com o cliente ou chefe do atendente que é responsável pelo contato com o cliente e
* O atendente deve ser o responsável pelo atendimento, isto é, o atendimento deve estar em poder do atendente ou chefe do atendente que é responsável pelo atendimento e
* O atendente ter permissão no perfil.   
  Para possibilitar a permissão é necessário que seja definido em Cadastros | Segurança | Perfis | Acesso a Menus no no acesso "Vincular/Associar cliente/representante ao atendimento"   
  Caso o atendente não possua permissão, o sistema permite que o mesmo preencha este campo apenas quando estiver abrindo um novo atendimento. Caso contrário, o atendente não consegue alterar o campo. O mesmo fica desabilitado.   
  **Atenção**  
  Apenas contatos de clientes cadastrados no TOTVS Aprovações e Atendimento podem ser editados e excluídos por esse aplicativo. Caso o contato tenha sido cadastrado no RMNucleus, o sistema não permite a edição e exclusão do contato pelo TOTVS Aprovações e Atendimento, é permitido apenas no RMNucleus. O sistema exibe tela com mensagem informando que o contato não pode ser excluído ou alterado, pois o mesmo não foi criado pelo TOTVS Aprovações e Atendimento. Além disso, o sistema não permite que sejam excluídos contatos que estão vinculados a algum atendimento.   
  Representante  
  Digite o código do representante e pressione a tecla TAB para que o sistema preencha com o respectivo nome. O sistema apresentará, automaticamente, o nome do representante.   
  **Observação**  
  Apenas atendentes que possuem permissão podem alterar o nome do representante. É necessário que seja definido em Cadastros | Segurança | Perfis | Acesso a Menus no no acesso "Vincular/Associar cliente/representante ao atendimento" a permissão para que o atendente vinculado a este perfil tenha permissão para alterar o nome do representante quando o atendimento for editado. Caso o atendente não possua permissão, o sistema permite que o mesmo preencha este campo apenas quando estiver abrindo um novo atendimento. Caso contrário, o atendente não consegue alterar o campo. O mesmo fica desabilitado.  
  Contato do representante  
  O sistema exibe a tela de visão de cadastro do contato do representante. Basta clicar duas vezes no nome para preencher o campo.   
  Apenas atendentes com permissão, conseguem alterar este campo. Para possibilitar a permissão é necessário que seja definido em Cadastros | Segurança | Perfis | Acesso a Menus no acesso "Vincular/Associar cliente/representante ao atendimento" a permissão para que o atendente vinculado a este perfil tenha permissão para alterar o nome do contato do representante quando o atendimento for editado. Caso o atendente não possua permissão, o sistema permite que o mesmo preencha este campo apenas quando estiver abrindo um novo atendimento. Caso contrário, o atendente não consegue alterar o campo. O mesmo fica desabilitado.   
  Lembrando que apenas atendentes com permissão conseguem incluir, alterar e excluir um contato do representante.   
  **Atenção**  
  Quando o contato do representante for excluído e esse contato estiver vinculado a algum atendimento, então o mesmo será colocado como inativo.  
  Tipo do Contato  
  Selecione qual a forma utilizada para solicitar o atendimento. Exemplos: "0800 Presidente", "Solicitação Interna", "Telefone Automático", "Web" etc.  
  Origem do contato  
  Selecione quem encaminhou o contato com o atendente: se foi o próprio cliente que entrou em contato, se foi através de representante ou se o contato teve origem interna.  
  Assunto  
  Mostra resumidamente o assunto pedido na solicitação.  
  **Atenção**  
  O botão a direita do campo "Assunto", ao ser clicado com o botão esquerdo do mouse invoca uma pesquisa de atendimentos que buscará todos os atendimentos com assunto igual ao assunto da ocorrência atual. Caso esse botão seja clicado com o botão direito do mouse são apresentadas as seguintes opções para refinar a pesquisa: "Expressão inteira no campo" e "Qualquer uma das palavras no campo". Cada uma dessas duas opções possuem as seguintes sub-opções que representam os campos em que o texto pode ser pesquisado: "Assunto", "Solicitação", "Discussão", "Solução" e "Todos acima".  
  Siga os próximos passos:  
  Avançar Etapa, permite que a ocorrência seja repassada automaticamente seguindo um fluxo de tarefas pré-determinado.   
  Permite o Repasse, da ocorrência para qualquer outro atendente mesmo que este seja de outra coligada.  
  Permite que o Atendimento seja Devolvido, ainda que você não tenha autorização de repasse para o destinatário. Antes de Repassar de Volta é obrigatório escrever a justificativa do repasse.  
  Atendimento Solucionado, e cujo cliente ainda não foi avisado.  
  Atendimento cujo Cliente foi Avisado, mas ainda não deu parecer sobre a solução apresentada.  
  Atendimento Confirmado, Atendimento solucionado e cujo cliente foi avisado e aprovou a solução apresentada.   
  Atendimento Agendado, cujo cliente foi avisado dos prazos do agendamento e concordou com ele.  
  Atendimento Ainda não Solucionado, Atendimento pendente.  
  Atendimento Cancelado, Não necessita atuação  
  Atendimento Paralizado, aguardando a intervenção de outros atendentes (diretoria, PDE, etc) ou procedimentos (Back up, teste, etc) para ser resolvido.  
  **Enviar E-mail sobre o atendimento**  
  O recurso de envio de e-mail permite que qualquer atendente envie informações relativas às ocorrências através de e-mail, para atendentes e/ou clientes (de qualquer tipo: Prospect, Suspect, Aluno, Professor, Cliente, Pessoa). Através desse recurso, pode-se acrescentar no e-mail informações contidas nos campos: solicitação e solução e ainda um breve resumo da ocorrência em questão, um ou vários arquivos arquivos também podem ser anexados ao e-mail.  
  Os anexos podem ser inseridos ou removidos através dos botões "" e "", eles adicionados na tela para facilitar a manipulação dos anexos. Ao clicar no botão "" uma caixa de diálogo será aberta para escolha do arquivo e uma lista será apresentada com os arquivos já foram anexados ao envio do e-mail. O botão "" remove o arquivo que estiver selecionado na caixa que lista os arquivos.  
  No lookup do campo "Com cópia", uma grid é aberto contendo os atendentes e seus respectivos e-mails. Ao selecionar os atendentes seus e-mails serão carregados automaticamente no campo. Também é possível digitar os e-mails diretamente no campo "Com cópia".  
  O e-mail enviado permite que os atendentes e/ou cliente atualizem-se sobre a ocorrência, obtendo informações importantes sobre a mesma.  
  Nos parâmetros gerais do sistema, um relatório global personalizado pode ser vinculado para que o modelo de e-mail contenha as informações relevantes para empresa. Caso não possua este parâmetro preenchido, o sistema busca o modelo fixo do sistema.  
    
  Passo a Passo:  
    
  Crie um relatório personalizado. (Gestão | RM Reports)  
  Associe o relatório personalizado. (Configurações | Parâmetros | E-mail | E-mail enviado por dentro do e-mail).  
  Após procedimentos de abertura do atendimento, clique no botão: Enviar e-mail sobre o atendimento (na edição do atendimento).  
  Verifique o e-mail enviado.  
  As informações do e-mail respeitarão e seguirão o modelo personalizado.  
    
  **Função de Fórmula para enviar cópia do e-mail de repasse**  
  É possível utilizar uma função de fórmula para enviar um novo email de repasse com as mesmas informações do email de repasse normal, para algum outro destinatário definido pelo usuário. Para isso, o tipo de repasse do tipo de atendimento deve ser "fórmula". A função de fórmula para esse procedimento é a ENVIAEMAILREPASSE, que possui os seguintes parâmetros:  
  • fromAddress - Endereço de email do remetente.  
  • to - Endereço de email do destinatário.  
  • cc - Endereço de email para enviar uma cópia do email  
  • repasse - Atendente ao qual o repasse será realizado, lembrando que isso será apenas para informações do email, não definirá de  ato quem receberá o atendimento, esse parâmetro pode ter dois formatos, '1;3' nesse caso significa que o atendimento foi repassado para o atendente 3 da coligada 1, ou '5' nesse caso significa que o atendimento foi repassado para o grupo de atendentes 5 da coligada do contexto.  
  Exemplo prático de utilização: ENVIAEMAILREPASSE('remetente@totvs.com.br', 'destinatario@totvs.com.br', 'copia@totvs.com.br', '1;3'). Essa função de fórmula ira enviar um email de repasse para o endereço de email destinatario@totvs.com.br com cópia para o email copia@totvs.com.br como se fosse enviado pelo endereço de email remetente@totvs.com.br e sendo um repasse feito para o atendente de código 3 da coligada 1.  
  **Criação da função de fórmula ANALISAR**  
  Ao utilizar um avanço de etapas de um atendimento cujo repasse seja por fórmula, caso esse avanço não estiver ocorrendo como deveria, é possível verificar uma possível inconsistência envolvendo variáveis, ou quando quiser verificar o valor de até 4 variáveis, pode ser usada a função de fórmula ANALISAR, ela recebe 4 parâmetros do tipo texto, interrompe a execução da fórmula e concatena as 4 variáveis para exibi-las ao usuário separadas por espaço. Segue abaixo exemplo de sua utilização: DECL VAR1; DECL VAR2; DECL VAR3; DECL VAR4; SETVAR(VAR1, '85'); SETVAR(VAR2, '27'); SETVAR(VAR3, '61'); SETVAR(VAR4, '49'); ANALISAR(VAR1, VAR2, VAR3, VAR4); O resultado seria a mensagem: 85 27 61 49, isso agiliza a analise caso um consultor ou atendente do suporte precisar verificar essas 4 variáveis em uma unica execução.   
  **Enviar e-mail de abertura de atendimento ao cliente**  
  Este recurso permite que seja encaminhado um e-mail para o contato do cliente avisando que foi aberto o atendimento referente à solicitação. Para os casos que não tiverem o contato preenchido, o e-mail será encaminhado diretamente para o endereço informado no cadastro. Caso o e-mail não seja válido o sistema alertará que a ação não foi completada. Veja a verificação de acordo com os tipos de cliente:  
  Cliente - A busca do endereço de e-mail é feita a partir do "Contato com o Cliente" caso não exista, o sistema irá buscar do próprio e-mail do Cliente.  
  Prospect: A busca do endereço de e-mail é feita diretamente no cadastro do Prospect/Suspect.  
  Suspect: A busca do endereço de e-mail é feita diretamente no cadastro do Prospect/Suspect.  
  Aluno: A busca do endereço de e-mail é feita verificando o cadastro do aluno e o cadastro da pessoa relacionada.  
  Professor:  A busca do endereço de e-mail é realizada verificando o cadastro do professor e o cadastro da pessoa relacionada.  
  Pessoa: A busca do endereço de e-mail é feita diretamente do cadastro da pessoa.  
  **Atenção**
* Qualquer envio de e-mail do sistema, está sujeito as regras do servidor SMTP configurado nos parâmetros globais, para mais detalhes, veja o seguinte link: <https://tdn.totvs.com/display/public/LRM/Envio+de+email+-+LINHA+RM>
* O sistema envia o e-mail apenas quando o contato do cliente tenha endereço de e-mail cadastrado. Caso não tenha, o sistema exibe mensagem informando que o contato do cliente não possui endereço de e-mail.
* Caso o e-mail seja enviado será registrado na discussão que foi enviado e-mail de abertura de atendimento para o cliente.

* Esse botão só estará habilitado, quando o atendimento não estiver em modo de inserção e possuir contato do cliente cadastrado.  
  Consultar FAQ/Dicas  
  Permite consultar FAQ/Dicas já cadastradas.  
  **Dica**  
  Quando um atendimento é solucionado por FAQ's (perguntas mais freqüentes) ou Dicas, o sistema preenche automaticamente o campo Discussão informando que a solução foi apresentada e no campo Solução os detalhes da informação da FAQ/Dica indicando o resultado final.  
  Requisitar o cadastro de uma nova FAQ\Dica de acordo com a solicitação e solução do atendimento  
  Permite requisitar o cadastro de uma FAQ's (Perguntas mais freqüentes) e as dicas dos aplicativos.  
  Cadastrar FAQ\Dicas  
  Permite cadastrar uma FAQ's (Perguntas mais freqüentes) e as dicas dos aplicativos.  
  Lista a relação de todos os atendimentos já abertos pelo cliente do atendimento atual  
  Ao clicar neste ícone, o sistema traz uma relação com todos os atendimentos abertos pelo cliente do atendimento atual. Esta funcionalidade utiliza o mesmo mecanismo de pesquisa de atendimentos, isto é, internamente o sistema passará para a pesquisa de atendimentos o código do cliente do atendimento atual e a partir deste código de cliente o motor da pesquisa se encarregará de efetuar a busca na base de dados e apresentará, em uma nova tela de visão de atendimentos, os atendimentos já abertos pelo cliente.  
  **Acompanhamento**  
    
  Solicitação   
  Nesta aba podemos visualizar, inserir e alterar as informações que foram referentes à Solicitação da ocorrência. Nela é destacado o problema que está ocorrendo, a melhoria sugerida ou qualquer motivo descrito na abertura do atendimento.   
  Discussão   
  Nesta aba podemos visualizar, inserir e alterar as informações referentes ao andamento da ocorrência. Podemos verificar quais foram os passos, os procedimentos e análises sobre à solicitação.   
  Ao inserir um texto no campo "Discussão", são registradas além do texto, informações sobre: o atendente/usuário que inseriu o texto, a data/hora, o tipo de inserção (Log, Repasse, Possível Solução), e caso exista, informações sobre o fluxo de trabalho que o atendimento percorreu.  
    
  Também é possível tornar a discussão que está sendo inserida "publicável". A discussão que for publicável estará disponível no Fórum.  
  Solução  
  Nesta aba podemos cadastrar as soluções apresentadas, os testes realizados e quaisquer outros comentários dos atendentes relativos à solução apresentada à solicitação da ocorrência.  
  **Observação**  
  Esta funcionalidade está disponível na tela de visão de atendimentos, dessa forma não será necessário editar o atendimento para sua visualização. Este recurso foi disponibilizado visando agilizar o processo e melhorar a usabilidade do sistema. O botão de "Avançar Etapas" também está visível neste anexo e permite verificar os campos obrigatórios/necessários para o avanço do atendimento e alerta sobre o seu preenchimento.   
  **Dados Adicionais**  
  Esta pasta permite acrescentar dados adicionais ao atendimento.   
  Siga os próximos passos:  
  Abertura Campo preenchido automaticamente pelo sistema com a data e hora de abertura do atendimento.  
  Fechamento Campo preenchido automaticamente pelo sistema com a data e hora de fechamento do atendimento (data e hora em que o atendimento foi "Concluído Respondido").  
  Data Primeiro Contato  
  Registro da data e hora da primeira ligação de retorno do cliente. Utilizado para atendimentos abertos através da caixa postal. Para atendimentos que não foram abertos através da caixa postal, o campo será preenchido com a data e hora de abertura. Para atendimentos abertos através da caixa postal, o registro do primeiro retorno é feito clicando-se no ícone representado abaixo. Após registrar o primeiro retorno, o ícone ficará desabilitado.  
  Agendamentos Apresenta o registro do número de vezes em que o atendimento já foi agendado, ou seja, incrementado automaticamente cada vez que for acionado o botão Agendado (respondido)  
  Nível de Acesso  
  Preencha neste campo, o nível de acesso da ocorrência editada.  
  Para que a ocorrência editada seja vista apenas por um grupo restrito de atendentes, tornando desta forma, o atendimento sigiloso. Devemos definir em: Cadastros | Atendentes | Atendentes os níveis de acesso que cada atendente possui.   
  Após a definição dos níveis dos atendentes, devemos preencher no campo Nível de Acesso na edição da ocorrência, qual o nível que a mesma possui.   
  O atendente só enxergará os atendimentos com nível de acesso menores ou iguais ao seu, ou atendimentos com nível de acesso superior, desde que este atendimento esteja sob a responsabilidade do atendente. Nem mesmo os atendentes que são chefes ou o responsável pelo contato com o cliente conseguem visualizar a ocorrência se a mesma possuir um nível de acesso maior que a do atendente definida no cadastro de atendentes.   
  Apenas os chefes têm permissão para alterar este campo na edição da ocorrência.   
  Responsável pela abertura  
  Apresenta os campos somente leitura: código e o nome do atendente responsável pela abertura do atendimento visando auxiliar no controle das informações. Mesmo em caso de repasse do atendimento o nome do atendente prevalece. Este campo é visível para atendimentos winforms e atendimentos web.  
  **Dica**  
  Podemos definir um nível de acesso para a ocorrência selecionando uma classificação que possua nível. Dessa forma, a ocorrência terá o mesmo nível que a classificação estiver. Basta cadastrarmos um novo atendimento e selecionarmos a classificação desejada ou mudarmos a classificação da ocorrência para outra que possua o nível desejado.  
  Caixa Postal  
  Número de mensagens gravadas pelo cliente (correspondentes a este atendimento) na caixa postal de voz do atendente. Se este campo estiver preenchido o sistema não permite que o atendimento seja repassado, agendado ou concluído. As mensagens devem ser ouvidas e o campo zerado para que o sistema permita.  
  **Parâmetros**  
  Selecione nesta janela o campo adicional necessário para o tipo de atendimento em questão. Por exemplo, caso o tipo de atendimento necessite do telefone do endereço de entrega pode ser cadastrado esse campo nos Parâmetros do cadastro de Atendimentos e selecioná-lo nesta janela.  
  Em Cadastro | Campos Complementares | Atendimento, podemos cadastrar campos relacionados à ocorrência, que por ventura não existem no aplicativo para atender a qualquer necessidade específica.   
  Após o cadastro dos campos, para visualizarmos os mesmos, basta editarmos qualquer ocorrência e acessarmos a aba "Campos Complementares". Poderemos então, preencher os campos de acordo com a nossa necessidade.  
  **Atenção**  
  Se não houver nenhum campo complementar cadastrado ou os mesmos não estiverem ativos, a aba "Campos Complementares" da edição do atendimento não ficará visível.  
  **Campos Complementares**  
    
  Em Cadastro | Campos Complementares | Atendimento, podemos cadastrar campos relacionados à ocorrência, que por ventura não existem no aplicativo para atender a qualquer necessidade específica.   
  Após o cadastro dos campos, para visualizarmos os mesmos, basta editarmos qualquer ocorrência e acessarmos a aba "Campos Complementares". Poderemos então, preencher os campos de acordo com a nossa necessidade.  
  **Atenção**  
  Se não houver nenhum campo complementar cadastrado ou os mesmos não estiverem ativos, a aba "Campos Complementares" da edição do atendimento não ficará visível.

  ---

  **Informações Complementares**  
    

  Informações Estratégicas   
  Ações de Serviços   
  Apontamento   
  Atendimentos relacionados   
  Arquivos Anexos do Atendimento   
  Histórico de Visualização dos Atendimentos na Fila  
  Texto Acompanhamento   
  Entendimento   
  Parâmetros   
  Histórico de Repasses   
  Histórico de Etapas   
  Histórico de Status   
  Movimento  
  Discussões do Atendimento  
  Informações do Aluno

  **Como Fazer**

  Repassar Atendimento  
  Repassar de Volta   
    
  Agendado Respondido   
    
    
    
    
  Aguardar Terceiros   
  Cancelar atendimento   
  Alteração de Parâmetros do Atendimento   
  Copiar Parâmetros entre Atendimentos   
    
  Gerar Atendimento A Partir de Outro   
  Relacionamento de Atendimentos   
  Transferência de Atendimentos   
  Inserir Entendimento para Atendimentos Selecionados   
  Imprimir Ocorrências   
  Adicionar Discussão  
  Adicionar Solução   
  Alterar Solução   
  Alterar Discussão   
  Alterar Solicitação   
  Alterar Status do Atendente   
  Atendimento em uma Fila   
  Adicionar Atendimentos ao Planejamento   
  Gerar Campanha a partir do Cliente  
  Estatísticas
