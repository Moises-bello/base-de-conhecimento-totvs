---
content_hash: f546a006bb30364ba0158a61183e267e90a9e7e1c2c2e7b7c672f548f3614a0b
fetched_at: '2026-06-29T00:11:53.578035+00:00'
page_id: '849549424'
product: rm
source: tdn-rm
title: Fila de Laudos
type: documentation
url: https://tdn.totvs.com/display/LRM/Fila+de+Laudos
version: 41
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Parâmetros e permissões**
   1. Parâmetros
   2. Permissões
3. **Atribuição de profissionais**
   1. Manual
   2. Automática
4. **Retirar Profissionais**
5. **Logs**
6. **Exames Recebidos**
7. **Entrega de Exames**
8. **Impressão de Laudos**
9. **Anexos**
10. **Escala de Trabalho**
    1. Visão Geral
    2. Cadastro de Escala
    3. Calendário de Visualização

Fila de LaudosFila de Laudos

## **01. VISÃO GERAL - FILA DE LAUDO****S**

Data do exame, para externos é data de agendamento  e para internos a previsão de execução

No campo de "**Filtros**" ao lado do botão de Gerenciar Tabela, temos todos os campos da tela que podem ser filtrados de acordo com a necessidade do cliente.

#### **Informação importante sobre o filtro do campo STATUS:**

Até o momento, o campo de status dentro do filtro é de única seleção (single select), ou seja, permite selecionar apenas um status por vez para filtrar os exames. Isso ocorre porque a equipe responsável pela ferramenta ainda vai corrigir o funcionamento do componente de multi seleção (multi select) para funcionar adequadamente nos filtros do RM.

Entretanto, existe uma maneira de "contornar" o problema. Para isso, usuário da fila deverá criar um filtro complexo com a consulta que ele quiser. Exemplo abaixo:

Nesse caso do campo de status, se o usuário quiser selecionar exames que estejam tanto em status Inicial quanto Em Digitação, deverá criar o filtro nesse construtor de consultas, utilizando a cláusula **OU**.

### **Regras Específicas**

* Na listagem de fila de laudos, só é exibido os laudos onde:

  + O status seja: **Inicial, Em Digitação, Digitação Concluída, Liberado, Emitido, Assinatura Pendente, Aguardando Revisão, Revisado e Reconvocado;**
  + O status da conta do atencimento do paciente não pode estar cancelado;
  + O pedido de exame não pode estar cancelado;
  + O exame deve ser um exame de imagem;
  + O exame deve possui uma modalidade definida;

Parâmetros e permissões

## **02. PARÂMETROS E PERMISSÕES**

Descreva a visão geral. 

Parametros e permissoesParâmetros

## **PARÂMETROS**

Os parâmetros referentes à fila de laudos se encontram no cadastro de "Unidade de Atendimento", mais especificamente na aba de "Exames".

**Distribuição dos laudos:**

Temos duas opções:

* Manual: o usuário irá atribuir o médico manualmente pelo botão atribuir.

* Automático: Quando houver uma escala para o dia, os médicos serão distribuídos automaticamente de acordo com o horário de atendimento, exame que o profissional lauda, faixa etária e sexo.

       Ao selecionar o parâmetro como "Manual", a opção "Automático" será desabilitada. No entanto, ao escolher "Automático", ambas as opções ficarão habilitadas, permitindo que o usuário altere para uma atribuição de sua preferência mesmo após uma atribuição automática.

**Utilizar médico do exame anterior:**

* Essa opção só é válida para exames internos e da mesma modalidade, ou seja, se o paciente realizou o exame anterior na instituição e esse exame é o mesmo do atual.
* Ao marcar o checkbox, o mesmo médico que laudou o exame anterior irá laudar o exame atual. O parâmetro funciona tanto para atribuição manual ou automática do médico. No caso da atribuição manual, há um aviso indicando que o médico anterior está sendo selecionado.

Observações:

* Durante o processo de inclusão de uma nova unidade de atendimento, o valor *default* (padrão) da distribuição de laudos será como "Automática".

* Unidades previamente cadastradas no sistema, não terão nenhuma das duas opções de distribuição marcada, porém na fila de laudos em si será considerada como "Automática".
Permissões

