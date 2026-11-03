---
content_hash: 7d5d2439fc048430c28c1014a660ad80f11251be4a46c1ce07b079582838695d
fetched_at: '2026-06-29T00:09:36.074459+00:00'
page_id: '425459465'
product: rm
source: tdn-rm
title: Modelos de Atendimento
type: documentation
url: https://tdn.totvs.com/display/LRM/Modelos+de+Atendimento
version: 7
---

**Modelos de Atendimento**

---

Este cadastro serve para criação de atendimentos modelo para geração de "Padrões de atendimento". A tela de cadastro de modelo de atendimento é muito parecida com o cadastro normal de atendimentos exceto por não ter todos os campos disponíveis e não seguir nenhuma regra ao salvar.

**Observação**  
   
O sistema permite que usuário que não possua atendente associado possa realizar o cadastro de modelos porém, o atendimento será gerado com a localidade do usuário e caso o mesmo não possua a primeira localidade encontrada na tabela HLOCALIDADE será utilizada. Somente os usuários que possuam atendentes nessa localidade estarão aptos a visualizar esses modelos em outras funcionalidades do sistema como: Grupo de E-mail , Tipo de Atendimento , Templates (RM Agilis Web).  
Através do cadastro é possível controlar:

**Identificação**   
   
Esta pasta permite editar os dados de identificação dos atendimentos, do aplicativo e do contato.

Abaixo é mostrada a descrição dos campos presentes nesta pasta e o procedimento correto para preenchê-los.

Opções da caixa Família do Atendimento:

**Atendimento**

Número criado automaticamente pelo sistema após salvar um novo atendimento. É único. Deve sempre ser informado ao cliente para que ele possa acompanhar a evolução do atendimento.

**Prazo limite final**

