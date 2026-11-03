---
content_hash: 5ae5f8d0fc584f12573fb73353e37e0326485ab1ae44c371bad648c7e95661cc
fetched_at: '2026-06-29T00:11:11.180443+00:00'
page_id: '646226744'
product: rm
source: tdn-rm
title: Painel Classificação de Risco
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=646226744
version: 62
---

## **CONTEÚDO**

1. **Visão Geral**
   1. **Exemplo de utilização**
   2. **Telas utilizadas**
   3. **Prefixo unidade**
   4. **Documentações relacionadas**
2. **Fluxo de triagem e atendimento**
3. **Atualização V. 12.1.2410**
   1. #### **Visão geral**
   2. **Classificação de risco**
   3. #### **Cadastros e parametrizações no RM**
4. **Configurações**

Visão geralVisão geral

## **1. Visão geral**

A tela do Painel de classificação de risco do PEP RM corresponde à aba "Atendimento Médico" do Painel de classificação de risco  do RM Saúde, cujo propósito é exibir a fila de pacientes classificação de risco a serem chamados pelo médico, segundo as configurações do RM Saúde.

Exemplo de utilização

## **a. Exemplo de utilização**

Ao acessar a tela de Painel de classificação de risco o sistema carregará 5 pacientes ou quantos estiverem agendados para atendimento no dia. Serão carregados apenas os pacientes das ultimas 24 horas.

Telas utilizadas

## **b. Telas utilizadas**

Para que a listagem de pacientes seja iniciada é necessário que a unidade seja informada, caso contrário não serão listados.

Para buscar mais pacientes podem ser realizadas as seguintes buscas:

* Busca de Pacientes: Através do campo "Buscar pacientes"  é possível realizar a busca pelo código, nome ou nome social do paciente e a palavra buscada poderá estar no início, meio ou final do nome e leitura da pulseira de identificação do paciente (código de barras).
* Ao filtrar os resultados, os filtros atualmente selecionados são refletidos logo acima da listagem;
* Carregar mais resultados: Em qualquer momento, pode-se clicar no botão "Carregar mais resultados", fazendo com que a página carregue mais 5 resultados da pesquisa.

A qualquer momento é possível selecionar o paciente desejado clicando na opção "Selecionar" no canto direito das informações do paciente.

Por padrão a tela virá com a opção **'Todos'** selecionada, trata-se da visão do perfil médico e enfermagem juntas, porem é possível escolher dentre os dois de forma separada. Ao escolher determinada opção os status serão limitados a somente os status daquela opção. É possível alterar os status manualmente e escolher por exemplo o status **'finalizados'** e **'ausentes'** que não faz parte de nenhum perfil, a listagem de pacientes será atualizada assim que qualquer filtro ou status for alterado.

Prefixo da unidade

## **c. Prefixo da unidade**

Existe uma configuração no cadastro de unidade de atendimento que permite que seja configurado um prefixo para todas as senhas obtidas no toten para aquela unidade. O acesso à configuração se dá conforme imagem abaixo:

RM > Cadastros > Unidade de atendimento > Seleciona a unidade > Aba "Painéis" > Classificação de Risco - Atendimentos de urgência/Emergência > Prefixo da senha.

Quando existir um prefixo configurado, ele aparecerá antes da senha no **painel de classificação de risco** do **PEP RM** da seguinte forma:

Documentações relacionadas

## **d. Documentações relacionadas**

Exemplo de UtilizaçãoIniciar Atendimento

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Perfil enfermagem**
4. **Perfil médico**
5. **Parametrizações necessárias**
6. **Definição de Sala**

## **01. VISÃO GERAL**

Esta funcionalidade está presente no painel de classificação de risco e tem como objetivo permitir que o profissional inicie um atendimento para um determinado paciente ou para o próximo eletivo.

## **02. EXEMPLO DE UTILIZAÇÃO**

Ao acessar a tela de Painel de urgência/emergência o sistema carregará os pacientes de acordo com o filtro por status do atendimento.

De acordo com o perfil do usuário logado no sistema, a opção chamar o próximo irá chamar paciente para triagem (perfil enfermagem) ou para atendimento (perfil médico).

O paciente também pode ser chamado direto em suas opções.

## **03. PERFIL ENFERMAGEM**

Caso seja chamado um paciente para triagem, é aberto uma modal informando os dados do paciente para confirmação do início de triagem.

Ao iniciar a triagem será aberto a modal para realizar a classificação de risco do paciente.

Após a classificação ser realizada, o paciente passará a estar com o status de **aguardando**, onde estará pronto para iniciar o atendimento médico.

