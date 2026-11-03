---
content_hash: 1b000e036a4e0fc60923f687a6d7bb55f7449b3d636782df230d6669d0e0c99b
fetched_at: '2026-06-29T00:11:55.762678+00:00'
page_id: '863917135'
product: rm
source: tdn-rm
title: 08. Mensagens Pessoais
type: documentation
url: https://tdn.totvs.com/display/LRM/08.+Mensagens+Pessoais
version: 59
---

A funcionalidade tem como objetivo viabilizar uma comunicação rápida, segura e simultânea, permitindo a troca de mensagens entre professores e a comunidade acadêmica, bem como entre alunos e/ou responsáveis e professores.

Permissão de acesso

Para acessar a funcionalidade, o perfil deverá ter a permissão em: **Serviços Globais | Segurança | Perfis | "Sistema" Educacional | eduCONNECT | Mensagens Pessoais**

**Perfil: Alunos para os Professores (da Turma/disciplina)                                                              Perfil: Pais para os Professores (da Turma/disciplina)**

**Perfil: Pais para os Professores                                                                                                         Perfil: Responsável Acadêmico para os Professores**

             

**Perfil: Responsável Financeiro para os Professores** **Perfil: Professores para os:****Alunos,** **Pais (Pais e/ou Mãe),****Responsáveis Acadêmicos e Financeiros**

false

O envio de mensagens é controlado por perfil, permitindo à instituição definir quais usuários estão autorizados a realizar a troca de mensagens e comunicados.

Para o correto funcionamento da funcionalidade, é necessário configurar as credenciais de acesso ao banco de dados, garantindo permissão às tabelas do módulo Educacional. Além disso, o perfil do usuário deve possuir permissão no seguinte caminho: **Serviços Globais > Segurança > Acesso > Código de Acesso > eduCONNECT**.

Configuração para clientes que não utilizam o protocolo HTTPS

Caso a instituição não utilize o protocolo HTTPS, é obrigatório ajustar o arquivo **Web.config** do TOTVS Educa Mobile. Para isso, localize e altere a seguinte configuração:

A TOTVS recomenda a utilização do protocolo HTTPS no produto TOTVS Educa Mobile.

Ambientes com Load Balance

**Atenção ao utilizar Proxy Reverso ou Load Balancer:**  
Caso a instituição utilize redirecionamento de tráfego, a comunicação interna entre o balanceador e o servidor do Educa Mobile pode ocorrer por meio do protocolo HTTP. Nessa situação, é necessário ajustar a configuração abaixo no arquivo **Web.config** para evitar falhas de conexão:

RequiredSSLMsgPessoal = false

Configuração do parâmetro para envio de Mensagens e Comunicados com anexos

O envio de arquivos (foto/documento) é definido por perfil, estando vinculado às permissões de envio de mensagens para grupos de usuários.

Para habilitar essa funcionalidade, acesse o caminho: **Serviços Globais > Segurança > Perfis > Sistema Educacional > eduCONNECT > Mensagens Pessoais > Enviar anexo**.

O ícone de envio de anexo será habilitado quando o usuário possuir pelo menos um perfil com permissão para realizar o envio de anexos.

**Perfil: Alunos para os Professores (da Turma/disciplina)                                                              Perfil: Pais para os Professores (da Turma/disciplina)**

**Perfil: Pais para os Professores                                                                                                          Perfil: Responsável Acadêmico para os Professores**

              

**Perfil: Responsável Financeiro para os Professores** **Perfil: Professores para os:****Alunos,****Pais e Mães,****Resp. Acadêmicos e Financeiro**

Parametrização de anexo

Para configurar o envio de anexos no Portal Gestão Educacional e no eduCONNECT, acesse: **TOTVS Gestão Educacional > Configurações > Parâmetros > Mensagens Pessoais**. Nessa tela, é possível definir as permissões e restrições aplicáveis aos arquivos anexados às mensagens.

Listar as turmas/disciplinas disponíveis para Mensagens e Comunicados

O sistema listará apenas as turmas/disciplinas que atendam às seguintes regras:

* O período letivo deve estar com a opção **“Exibe no Portal” marcada**.
* A exibição de turmas/disciplinas gerenciais e/ou gerenciadas seguirá a configuração do parâmetro:  
  **Educacional > Configurações > Parâmetros > Geral (1/6) > Utilizar turma/disciplina gerencial na digitação de notas, faltas, avaliação, frequência diária, plano de aula, upload de materiais no portal e mensagem pessoal no Meu eduCONNECT**.

De acordo com a configuração desse parâmetro:

* **Quando marcado:** Será exibida apenas a turma/disciplina gerencial, apresentando a relação de alunos matriculados (com usuários gerados) nas turmas gerenciadas.
* **Quando desmarcado:** Serão exibidas as turmas/disciplinas gerenciadas individualmente, apresentando a relação de alunos matriculados em cada turma separadamente.
Visualização de Mensagens e Comunicados

As mensagens pessoais e os comunicados estarão disponíveis no menu **Mensagens**. O menu **Mensagens** não exibe contador de mensagens não lidas ao ser acessado. A quantidade de mensagens não lidas é apresentada no painel de mensagens.

* Quando a mensagem for um comunicado, será exibido o ícone de megafone, juntamente com o assunto, a primeira linha do texto e o horário de envio do comunicado, conforme o exemplo abaixo:

* Quando a mensagem for pessoal, serão exibidos a foto, o nome e a primeira linha do texto do usuário com quem se está conversando, além do horário de envio da mensagem, conforme o exemplo abaixo:

Nessa tela, o usuário pode realizar buscas por **nome, assunto ou texto da mensagem**. Para isso, basta digitar uma palavra no campo **Buscar**, com no mínimo 5 caracteres, conforme o exemplo abaixo:

Detalhes da conversa – Mensagem pessoal

Ao selecionar uma mensagem pessoal no painel de mensagens, o sistema exibirá o histórico de conversas entre o usuário e o contato selecionado.

### **Cabeçalho**

Será exibido o nome do usuário participante da conversa.

### **Área de mensagens**

As mensagens serão apresentadas em formato de conversa, com a seguinte disposição:

* Mensagens enviadas pelo usuário: alinhadas à direita;
* Mensagens recebidas: alinhadas à esquerda.

Inicialmente, serão carregadas as **10 mensagens mais recentes**.

Ao realizar o gesto de **puxar para baixo (pull to refresh)**, o sistema carregará as **10 mensagens anteriores**, permitindo a navegação contínua no histórico.

### **Envio de mensagem**

Na parte inferior da tela, será exibida a barra de envio, contendo:

* Campo para digitação da mensagem;
* Botão para anexar arquivos;
* Botão para envio da mensagem.

Detalhes da conversa – Comunicados

Ao selecionar um comunicado no painel de mensagens, o sistema exibirá as mensagens relacionadas ao mesmo **assunto**, agrupando todos os comunicados enviados sob esse critério em uma única visualização.

### **Cabeçalho**

Será exibido o título fixo: **“Comunicado”**.

### **Área de mensagens**

Serão exibidas as mensagens dos comunicados com o mesmo assunto.

* Inicialmente, serão carregadas as **10 mensagens mais recentes**;
* Ao realizar o gesto de **puxar para baixo (pull to refresh)**, o sistema carregará as **10 mensagens anteriores**, permitindo a navegação contínua no histórico;
* Ao lado da data de cada mensagem, será exibido um ícone que permite visualizar os **destinatários do comunicado**.

### **Ações disponíveis**

* Na parte inferior da tela, será exibido o botão **“Novo comunicado”**, quando o usuário possuir permissão para envio, conforme os tipos de usuários envolvidos.

### **Visualização de destinatários**

Ao clicar no ícone exibido ao lado da data, o sistema apresentará a lista de destinatários do comunicado.

Após clicar no ícone ao lado da data, serão exibidos os destinatários conforme o exemplo abaixo:

Leitura de Mensagens e Comunicados

Somente serão marcadas como lidas as mensagens efetivamente visualizadas na conversa. Ao reabrir uma mensagem pessoal ou comunicado, o sistema exibirá o próximo item não lido. Esse item será marcado como lido quando o usuário sair da conversa.

Pré-visualização

Todos os itens citados que possuem pré-visualização (preview) serão exibidos inicialmente em baixa resolução, com o objetivo de otimizar o carregamento da página.

Após o download do anexo, o arquivo será armazenado no dispositivo e exibido em maior resolução.

> Os arquivos baixados serão salvos na pasta de cache do aplicativo.

Atualização automática de novas Mensagens e Comunicados (Push / Toast).

Os usuários destinatários serão notificados de novas mensagens e comunicados por meio de **Push Notification**, quando o aplicativo estiver em **segundo plano** ou **fechado**. Nesse cenário, o usuário receberá um Push com a mensagem ou comunicado.

Quando o texto da mensagem pessoal possuir mais de 10 caracteres, será exibida uma reticência (**...**) ao final da frase, indicando a existência de conteúdo adicional.

Quando a mensagem ou comunicado contiver apenas um anexo ou foto, o texto do Push será exibido como: **“Anexo”**.

