---
content_hash: 4fff2ec36c4e87419a11324feb2ab44b749f8b56901727ea47f329e12fd247f8
fetched_at: '2026-06-29T00:09:36.307719+00:00'
page_id: '425459495'
product: rm
source: tdn-rm
title: Chamada de candidato aprovado
type: documentation
url: https://tdn.totvs.com/display/LRM/Chamada+de+candidato+aprovado
version: 7
---

Após realizar a classificação de todas as áreas ofertadas do processo seletivo, o próximo passo é fazer a chamada das respectivas áreas.  Uma chamada consiste em convocar um número de candidatos, que estejam classificados, igual ao que foi ofertado para uma área. Após chamar estes candidatos para uma área, os mesmos deverão comparecer à instituição de ensino para efetivarem a matrícula. Para maiores detalhes acesse:  .

Durante a execução deste processo, cada área será minuciosamente analisada considerando dois fatores principais: o número de **vagas livres disponíveis para chamadas** e o **número atual de candidatos em cada chamada**. Esta análise é crucial, pois permite realizar múltiplas chamadas, assegurando que para cada nova chamada seja calculado precisamente o número de vagas restantes. O processo é iterativo, realizando tantas chamadas quanto necessário para preencher todas as **vagas disponíveis**.

Além disso, o sistema gerará um log detalhado, listando todas as áreas já classificadas e indicando o número de candidatos que ainda podem ser convocados, proporcionando uma visão clara e organizada do andamento do preenchimento de vagas.

Importante Lembrar

Somente as áreas de interesse que possuem **vagas disponíveis** para chamada de candidatos, serão exibidas na listagem para a execução do processo de chamada de candidato aprovado.

**Importante**:    
Somente candidatos que foram classificados em suas respectivas áreas estarão aptos a receberem chamadas. Após a execução do processo será exibido um Log com o resultado do processamento.   
   
No Log o processo informará os seguintes dados:  
   
- Número de vagas livres antes da chamada: calcula o número de vagas que ainda existem disponíveis antes de realizar a chamada.  
   
- Número de convocados para a chamada: calcula o número de candidatos classificados que foram convocados para a chamada.   
- Número de vagas livres após a chamada: calcula o número de vagas que ainda restam mesmo após a realização da chamada. Isso pode acontecer quando o número de candidatos classificados for menor que o número de vagas ofertadas pela área.  
   
Serão exibidos os nomes em ordem alfabética dos candidatos que foram convocados para a chamada.

No grid será possível selecionar uma ou mais áreas ofertadas para execução da chamada.

Se na área ofertada não existir candidato classificado a ser chamado, o sistema irá mostrar uma mensagem e não deixará selecioná-la.  
   
As regras a seguir são consideradas ao executar uma chamada:  
   
**Caso 1:**  
O candidato está com o status *"Compareceu à Chamada"* na sua 1ª opção:   
- Ele não será chamado para nenhuma outra opção.  
**Caso 2:**  
O candidato está com o status *"Compareceu à Chamada"* em sua 2ª opção:   
- Ele, somente, será chamado em uma opção de maior prioridade para ele.   
- O seu status na área em que foi chamado anteriormente passará para *"Convocado para outra opção"*  
**Caso 3**:  
O candidato não compareceu a chamada em uma opção, ou seja, está com o status *"Não compareceu à chamada"*:   
- Ele não poderá ser chamado para a atual opção que está chamando, mas poderá ser chamado para outra opção.   
**Caso 4**:   
O candidato está com o status *"Classificação pendente"* na área que está sofrendo chamada:   
- Ele não terá o status alterado, mas irá reter a vaga se estiver na zona de chamada. Ou seja, nenhum excedente será chamado para a vaga desse candidato.

Candidatos com mais de uma opção

Caso a área ofertada permita mais de uma opção e o candidato possua nota mínima de classificação, ao realizar a chamada, o mesmo será chamado em todas as áreas ofertadas na sua inscrição conforme a disponibilidade de vagas de cada área, ou seja, estará apto a ser matriculado em uma das áreas ou até mesmo em todas que ele selecionou na sua inscrição, caso o candidato possa de inscrever em mais de uma área porém só poderá ser chamado em uma única área ofertada, deve ser marcado o parâmetro geral "Utilizar o controle de chamada de uma única área ofertada por candidato, respeitando a ordem de prioridade", assim o sistema irá considerar a disponibilidade de vagas de cada área, sua classificação e a ordem de prioridade das vagas para realizar a chamada.