## **PERMISSÕES**

Para a fila de laudos e cadastro de escalas médicas, foram criadas novas permissões no menu de Perfis no RM:

**Parâmetros da Fila**

* Fila de Laudos: Permite que o usuário acesse a tela da fila de laudos e filtre.
* Atribuir médico: Permite que o usuário atribua médico aos laudos da fila.
* Retirar atribuição: Permite que o usuário retire a atribuição de um laudo da fila.
* Impressão de laudo: Permite que o usuário imprima um laudo da fila.

**Parâmetros da Escala:**

* Escala de Trabalho - Visualização da escala de trabalho no processo.
* Inclusão de escala - Permite que o usuário inclua uma escala médica.
* Edição de escala - Permite que o usuário altere os dados da escala.
* Inativar a escala - Permite que o usuário inative uma escala, sendo que este médico neste período da escala não estará mais disponível.

* Visualizar tela de log: Permite que o usuário visualize e tenha acesso à tela de log, tanto das escalas médicas quanto da fila de laudos.

**OBS.:** Se o parâmetro "Fila de Laudos" não estiver marcado, não será possível acessar a tela de Fila de Laudos, mesmo que os outros estejam marcados.

Atribuição de profissionais

## **03.** **ATRIBUIÇÃO DE PROFISSIONAIS**

Descreva a visão geral. 

Opções de AtribuiçãoManual

## **MANUAL**

**Para atribuir o profissional ao laudo, basta seguir os passos abaixo:**

1) Selecione um ou mais laudos que deseja atribuir o profissional;

2) Click no botão "Opções";

3) Será aberto o menu com a opções, click em "Atribuir Responsável".

**Será aberto a janela de atribuir laudo mostrando os laudos selecionados:**

1) Na listagem de laudos exibida, voce poderá ainda marcar ou desmarcar os laudos que deseja ou não deseja atribuir neste momento;

2) Abaixo da listagem de laudos, voce irá selecionar o responsável que deseja atribuir aos laudos selecionados;

3) Após informado o responsável, click no botão "Confirmar" para atribuir o responsável.

**Informações:**

* + Se o usuário selecionar laudos sem responsável atribuido e laudos com responsável, ao abrir a tela de atribuir laudo, o sistema irá notificar o usuário mostrando os laudos que já possuem responsável atribuido, e esses laudos não serão exibidos na listagem;
  + Se o usuário selecionar laudos onde o status seja diferente de **Inicial ou Em Digitação**, ao abrir a tela de atribuir laudo, o sistema irá notificar o usuário mostrando os laudos que estão com status diferente, e esses laudos não serão exibidos na listagem;
  + Ao abrir a seleção de responsável, o sistema irá buscar os profissionais se baseando no prazo dos laudos selecionados e a escala do profissional, se o sistema encontrar profissional com escala que correspoda com o prazo dos laudos, ele irá listar apenas esses profissionais. Se o sistema não encontrar profissional onde sua escala corresponda ao prazo dos laudos ele irá trazer todos os profissionais ativos;
  + Se o usuário desejar alterar o profissional atribuido em um ou mais laudos, é necessário que seja feira a retirada da atribuição e feita uma nova atribuição. Isso é necessário pois a cada ação feita é registrado sua modificação no log;
  + Só será possivel atribuir o proficional se o status do laudo do exame estiver como: **Inicial ou Em Digitação**;

Descreva a visão geral. 

Automática

## **AUTOMÁTICA**

A atribuição automática é realizada ao pressionar o botão "Distribuição Automática" situado no topo direito da tela da Fila de Laudos. Apenas os exames em que a unidade de execução/atendimento tenha sido parametrizada para realizar a distribuição automática (veja em **02. PARÂMETROS E PERMISSÕES**) serão considerados por esta ação.

A ação faz com que o sistema avalie os exames com data para o **dia atual** e que estejam com status **Inicial** ou **Em Digitação** e atribua automaticamente um profissional com escala de trabalho vigente aos exames sem responsável.  São respeitadas as condições da **Escala de Trabalho** de cada profissional. As informações do exame, período e horário de vigência, unidade de execução/atendimento, código do exame, sexo do paciente, idade e prioridade são utilizadas para determinar se a escala de trabalho do profissional atende ao exame.