## **04. PERFIL MÉDICO**

Caso seja chamado um paciente para atendimento médico, é aberto uma modal informando os dados do paciente para confirmação do início do atendimento.

## **05. PARAMETRIZAÇÕES NECESSÁRIAS**

Para que seja possível chamar um paciente específico no PEP é necessário que o parâmetro '**Chama o paciente nas filas através do duplo clique no registro do grid'** seja habilitado através da antiga MDI do RM (Delphi).

A tela para alteração deste parâmetro pode ser acessada pelo menu '**Parâmetros Gerais**':

Na aba '**Classificação de Risco**' o parâmetro pode ser encontrado no canto inferior esquerdo:

A partir da **versão 12.1.2406**, esse parâmetro foi movido para: RM > Ambiente > Parâmetros > Gestão Hospitalar > Classificação de risco > Classificação de risco 2/3.

**Parametrização de risco:** RM Saúde > Cadastros > Cuidados com o paciente > Outros Cadastros > Cadastro e Parametrização de risco.

Sugerimos que seja utilizado o padrão:

Emergente - VERMELHO 198,72,64   
Muito Urgente - LARANJA 255,107,0  
Urgente - AMARELO 255,168,0  
Pouco Urgente - VERDE 86,185,107  
Não Urgente - AZUL 12,154,190

Para realizar a alteração de cor RGB segue:

## **06. DEFINIÇÃO DE SALA**

Para definir a sala no PEP RM, basta preencher o campo ao lado da unidade. Caso ele já tenha sido informado no RM Saúde, a informação de lá será exibida também e o preenchimento deste campo também afeta a sala informada pelo RM Saúde para o mesmo usuário.

      

Finalizar Atendimento

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Parametrizações necessárias**

## **01.****VISÃO GERAL**

Esta funcionalidade presente no painel de classificação de risco tem como objetivo permitir que o profissional finalize um atendimento para um determinado paciente.

## **02. EXEMPLO DE UTILIZAÇÃO**

Ao acessar a tela de Painel de classificação de risco o sistema carregará os pacientes de acordo com o filtro por status do atendimento.

É possível finalizar utilizando o painel ou o próprio prontuário do paciente.

Caso esteja no painel de classificação a funcionalidade estará disponível em:

**\*Observação: Funcionalidade presente somente a partir da versão 12.1.2310 no painel "Médico(a)";**

Caso esteja no prontuário do paciente em atendimento a funcionalidade estará disponível em:

Selecionando a opção de finalização de atendimento, uma modal será aberta onde devem ser informados alguns dados, tais como tipo de saída e CID para confirmar a finalização.

Caso o atendimento seja de enfermagem, ao finalizar as informações não serão necessárias.

Após a confirmação e retornar para a listagem, o status do paciente constará como finalizado. Para listar pacientes com esse status basta selecionar a opção acima.

## **03. PARAMETRIZAÇÕES NECESSÁRIAS**

E possível parametrizar o tipo de saída padrão e definir se o CID é obrigatório ou não ao finalizar atendimento. Para que seja possível deve ser configurado através da antiga MDI do RM (Delphi).

A tela para alteração deste parâmetro pode ser acessada pelo menu '**Parâmetros Gerais**':

Na aba '**Classificação de Risco**' o parâmetro de motivo de desistência pode ser encontrado em:

Na aba '**Registro e Controle**' o parâmetro de CID obrigatório pode ser encontrado no canto inferior esquerdo:

É possível parametrizar a confirmação da triagem tornando obrigatório ou não ao finalizar atendimento. Para que seja possível deve ser configurado através da tela de unidade de atendimento no RM Saúde:

RM Saúde > Cadastros > Unidade de Atendimento > Aba PEP RM > Geral.

Enviar para Observação 

## **CONTEÚDO**

1. **Visão Geral**
2. **Telas utilizadas**

## **01. VISÃO GERAL**

Esta funcionalidade está presente no painel de classificação de risco e tem como objetivo permitir que o profissional envie um determinado paciente para observação.

## **02. TELAS UTILIZADAS**

Ao acessar a tela de Painel de classificação de risco o sistema carregará os pacientes de acordo com o filtro por status do atendimento.

Para enviar o paciente para observação o mesmo deve estar no status '**Em Atendimento**'

Nas ações disponíveis para o paciente na tabela, deve-se selecionar a opção **'Enviar para observação'**.

O paciente será enviado para observação somente após a confirmação da ação.

Retornar Atendimento

## **CONTEÚDO**