Para mais informações sobre o parâmetro acesse  .

   
**Novo**: **Chamada de candidatos utilizando cotas federais** Respeitando a Lei de Cotas (Lei nº 12.711/2012), a chamada será realizada reservando-se vagas, de acordo com as informações configuradas, para os grupos de cotas definidos, da forma descrita abaixo: Informações necessárias  
**Informações do formulário de cotas para instituições federais, no anexo da visão de processos seletivos:**  
**I1** - *"Utiliza de cota no processo seletivo?"* O Sistema somente trabalhará com cotas se o **I1** estiver ativo, ou seja com valor "**T**".  
**I2** - *"Número de vagas total da área ofertada"*.   
**I3** - *"Percentual de vagas destinadas a egressos de ensino público"*.  
**I4** - *"Percentual de vagas destinadas a candidatos de baixa renda"*.  
**I5** - *"Percentual de vagas destinadas a candidatos autodeclarados pretos, pardos ou índios"*.  
**I6** - *"Percentual de vagas destinadas a candidatos autodeclarados pretos, pardos ou índios com deficiência"*.  
   
**Outras informações:**  
**I7** - *"Grupo de cotas que o candidato está inscrito"*.  
**I8** - *"Classificação do candidato dentro do grupo de cota"*.  
**I9** - *"Classificação do candidato na área ofertada"*.  
   
Grupos de cotas:  
**Grupo 1**: Egressos de escola pública, com baixa renda familiar, que se autodeclaram pretos, pardos ou indígenas.  
**Grupo 2**: Egressos de escola pública, com baixa renda familiar, que NÃO se autodeclaram pretos, pardos ou indígenas.  
**Grupo 3**: Egressos de escola pública, que se auto declaram pretos, pardos ou indígenas.  
**Grupo 4**: Egressos de escola pública, que NÃO se auto declaram pretos, pardos ou indígenas.  
**Grupo 5**: (Ampla concorrência): candidatos que não participam do programa de cotas.  
**Grupo 6**: Egressos de escola pública, com baixa renda familiar, que se autodeclaram pretos, pardos ou indígenas, com deficiência.  
**Grupo 7**: Egressos de escola pública, com baixa renda familiar, que NÃO se autodeclaram pretos, pardos ou indígenas, com deficiência.  
**Grupo 8**: Egressos de escola pública, que se auto declaram pretos, pardos ou indígenas, com deficiência.  
**Grupo 9**: Egressos de escola pública, que NÃO se auto declaram pretos, pardos ou indígenas, com deficiência.   
   
Quantidade de vagas por grupo de cota:

* **V1** -"Vagas destinadas a alunos de escola pública": calcula-se através do percentual **I3** de **I2** (total de vagas).
* **V2** - "Vagas destinadas a alunos de baixa renda": calcula-se através do percentual **I4** de **V1**.
* **V3** - "Vagas destinadas a candidatos de renda superior a 1,5 salário per capita": calcula-se através do restante **V1** - **V2**.
* **V4** - "Vagas destinadas a candidatos de baixa renda, que se auto declaram pretos, pardos e indígenas": calcula-se através do percentual **I5** de **V2**.
* **V5** - "Vagas destinadas a candidatos de baixa renda, que **NÃO** se auto declaram pretos, pardos e indígenas": calcula-se através do restante **V2 - V4**.
* **V6** - "Vagas destinadas a candidatos de renda superior a 1,5 salário per capita, que se auto declaram pretos, pardos e indígenas": calcula-se através do percentual **I5** de **V3**.
* **V7** - "Vagas destinadas a candidatos de renda superior a 1,5 salário per capita, que **NÃO** se auto declaram pretos, pardos e indígenas": calcula-se através do restante **V3** - **V6**.
* **V8** - "Vagas destinadas ao grupo **1**": calcula-se através do restante **V4** – **V12**.
* **V9** - "Vagas destinadas ao grupo **2**": calcula-se através do restante **V5 - V13**.
* **V10** - "Vagas destinadas ao grupo **3**": calcula-se através do restante **V6 - V14**.
* **V11** - "Vagas destinadas ao grupo **4**": calcula-se através do restante **V7 - V15**.
* **V12** - "Vagas destinadas ao grupo **6**": calcula-se através do percentual **I6** de **V4** .
* **V13** - "Vagas destinadas ao grupo **7**": calcula-se através do percentual **I6** de **V5** .
* **V14** - "Vagas destinadas ao grupo **8**": calcula-se através do percentual **I6** de **V6** .
* **V15** - "Vagas destinadas ao grupo **9**": calcula-se através do percentual **I6** de **V7** .
* **V16** - "Vagas destinadas a ampla concorrência": O valor restante de **I2 - V1** será destinado a ampla concorrência - grupo **5**.