Se o parâmetro do médico anterior (veja em **02. PARÂMETROS E PERMISSÕES**) estiver ativo para a unidade será atribuído o médico que fez o laudo do último exame, desde que o mesmo tenha uma escala vigente.

O objetivo é que ao final do dia de trabalho deveremos ter a divisão de exames o mais igualitária possível entre os médicos que possuam escala de trabalho cadastrada. Caso já exista um médico responsável no exame, o mesmo será mantido e considerado no calculo para garantir uma distribuição igualitária.

Retirar profissionais

## **04. RETIRAR PROFISSIONAIS**

**Para retirar a atribuição de um profissional, basta seguir os passos abaixo:**

1) Selecione um ou mais laudos que deseja retirar a atribuição do profissional;

2) Click no botão "Opções";

3) Será aberto o menu com a opções, click em "Retirar Atribuição".

**Após a abertura da janela de confirmação, basta clicar em Confirmar:**

**Informações:**

* + Se o usuário selecionar laudos com responsável atribuido e laudos sem responsável. Ao abrir a tela para confirmação, o sistema irá notificar o usuário mostrando os laudos que não possuem responsável atribuido, e esses laudos serão desconsiderado pois não possuem responsável;
  + Só será possivel remover a atribuição se o status do laudo do exame estiver como: **Inicial ou Em Digitação**;

Logs

## **05. LOGS**

É possível visualizar o histórico de alteração dos registros da escala médica e da fila de laudos por meio do log.

**Log na fila de laudos:**

A tabela exibida com os registros é filtrada para aparecer somente as alterações referentes à distribuição de laudos. Toda vez que um médico é atribuído ou retirado (manualmente ou automaticamente), um novo registro na tabela será criado, com os seguintes dados:

* + **Rotina:** Fila de Laudo;
  + **Tipo de ação**: Atribuir/Retirar;
  + **Descrição**: Modo de atribuição (manual ou automático), se houver - Medico responsável (que foi incluído ou retirado);

**Log na escala médica:**

A tabela exibida com os registros é filtrada para aparecer somente as alterações referentes às escalas médicas. Qualquer alteração nas escalas de um médico, seja inclusão, edição ou exclusão, gera um novo registro na tabela, com os seguintes dados:

* + **Rotina:** Escala Médica;
  + **Tipo de ação**: Incluir/Editar/Excluir;
  + **Descrição**: nula;

Exames recebidos

## **05. EXAMES RECEBIDOS**

A funcionalidade de exames recebidos serve para cadastrar e visualizar exames que o paciente realizou anteriormente.

Esses exames são físicos, ou seja, o seu **resultado** não é cadastrado no nosso sistema. Entretanto, são recebidos pelo médico e são identificados através dessa funcionalidade.

Os exames recebidos funcionam por ordem de serviço. Isso é, se eu selecionar um exame X e cadastrar um exame recebido para ele, todos os outros exames do mesmo pedido também terão o mesmo exame recebido cadastrado.

Para cadastrar um exame recebido, é necessário selecionar **UM** exame no grid da Fila de Laudos e abrir o menu "Opções", podendo visualizar assim o botão de "Exames recebidos":

  =>

É **necessário** que o exame esteja no status **"Inicial" ou "Em Digitação"** para que o usuário consiga inserir um exame recebido. Caso contrário, a seguinte mensagem será exibida:

Na tela de exames recebidos, é **necessário**que os dois campos marcados como obrigatório sejam preenchidos, e são eles: **Exame recebido e Data do Exame**. Caso não preencha, a seguinte mensagem será exibida:

O campos "Observações" é um campo de texto livre opcional, para adicionar qualquer informação adicional caso seja necessário.

Na tela, o usuário poderá adicionar quantos exames quiser, assim como removê-los caso deseje, na hora da inserção.

Para **adicionar** mais exames, basta clicar no botão "Adicionar mais exames" e os três novos campos irão surgir para o preenchimento.

Para **remover** um exame, basta clicar no ícone de lixeira no canto superior direito dos campos. Obs.: Caso o usuário só tenha somente três campos (um exame) na tela, esse ícone será desabilitado.

Ao clicar em "Adicionar mais exames":