### **Comportamento no aplicativo aberto**

* Se o usuário estiver com o menu **Mensagens** aberto, o painel de conversas será atualizado automaticamente. Nesse caso, o usuário não receberá Push nem banner temporário.
* Se o usuário estiver em outros menus (ex.: Notificações, Acadêmico ou Perfil), será exibido um **banner temporário** na barra superior do aplicativo, com duração de **3 segundos**, apenas para sinalização de nova mensagem ou comunicado.

false

O banner temporário tem como finalidade apenas sinalizar a chegada de uma nova mensagem ou comunicado. Para acessar o conteúdo, o usuário deverá entrar no menu **Mensagens**.

Diferentemente do Push Notification, o banner não realiza redirecionamento ao ser exibido; o redirecionamento ocorre somente ao clicar na notificação Push.

Envio de Mensagens e Comunicados

O processo de envio de mensagens e comunicados possui dois tipos:

* **Mensagens pessoais:** correspondem ao envio e recebimento de mensagens entre dois usuários.
* **Comunicados:** correspondem ao envio de mensagens para um grupo de usuários (mais de um destinatário).

falseFiltro de Usuários1Professores para Comunidade Acadêmica11Comunicados

Os comunicados consistem no envio de mensagens para mais de um usuário, podendo incluir alunos, professores, responsáveis acadêmicos e responsáveis financeiros.

Para professores, será disponibilizada a visualização das turmas sob sua responsabilidade, seguindo o mesmo critério utilizado no Portal do Professor (filtro de turmas do Diário de Classe), permitindo a seleção de turmas específicas ou de alunos/responsáveis individualmente.

A visualização é agrupada por turma, apresentando os alunos e seus respectivos responsáveis, permitindo que o professor selecione os destinatários da mensagem. O envio pode ser realizado para uma ou mais turmas, bem como para dois ou mais alunos e/ou responsáveis.

O filtro de perfis de usuários é apresentado de acordo com as permissões de envio de mensagens. Por exemplo, se o professor possuir permissão para enviar mensagens apenas para alunos e responsáveis financeiros, serão exibidos apenas esses filtros disponíveis para seleção.

Lista de turmas/disciplinas para serem exibidas

A lista de turmas/disciplinas exibida segue o mesmo critério utilizado no Portal.

* Serão apresentadas apenas as turmas/disciplinas cujo período letivo não esteja encerrado e que possuam a opção **“Exibir no Portal”** **marcada**.
Processo de envio de Comunicados

O professor pode enviar mensagens simultaneamente para vários usuários por meio do painel de **Comunicados**.

### **Passo a passo:**

1. Acessar o menu **Mensagens**;
2. Clicar no botão **Nova Mensagem**;
3. Selecionar o filtro de usuários;
4. Selecionar a(s) turma(s) correspondente(s) para o envio do comunicado;
5. Informar o **assunto** e o texto do comunicado;
6. (Opcional) Para visualizar a relação de possíveis destinatários, clicar sobre a turma e, em seguida, no ícone correspondente;
7. Clicar no botão **Enviar** para concluir o envio.

Atualização no fluxo de envio de Comunicados: Os comunicados enviados não serão mais atualizados no painel de visualização de conversas particulares do destinatário.

A partir das versões abaixo:

* **RM:** 12.12506.XXX
* **App Meu eduCONNECT:** 08.2601.01

Após o envio de um comunicado pelo professor, o conteúdo **não será incluído nas conversas pessoais** com os mesmos destinatários.

O comunicado somente ficará visível quando o professor acessar a conversa específica e consultar o histórico de mensagens.

> ### **Exemplo**
>
> Envio de um comunicado em que um dos destinatários já possui conversa pessoal ativa com o professor.

2Mensagens Pessoais

O processo de mensagens pessoais consiste na troca de mensagens entre dois usuários.

O professor poderá enviar a mensagem para um usuário, a partir do painel de mensagens. caso tenha uma conversa iniciada ou selecionar o usuário através do Painel de Mensagens e pela tela de filtro de usuários. Para o envio das mensagens é necessário que o professor tenha permissão para o envio de mensagens para o perfil do usuário desejado.

### **1) Envio de mensagens a partir do painel de mensagens**

1. Acessar o menu **Mensagens**;
2. Selecionar o usuário com quem deseja conversar;
3. Informar o texto da mensagem no campo **“Digite a mensagem”**;
4. Clicar no botão **Enviar**.

 

### **2) Envio de mensagens a partir do filtro de usuários**

1. Acessar o menu **Mensagens**;
2. Clicar no botão **Nova Mensagem**;
3. Selecionar o usuário para quem deseja enviar a mensagem;
4. Informar o texto da mensagem no campo **“Digite a mensagem”**;
5. Clicar no botão **Enviar**.

 