**– Os valores resultantes do cálculo percentual de vagas para candidatos com deficiência, quando possuem casas decimais, são arredondados para o menor valor inteiro.**  
   
Ajustes nas vagas por grupo de cota: Poderão haver ajustes, a fim de completar a quantidade de vagas ofertadas pela área de interesse (**I2**), caso não haja um número de candidatos classificados suficientes para completar as vagas aos quais se enquadram. Os mesmos seguirão as regras a seguir:

* Havendo mais vagas destinadas ao grupo **1** do que candidatos classificados:
  + As vagas excedentes serão disponibilizadas para o grupo **2**.
  + Não sendo preenchidas pelo grupo **2**, serão disponibilizadas para o grupo **3**.
  + Não sendo preenchidas pelo grupo **3**, serão disponibilizadas para o grupo **4**.
  + Não sendo preenchidas pelo grupo **4**, serão disponibilizadas para o grupo **6**.
  + Não sendo preenchidas pelo grupo **6**, serão disponibilizadas para o grupo **7**.
  + Não sendo preenchidas pelo grupo **7**, serão disponibilizadas para o grupo **8**.
  + Não sendo preenchidas pelo grupo **8**, serão disponibilizadas para o grupo **9**.
  + Ainda assim, não sendo preenchidas, serão disponibilizadas para ampla concorrência.

* Havendo mais vagas destinadas ao grupo **2** do que candidatos classificados:
  + As vagas excedentes serão disponibilizadas para o grupo **1**.
  + Não sendo preenchidas pelo grupo **1**, serão disponibilizadas para o grupo **3**.
  + Não sendo preenchidas pelo grupo **3**, serão disponibilizadas para o grupo **4**.
  + Não sendo preenchidas pelo grupo **4**, serão disponibilizadas para o grupo **6**.
  + Não sendo preenchidas pelo grupo **6**, serão disponibilizadas para o grupo **7**.
  + Não sendo preenchidas pelo grupo **7**, serão disponibilizadas para o grupo **8**.
  + Não sendo preenchidas pelo grupo **8**, serão disponibilizadas para o grupo **9**.
  + Ainda assim, não sendo preenchidas, serão disponibilizadas para ampla concorrência.

* Havendo mais vagas destinadas ao grupo **3** do que candidatos classificados:
  + As vagas excedentes serão disponibilizadas para o grupo **4**.
  + Não sendo preenchidas pelo grupo **4**, serão disponibilizadas para o grupo **1**.
  + Não sendo preenchidas pelo grupo **1**, serão disponibilizadas para o grupo **2**.
  + Não sendo preenchidas pelo grupo **2**, serão disponibilizadas para o grupo **6**.
  + Não sendo preenchidas pelo grupo **6**, serão disponibilizadas para o grupo **7**.
  + Não sendo preenchidas pelo grupo **7**, serão disponibilizadas para o grupo **8**.
  + Não sendo preenchidas pelo grupo **8**, serão disponibilizadas para o grupo **9**.
  + Ainda assim, não sendo preenchidas, serão disponibilizadas para ampla concorrência.

* Havendo mais vagas destinadas ao grupo **4** do que candidatos classificados:
  + As vagas excedentes serão disponibilizadas para o grupo **3**.
  + Não sendo preenchidas pelo grupo **3**, serão disponibilizadas para o grupo **1**.
  + Não sendo preenchidas pelo grupo **1**, serão disponibilizadas para o grupo **2**.
  + Não sendo preenchidas pelo grupo **2**, serão disponibilizadas para o grupo **6**.
  + Não sendo preenchidas pelo grupo **6**, serão disponibilizadas para o grupo **7**.
  + Não sendo preenchidas pelo grupo **7**, serão disponibilizadas para o grupo **8**.
  + Não sendo preenchidas pelo grupo **8**, serão disponibilizadas para o grupo **9**.
  + Ainda assim, não sendo preenchidas, serão disponibilizadas para ampla concorrência.