* O botão "Cancelar" tem a mesma funcionalidade do botão de "X" no canto superior direito, que é fechar o modal e limpar todos os exames preenchidos.
* O botão "Confirmar" confirma a ação e salva o exame recebido para todos os exames daquela ordem de serviço do exame selecionado.
* Ao salvar, será gerado um registro na tabela de log: SZLOGUNIDADEDIAGNOSTICO.

Quando uma ordem de serviço possuir exames recebidos cadastrados, a coluna 'Exames Recebidos' na Fila de Laudos, ficará marcada com um *check* verde. Caso contrário, marcado com um *x*vermelho.

Entrega de Exames

## **06. ENTREGA DE EXAMES**

# **Definição:**

A funcionalidade "Entregar Exames" tem como objetivo **entregar o laudo do exame selecionado ao paciente, realizando juntamente a devolução dos exames recebidos** (se houver).

Assim que a ação for executada, o status do exame será atualizado para **"Entregue"** e o laudo não aparecerá mais na Fila de Laudos, sendo exibido apenas no RM.

Inicialmente, a ação está localizada no **menu de Opções** da Fila de Laudos e será single-select no grid. Isso é, para que o processo apareça no menu, **deve ser selecionado apenas um exame.**

O exame selecionado deve estar com o status **"Liberado" ou "Emitido"**. Caso contrário, a seguinte mensagem será exibida:

Selecionando o exame em um desses dois status (Liberado ou Emitido), ao clicar na opção de "Entregar Exames" abrirá o modal de entrega do laudo:

                   

# **Informações dos campos:**

## Nome e CPF do responsável pela retirada:

* + Os campos de Nome e CPF do responsável virão preenchidos automaticamente conforme os dados do próprio paciente do exame selecionado. Caso o responsável pela retirada seja outra pessoa, basta selecionar a opção "Outra Pessoa" e preencher os dados;
  + O **preenchimento de ambos** os campos é **obrigatório**.

## Data e Hora:

* + A data e hora virão preenchidos conforme a data e hora atuais, mas podendo ser alterados para até 24h antes da data atual (ou seja, se estou confirmando a entrega dia 05/09 às 14:30, é possível registrá-la para até dia 04/09 às 14:30). Não é permitido preencher a data com uma data futura;
  + O **preenchimento de ambos** os campos é **obrigatório**;

# Exames recebidos inseridos:

* + O campo de "Exames recebidos inseridos" traz todos os exames recebidos previamente cadastrados para aquela ordem de serviço no qual o exame selecionado no grid está inserido;
  + Caso não haja nenhum exame recebido naquela ordem de serviço, o campo de *"Exames recebidos inseridos"* e a flag do termo de declaração *"Declaro que foi entregue..."* irão ficar **desabilitados**;
  + **Caso haja pelo menos 1 (um) exame recebido** preenchido no multi-select, **a seleção da flag** do termo de declaração *"Declaro que foi entregue..."***será** **obrigatória**;

### Após o preenchimento dos campos obrigatórios e confirmação da entrega do laudo, se o processo for executado com sucesso, o exame terá seu status atualizado para **"Entregue"** e não aparecerá na Fila de Laudos, apenas na tela de laudos de imagem do RM.

Impressão de Laudo

## **07. IMPRESSÃO DE LAUDO**

Para imprimir um laudo, é necessário selecionar o laudo no grid da Fila de Laudos e abrir o menu "Opções", e clicar no botão de "Impressão de Laudo":

**Informações:**

* Laudos com status inicial não possui impressão, será exibido uma mensagem de erro ao usuário;
* Laudos com status em digitação, digitação concluída ou assinatura pendente, será exibido uma mensagem de alerta informando que o laudo não esta liberado e será impressão com o termo "RASCUNHO";
* Laudos com status liberado ou entregue terão sua impressão normal;

Anexos

## **08. ANEXOS**

1. Para acessar os anexos, selecione um item da tabela "Fila de Laudos" e, em seguida, escolha a opção "Anexos" no menu.
2. A próxima tela exibirá todos os anexos vinculados ao laudo que você escolheu anteriormente.
3. Para adicionar um novo arquivo, clique no botão **“+ Incluir”** no canto superior direito da tela. Você será direcionado para uma nova tela com todos os campos necessários para inserir o anexo.
   1. Ao clicar em Incluir, você verá uma tela onde deve preencher todos os campos obrigatórios. Para adicionar um arquivo, clique em Selecionar arquivo e, em seguida, clique em Enviar para concluir.