Você pode definir um prazo limite (agendar) para a resolução do atendimento (após clicar no botão Agendado (a responder) Ao definir este prazo, todas as pessoas envolvidas no processo do atendimento (os atendentes anteriores e aquele responsável pelo contato com o cliente) receberão um e-mail informando este prazo.

**Categoria Individual**

Selecione a categoria individual. As categorias individuais são visíveis a todos os usuários, para classificar seus atendimentos.

**Grupo de Atendimento**

No cadastro de um novo atendimento, pode ser definido se o mesmo seguirá um fluxo de tarefas pré-definido.

Para que o atendimento siga um fluxo de tarefas, é necessário que seja definido no cadastro do mesmo, qual o grupo de atendimentos ele vai fazer parte.

Selecione neste campo o grupo de atendimento que a ocorrência em questão pertencerá.

Este campo ficará habilitado apenas quando for cadastrado um novo atendimento, na edição do mesmo não é possível o preenchimento ou alteração deste campo.

**Tipo de Atendimento**

Para que o atendimento siga um fluxo de tarefas é necessário também que seja definido qual o tipo de atendimento ele vai ser. Para cada tipo, são definidos tarefas e o fluxo delas.

O atendimento poderá ser repassado automaticamente para um atendente que é responsável por uma tarefa e após a conclusão desta tarefa o atendimento pode ser repassado novamente para outro atendente, ou não, isso vai depender se ele for responsável pela próxima tarefa também.

Todas essas informações são cadastradas no tipo de atendimento.

Selecione neste campo o tipo de atendimento que a ocorrência em questão vai ser.

O cadastro do tipo de atendimento é feito em: Cadastros | Atendimentos | Tipos de Atendimentos.

Este campo ficará habilitado apenas quando for cadastrado um novo atendimento, na edição do mesmo não é possível o preenchimento ou alteração deste campo.

**Código de Classificação**

Este campo permite classificar os atendimentos. Tal classificação é importantíssima para que as outras pessoas envolvidas na resolução possam saber a origem do problema. Veja opções abaixo. As opções estão posicionadas em ordem alfabética para facilitar a escolha da mesma.

**Atenção!**

Veja abaixo a forma correta de utilizar cada opção para classificar os atendimentos:

**A Classificar**

Atribuído automaticamente pelo sistema para atendimentos novos, manuais ou automáticos. Sempre que tentar salvar um atendimento com esta classificação, será emitido um aviso ao usuário para que a mude. Caso contrário, o alarme disparará a cada 2 dias.

**BUG**

Quando o motivo/solicitação do atendimento for resolvido com uma nova versão do aplicativo.

**Implementação:**

Sempre que o sistema não possuir recurso para atender à solicitação do cliente.

**Dúvida**

Para os questionamentos sobre os aplicativos (se existir no aplicativo um recurso para solucionar o questionamento efetuado pelo cliente), ou seja, sempre que não for um erro (BUG) ou uma Implementação. Também deverão ser classificados como dúvida os erros não simulados pelos técnicos.

**Cancelado**

Para cancelar uma ocorrência.

**Instalação do Aplicativo**

Quando for solicitado ao Departamento de Suporte, no caso dos aplicativos DOS, ou ao Departamento de Implantação, no caso dos aplicativos RM, a instalação do sistema. É utilizado pelo Departamento Comercial, quando o cliente adquire a licença de uso.

**Assuntos não relacionados aos aplicativos**

Quando ocorrerem problemas de ambiente (rede, banco de dados, configurações de equipamentos: memória, config, autoexec etc), solicitação de senha, arquivo Aponta e informações sobre o código da ultima versão lançada.

**Versão/Senha/Aponta**

Quando o cliente solicita soluções referentes às versões liberadas, senhas e problemas com o arquivo Aponta.

**Elaboração de relatórios**

Para solicitações referentes à geração de relatórios específicos da situação da empresa.

**RUNTIME**

Para solicitações referentes às mensagens emitidas pelo sistema e que são específicas do compilador (Ex.: Pascal). Para cada número de Runtime informado existe uma relação com a solução do problema.

**RECLAMAÇÃO 0800/INTERNET**

Atendimentos ao cliente através do número 0800 ou pelo site da TOTVS, através de e-mail. Utilizado pelo Departamento de Marketing.

**Restaurar Backup/CORPORE**

Solicitações de restauração de Backup's de bases CORPORE para simulações de problemas na base de dados do cliente.

**Visita técnica**

Utilizado para solicitações que só podem ser resolvidas com uma visita do técnico atendente ao cliente, para solução In House. Normalmente, transcreve-se o Relatório de Atendimento Técnico (RAT) no atendimento.

**BUG/SGBD**

Solicitações devido a problemas no Sistema de Gerenciamento de Banco de Dados.

**LIBERAÇÃO DE VERSÃO/FTP:**

Solicitação de disponibilidade de versões e/ou bases no FTP. Utilizado pelo Departamento Administrativo.

**GERAÇÃO DE MÍDIA/CD**

Solicitação de geração de CD's ou mídias.

**Alarmes**

Status para o atendimento gerado pelo sistema para o chefe do atendente quando vence o prazo para a resolução de um atendimento específico (dispara o alarme).

**Documentação**

Status para o atendimento gerado para os documentadores solicitando verificação na Ajuda do aplicativo.

**Comercial (uso do Depto. Comercial):**

Uso exclusivo do Departamento Comercial.

**Homologação**

Utilizado pelos homologadores para informar os problemas encontrados durante os testes dos aplicativos.

**Dica**

Status para o atendimento requisitando o cadastro de uma nova dica ou pelo atendimento gerado quando é solicitada uma nova dica a partir da solução de um atendimento (clicando no ícone Requisição de Nova Dica).   
Melhorias Futuras

Utilizado para atendimentos que se referem a sugestões de aperfeiçoamento dos produtos, originadas internamente ou dos clientes, e que deverão ficar registradas sem data limite e/ou sem versão de liberação. Após classificar o atendimento com esse status, clique no botão "Aguardando Terceiros" e preencha a justificativa como "Analisando Proposta". O atendimento ficará entre os que estão aguardando terceiros na Árvore de Atendimentos da Visão de Atendimentos.  
Prioridade  
Selecione a prioridade do atendimento.

**Atenção**

Veja abaixo a forma correta de utilizar cada opção para classificar a prioridade dos atendimentos:

**Baixa:** Utilizado quando o problema não impede a operação do sistema e pode esperar um prazo mais longo para a solução.

**Normal:** para problemas que possuem uma solução alternativa, não impedindo a operação do sistema. Podem esperar um prazo determinado sem gerar maiores transtornos ao cliente.

**Alta**: utilizado quando existe uma solução alternativa que contorna o problema mas não é operacional, requerendo grande esforço para o cliente. A solução definitiva deverá ser implementada em curto prazo.

**Urgente**: necessita de solução imediata pois o cliente está parado e não existe uma solução para contornar o problema.   
  
**Categoria Geral**

Selecione a categoria geral. As categorias gerais são visíveis a todos os usuários, para classificar seus atendimentos.

**Produto**

Selecione o nome do aplicativo.

**Detalhe do Produto**

Selecione o módulo onde está localizado o problema relatado pelo cliente.

**Cliente**

Um atendimento pode ter como cliente os registros dos seguintes cadastros: Cliente / Fornecedor, Prospect / Suspect, Pessoa, Aluno ou Professor. A pesquisa para localizar o cliente pode ser realizada através do lookup informando os filtros de acordo com a real necessidade da organização, de forma rápida e precisa devido a possibilidade de realizar combinações de campos para resultados melhores, como por exemplo, por tipo de cliente e nome ou CPF/CNPJ. No caso do cadastro de Cliente / Fornecedor, se o parâmetro "Não permitir cadastrar atendimentos para fornecedores" do TOTVS Aprovações e Atendimento estiver marcado, então a apresentação dos clientes será filtrada para não mostrar cliente que são fornecedores. No cadastro de Prospect/Suspect, se o registro estiver com a opção "Inativo" marcada, também não será apresentado no lookup de cliente. Digite o código identificador do cliente e pressione a tecla TAB para que o sistema preencha com o respectivo nome (razão social). Ou, então, digite o nome do cliente (razão social), o sistema apresentará automaticamente, o código identificador do cliente.

Contato do cliente

O sistema exibe a tela de visão de cadastro do contato do cliente. Basta clicar duas vezes no nome para preencher o campo.   
Para conseguir alterar ou excluir um contato com o cliente a seguinte regra deverá ser obedecida:

* O atendimento NÃO pode estar fechado/concluído e
* O atendente deve ser o responsável pelo contato com o cliente ou chefe do atendente que é responsável pelo contato com o cliente e
* O atendente deve ser o responsável pelo atendimento, isto é, o atendimento deve estar em poder do atendente ou chefe do atendente que é responsável pelo atendimento e

O atendente ter permissão no perfil.   
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

**Siga os próximos passos:**

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

Enviar E-mail sobre o atendimento

O recurso de envio de e-mail permite que qualquer atendente envie informações relativas às ocorrências através de e-mail, para atendentes e/ ou clientes. Através desse recurso, pode-se acrescentar no e-mail informações contidas nos campos: solicitação e solução e ainda um breve resumo da ocorrência em questão.

O e-mail enviado, permite que os atendentes e/ou cliente atualizem-se sobre a ocorrência, obtendo informações importantes sobre a mesma.  
Enviar e-mail de abertura de atendimento ao cliente

Ao clicar nesse botão será enviando um e-mail para o contado do cliente avisando que foi aberto atendimento referente à solicitação dele e informa o número do atendimento.

**Atenção**

O sistema envia o e-mail apenas quando o contato do cliente tenha endereço de e-mail cadastrado. Caso não tenha, o sistema exibe mensagem informando que o contato do cliente não possui endereço de e-mail.

Caso o e-mail seja enviado será registrado na discussão que foi enviado e-mail de abertura de atendimento para o cliente.

Esse botão só estará habilitado, quando o atendimento não estiver em modo de inserção e possuir contato do cliente cadastrado.

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

Atendimentos - Dados Adicionais   
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

**Dica**

Podemos definir um nível de acesso para a ocorrência selecionando uma classificação que possua nível. Dessa forma, a ocorrência terá o mesmo nível que a classificação estiver. Basta cadastrarmos um novo atendimento e selecionarmos a classificação desejada ou mudarmos a classificação da ocorrência para outra que possua o nível desejado.  
Caixa Postal  
Número de mensagens gravadas pelo cliente (correspondentes a este atendimento) na caixa postal de voz do atendente. Se este campo estiver preenchido o sistema não permite que o atendimento seja repassado, agendado ou concluído. As mensagens devem ser ouvidas e o campo zerado para que o sistema permita.