Quando o usuário destinatário visualizar as mensagens, será exibido um ícone ao lado do nome. .

Aluno que não tiver um usuário vinculado

O aluno que não possuir usuário vinculado será exibido de forma esmaecida e não poderá ser selecionado.

Envio de Mensagens e Comunicados com anexo

Para o envio de mensagens e comunicados com anexo, o usuário deve selecionar o ícone correspondente, disponível no campo de digitação da mensagem.

São três opções que ficam disponíveis ao clicar no envio de anexos:

### **1 - Foto (Câmera)**

Permite o envio de fotos capturadas diretamente pela câmera do celular.

### **2 - Documentos**

Permite o envio de documentos.

* É permitido apenas **um arquivo por envio**;
* Não é exibido preview do arquivo.

### **3 - Fotos**

Permite a seleção de múltiplas fotos e a inclusão de legenda para o conjunto de imagens.

**Regras de comportamento da legenda:**

* Se o usuário informar a legenda e posteriormente o texto da mensagem, o sistema considerará o **texto da mensagem**;
* Se o usuário informar o texto da mensagem e posteriormente a legenda, o sistema considerará a **legenda das fotos**.

Para documentos, não é possível informar legenda, pois a descrição do arquivo já contém as informações necessárias para os destinatários.

Será exibido um **carrossel com o preview** das imagens selecionadas.

> **Observação**
>
> Serão exibidos apenas arquivos com extensões parametrizadas nos parâmetros de **Mensagem Pessoal**. Caso nenhuma extensão seja configurada, todos os tipos de arquivos serão considerados.

Excluir anexo da Mensagens e Comunicados

O usuário de envio e/ou destinatário pode remover o arquivo selecionado ao clicar no ícone correspondente

Caso todos os arquivos sejam removidos, o sistema retornará para a tela de listagem de conversas.

2Alunos/Responsáveis para Professores21Mensagens/Comunicados

Os alunos e responsáveis (pais, responsáveis acadêmicos e responsáveis financeiros) podem enviar mensagens aos professores da turma/disciplina.

A lista de professores e disciplinas segue a seguinte ordem de exibição:

* Disciplinas em curso;
* Disciplinas cursadas (concluídas).

Permissão para o envio de mensagens

Para o envio de mensagens, é necessário que o aluno ou responsável possua permissão para envio de mensagens.

**Perfil: Alunos para os Professores (da Turma/disciplina)                                                          Perfil: Pais para os Professores (da Turma/disciplina)**

**Perfil: Pais para os Professores                                                                                                     Perfil: Responsável Acadêmico para os Professores**

         

**Perfil: Responsável Financeiro para os Professores**

Lista de professores disponível para a comunicação

O sistema deverá listar os professores que atendam aos seguintes critérios:

* Possuam usuário gerado;
* Estejam associados ao horário da turma/disciplina;
* Estejam dentro do período de vigência no cadastro da turma/disciplina;
* Possuam vínculo ativo na **Filial do Professor**, sendo que:
  + A filial associada à turma/disciplina do aluno deve estar ativa;
  + A chapa vinculada a essa filial deve estar com situação **Admitido** no RH.

Processo de envio de mensagens/comunicados de Aluno(s) para Professores

O aluno pode enviar mensagens para um ou mais professores a partir do **Painel de Mensagens**. Caso já exista uma conversa iniciada com o professor, o aluno poderá continuar a conversa diretamente ou utilizar o **Filtro de Professores** para iniciar um novo contato.

## **1) Listagem de turmas/disciplinas**

O sistema exibirá a lista de turmas/disciplinas disponíveis para que o aluno possa selecionar os professores para envio de mensagens.

## **2) Envio de mensagens (mensagem pessoal)**

1. Acessar o menu **Mensagens**;
2. Clicar no botão **Nova Mensagem**;
3. Selecionar o professor/disciplina com quem deseja conversar;
4. Clicar no ícone de nova mensagem;
5. Informar o texto da mensagem no campo **“Digite a mensagem”**;
6. Clicar no botão **Enviar**.

## **3) Envio de comunicados**

1. Acessar o menu **Mensagens**;
2. Clicar no botão **Nova Mensagem**;
3. Selecionar um ou mais professores/disciplinas;
4. Clicar no ícone de nova mensagem;
5. Informar o **assunto** e o texto do comunicado;
6. Clicar no botão **Enviar**.

Processo de envio de mensagens/comunicados – Responsáveis (Pais, Financeiro e Acadêmico) para Professores