1. **Visão Geral**
2. **Telas utilizadas**

## **01. VISÃO GERAL**

Esta funcionalidade está presente no painel de classificação de risco e tem como objetivo permitir que o profissional retorne um atendimento finalizado para em atendimento.

## **02. TELAS UTILIZADAS**

Ao acessar a tela de Painel de classificação de risco o sistema carregará os pacientes de acordo com o filtro por status do atendimento.

Para enviar o paciente para observação o mesmo deve estar no status '**Finalizado**'

Nas ações disponíveis para o paciente na tabela, deve-se selecionar a opção **'Retornar atendimento'**.

O paciente será enviado para "Em atendimento" somente após a confirmação da ação.

OBS: Não será possível utilizar a opção caso exista outro paciente em atendimento pelo mesmo médico.

Retornar para aguardando

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**

## **01. VISÃO GERAL**

Esta tela tem como objetivo auxiliar o profissional quando for necessário retornar o paciente para o status de aguardando.

## **02. EXEMPLO DE UTILIZAÇÃO**

Ao acessar a tela de painel de classificação de risco o sistema carregará os pacientes de acordo com o filtro selecionado trazendo ações disponíveis na última coluna da tabela.

Essa função é exclusiva de pacientes que estejam com o atendimento iniciado.

O paciente será enviado para aguardando somente após a confirmação da ação.

Transferir paciente

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**

## **01. VISÃO GERAL**

Esta tela tem como objetivo auxiliar o profissional quando for necessário transferir paciente.

## **02. EXEMPLO DE UTILIZAÇÃO**

Ao acessar a tela de painel de classificação de risco o sistema carregará os pacientes de acordo com o filtro selecionado trazendo ações disponíveis na última coluna da tabela.

Essa função é exclusiva de pacientes que estejam com o atendimento iniciado.

Triagem

## **CONTEÚDO**

1. **Visão Geral**
2. **Composição da tela**
3. **Exemplo de utilização**

Atualização

A partir da versão 12.1.2410 o Painel de urgência/emergência, as parametrizações e o formulário de classificação de risco do sistema passaram por atualização visual e foram adicionadas novas funções. Confira as mudanças na aba "Atualização 12.1.2410".

## **01. VISÃO GERAL**

Esta tela tem como objetivo auxiliar o profissional quando for necessário realizar a classificação do paciente.

## **02. COMPOSIÇÃO DA TELA**

Ao iniciar a triagem pelo painel de classificação ou pelo prontuário do paciente o registro passará a ter o status **'triagem iniciada'** e uma janela será aberta contento alguns dados do paciente e do responsável pelo atendimento. Alguns dados dessa janela são provenientes de cadastros vindos do RM, tais como os sinais vitais.

Estes estão disponíveis seguindo o caminho: Gestão Hospitalar > Cadastros > Prescrição médica > Itens de Enfermagem e filtrar pelo tipo 19 (Sinais Vitais)

Protocolos, disponíveis em: Gestão Hospitalar > Cadastros > Outros cadastros >  Fluxos de protocolo de classificação de risco.

E os discriminadores, que podem ser vinculados de duas formas aos parâmetros de risco.

Vinculo com o protocolo selecionado e ao parâmetro de classificação.

 Gestão Hospitalar > Cadastros > Outros cadastros >  Fluxos de protocolo de classificação de risco.

E o vinculo direto ao parâmetro de classificação em: Gestão Hospitalar > Cadastros > Outros cadastros >  Discriminadores da classificação de risco.

A tela também possui escala de dor e Glasgow.

Caso seja informado a opção fluxo de atendimento de enfermagem, o atendimento aparecerá no painel de enfermagem onde poderá ser realizado o atendimento ou encaminhado para o médico na opção "Encaminhar".

O fluxo de atendimento de enfermagem também é seguido caso seja selecionado uma especialidade que não realiza atendimento médico.

Ao utilizar fluxo de enfermagem ou uma especialidade que não realiza atendimento médico os discriminadores que determinam o parâmetro de risco são limpos e desabilitados.

## **03.****EXEMPLO DE UTILIZAÇÃO**

Após preencher os campos de classificação e finalizar, o registro estará pronto para atendimento médico tendo o status de **'aguardando'**e informando sempre a classificação atual.

Reclassificação

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**

## **01. VISÃO GERAL**

Esta tela tem como objetivo auxiliar o profissional quando for necessário reclassificar o registro de atendimento

## **02. EXEMPLO DE UTILIZAÇÃO**

Ao acessar a janela de classificação com a triagem finalizada, é possível selecionar a classificação atual e realizar a reclassificação.

