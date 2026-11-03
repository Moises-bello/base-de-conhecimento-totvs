---
content_hash: 6ea03aebd9c0259b2b30ab8c57e072c10148358750283a7558c208df5b7a3a03
fetched_at: '2026-06-29T00:12:01.531014+00:00'
page_id: '896207837'
product: rm
source: tdn-rm
title: 12. Agenda Infantil
type: documentation
url: https://tdn.totvs.com/display/LRM/12.+Agenda+Infantil
version: 33
---

A **Agenda Infantil** tem como objetivo manter os pais e responsáveis atualizados sobre as rotinas diárias do(s) aluno(s). A Agenda funciona como um **“Caderno Virtual”**, contendo os eventos diários disponibilizados para os pais e/ou responsáveis por meio do aplicativo **Meu eduCONNECT**.

As **Agendas** e os **Eventos** são estruturados por **contexto**; seu cadastro e visibilidade ficam disponíveis apenas para a **Coligada**, **Filial** e **Nível de Ensino** nos quais foram devidamente parametrizados.

### Essa funcionalidade está disponível apenas para o contexto Ensino Básico

Parametrização

Primeiramente, é necessário que a Instituição de Ensino configure a [URL Rewrite](https://tdn.totvs.com/x/RURGIQ) e o [Application Request Routing Cache (ARR)](https://tdn.totvs.com/x/2vzAI) .

Permissão de acesso

Antes de tudo, a instituição de ensino deve configurar a Agenda, os Eventos e as Ações

* Agenda - **Serviços Globais | Segurança | Perfil | "Sistema" Educacional | eduCONNECT | Central de Comunicações | eduCONNECT | Agenda**
* Evento - **Serviços Globais | Segurança | Perfil | "Sistema" Educacional | eduCONNECT | Central de Comunicações | eduCONNECT | Evento**
* Ação dos Eventos - **Serviços Globais | Segurança | Perfil | "Sistema" Educacional | eduCONNECT | Central de Comunicações | eduCONNECT | Ação**

Cadastro de agenda

No cadastro da Agenda, o usuário poderá incluir, editar e excluir, conforme as permissões definidas em: **Serviços Globais | Segurança | Perfil | "Sistema" Educacional | eduCONNECT | Central de Comunicações | eduCONNECT | Agenda (Incluir, Excluir e Editar).**

Para efetuar o cadastro, acessar o menu: **Gestão Educacional | Atividades Acadêmicas | Central de Comunicações | eduCONNECT | Agenda**

Cadastro de evento

No **cadastro de Evento**, o objetivo é unificar a listagem das Ações de acordo com cada acontecimento relacionado à rotina diária do aluno. Os eventos parametrizados serão exibidos no aplicativo **Meu eduCONNECT**, tanto na visão do professor quanto na visão do responsável acadêmico. Caso haja mais de uma Agenda vinculada às turmas/disciplinas, os eventos serão apresentados conforme as permissões e configurações estabelecidas.

Para realizar o cadastro, acesse o menu: **Gestão Educacional | Atividades Acadêmicas | Central de Comunicações | eduCONNECT | Evento**

No cadastro, o usuário poderá **incluir, editar e excluir**, desde que possua permissão configurada em: **Serviços Globais | Segurança | Perfil | "Sistema" Educacional | eduCONNECT | Central de Comunicações | eduCONNECT | Evento** (Incluir, Excluir e Editar).

Imagem

No **cadastro do Evento**, o usuário tem a opção de incluir uma imagem para proporcionar uma identificação visual aos professores e responsáveis.

A imagem ficará **visível durante as respostas dos professores** e também na **visualização da Agenda pelos responsáveis** no aplicativo *Meu eduCONNECT*.

Cadastro de ação de evento

No **cadastro da Ação dos Eventos**, o usuário poderá **incluir, editar e excluir**, desde que possua permissão configurada em: **Serviços Globais | Segurança | Perfil | "Sistema" Educacional | eduCONNECT | Central de Comunicações | eduCONNECT | Ação** (Incluir, Excluir e Editar).

O cadastro do **Parâmetro** tem como objetivo **vincular as opções que serão disponibilizadas nos eventos**.

No cadastro do Parâmetro, o usuário poderá definir:

* **Nome**
* **Descrição**
* **Tipo de campo** a ser apresentado ao usuário, podendo ser:

  + Data/Horário
  + Classificação *Smile* (Feliz, Neutro e Triste)
  + Texto curto
  + Texto longo
  + Data/Hora
  + Emoticon
  + Números
  + Hora
  + Sim/Não

Ação do evento com Foto

A partir da versão **12.1.2506**, está disponível a parametrização de ações do tipo **FOTO** nos eventos. O processo de configuração segue o mesmo padrão utilizado para os demais tipos de ação vinculados aos eventos.

Antes de iniciar o cadastro, é necessário **configurar o diretório de armazenamento** e **definir o tamanho máximo permitido para os arquivos**. [Clique aqui](https://tdn.totvs.com/x/N8ukOQ) para acessar essas configurações.

Após concluir essa etapa, acesse o **cadastro da Ação**. A opção para o tipo **FOTO** será exibida conforme demonstrado abaixo:

Para efetuar o cadastro, acessar o menu: **Gestão Educacional | Atividades Acadêmicas | Central de Comunicações | eduCONNECT | Ação**

Vincular a ação ao evento

Após o cadastro dos **Parâmetros**, é necessário vinculá-los ao **Evento**.

O sistema oferece **duas formas** de realizar esse vínculo:

1. **Pelo cadastro das Ações:**  
   O usuário pode vincular uma ou mais Ações a um ou mais Eventos.
2. **Pelo cadastro do Evento:**  
   O usuário pode incluir manualmente as Ações que deseja associar ao Evento.

Durante esse processo, o usuário também poderá **definir a ordem de exibição das Ações**, organizando a sequência em que serão apresentadas aos professores durante o preenchimento das informações do Evento.

0.2falsesamplesfadetrue11- Ações- Associar Ações(s) ao(s) Evento(s)

No **cadastro do Parâmetro**, o usuário poderá realizar o **cadastro em massa**, vinculando um ou mais Parâmetros a um ou mais Eventos simultaneamente.

true22- Evento - Ações ao Evento

No **cadastro do Evento**, o usuário tem a opção de **incluir manualmente as Ações**. Nesse cadastro, é possível adicionar **uma ou mais Ações** ao Evento conforme a necessidade.

Vincular o evento na agenda

Após realizar o cadastro da **Agenda** e do **Evento**, é necessário **vincular o Evento à Agenda**.

O sistema permite que o usuário cadastre **um ou mais Eventos** em **uma ou várias Agendas**, oferecendo dois tipos de procedimentos:

* Cadastro manual do Evento na Agenda
* Cadastro em massa de vários Eventos em uma ou várias Agendas

### **Permissões necessárias**

Antes de iniciar o processo, é necessário conceder as permissões adequadas:

* **Cadastro Manual:** Serviços Globais | Segurança | Perfil | "Sistema" Educacional | eduCONNECT | Central de Comunicações | eduCONNECT | Agenda | Evento da Agenda
* **Cadastro em Massa:** Serviços Globais | Segurança | Perfil | "Sistema" Educacional | eduCONNECT | Central de Comunicações | eduCONNECT | Agenda | Associar Evento na Agenda

Durante o processo, o usuário poderá **definir a ordem de exibição dos Eventos** na Agenda, organizando a sequência em que serão apresentados aos professores durante o preenchimento das informações.

A **ordem definida** será a mesma exibida quando o professor acessar os Eventos da Agenda no aplicativo *Meu eduCONNECT*.

0.2falsesamplesfadetrue11 - Cadastro Manual do Evento na Agenda

Para realizar o **cadastro manual**, o usuário deve acessar a **Agenda desejada** e vincular o **Evento** à Agenda de forma manual.

### **Parametrização da Tela: Eventos da Agenda**

Nesta seção, o usuário poderá configurar as opções e visualizações relacionadas aos **Eventos vinculados à Agenda**, incluindo visibilidade, ordem de exibição e vinculação de Ações.

### **Visível**

Após realizar o cadastro, o usuário poderá **definir a visibilidade do Evento** utilizando o campo **Visível**.

* **Marcado:** o Evento da Agenda será exibido.
* **Desmarcado:** o Evento da Agenda não será exibido.

### **Destino**

O campo **Destino** tem como finalidade **definir o destinatário do Evento da Agenda**.

* **Observação**

 Para campos do tipo **Texto Longo**, serão exibidos apenas os **100 primeiros caracteres**.

* ### **Professor**

  Se a ação do Evento for do tipo **Texto Simples** ou **Texto Longo**, marcar esta opção fará com que o Evento fique **disponível apenas para o Responsável**.

* ### **Responsável**

  Marcar esta opção fará com que o Evento fique **disponível apenas na Agenda do Professor**.

true22 - Cadastro em 'massa' de vários Eventos em várias Agendas

No **cadastro em massa**, o usuário poderá **selecionar uma ou mais Agendas** e **adicionar um ou mais Eventos** simultaneamente.

Vincular a agenda na turma/disciplina

O vínculo da Agenda à Turma/Disciplina pode ser realizado de **três formas**:

1. **No cadastro da Agenda na Turma/Disciplina** – vinculando diretamente durante o cadastro da Agenda.
2. **No cadastro da Agenda em várias Turmas/Disciplinas** – utilizando o processo *Associar Agenda à Turma/Disciplina*.
3. **No cadastro da Agenda ao realizar o cadastro de várias Turmas/Disciplinas** – na visão **Turma**, permitindo vincular múltiplas turmas de uma só vez.

false

Com o objetivo de otimizar a **exibição e o preenchimento da Agenda**, recomenda-se **parametrizar apenas uma Agenda por Turma/Disciplina**, escolhendo aquela que faça mais sentido e que inclua todos os professores aptos a responder.

Para auxiliar nesse processo, foi inserido um **Tooltip** que orienta a Instituição de Ensino sobre a **melhor forma de otimizar a Agenda na Turma/Disciplina**.

0.2falsesamplesfadetrue11 - Cadastro da Agenda na Turma/Disciplina

Para vincular a Agenda de forma pontual, basta:

1. Acessar o **cadastro da Turma/Disciplina**.
2. Realizar o vínculo utilizando o **LookUp: Agenda**, localizado na aba **Informações Adicionais**.

true22 - Cadastro da Agenda em várias Turmas/Disciplinas 

Para vincular uma Agenda a **várias Turmas/Disciplinas**, utilize o processo **Associar Agenda a Turma/Disciplina** disponível no cadastro da Turma/Disciplina.

Antes de iniciar, é necessário **habilitar a permissão** do usuário para executar este processo: **Serviços Globais | Segurança | Perfil | "Sistema" Educacional | Currículo e Oferta | Oferta | eduCONNECT | Turmas/Disciplinas | Associar Agenda a Turmas/Disciplinas**

Após habilitar a permissão, siga os passos abaixo:

1. Acesse a **visão de Turmas/Disciplinas**.
2. Selecione as Turmas/Disciplinas nas quais deseja realizar o **vínculo da Agenda**.
3. Concluído o processo, será exibido um **log** contendo um resumo, incluindo:

   * Quantidade de Turmas/Disciplinas selecionadas
   * Quantidade de registros que foram **atualizados** ou **incluídos**

true33 - Cadastro da Agenda através da visão: Turma

Na **visão Turma**, ao realizar o cadastro de **várias Turmas/Disciplinas** através do processo **Cadastrar Turmas/Disciplinas**, o usuário poderá **associar uma Agenda** durante o cadastro múltiplo, vinculando-a a todas as turmas selecionadas.

Agenda infantil - eduCONNECT

O menu **Agenda Infantil** estará disponível para o **Professor** e para o **Responsável Acadêmico** do aluno. O acesso ao menu dependerá das **permissões concedidas** aos usuários em questão.

false0.2falsesamplesfadetrueProfessor

Através deste menu, o **professor** poderá visualizar a relação de **Turmas/Disciplinas**, seguindo os mesmos critérios de exibição utilizados no Portal:

* O **período letivo** não deve estar encerrado;
* A opção **“Exibir no Portal do Professor”** deve estar habilitada;
* A turma/disciplina deve possuir **alunos matriculados**;
* Os responsáveis devem ter **usuários criados no sistema**, caso sejam eles os responsáveis por visualizar a agenda do aluno.

Visualizar as turma/disciplinas e alunos

Para habilitar a funcionalidade para o **professor**, é necessário conceder a permissão em: **Serviços Globais | Segurança | Perfis | "Sistema" Educacional | eduCONNECT | Agenda Infantil | Acesso ao Professor**

Ao acessar no menu: Agenda Infantil, o professor irá visualizar a relação de Turmas/disciplinas no qual ele é professor e nestas Turmas/disciplinas possui uma **Agenda** devidamente parametrizada.

false

Caso a Turma tenha somente uma turma/Disciplina com Agenda vinculada, ao acessar o aplicativo: Meu eduCONNECT, será exibido apenas o nome da Turma.

Nessa tela, o **professor** visualizará os dados da **Turma/Disciplina**, incluindo:

* Período Letivo
* Nome da Turma
* Nome da Disciplina

Ao acessar a Turma/Disciplina, o professor verá a **relação de alunos matriculados** na mesma.

Preencher dados do evento da agenda

Para preencher a **Agenda**, o **professor** poderá:

* Selecionar **um ou mais alunos** individualmente;
* Selecionar **todos os alunos da Turma/Disciplina** simplesmente marcando a própria Turma/Disciplina.

false

O **professor** não poderá selecionar mais de uma **Turma/Disciplina** ao preencher os Eventos da Agenda.

Se mais de uma Turma/Disciplina for selecionada, o botão **“Continuar”** não será exibido.

Para iniciar o preenchimento da Agenda, o professor deverá selecionar uma data; basta clicar no respectivo dia do calendário (por default virá habilitado a data corrente).

E selecionar a Turma/disciplina  (ou o(s) aluno(s)).

 

Após selecionar a Turma/Disciplina ou o(s) Aluno(s) e clicar no botão **Continuar**, será exibida a relação de alunos.

O professor poderá responder os eventos para um único aluno ou para todos os alunos da Turma/Disciplina selecionada.

Além disso, o professor pode definir quais eventos terão suas respostas e visualizações replicadas para todos os alunos selecionados, por meio do switch **Aplicar resposta a todos os alunos selecionados**.

Além disso, será apresentada a relação de eventos parametrizados na Agenda, na mesma ordem em que foram configurados pela Instituição de Ensino.

Ao expandir um evento, serão exibidas as ações conforme a parametrização definida pela IE.

As ações de preenchimento obrigatório serão identificadas com o símbolo (**\***), conforme demonstrado na imagem abaixo.

Envio de FOTOS 

Ao acessar a Agenda Infantil para um evento do tipo **Foto**, o professor terá a opção de capturar imagens diretamente pela câmera ou selecionar fotos da galeria do dispositivo. É possível incluir até **20 fotos por ação**.

 

Salvar os eventos e liberar para os responsáveis

**01. Liberar eventos pontualmente**

Ao acessar a tela de respostas, o professor poderá selecionar um ou vários alunos da turma; porém, a visualização e o preenchimento das informações são realizados individualmente por aluno.

Após registrar as respostas, o professor poderá clicar no botão **Salvar** e, somente depois, **Liberar a Agenda** para os responsáveis.

    **Salvar                                                  Liberar**

 

Uma vez que o evento ou a agenda tiver sido liberado(a) para os responsáveis, o professor **não poderá realizar edições**.

Após a liberação, o evento será marcado com um **ícone de identificação**, permitindo ao professor visualizar facilmente quais itens já foram liberados.

### **02**LIBERAR EVENTOS EM LOTE

A Instituição de Ensino poderá realizar o lançamento dos eventos da Agenda de forma pontual (salvando os registros) e, posteriormente, liberar todos os eventos da Turma/Disciplina ou de um ou mais alunos selecionados dentro da turma.

Para utilizar essa funcionalidade, é necessário que o professor tenha a permissão correspondente habilitada. A configuração pode ser feita em: **Serviços Globais | Segurança | Perfis | "Sistema" Educacional | eduCONNECT | Agenda Infantil | Permite Liberar eventos em lote.**

O professor poderá liberar o(s) evento(s) de duas formas:

* Selecionando uma ou mais Turmas/Disciplinas;
* Selecionando um ou mais Alunos da turma.

Após realizar a seleção das Turmas/Disciplinas e/ou dos Alunos e clicar no botão **“Liberar agenda”**, será exibida uma mensagem de confirmação perguntando ao usuário se deseja realmente liberar o(s) evento(s) para a data selecionada.

Ao marcar a opção **“Confirmar liberação”**, os eventos serão liberados para os responsáveis da(s) Turma(s)/Disciplina(s) e/ou do(s) Aluno(s) selecionado(s).

Após a liberação, as informações estarão imediatamente disponíveis para os responsáveis dos alunos.

Visualizar recado enviado pelo responsável

Para que o professor possa visualizar o recado enviado pelo responsável, é necessário que ele possua a permissão habilitada em: **Serviços Globais | Segurança | Perfis | "Sistema" Educacional | eduCONNECT | Agenda Infantil | Permite visualizar recado do responsável**

Ao acessar o app e clicar no dia correspondente no calendário, caso exista um recado enviado pelo responsável, será exibido um **ícone de envelope** na turma indicando a presença de um recado não lido.

Notificação de um novo recado do responsável

Caso o responsável envie um recado, o professor será notificado por meio de um **ícone de cartinha em destaque** ao acessar a Agenda da turma.

Ao clicar na seta para a direita na listagem de alunos, será exibido o mesmo **ícone de recado não lido** ao lado do aluno que possui uma mensagem pendente.

Notificação de um novo recado do responsável

Caso o responsável envie um recado, o professor será notificado por meio de uma **cartinha em destaque** exibida logo abaixo do nome do aluno correspondente.

Ao acessar a Agenda do aluno, será exibido um **ícone de avisos** indicando que há um recado “colapsado”. Ao clicar na seta para baixo, o conteúdo do recado será expandido e exibido ao professor.

 

Caso o professor acesse um aluno que não possui recado e clique na seta para baixo para visualizar, será exibida a indicação correspondente informando que **não há recados disponíveis**, conforme demonstrado abaixo.

trueResponsável Acadêmico

Para que o Responsável Acadêmico possa visualizar a Agenda, é necessário que a Agenda ou o Evento tenha sido liberado previamente pelo Professor.

Visualizar recados

Para habilitar a funcionalidade para o Responsável Acadêmico, é necessário conceder a permissão em: **Serviços Globais | Segurança | Perfis | "Sistema" Educacional | eduCONNECT | Agenda Infantil | Acesso ao Responsável Acadêmico**

Lista de aluno(s) e suas respectivas turma(s)/disciplina(s)

Lista de aluno(s) e suas respectivas turma(s)/disciplina(s):

**1.** Situação da matrícula – turmas em andamento

* + Status final = **Não**
  + Disponível na web = **Sim**
  + Disciplina = **Sim**
  + Disciplina em curso = **Sim**  
            ou  
        Aluno matriculado na disciplina = **Sim**

**2.** Situação da matrícula – turmas concluídas ou em fase de conclusão

* + Status final = **Sim**
  + Atender a pelo menos uma das condições:  
              o    Possui crédito em andamento = **Sim** e Disciplina em curso = **Sim**  
              o    Aprovado = **Sim**
  + Disponível na web = **Sim**
  + Aluno vinculado à disciplina = **Sim**

**3.** Condições adicionais

* + Turma/Disciplina ativa = **Sim**
  + Período letivo configurado para exibição no portal
  + Período letivo encerrado: será considerado de acordo com a parametrização do sistema
  + Período letivo vigente: a data atual deve estar entre a data de início e a data prevista de término do período letivo

Por padrão, a data corrente virá selecionada. Caso o responsável deseje visualizar uma data anterior ou posterior, basta clicar sobre as informações de data.

Se houver mais de um aluno vinculado ao responsável, os nomes serão exibidos em **ordem alfabética**.

**Seleção do Calendário                  Exibição do Menu**

 

Um único dependente

Caso o usuário seja um responsável e possua apenas um aluno como dependente, a lista de alunos não será exibida. Nesse caso, serão apresentadas somente as informações referentes a esse dependente.

Se nenhum dos dependentes possuir informações de agenda disponíveis, será exibida uma tela informando que **nenhum dado foi encontrado**.

**Contexto selecionado**

O responsável tem a opção de permanecer no seu próprio contexto ou selecionar diretamente o contexto de um aluno específico.

Quando o responsável estiver em seu próprio contexto, será exibida a lista de alunos sob sua responsabilidade. Ao selecionar um aluno, a agenda correspondente a esse aluno será apresentada.

Se o responsável selecionar o contexto de algum aluno, a lista de alunos não será exibida. Nesse caso, serão apresentadas apenas as informações de agenda referentes ao aluno escolhido.

 

Se o responsável selecionar o contexto de um aluno que não possui informações de agenda, será exibida uma tela informando que **não existe conteúdo disponível**.

Caso existam várias Agendas liberadas em turmas/disciplinas diferentes, serão exibidos o **nome da Agenda** e o **nome da Disciplina**, garantindo uma melhor identificação e visualização por parte dos responsáveis.

Se houver apenas uma Agenda/TurmaDisciplina disponível para o aluno, nenhuma aba será exibida.

Para selecionar outra Agenda, basta que o usuário clique sobre o **nome da Agenda** e/ou sobre o **nome da Disciplina**.

**Tipos de ações de eventos**

Abaixo estão os tipos de ações de eventos que podem ser exibidos na Agenda:

* Data/Hora
* Hora
* Sim/Não
* Número
* Emoticon (Feliz, Neutro, Triste)
* Texto curto
* Texto longo

A opção de **Texto Longo** exibirá apenas os **100 primeiros caracteres**, seguidos por **"..."**, caso o conteúdo ultrapasse esse limite. Nesses casos, será apresentada a opção **“Leia mais”**, que ao ser clicada exibirá o texto completo. Após expandido, será disponibilizada a opção **“Leia menos”**, permitindo que o conteúdo volte a ser exibido apenas com os 100 primeiros caracteres seguidos por **"..."**.

 

Atualização automática de nova liberação da Agenda/Evento  (Push / Tost) 

Essa funcionalidade está disponível apenas para o **Responsável Acadêmico**.

Após o professor liberar a(s) Agenda(s) ou o(s) Evento(s), os responsáveis serão notificados por meio de uma mensagem **Push/Toast**.

O texto da notificação incluirá as seguintes informações:

* **Nome da Agenda**;
* **Nome do(s) filho(s)**.

Ao clicar sobre o **Push**, o Responsável será redirecionado para o menu **Agenda**, onde poderá visualizar o conteúdo liberado pelo professor.

**Observação:** Caso o aluno possua mais de uma Turma/Disciplina, o Responsável deverá localizar o conteúdo entre as opções exibidas. O Push **não** redirecionará o usuário diretamente para a Turma/Disciplina que teve a Agenda e/ou Evento liberado.

Os responsáveis serão notificados da liberação da Agenda/Evento através de Push, seguindo a regra:

* Quando o aplicativo estiver em **segundo plano** ou **fechado**, o usuário receberá o Push com a mensagem correspondente.

* Se o usuário estiver com o menu **Agenda** aberto, o painel será atualizado automaticamente, **sem exibir Push ou Toast** para sinalização.

* Se o usuário estiver acessando outro menu — como **Notificações**, **Acadêmico** ou **Perfil** — ele será notificado por meio de um **Toast**, no qual será exibido apenas o **Nome da Agenda**.  
  A notificação aparecerá na barra inferior do app e permanecerá visível por **2 segundos**.

O **Toast** serve apenas para sinalizar ao Responsável que a Agenda/Evento foi liberado. Para visualizar o conteúdo, o Responsável deverá acessar manualmente o menu **Agenda**.  
Diferentemente do Push, ao clicar na notificação o usuário **não é redirecionado** para o menu correspondente.

Quando o Responsável Acadêmico possuir mais de um perfil associado (Responsável Acadêmico e/ou Professor), será exibida uma tela de seleção de contexto para que ele escolha **qual tipo de acesso deseja utilizar**.

Enviar recado do responsável para o professor

Para habilitar essa funcionalidade, é necessário realizar algumas parametrizações:

No cadastro do Evento, foram criados dois campos, sendo o primeiro:

* **Destino:** A Instituição deverá parametrizar para qual público-alvo o Evento será apresentado, definindo se ele será exibido para o **Professor** ou para o **Responsável**.

* **Horário Limite:** A Instituição de Ensino poderá definir um horário de corte para o envio de recados. Por exemplo, se o horário limite for configurado para **10h00**, após esse horário o app bloqueará o envio de mensagens pelo responsável.

Como exemplo, caso o horário limite seja definido para **10h00**, ao tentar enviar um recado para o professor após esse horário, será exibida a seguinte mensagem:

Para habilitar essa funcionalidade, é necessário conceder a seguinte permissão: **Serviços Globais | Segurança | Perfis | "Sistema" Educacional | eduCONNECT | Agenda Infantil | Enviar recado de Responsável para Professores**

Ao acessar o aplicativo **Meu eduCONNECT** utilizando um perfil de responsável, o botão para envio de recados na **Agenda Infantil** será exibido e habilitado automaticamente.

Para enviar o recado, o responsável poderá selecionar uma data — basta clicar no ícone de **calendário** (por padrão, a data corrente virá selecionada).

Será apresentada a relação de **Eventos parametrizados na Agenda** para a Turma/Disciplina correspondente, seguindo exatamente a ordem definida pela Instituição de Ensino.

Ao expandir um Evento, serão exibidas as **Ações** conforme a parametrização realizada pela IE.

As ações de **preenchimento obrigatório** estarão identificadas com o símbolo **(\*)**, conforme demonstrado na imagem abaixo.

Após o envio do recado, ele será marcado com um **ícone de identificação**, permitindo ao responsável visualizar com facilidade quais mensagens já foram enviadas.

 

Uma vez que o recado tiver sido enviado aos professores, o responsável **somente poderá editá-lo** caso o professor ainda **não tenha visualizado** a mensagem ou caso o **tempo de expiração do evento** ainda não tenha sido atingido.

Após o envio, o recado será exibido na **linha do tempo** do responsável.

Após a leitura da mensagem por parte do professor, será exibido o **ícone correspondente**, indicando que o recado já foi visualizado.

falseTabela envolvidadas

SAGDAGENDA - Cadastro da Agenda

SAGDAGENDAEVENTO - Cadastro do Evento na Agenda

SAGDEVENTO - Cadastro do Evento

SAGDPARAM - Cadastro da Ação dos Eventos

SAGDALUNO - Vínculo da Agenda no cadastro do Aluno.

    Coluna: LIBERADO

        se =  0 - O Evento não foi liberado

        se =  1 - O Evento foi liberado

    Coluna: DATAREGISTROS - Grava a data e hora  que o registro foi inserido na base de dados