O responsável pode enviar mensagens para um ou mais professores a partir do **Painel de Mensagens**. Caso já exista uma conversa iniciada com o professor, é possível continuar o envio diretamente pela conversa ou acessar o **Filtro de Professores**.

## **1) Listagem de turmas/disciplinas**

O sistema exibirá a lista de turmas/disciplinas dos dependentes do responsável, permitindo a seleção dos professores para envio de mensagens.

## **2) Envio de mensagens (mensagem pessoal)**

1. Acessar o menu **Mensagens**;
2. Clicar no botão **Nova Mensagem**;
3. Selecionar o professor/disciplina com quem deseja conversar;
4. Clicar no ícone de nova mensagem;
5. Informar o texto da mensagem no campo **“Digite a mensagem”**;
6. Clicar no botão **Enviar**.

## **3) Envio de comunicados**

1. Acessar o menu **Mensagens**;
2. Clicar no botão **Nova Mensagem**;
3. Selecionar um ou mais professores/disciplinas;
4. Clicar no ícone de nova mensagem;
5. Informar o **assunto** e o texto do comunicado;
6. Clicar no botão **Enviar**.

Atualização no fluxo de envio de Comunicados: Os comunicados enviados não serão mais atualizados no painel de visualização de conversas particulares do destinatário.

Após o envio de um comunicado pelo professor, o conteúdo não será incluído nas conversas pessoais com o mesmo destinatário.

O comunicado somente ficará visível quando o professor acessar a conversa específica e consultar o histórico de mensagens.

> **Exemplo:** envio de um comunicado em que um dos destinatários já possui conversa pessoal ativa com o professor.

Responsável (Pais,Financeiro e Acadêmico) tenha mais de um dependente

Caso o responsável (pais, financeiro e acadêmico) possua mais de um dependente, ao acessar a tela de **Filtro de Professores**, a relação de professores e turmas/disciplinas será exibida agrupada por dependente.

Exclusão de Mensagens e Comunicados

O usuário poderá excluir mensagens de **histórico de conversas**, **conversas pontuais** e **comunicados**.

Para realizar a exclusão, o usuário deve pressionar e segurar a mensagem desejada e, em seguida, clicar no botão **Excluir**.

**Exclusão do histórico do Comunicado**                                               **Exclusão da mensagem do Comunicado**

                                                 

**Exclusão do histórico de conversa com o usuário (Mensagem)        Exclusão "pontual" da mensagem como usuário**

                                           

Mensagens Pessoais - Identificação do aluno nas conversasfalse

Essa funcionalidade está disponível na versão:

* Versão do RM: 12.1.2602
* Versão do aplicativo: 08.2602.01

Essa funcionalidade permite que o aplicativo identifique automaticamente a qual aluno a conversa está vinculada, garantindo maior clareza tanto para o responsável quanto para o professor.

Para realizar o primeiro vínculo, siga os passos abaixo:

Mensagens pessoaisPerfil: Responsável (Responsável Acadêmico | Responsável Financeiro | Pai | Mãe)

Após realizar o login e acessar o menu **Mensagens**, ao iniciar ou continuar uma conversa com o professor, será exibida uma tela para que o responsável realize o **primeiro vínculo**. A partir desse momento, a conversa ficará associada ao aluno(a) selecionado(a).

Após a confirmação do vínculo, será exibida uma tag identificando o aluno, no formato: **Aluno(a): Nome do aluno**, indicando a qual dependente a conversa está vinculada.

O vínculo é realizado apenas uma única vez e não poderá ser alterado posteriormente.

Perfil: Professor

**O professor não realiza o processo de vínculo.**

Após o vínculo ser realizado pelo responsável, o sistema atualizará automaticamente o painel de conversa do professor, exibindo uma tag no formato **Aluno(a): Nome do aluno**, indicando o aluno ao qual a conversa com o responsável está associada.

ComunicadosPerfil: Responsável (Responsável Acadêmico | Responsável Financeiro | Pai | Mãe)

Ao receber um comunicado do professor, ao visualizar a mensagem, será exibida uma tela para que o responsável realize o **primeiro vínculo**. A partir desse momento, a conversa ficará associada ao aluno(a) selecionado(a).

Perfil: Professor

Após o professor enviar o comunicado ao responsável e este visualizar a mensagem, será solicitado o **vínculo do aluno**.

Após a realização do vínculo, será exibida a tag no formato **Aluno(a): Nome do aluno**, indicando o aluno ao qual a conversa está associada entre o responsável e o usuário.

Envio de comunicado ( Visão do Professor)                Recebimento do Comunicado do professor ( Visão do Responsável)