É possível realizar quantas reclassificações forem necessárias, bastando informar o motivo, observação e a nova classificação. Após a confirmação da reclassificação será possível editar quaisquer campos da classificação anterior

O campo motivo é proveniente de um cadastro do RM, disponível em Gestão Hospitalar > Cadastros > Outros cadastros >  Cadastro de motivos (Reclassificação, repriorização).

Adicionar ou Remover Pacientes da Fila 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Telas utilizadas**

## **01. VISÃO GERAL**

Esta tela tem como objetivo auxiliar o profissional quando for necessário remover ou adicionar pacientes da fila.

## **02. EXEMPLO DE UTILIZAÇÃO**

Ao acessar a tela de painel de classificação de risco o sistema carregará os pacientes de acordo com o filtro selecionado trazendo ações disponíveis na última coluna da tabela. Para filtrar pelos pacientes ausentes, basta selecionar o filtro ausentes.

## **03. TELAS UTILIZADAS**

A qualquer momento é possível remover o paciente da fila, para isso basta selecionar a opção a **'Remover da fila'** nas opções do paciente.

O paciente será removido da fila somente após a confirmação da ação.

Para retornar o paciente a fila basta selecionar a opção **'Adicionar à fila'**, opção exclusiva de pacientes com status **'Ausente'.**

O paciente será adicionado à fila somente após a confirmação da ação.

Fluxo de triagem e atendimento

## **2. Fluxo de triagem e atendimento**

O usuário poderá alterar a ordem do fluxo de atendimento para que os profissionais realizem a triagem e a classificação de risco antes que o paciente faça o registro de atendimento, utilizando o parâmetro **"Utiliza registro de atendimento ANTES da classificação de risco"** no RM.

RM > Ambiente > Parâmetros >  Gestão Hospitalar > Classificação de risco > Classificação de risco  1/3 > Desmarcar checkbox do parâmetro "Utiliza registro de atendimento ANTES da classificação de risco".

Com essa parametrização, após o paciente retirar sua senha no toten de atendimento e ser chamado pelo painel, ele será encaminhado para realizar a triagem. No painel de urgência e emergência, utilizando um usuário de enfermeiro, na tabela será exibido a senha gerada, o status "Aguardando triagem", o tempo de espera e a especialidade selecionada.  Após o(a) enfermeiro(a) chamar o paciente pelo painel, o único dado exibido na modal será a senha gerada para o paciente.

 Ao clicar no botão "Iniciar triagem", o usuário será redirecionado para a nova tela de triagem e será exibido o formulário de classificação, com a seção adicional "Dados do paciente" e os campos para preenchimento: "Nome do paciente", "Data de nascimento", "Nome da mãe" e "Meio de chegada".

Os campos “Nome da mãe” e “Data de nascimento” são opcionais, mas podem ser parametrizados como obrigatórios no RM:

RM > Ambiente > Parâmetros >  Gestão Hospitalar > Classificação de risco > Classificação de risco  2/3 > Marcar checkbox do parâmetro "Obriga preenchimento de Nome da mãe e Data de nascimento na classificação de risco".

Com a parametrização habilitada, os campos serão sinalizados como obrigatórios no formulário, e o botão “Finalizar” permanecerá desabilitado até que todos os campos obrigatórios sejam preenchidos.

Ao finalizar a triagem, o(a) enfermeiro(a) poderá marcar o checkbox "Fluxo atendimento de enfermagem" para que o paciente seja atendido por enfermeiros(as) ou finalizar sem marcar o checkbox e seguir o fluxo de atendimento médico com a especialidade selecionada.

Após a finalização da triagem, os dados do paciente preenchidos no formulário de classificação de risco serão exibidos no painel de classificação de risco no RM, na aba "Registro de atendimento" e o registro de atendimento deverá ser realizado conforme o usual no RM.

Ao selecionar o paciente, o usuário deverá confirmar os dados clicando em "Pesquisar" e se o paciente já estiver registrado na base será exibido na lista todas as informações cadastradas.

Após finalizar o registro de atendimento, o paciente será exibido na lista de atendimento médico ou de enfermagem, conforme o fluxo selecionado na finalização da triagem.

Atualização V. 12.1.2410

## **3.****Atualização V. 12.1.2410**

##### **Funcionalidade disponível a partir da versão 12.1.2410.**

## **a. Visão Geral**

A partir da versão 12.1.2410, o Painel de urgência/emergência, as parametrizações e o formulário de classificação de risco do sistema passaram por atualização visual e foram adicionadas novas funções. 

