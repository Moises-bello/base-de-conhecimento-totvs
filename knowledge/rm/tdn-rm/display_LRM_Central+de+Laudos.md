---
content_hash: c34669eb00ec9c264b6c9ae3653f9cc1b76b9338b232470a53d9a9f4476ff967
fetched_at: '2026-06-29T00:11:28.783074+00:00'
page_id: '733191101'
product: rm
source: tdn-rm
title: Central de Laudos
type: documentation
url: https://tdn.totvs.com/display/LRM/Central+de+Laudos
version: 61
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
   1. **Central de laudos**
      1. **Login PEP RM**
      2. **Tela de laudagem**
3. **Integração Laudite**

Central de LaudosVisão Geral

## **01. VISÃO GERAL**

Possibilidade de visualizar laudo e/ou laudar.

Central de laudos

## **02. EXEMPLO DE UTILIZAÇÃO**

Central de Laudos

sumarioLogin PEP RM

**Login PEP RM**

**Selecionar o menu Central de Laudos**

**A partir da versão 2510, o layout da tela foi atualizado para esse:**

**Obs.: Serão exibidos na tabela da Central de Laudos somente exames configurados como laudo pré-impresso e que possuem modalidade.**

Irá exibir a tela de home da Central com os filtros:

* **Por Unidade:** exibe as unidades cadastradas no RM saúde em cadastro de unidade e que o usuário tenha acesso
* **Por modalidade:** modalidades DICOM cadastradas no RM saúde no cadastro do exame
* **Pedido, Exame ou paciente:** filtra pelo número do pedido, nome do exame ou nome do paciente
* **Busca de pacientes:** realiza a busca pela leitura da pulseira de identificação do paciente (código de barras)
* **Botão Filtros:** exibe as opções de filtro por período (data inicia e final) , Número do prontuário e buscar profissional

* **Botão Todos:** exibe todos os exames de acordo com os filtros pré-selecionados
* **Botão Meus laudos:** exibe somente os laudos que o usuário logado é responsável
* **Status:** Inicial, em digitação, Digitação Concluída, Liberado, Assinatura Pendente, Aguardando Revisão e Revisado
* **Botão Assinar:** pode ser utilizado para assinar um laudo ou assinar e lote quando selecionados os meus laudos

A partir da 2510, houveram algumas alterações:

* Os botões de status viraram um único componente multi-select;
* A pesquisa de pedido, paciente, exame continua com o mesmo funcionamento, porém com o tooltip "Buscar na tabela"

Na grid consta as seguintes informações:

**Na grid consta as seguintes informações:**

* **Pedido:** número do pedido de exames gerado no RM saúde
* **Situação:** Normal, Urgente ou Emergência de acordo com o pedido de exames do gerado no RM saúde
* **Status:** Inicial, em digitação, Digitação Concluída, Liberado, Assinatura Pendente, Aguardando Revisão e Revisado
* **Exame:** descrição do exame que consta no pedido
* *Prontuário***:** número do prontuário do paciente (**agora essa opção se encontra no Gerenciador de Colunas, sendo substituída pela data prevista de entrega**).
* **Previsão de Entrega:**coluna mostrando a data e hora prevista de entrega do exame. Foi retirada essa informação do campo de +Info.
* **Nome do paciente:** Nome do paciente
* **+ Info :**
  + Sempre será exibido: tipo de atendimento (interno ou externo), modalidade, código do paciente, sexo biológico do paciente, nome do solicitante do exame , nome do médico executante, convênio e data de nascimento do paciente;
  + Se o exame for uma reconvocação:
    - Será exibido os campos: data da solicitação da reconvocação, nome do solicitante da reconvocação, motivo(s) da reconvocação (separado por ";"), pedido do exame reconvocado, status do pedido de exame reconvocado, data agendada para exame o reconvocado;
    - Tambem irá exibir um calendário como ícone. Se a reconvocação ja tiver um pedido de exame será exibido em amarelo, caso contrário será exibido na cor padrão de texto da tela;