* Havendo mais vagas destinadas ao grupo **6** do que candidatos classificados:
  + As vagas excedentes serão disponibilizadas para o grupo **1**.
  + Não sendo preenchidas pelo grupo **1**, serão disponibilizadas para o grupo **2**.
  + Não sendo preenchidas pelo grupo **2**, serão disponibilizadas para o grupo **3**.
  + Não sendo preenchidas pelo grupo **3**, serão disponibilizadas para o grupo **4**.
  + Não sendo preenchidas pelo grupo **4**, serão disponibilizadas para o grupo **7**.
  + Não sendo preenchidas pelo grupo **7**, serão disponibilizadas para o grupo **8**.
  + Não sendo preenchidas pelo grupo **8**, serão disponibilizadas para o grupo **9**.
  + Ainda assim, não sendo preenchidas, serão disponibilizadas para ampla concorrência.

* Havendo mais vagas destinadas ao grupo **7** do que candidatos classificados:
  + As vagas excedentes serão disponibilizadas para o grupo **6**.
  + Não sendo preenchidas pelo grupo **6**, serão disponibilizadas para o grupo **1**.
  + Não sendo preenchidas pelo grupo **1**, serão disponibilizadas para o grupo **2**.
  + Não sendo preenchidas pelo grupo **2**, serão disponibilizadas para o grupo **3**.
  + Não sendo preenchidas pelo grupo **3**, serão disponibilizadas para o grupo **4**.
  + Não sendo preenchidas pelo grupo **4**, serão disponibilizadas para o grupo **8**.
  + Não sendo preenchidas pelo grupo **8**, serão disponibilizadas para o grupo **9**.
  + Ainda assim, não sendo preenchidas, serão disponibilizadas para ampla concorrência.

* Havendo mais vagas destinadas ao grupo **8** do que candidatos classificados:
  + As vagas excedentes serão disponibilizadas para o grupo **1**.
  + Não sendo preenchidas pelo grupo **1**, serão disponibilizadas para o grupo **2**.
  + Não sendo preenchidas pelo grupo **2**, serão disponibilizadas para o grupo **3**.
  + Não sendo preenchidas pelo grupo **3**, serão disponibilizadas para o grupo **4**.
  + Não sendo preenchidas pelo grupo **4**, serão disponibilizadas para o grupo **7**.
  + Não sendo preenchidas pelo grupo **7**, serão disponibilizadas para o grupo **9**.
  + Ainda assim, não sendo preenchidas, serão disponibilizadas para ampla concorrência.

* Havendo mais vagas destinadas ao grupo **9** do que candidatos classificados:
  + As vagas excedentes serão disponibilizadas para o grupo **1**.
  + Não sendo preenchidas pelo grupo **1**, serão disponibilizadas para o grupo **2**.
  + Não sendo preenchidas pelo grupo **2**, serão disponibilizadas para o grupo **3**.
  + Não sendo preenchidas pelo grupo **3**, serão disponibilizadas para o grupo **4**.
  + Não sendo preenchidas pelo grupo **4**, serão disponibilizadas para o grupo **7**.
  + Não sendo preenchidas pelo grupo **7**, serão disponibilizadas para o grupo **8**.
  + Ainda assim, não sendo preenchidas, serão disponibilizadas para ampla concorrência.

Aos candidatos que ainda assim não forem chamados dentro do regime de cotas, continuarão competindo as vagas de ampla concorrência, considerando-se a pontuação obtida.   
Chamada de candidatos aprovados em programa de cotas

1. Primeiramente, o sistema preencherá as vagas de cotista, conforme definido acima, de acordo com a classificação dos candidatos dentro das cotas (**consultando I7 e I8**).
2. Em um segundo momento, preencherá as vagas de ampla concorrência com os candidatos classificados que ainda não foram chamados, respeitando-se a ordem proveniente da pontuação de cada um (**consultando I9**).

O processo deverá gravar em qual grupo de cotas cada candidato foi chamado no campo***SPSOPCAOINSCRITO.TIPOCOTACHAMADO***. Chamadas posteriores Para as chamadas posteriores, a mesma regra vale. Serão preenchidas primeiramente as vagas remanescentes de cotas, respeitando-se os ajustes nas vagas por grupo de cotas (**consultando I7 e I8**) e posterirormente preenchendo às vagas de ampla concorrência (**consultando I9**).

O processo deverá gravar em qual grupo de cotas cada candidato foi chamado no campo***SPSOPCAOINSCRITO.TIPOCOTACHAMADO***. Log de execução No log, a lista de nomes em ordem alfabética dos candidatos convocados na chamada terá alguns ajustes:

* Será exibida uma legenda descritiva contendo os grupos de cota.
* Serão exibidos após os nomes, em parêntese, qual grupo de cota o candidato está sendo chamado.

   
 **Pré-requisitos do processo**

Ter executado o processo Classificar Candidatos para todas as áreas ofertadas do processo seletivo.