As funcionalidades da tela inicial do Painel de urgência e emergência permanece conforme a utilização geral anterior.

O histórico de triagem e o formulário da classificação realizada no dia poderão ser visualizadas através da aba " Classificação de risco", no menu lateral do prontuário eletrônico, sem possibilidade de edição.

## **b. Classificação de risco**

A triagem é fundamental para a realização de uma avaliação inicial estruturada e eficiente para o paciente. O formulário de classificação de risco aplicado durante a triagem ajuda a priorizar o atendimento de acordo com a gravidade das condições de saúde dos pacientes, visando permitir uma avaliação eficiente e precisa, padronizando a triagem e garantindo que todos os pacientes sejam avaliados de maneira consistente e conforme os protocolos da instituição.

Após o(a) enfermeiro(a) chamar o paciente pelo painel, confirmar os dados exibidos e clicar no botão "Iniciar triagem", o usuário será redirecionado para a nova tela de triagem e será exibido o formulário com as seguintes seções e campos para preenchimento:

Tela inicial

### **a. Tela inicial**

* Tag Classificação: essa tag indica a classificação do paciente.
* Tag Atendimento: essa tag indica o total de atendimentos no pronto atendimento daquele serviço.
* Último atendimento realizado: quando houver, será exibido uma mensagem ao lado das tags informando a data e horário do último atendimento do paciente realizado na instituição.
* Checkbox "Fluxo atendimento de enfermagem": o usuário poderá sinalizar a utilização do fluxo de atendimento de enfermagem marcando o checkbox, quando necessário.
* Botão "Histórico de triagem": exibe a data, hora e a classificação escolhida para os atendimentos realizados anteriormente, quando houver. Ao expandir o accordion é exibido o nome do profissional responsável pela triagem e o conselho.
* Botão "Finalizar": finaliza a triagem.

Ao clicar no botão "Finalizar", uma modal de finalização será exibida, composta pelo resultado da triagem e o direcionamento do atendimento para especialidades, caso não tenha sido definido durante o registro de atendimento.

O nível de urgência será preenchido automaticamente com uma sugestão de triagem com base nos critérios definidos no cadastro do protocolo (quando o profissional preencher o campo relacionado aos protocolos) e o(a) profissional tem autonomia para trocar a triagem proposta pelo sistema.

Para salvar a triagem o usuário poderá clicar em "Finalizar" ou "Finalizar e imprimir". Para retornar a triagem o usuário poderá clicar em "Cancelar".

Durante a triagem, o enfermeiro pode alterar a especialidade para refletir melhor a necessidade clínica do atendimento. Quando a especialidade for alterada na triagem o sistema deve **atualizar automaticamente a especialidade no registro de atendimento**.

Escuta inicial

### **b. Escuta Inicial:**

* Protocolo de classificação de risco: campo de listagem para seleção dos protocolos cadastrados na classificação de risco no RM.
* Duração: campo aberto para preenchimento da duração dos sintomas.
* Queixa secundária: campo de texto livre para descrever outras queixas.
* Sintomas: quando o usuário selecionar um protocolo serão exibidos os sintomas relacionados conforme cadastro no RM e quando não selecionar nenhum protocolo, todos os sintomas cadastrados no RM serão exibidos.
* Detalhes da queixa/sintomas: campo de texto livre para descrever os detalhes de queixas e sintomas.

Gerenciamento de Risco

### **c. Gerenciamento de Risco**

Ao habilitar, será exibida uma tabela para registrar os riscos apresentados pelo paciente. O usuário poderá escolher o tipo de risco que iniciará o cadastro sendo, alergia, alerta clinico ou isolamento.

Para o cadastro de alergia é necessário trazer o princípio ativo atrelado ao risco, para o alerta clínico o usuário digita qual o tipo de alerta será registrado e isolamento qual o isolamento, a causa e a descrição.

Os registros vão compor a funcionalidade do PEP portanto, o que é cadastrado no momento da triagem será populado do gerenciamento de risco do PEP com mais opções de registros.

Sinais vitais

### **d. Sinais vitais:**