* **Assinatura:** se o exame estiver assinado fica com um visto
* **Laudo selecionar:** direciona para a tela de laudagem do exame selecionado

**- Abrir prontuário:** abre uma nova aba no prontuário do paciente

**-  Laudar:** direciona para a tela de laudagem do exame selecionado

**- Histórico**: abre uma nova aba no prontuário do paciente na aleta de resultados de exames

                  - **Liberar** : assinar e finalizar exames que estavam com status Digitação Concluída e o usuário logado for o médico responsável;

**- Imprimir:** Imprime o laudo

* **Botão ver mais exames:** carrega de 5 em 5 exames

* **Gerencia as colunas** de exibição, mas não salva por usuário
* **Painel de notificações:** são exibidas de acordo com o perfil do usuário
Tela de Laudagem

# **Tela de Laudagem**

**Cabeçalho de identificação:**

* **Nome completo** do paciente
* **Sexo / idade** em anos, meses e dias
* **Sigla de identificação** se o exame é normal, urgência ou emergência / número do prontuário, Peso e Altura caso tenham preenchido nas informações complementares do pedido de exames
* **Número do pedido / Previsão de entrega** (se preenchido no RM saúde)
* **Descrição do exame**
* **Unidade de Execução**
* **Digitador:** usuário digitador.
  + Ao iniciar a digitação de um laudo, se não houver usuário digitador informado, o usuário logado que inicio a digitação será gravado como usuário digitador;
* **Responsável:** médico responsável que irá assinar o exame.
  + Se clicar no campo de responsável será aberta uma opção para poder alterar o responsável, a busca inicia a partir do 3° caracteres digitado;
  + Se não houver responsável definido o proprio usuário digitador poderá informar um médido responsável, desde que o status do laudo seja "Inicial" ou "Em Digitação" ou "Revisado";
  + Se já houver responsável definido somente o usuário logado que for o próprio responsável poderar alterar, desde que o status do laudo seja "Inicial" ou "Em Digitação" ou "Revisado" e o usuário tenha parmissão de alterar responsável atravez do perfil do usuário logado;
* **Status do Exame:** Inicial, em digitação, Digitação Concluída, Liberado, Assinatura Pendente, Aguardando Revisão e Revisado
* **DUM:** Data da última menstruação. Esta informação só aparece para pacientes do sexo feminino. Caso o usuário tenha preenchido essa informação no pedido de exames a data vira preenchida, podendo ser alterada (nunca para data futura), caso não tenham informado no pedido virá preenchido com Não informado, podendo ser incluída a data. Não é possível excluir a DUM pela Central, o calendário não aceita valores nulos, nem incompletos.

Caso na fila de laudos tenha sido informado que foram entregues exames fisicamente na unidade a mensagem abaixo é informada.

### **Regras Específicas**

* Quando um usuário abre o laudo com status **"Inicial"** e inicia a digitação do laudo na edição de texto, o status passa a ser "**Em Digitação"** e o usuário logado passa a ser o usuário digitador se não existir o usuario digitador;
* Quando o status estiver em **"Inicial"** ou **"Em Digitação"** e não houver médico responsável definido, é possivel informar o médico responsável se o usuário logado for o usuário digitador. Também será possivel alterar o médico responsável se o usuário logado for o médico responsável.
* A edição do laudo só é permitida para os status: **Inicial, Em Digitação e Revisado;**
* Ao tentar alterar um laudo onde o status esteja como **Revisado**, o mesmo será alterado automaticamente para o status **Em Digitação;**
* Ao concluir a digitação do laudo (Clicar no botão **Digitação Concluída**), é realizado:
  + Alteração do status do laudo para Digitação Concluída;
  + Salvo uma versão do laudo para possível consulta posterior (para realizar a consulta da versão do laudo, basta clicar no botão **Ações** e em seguida na opção **Versões do Laudo**);