Escala de trabalho

## **09. Escala de trabalho**

Descreva a visão geral. 

EscalasVisão Geral

## **VISÃO GERAL**

A tela de Escala de Trabalho apresenta uma tabela com todas as escalas cadastradas. As escalas de trabalho são períodos definidos para um ou mais profissionais, onde está indicado quais exames poderão ser atribuídos para o responsável técnico fazer o laudo.

É possível filtrar as escalas através do botão e gerenciar a ordem das colunas da tabela no botão . Na barra de busca é possível buscar entre os itens carregados na tabela por palavras ou números.

Ao selecionar uma das escalas o menu de ações é apresentado, onde o usuário pode excluir ou editar as escalas já cadastradas.

Cadastro de Escala

## **CADASTRO DE ESCALA**

Ao clicar no botão Incluir no topo superior direito da tela de **Escala de Trabalho** abrirá a tela para cadastrar uma nova escala.

**Descrição (Obrigatório):** Descrição breve que represente a Escala de trabalho. Exemplo: Plantão noturno de Raio X

**Unidade de Atendimento (Obrigatório):** Define uma unidade dentre as configuradas como Central de Exames e/ou Diagnóstico por Imagem para ser atendida pela Escala.

**Nome do Profissional (Obrigatório):**Pode selecionar um ou mais profissionais, serão exibidos na busca os prestadores cadastrados como responsáveis técnicos na Cadastros > Unidade Diagnostica > Responsáveis Técnicos.

**Dias da Semana (Obrigatório):**Exibe os dias da semana de domingo a sábado para o usuário selecionar um ou mais dias.

**Horário início (Obrigatório):**Define o horário inicial do período da escala de trabalho.

**Horário final (Obrigatório):** Define o horário final do período da escala de trabalho.

**Modalidade:** Exibe as modalidades de acordo com a DICOM e poderá ser selecionado uma ou mais modalidades. Caso tenha selecionado modalidade(s), está será utilizada para filtrar o lookup de exames, que mostrará apenas exames cadastrados com uma das modalidades selecionadas.

**Exames (Obrigatório):** Seleção de exames que serão atendidos pela escala e poderá ser selecionado uma ou mais exames.

**Restrição de faixa etária:** Poderá ser selecionada uma ou mais faixas etárias cadastradas para restringir o atendimento.

**Sexo (Obrigatório):**Define o sexo dos pacientes que serão atendido pelos médicos da escala. Feminino , masculino ou ambos.

**Data início (Obrigatório):**Define a data inicial do período da escala de trabalho.

**Data final (Obrigatório):** Define a data final do período da escala de trabalho.

**Prioridade (Obrigatório):** Indica quais prioridades de exame que serão atendidas pela escala (Emergência, Urgência e/ou Normal).

Calendário de Visualização

## **CALENDÁRIO DE VISUALIZAÇÃO**

Ao clicar no botão "Calendário" no topo superior direito da tela de **Escala de Trabalho** abrirá a tela para visualização das escalas para a semana que estamos.

**Visão Geral**  
A tela de Escala de Trabalho exibe a programação semanal dos profissionais de saúde em um formato de calendário. Esta tela permite visualizar a agenda de trabalho de diversos médicos ao longo de uma semana, organizada por unidade e exame, facilitando a gestão e consulta dos horários de trabalho.  
  
**Funcionalidades**

1. **Calendário Semanal:**
   1. A tela apresenta uma visão semanal, mostrando a programação de segunda a domingo.
   2. Cada dia é exibido em uma coluna separada, permitindo uma visão clara das atividades diárias.
2. **Filtros de Unidade**:

   1. Inclui filtros para selecionar a unidade de atendimento.
   2. Ao aplicar o filtro, a tela é atualizada para exibir apenas a escala da unidade selecionada.
3. **Detalhes da Escala**:

   1. Cada item dentro do calendário exibe o nome do profissional e o horário de início e fim da sua escala.
   2. Os horários são apresentados no formato de 24 horas