Ao habilitar, será exibida uma tabela para registrar os sinais vitais. Ao clicar no botão "+Adicionar", a mesma modal da aba de [Monitorização Geral](https://tdn.totvs.com/pages/viewpage.action?pageId=815586862), será exibida para preenchimento. Os sinais vitais adicionados na triagem também serão salvos na tabela de “Monitorização Geral”, em  [Controles de Enfermagem](https://tdn.totvs.com/pages/viewpage.action?pageId=811696943).

O usuário poderá desabilitar a sessão caso não tenha aferido os sinais vitais do paciente.

Glicemia capilar

### **e. Glicemia capilar:**

Ao habilitar, será exibida uma tabela para registrar a glicemia capilar. Ao clicar no botão "+Adicionar", a mesma modal da aba de [Monitorização Geral](https://tdn.totvs.com/pages/viewpage.action?pageId=815586862), será exibida para preenchimento. A glicemia capilar adicionada na triagem também será salva na tabela de “Monitorização Geral”, em [Controles de Enfermagem](https://tdn.totvs.com/pages/viewpage.action?pageId=811696943).

O usuário poderá desabilitar a sessão caso não tenha aferido a glicemia capilar do paciente.

Scores e escalas

### **f. Scores e escalas:**

Ao habilitar, será exibida uma tabela para registrar os scores e escalas aplicadas. Ao clicar no botão "+Adicionar", a mesma modal utilizada nos [Scores](https://tdn.totvs.com/pages/viewpage.action?pageId=844259781) será exibida para preenchimento com os scores e escalas parametrizadas para serem utilizados na unidade de atendimento referente a triagem. Todos os registros adicionados na triagem também serão salvos na aba de [Scores](https://tdn.totvs.com/pages/viewpage.action?pageId=844259781) no PEP.

O usuário poderá desabilitar a sessão caso não tenha aplicado scores e escalas.

Antecedentes clínicos pessoais

### **g. Antecedentes clínicos pessoais:**

Ao habilitar, será exibido um campo de busca listando algumas enfermidades, com o mesmo comportamento do  e o campo "Observações antecedentes clínicos pessoais" de texto livre para acrescentar um ou mais antecedente clínicos e/ou complementar as informações.

Medicamentos de uso contínuo

### **h. Medicamentos de uso contínuo**

Ao habilitar, uma tabela será exibida para registrar os medicamentos de uso contínuo do paciente. Ao clicar no botão "+Medicamento", a mesma modal utilizada no  será exibida para preenchimento.

Observações

### **i. Observações**

Campo de texto livre para informações complementares.

Relatório da classificação de risco

### **j. Relatório da classificação de risco**

Ao finalizar a triagem e clicar em "Finalizar", o usuário poderá finalizar apenas ou finalizar e imprimir. No prontuário do paciente, na aba "Classificação de risco" o usuário também poderá gerar o relatório clicando no botão "Imprimir". O relatório da triagem será exibido em uma nova aba do navegador e poderá ser impresso, se necessário.

Reclassificação 

### **k. Reclassificação**

Com um perfil médico (CRM) ou de enfermagem (COREN), ao acessar a aba "Classificação de risco" no prontuário do paciente com a triagem finalizada, o usuário poderá reclassificar a triagem, confirmar a triagem e clicando no botão mais ações terá as opções de imprimir o formulário e de visualizar o histórico de triagem.

## **c.** **Cadastros e parametrizações no RM**

Parametrização de Riscos

### a. Parametrização de Riscos

Na parametrização de de riscos, o cadastro das classificações "Emergência", "Muito Urgente", "Urgente", "Pouco Urgente", "Não Urgente" e "Outros" são fixos  e o usuário poderá cadastrar o protocolo de triagem utilizado na instituição trazendo a nomenclatura desejada, cor e SLA (tempo de espera) de atendimento de acordo com a criticidade do paciente.

RM > Cadastro > Cuidados com o Paciente > Outros cadastros > Gerenciamento de riscos > Cadastro e parametrização de riscos.

 

Sintomas

### **b. Sintomas**

No cadastro de sintomas, foi adicionado um anexo para que o usuário consiga parametrizar quais classificações utilizam o sintoma cadastrado, por exemplo: o sintoma "febre" pode ser classificado como "Urgente" dentro de um conjunto de outros sintomas ou como "Emergência" em outros.

RM > Cadastro > Cuidados com o Paciente > Outros Cadastros > Gerenciamento de riscos > Sintomas da Classificação de risco;

Selecione o sintoma > Anexo "Classificação de risco do sintoma" > Botão "adicionar" ou "editar" > digite a classificação de risco no campo de busca "Código parametrização risco" > Salvar.

Protocolo de Classificação de riscos 

### **c. Protocolo de Classificação de riscos**

O usuário poderá cadastrar o nome do protocolo de atendimento clínico utilizado na triagem pela instituição, para fazer a amarração da queixa principal com sintomas associados no cadastro da classificação de risco.

RM > Cadastro > Cuidados com o Paciente >  Outros Cadastros > Gerenciamento de riscos > Fluxos do Protocolo de Classificação de Risco.

Ao clicar no botão "Adicionar" o usuário deverá preencher o campo "Descrição". 

Para associar os sintomas clique na aba "Discriminadores associados", e em "Processos" clique em "Associar discriminadores da classificação de risco".

Para exibir os sintomas, preencha o campo de busca "Classificação de risco" com a classificação desejada e todos os sintomas que foram parametrizados com a respectiva classificação serão exibidos para seleção. Marque o checkbox de todos os sintomas necessários e clique no botão "Executar" para finalizar a inclusão. Uma mensagem será exibida indicando se o processo foi executado com sucesso.

Para fechar a tela de inclusão, clique no botão "Cancelar". Clique no ícone de atualização , para exibir os sintomas adicionados. Para finalizar e fechar a modal, clique no botão "Ok".

### 

### 

Cadastro de Classificação de Risco (Protocolos de triagem - steps RM)

### **d. Cadastro de Classificação de Risco (Protocolos de triagem - steps RM)**

O usuário poderá realizar o cadastro das classificações de risco, para definir os parâmetros e critérios que auxiliarão na triagem de pacientes. O cadastro será baseado nos Protocolos de Classificação de Risco previamente cadastrados (RM > Cadastro > Cuidados com o Paciente >  Outros Cadastros > Gerenciamento de riscos > Fluxos do Protocolo de Classificação de Risco).

RM > Cadastro > Cuidados com o Paciente > Outros Cadastros > Gerenciamento de riscos > Cadastro de Protocolos de triagem.

Na tela inicial, todos os protocolos cadastrados serão apresentados em uma tabela contendo as colunas: "Protocolo de Classificação de Risco" e "Unidade de Atendimento" selecionadas no cadastro. Para visualizar os protocolos cadastrados, clique no ícone de seta do respectivo protocolo na tabela.

Pra cadastrar um novo protocolo, clique no botão "+ Incluir". Em seguida um novo formulário será exibido com as seguintes sessões para preenchimento:

* ### **Critérios:**

Protocolo de Classificação de Risco: o campo exibe uma lista com todos os  protocolos de classificação de risco cadastrados.

Unidade de Atendimento:  o campo exibe uma lista com todas as unidades de atendimento para seleção e será permitido apenas um cadastro por unidade.

* ### **Parâmetros:**

No cadastro serão apresentados 6 níveis de criticidade para a classificação, sendo: "Emergência", "Muito Urgente", "Urgente", "Pouco Urgente", "Não urgente" e "Outros'. Cada nível de criticidade terá um "step" a ser preenchido com os critérios relacionados com aquele descritor e classificação. Por exemplo: dor abdominal - Vermelho (atendimento imediato), será utilizado de acordo com determinados resultados dos sinais vitais, scores e sintomas. 

Cada nível de criticidade estará associado a uma nomenclatura, descrição, cor e tempo de espera definido pelo usuário no cadastro e parametrização de riscos (RM > Cadastro > Cuidados com o Paciente > Outros cadastros > Gerenciamento de riscos > Cadastro e parametrização de riscos). Os campos serão preenchidos automaticamente sem a possibilidade de edição de acordo com cada step que o usuário estiver preenchendo.

Em seguida o usuário poderá habilitar ou desabilitar, conforme necessidade, os parâmetros de sintomas, sinais vitais e scores/escalas:

Ao desabilitar, os parâmetros ficam ocultos e o usuário poderá clicar no botão "Próximo", para seguir com o preenchimento do próximo step.

Ao habilitar, todos os parâmetros serão exibidos para preenchimento e o usuário poderá desabilitar individualmente cada parâmetro que não for necessário:

* ### **Sintomas:**

Ao habilitar a parametrização de sintomas, será exibido no campo de busca uma lista para seleção contendo apenas os sintomas associados ao cadastro do protocolo selecionado se tiverem a respectiva criticidade do step. Por exemplo: Cadastro do Protocolo de "dor abdominal" para criticidade "Muito Urgente", apenas os sintomas associados a "dor abdominal" com a classificação "muito urgente" serão exibidos na lista. 

Não é possível acrescentar novos sintomas que **não** **estejam previamente vinculados** ao cadastro do protocolo de classificação.

Não é obrigatório um cadastro de sintoma na classificação de risco, porém deve-se definir os valores mínimos e/ou máximos dos filtros (Sinais Vitais ou Scores).

* ### **Sinais vitais:**

Ao habilitar a parametrização de sinais vitais, será exibido uma tabela contendo os sinais vitais e o usuário poderá relacionar ao protocolo o valor mínimo e máximo para alterações. Os campos de sinais vitais são fixos (o usuário não pode adicionar ou remover qualquer sinal vital da tabela), e o usuário não precisa preencher todos eles para prosseguir.

Os valores máximos e minímos são valores de normalidade, ou seja, tudo que estiver fora da faixa cadastrada será relevante para o cálculo final do nível de urgência.

* ### **Scores/escalas:**

Ao habilitar a parametrização de scores e escalas, será exibido no campo de busca uma lista conforme cadastro prévio dos  que o produto já apresenta (RM > Cadastro> Cuidados com o paciente > Outros Cadastros > Gerenciamento de Risco> Cadastro de Scores) e também poderá definir o valor mínimo e máximo de alteração para cada score e escala.

Após o preenchimento, ao clicar no botão "+Adicionar" o score ou escala é exibido abaixo da seleção em uma tabela, contendo as colunas "Descrição", "Valor mínimo" e "Valor máximo". Nessa tabela, o usuário consegue alterar o valor mínimo e máximo adicionado anteriormente, basta clicar sobre o campo e digitar o novo valor.

Para remover um score ou escala clique no botão "-Remover" na respectiva linha do item.  

Para continuar o preenchimento, clique no botão "Próximo" para ser encaminhado ao próximo step de classificação e repetir o processo de preenchimento, não sendo obrigatório realizar o preenchimento de todos os "steps".

Ao chegar no último step, o botão "Finalizar" no topo da página ficará habilitado. Para finalizar o cadastro do protocolo, clique no botão "Finalizar" e o protocolo será exibido na tabela inicial com a possibilidade de edição.

### **Exemplo Prático**

Discriminador: **Febre** (Sempre deve ser considerado como Classificação mais baixa se não for definido um valor mínimo e/ou máximo)

| Sinal Vital | Emergência | Muito Urgente | Pouco Urgente | Não Urgente |
| --- | --- | --- | --- | --- |
| Temperatura | > 41º | > 39º | > 37º | < 37º |

Cadastro de Motivos

### **e. Cadastro de Motivos**

O usuário poderá cadastrar os motivos para reclassificação, repriorização ou motivo de saída do PA.

RM > Cadastro > Cuidados com o Paciente >  Outros Cadastros > Gerenciamento de riscos > Cadastro de Motivos.

Ao clicar em adicionar ou editar, o usuário poderá escolher o tipo ("Reclassificação", "Repriorização" ou "Motivo saída PA") e a descrição do motivo.

Parametrização para sinal vital obrigatório

### **f. Parametrização para sinal vital obrigatório**

Com a parametrização "Pelo menos um sinal vital obrigatório" habilitada, a classificação de risco não poderá ser finalizada até que um sinal vital seja registrado para o paciente. 

RM > Ambiente > Parâmetros > Gestão hospitalar > Classificação de risco > Classificação de risco 3/3.

Ao clicar no botão "Finalizar" antes de registrar um sinal vital, uma mensagem de alerta será exibida para o usuário:

Configurações

## **4. Configurações**

No painel de Urgência e Emergência, existe um filtro chamado **Médico responsável**, usado para visualizar atendimentos associados a um profissional específico.

Agora você pode escolher **como esse campo deve ser preenchido** ao acessar o painel:

* **Automaticamente**, com o seu nome.
* **Manual**, deixando o campo em branco para que você selecione outro médico.

Essa flexibilidade permite visualizar atendimentos de outros profissionais de forma mais rápida e prática.

1. Acesse o menu **PEP > Minhas Configurações**.
2. Procure pela opção:

**“Selecione como o campo ‘Médico responsável’ deve ser preenchido”**

1. Escolha uma das duas opções apresentadas:

Automática

* O campo “Médico responsável” é preenchido automaticamente com o médico logado no sistema.
* Ideal para quem sempre utiliza o próprio usuário como filtro.
* Mesmo com o preenchimento automático, você pode alterar manualmente se quiser.
Manual

* O campo aparece **em branco** ao acessar o painel.
* Você escolhe manualmente o médico desejado.
* Ideal para quem alterna entre diferentes médicos ou supervisores.

**Qual é o comportamento padrão?**

Se você nunca alterou essa configuração, o sistema inicia com o comportamento **Automático**, preenchendo o campo com o seu usuário.

**A configuração fica salva?**

Sim.  
Depois de ajustar sua preferência, ela será mantida para os próximos acessos, mesmo se você sair e entrar novamente no sistema.