## **Botões**

### **Os botões da barra inferior foram alterados (12/2023):**

* **'Assinar e Finalizar'** se transformou em **'Liberar'**, mantendo a mesma função. Será habilitado **SOMENTE** no momento em que o exame estiver com status **"Digitação Concluída"** e o usuário logado for o médico responsável;

* **'Concluir Digitação'** passou para a barra inferior e saiu do dropdown de 'Ações'. Será habilitado no status **'Em digitação'.**

**Laudo:** Tela de laudagem com o ckeditor

**Documentos:** exibe os documentos anexados no pedido de exames do RM saúde

**Dados do paciente:** Informações pessoais e do atendimento oriundos do RM

**Médico solicitante:** dados do médico solicitante cadastrado no RM

**Botão Ações**

*Concluir digitação: exames com status Em Digitação podem ser Concluídos (**não aparece mais no botão de Ações, está incluso direto na barra inferior**)*

**Fechar:** fecha a tela de laudagem e vai para a Home da Central de laudos

**Imprimir:** imprime laudo com status liberado

**Limpar Digitação e reiniciar status:** limpa a tela de laudagem, deixando em branco e volta para o status Inicial

**Salvar Modelo:** Salva o modelo do laudo (**antes, ficava ao lado do botão Assinar e Finalizar, agora indo para o dropdown de ações**)

**Abrir prontuário do paciente:** abre o prontuário do paciente em uma nova aba

**Abrir histórico do paciente:** abre o histórico de exames do paciente em uma nova aba

**Observações do laudo:** abre um pop up de texto livre para incluir as observações, essas observações não são impressas no laudo

**Versões do laudo:** Abre um pop up com as versões do laudo , nessa tela não é possível editar somente visualizar os laudos

**Histórico evolução:** Abre um pop up com o histórico de evolução de enfermagem(exibe apenas as evoluções feitas por prestadores com conselho COREN)

Visualizar histórico status: [Histórico de status exame](https://tdn.totvs.com/pages/viewpage.action?pageId=734371774)

**Ações> Adicionar/Gerenciar > Auto Texto**

Adicionar NOVO: usuário inclui os auto textos que serão utilizados no laudo

Nome: Mnemônico ou descrição abreviada do texto a ser utilizado

Meus Textos: são os auto textos salvos ou criados por um usuário e será exibido somente para ele

Textos Públicos: são auto textos salvos ou criados por um usuário com a opção de “Salvar como auto texto como Público”

então será exibido para todos os usuários.

Os auto textos podem ser selecionados no campo auto texto ou digitando no laudo o mnemônico do auto texto + **CTRL + ESPAÇO** (Atualizado em 12/2023) e o mnemônico será substituído pelo texto cadastrado anteriormente.

 Documentação para cadastro de fórmula -

NotificacaoCentralNotificaçõesNotificações da Central

# **Notificações**

A Central de Laudos possuí algumas notificações que devemos prestar atenção, lembrando que todas as notificações exibidas são atividade de responsabilidade do usuário logado:

* **Laudos com entregas vencidas**: Laudos em que o usuário é responsável e a data de entrega já tenha vencido.
* **Pendente 2º assinatura**: Laudos que o usuário foi solicitado para assinar.
* **Aguardando revisão**: Laudos que o usuário solicitou revisão e está aguardando as revisões serem finalizadas.
* **Laudos Revisados**: Laudos que as revisões foram finalizadas e estão aguardando o usuário continuar com a laudagem.
* **Laudos a Revisar**: Laudos que foram solicitados ao usuário para revisar.

Clicando no ícone de notificação apresentado anteriormente visualizamos uma lista de notificações, clicando em "Aguardando revisão" é aberto uma lista com os laudos:

Ao clicar no ícone do olho, o sistema nos leva ao laudo em questão:

StatusStatus

**Status**

**Inicial:** pedido de exames realizado

**Em Digitação:** usuário iniciou a digitação do laudo

**Digitação Concluída:** Finalizada a digitação

**Liberado:** Laudo Assinado

**Retornar status exame:** [Retornar status exame](https://tdn.totvs.com/display/LRM/Retornar+status+exames), somente é possível retornar para o status anterior ao atual

**Assinatura Pendente**: assinatura digital deu erro ou pendente da segunda assinatura

**Histórico Status:** abre um pop up com o nome do usuário, data e hora de alteração e o status

Ditado de Laudo com Transcrição Automática

## **Ditado de Laudo com Transcrição Automática**

## Objetivo

A funcionalidade de **Ditado de Laudo com Transcrição Automática** permite ao médico radiologista ditar o conteúdo do laudo diretamente por voz, utilizando um botão integrado ao editor de texto. O sistema realiza a transcrição automática, aplicando pontuação e estrutura textual em tempo real, o que **agiliza a elaboração e finalização de laudos** sem comprometer a qualidade técnica.

### Disponibilidade

O ditado por voz estará disponível apenas nos seguintes **status de laudo**:

* Inicial
* Em Digitação
* Revisado (retorna para "Em Digitação" após ajustes)

Ao iniciar a gravação por voz, o status do laudo será **automaticamente alterado para “Em Digitação”**, garantindo rastreabilidade e coerência com o fluxo do sistema.

## Como Usar

### 1. Acesso à Função

Na Central de Laudos, ao abrir o editor do laudo, o botão de **microfone flutuante** será exibido no canto inferior direito da tela:

* Ícone de microfone (Iniciar)
* Ícone de microfone cortado (Encerrar)

### 2. Iniciar Gravação

Clique no botão com o ícone  para iniciar o ditado.  
Se o cursor do editor **não estiver posicionado**, será exibido um aviso solicitando que o médico clique primeiro dentro do laudo.  
O sistema garante que o texto será transcrito **exatamente na posição do cursor**, mesmo após cliques fora do editor.

### 3. Ditado com Pontuação e Comandos

O sistema reconhece comandos por voz para aplicar **pontuação e estrutura textual**, como:

| Comando falado | Resultado inserido |
| --- | --- |
| “ponto final” | `.` |
| “vírgula” | `,` |
| “dois pontos” | `:` |
| “interrogação” | ? |
| “exclamação” | ! |
| “nova linha” | Ação: Quebra de linha |
| “parágrafo” | Ação: Novo parágrafo |
| “aspas simples” | ' |
| “aspas dupla” | `"` |

O sistema aplica **capitalização automática** sempre que uma nova frase, parágrafo ou linha é iniciada, facilitando a legibilidade.

### 4. Encerrar Gravação

Clique no botão  para encerrar a transcrição por voz.  
O texto já estará no editor, pronto para ser revisado, ajustado ou complementado com o teclado normalmente.

ExamesAnterioresExames Anteriores

**Exames Anteriores**

**Filtro de Modalidades:** Exibe todas as modalidades disponíveis nos exames anteriores. Ao selecionar uma ou mais modalidades, serão exibidos apenas os exames correspondentes às opções escolhidas. O campo permite a seleção múltipla, possibilitando escolher uma ou mais modalidades para visualização.

**Filtro de Anos:** Exibe todos os anos disponíveis dos exames anteriores. Ao selecionar um ano, serão exibidos apenas os exames correspondentes a essa seleção. O campo é de seleção única, permitindo escolher apenas um ano para exibição.

Apresenta os exames da mesma modalidade, exibe a data e o exame

**Botão info:** traz o nome do exame, médico solicitante e medico executante do exame selecionado

**Ver laudo**: exibe o laudo anterior em uma nova aba, caso não tenha laudo ainda será exibida a mensagem

**Ver imagem:** se o exame foi realizado em um pacs integrado será exibida a imagem em uma nova aba, caso contrário irá exibir a mensagem em abaixo

**Copiar laudo:** copia o laudo do exame e cola no laudo atual

**Botão carregar mais exames:** carrega mais 5 exames anteriores se houver

Dupla Assinatura

Para utilização da dupla assinatura na Central de Laudos é necessário configurar os exames que terão a dupla assinatura

No RM saúde  Cadastro > Unidades de Diagnóstico > Exames e Serviços

Duplo clique em cima do exame, será aberta a tela de cadastro, marcar o check box Dupla Assinatura de laudo

Na Central de laudos

 Buscar o paciente/pedido para laudar , quando chegar no status DIGITAÇÃO CONCLUÍDA, clicar em LIBERAR é exibida a tela para informar o médico responsável pela segunda assinatura e o status passa para ASSINATURA PENDENTE

Após a solicitação da segunda assinatura, o médico responsável pela segunda assinatura deverá acessar a Central de laudos

no painel de notificação ( ícone de sino no canto inferior direito)  - Pendente de 2º assinatura

  clicar no ícone de olho e irá abrir o laudo que esta pendente de assinar , o usuário clica em LIBERAR  e laudo será liberado com uma mensagem de sucesso.

[Criar](https://tdn.totvs.com/pages/createpage.action?spaceKey=LRM&fromPageId=733191101&src=quick-create "Criar página em branco (Insira '''c''')")

ModeloModelo

## **Modelo de Laudo**

### **Objetivo**

Permitir ao usuário cadastrar modelos com formatação e fórmulas para facilitar a laudagem.  
Verifique como usar fórmulas no modelo:   
Acesso para cadastrar **Modelos,** clicar no botão de ações da tela de laudagem > Adicionar/Gerenciar > Modelo

Ao acessar a tela de modelos podemos ver os modelos privados(meus modelos e os públicos(modelos públicos)

Adicionar Novo: O usuário pode criar modelos para utilizar posteriormente, no modelo podem ser incluídos Fórmulas e tabelas.  Cadastro de formulas: <https://tdn.totvs.com/pages/viewpage.action?pageId=773521363>

Incluir o nome do modelo, se desejar incluir uma fórmula deverá ser escolhida no campo fórmula e posteriormente clicar no botão selecionar e o mnemônico

da fórmula é incluído no modelo.

É possível incluir uma tabela no modelo e, dentro dela, inserir fórmulas. Também é permitido utilizar campos avulsos, desde que uma fórmula já tenha sido previamente selecionada.

Tanto ao aplicar uma fórmula no modelo quanto ao utilizar uma fórmula avulsa, o sistema exibirá um modal para o preenchimento dos campos necessários.

Fórmulas que envolvem datas são restritas a operações de soma e subtração. Um exemplo válido seria: `CampoData + 1`, em que `CampoData` representa uma variável que será preenchida dinamicamente com uma data. É possível incluir outros campos na fórmula para fins de cálculo, porém, somente uma variável de data pode estar presente na expressão.

Outro exemplo:

.

Após cadastrar, é possível selecionar no combo da tela de laudagem:

O modelo aplicado na tela de laudagem:

Solicitação de RevisãoSolicitação de Revisão

## **Solicitar Revisão de Laudo**

### **Objetivo**

Permitir ao médico radiologista solicitar a revisão de um laudo por um ou mais colegas radiologistas, promovendo uma análise colaborativa e qualificada, contribuindo para a segurança do paciente.

### **Disponibilidade**

A funcionalidade estará disponível **exclusivamente** para exames com status:

* **Digitação Concluída**
* **Revisado**

### **Acesso**

Na **Central de Laudos**, dentro do menu **“Ações”**, estará disponível a nova opção:

* **Solicitar Revisão**

### **Fluxo da Solicitação**

1. O médico clica em **“Solicitar Revisão”**.
2. É exibida uma **caixa de seleção com multiselect** contendo **médicos radiologistas com a flag de responsável técnico** ativa no cadastro.
3. O médico pode **selecionar um ou mais colegas** da lista.
4. Ao confirmar:

   * O status do laudo muda para **“Aguardando Revisão”**.
   * É exibida uma **mensagem de sucesso** confirmando o envio.
   * O(s) médico(s) revisor(es) receberão uma **notificação** com o exame designado.
   * O **solicitante da revisão** (digitador ou médico responsável) verá no painel que o laudo está aguardando revisão.
   * Para fins de notificação, o solicitante será **o médico responsável** do exame.

### **Regras Específicas**

* A lista exibida será preenchida com **médicos radiologistas** ativos que possuem a **flag de “Responsável Técnico”** habilitada.
* A solicitação de revisão **não é possível** em status diferentes dos permitidos.
* A **notificação de revisão** será enviada **individualmente para cada revisor selecionado**.
* A **seleção da revisão é obrigatória** (não pode confirmar sem selecionar pelo menos um médico).
* A nova funcionalidade **não interfere nos campos ou status atuais da tela de laudagem**.

### **Edição de Solicitação de Revisão**

**Nova Aba "Revisões"**:  
Foi adicionada uma nova **aba** ao lado da aba de **Exames Anteriores**, com o título **"Revisões"**.

Ao acessar a aba de Revisão de Laudos, será exibido o **nome do(s) médico(s)** designado(s) para revisar o laudo.

Caso nenhuma revisão tenha sido feita ainda, uma mensagem informativa será exibida na aba: "Nenhuma revisão registrada até o momento."

1. #### Abertura do Modal

   1. **Ação**: Clicar no ícone **"+"**.
   2. **Resultado**: Exibição de um **modal** contendo:

      * Campo de texto para revisão (limite de **8000 caracteres**).
   3. Checkbox: **"Sem observações"**.
2. #### Comportamentos do Checkbox

   1. Quando **marcado**:

      1. O campo de texto será **bloqueado** para edição.
      2. Se o campo já tiver sido preenchido antes de marcar o checkbox, uma **mensagem de confirmação** será exibida:

         > "Ao marcar que não houve observações, o conteúdo digitado será apagado. Deseja continuar?"

         1. Se **SIM**, o campo será limpo.
         2. Se **NÃO**, a marcação do checkbox será revertida.
   2. Quando **desmarcado**:

      1. O campo de texto será novamente **habilitado** para edição.
3. #### Salvamento

   1. A revisão será considerada **finalizada** **somente** ao clicar no botão:

      1. **"Adicionar Revisão"** (confirmação/finalização da revisão).

         1. Caso o botão seja clicado sem que o checkbox 'Sem observações' esteja marcado e o campo de observações esteja vazio, uma mensagem de alerta será exibida ao usuário.
   2. Ao clicar no **ícone de X** no canto do modal, a janela será fechada **sem salvar alterações**.
   3. Ao clicar no botão **'Adicionar Revisão'**, caso a observação esteja preenchida ou o checkbox **'Sem observações'** esteja marcado, uma mensagem de sucesso será exibida confirmando a finalização do registro.

### **Painel de Revisões**

###### Neste painel, é possível visualizar todas as revisões referentes ao laudo selecionado.

1. O acesso ao painel é feito por meio do botão **"Ver todas as revisões".**
2. Ao clicar no botão, será exibido um painel contendo todas as revisões, com suas respectivas observações abertas e visíveis ao usuário.

### **Cancelamento de Solicitação de Revisão**

1. Vá em **Central de Laudos**, no menu **“Ações”**, opção **“Cancelar Solicitação de Revisão”;**
2. A opção **“Cancelar Solicitação de Revisão”** só estará disponivel se o status do laudo for **"Aguardando Revisão";**

1. Após clicar será exibida uma tela onde é possivel informar um **motivo** para o cancelamento e as opções para **confirmar ou cancelar**.
2. Ao clicar bo botão confirmar:

   * O cancelamento só ocorrerá se:
     + Existir solicitação de revisão para o laudo;
     + O status do laudo for **"Aguardando Revisão";**
     + O usuário que esta solicitando o cancelamento for o mesmo usuário que solicitou a revisão**;**
   * O status do laudo mudará para **“Digitação Concluída”** se não houver nenhum solicitação de revisão com status **"Finalizado"**.
   * O status do laudo mudará para **“Revisado”** se houver uma ou mais solicitação de revisão com status **"Finalizado"**.
3. Ao clicar bo botão cancelar:
   1. Irá fechar a tela apenas;

Gravador de Áudio de Laudo

## **Gravador de Áudio de Laudo** **Objetivo**

O componente de **Gravação de Áudio de Laudo** permite ao médico responsável gravar observações de voz relacionadas a um exame em andamento. A funcionalidade é controlada por regras específicas de status do laudo, tempo de gravação e permissões por usuário.

### **Disponibilidade**

A funcionalidade de gravação de áudio **só estará disponível** quando o laudo estiver em um dos seguintes status:

* **Inicial**
* **Digitação**
* **Revisado**

### **Acesso**

Na **Central de Laudos**, ele estará diretamente disponível ao abrir o laudo:

1. **Iniciar Gravação**
   1. Clique no botão com o ícone de **microfone** para começar a gravação.
   2. Se o laudo **não tiver médico responsável atribuído**, o sistema vai automaticamente definir o **usuário logado como responsável** antes de iniciar a gravação.
2. **Pausar e Retomar**
   1. Durante a gravação, você verá dois botões (Você pode pausar e retomar quantas vezes quiser dentro do tempo limite):
      1. **⏸️ Pausar**: Interrompe temporariamente a gravação.
      2. **▶️ Retomar**: Continua a gravação de onde parou.
3. **Encerrar a Gravação**
   1. Clique no botão **⏹️ Parar** para finalizar a gravação.
      1. O áudio será processado e exibido automaticamente abaixo do gravador em formato de **player**, permitindo ouvir o que foi gravado.
      2. Você poderá escutar, ajustar a velocidade.
4. ### Limite de Gravação

   1. O tempo máximo de gravação é de **15 minutos**.
   2. Ao atingir esse limite, a gravação será finalizada automaticamente.
5. ### Quando o Áudio é Apagado

   1. Se o status do laudo for alterado para **"Emitido"**, o áudio gravado será **automaticamente excluído** do sistema.
   2. Isso garante que apenas exames em edição mantenham anotações de voz ativas.

Solicitação de Reconvocação

## **Solicitação de Reconvocação de Exame** **Objetivo**

A funcionalidade de **Solicitação de Reconvocação** permite ao médico radiologista solicitar a repetição de um exame que já foi realizado, visando garantir maior precisão no diagnóstico. A solicitação é acompanhada de justificativa e classificação de urgência, sendo registrada no sistema com atualização automática do status do exame.

### **Disponibilidade**

A opção de solicitar reconvocação estará disponível **somente para exames com os seguintes status**:

* **Inicial**
* **Em Digitação**

### Motivo da Solicitação

* O campo de **motivo da reconvocação** é **obrigatório**.
* Será exibida uma **lista de motivos** onde podemos gravar novos motivos ou apagar.
* Um **campo de complemento descritivo (opcional)** estará disponível para detalhamento adicional, quando necessário.

### Classificação da Urgência

* O solicitante deverá **especificar a urgência** da reconvocação:

  + **Urgente**
  + **Normal**
* A urgência será utilizada para priorização no fluxo de atendimento.

### Atualização de Status

* Após o envio da solicitação, o sistema irá **alterar automaticamente o status do exame para "Reconvocado"**.
* Esse status será utilizado para indicar que o exame está pendente de nova execução.

### **Acesso**

Na **Central de Laudos**, ele estará diretamente disponível ao abrir o menu de ações:

Ao selecionar o item no menu, será exibido um modal contendo todos os campos obrigatórios para preenchimento da solicitação:

#
