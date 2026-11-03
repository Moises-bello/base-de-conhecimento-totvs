---
content_hash: eb6bc6dc63c73be381ab3611d0d75e348902656ac2e0f99f5a1e07a472efae03
fetched_at: '2026-06-29T00:09:13.727680+00:00'
page_id: '421385097'
product: rm
source: tdn-rm
title: Apontamento de Mão de Obra
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385097
version: 9
---

---

**Conceito:**

O apontamento de mão de obra refere-se ao processo de monitoramento, registro e controle da presença, atividades e produtividade dos trabalhadores envolvidos no projeto.

Esse processo é essencial para manter o controle sobre as horas trabalhadas, tarefas executadas, e custos com mão de obra.

No apontamento de mão de obra, são registrados dados como:

* **Jornada de Trabalho**: Controle das horas de entrada, saída e intervalos de cada trabalhador.
* **Atividades Realizadas**: Registro das tarefas desempenhadas por cada trabalhador (ex.: escavação, concretagem, armação de ferragens).
* **Equipe e Local de Trabalho**: Identificação da equipe e setor onde o trabalho foi realizado.
* **Produtividade**: Medição do desempenho em relação às metas estabelecidas para cada atividade.
* **Custos**: Cálculo dos custos de mão de obra associados a cada atividade.

**Objetivo**:

O objetivo é permitir uma gestão eficiente, ajudando a reduzir desperdícios, aumentar a produtividade e fornecer uma base confiável para a medição de desempenho e controle de custos.

Esses dados são, geralmente, registrados diariamente e organizados em relatórios para que os gestores da obra possam tomar decisões e fazer ajustes no cronograma e orçamento.

O apontamento de Mão de obra é realizado pelo app Minha Obra veja os detalhes em :

Essa visão|tela "Apontamento de Mão de Obra"  exibe o apontamento da mão de Obra retornado pelo app sem inconsistências.

Na visão|tela Folha Tarefa, também será possível visualizar os apontamentos de mão de obra e também no menu Anexos | Apontamentos de Mão de Obra.

Será exibida uma visão com informações sobre os apontamentos feitos pelo coletor .

Ao ser importado pelo WebService, o apontamento é analisado de forma que todas as informações estejam aptas para que o Processo de "Apropriação de Mão de Obra" gere a apropriação dos apontamentos sem inconsistências. Para a validação do apontamento, dois campos são importantes: "Status" e "Motivo de Inconsistência"   
O Status pode ter quatro características:

* Pendente  = Define o apontamento como pendente de apropriação; - Apropriado  =  Representa os apontamentos já apropriados; - Inconsistente  = Define o registro como impossibilitado de ser apropriado; - Pendente de Ponto = Define registros inconsistentes em relação ao ponto do membro da equipe.  
  Ao receber os dados dos apontamentos de mão de obra, o sistema irá validar registro por registro a fim de definir o status de cada apontamento, garantindo que o mesmo esteja apto para ser apropriado.   
  Serão validados os seguintes campos:
  + Tarefa: {\*}Se a tarefa e o código de barras da mesma não vierem preenchidos e o centro de custo informado, a tarefa do apontamento será a primeira encontrada no rateio de centro de custo. Se vier preenchida, a mesma será validada em relação ao projeto do apontamento. O campo Observação receberá um log informando a inconsistência.
  + Código de Barras da Tarefa:\* Deve ser considerado em caso de o campo Tarefa não vier preenchido. Esse campo deve ser utilizado a fim de validar qual a tarefa do apontamento.
  + Centro de Custo:\* Se o Centro de Custo não vier preenchido o campo Observação receberá um log informando a inconsistência.
  + Membro da Equipe:\* A matrícula do membro será validada no momento da importação. Deve obedecer ao layout de 14 caracteres, sendo 4 para coligada e 10 para o identificador do membro. Caso não seja encontrado o respectivo membro o campo Observação receberá um log informando a inconsistência.
  + Data e Hora Inicial:\* Se a Data e Hora Inicial não vier preenchida o campo Observação receberá um log informando a inconsistência.
  + Data e Hora Final:\* Se a Data e Hora final  não vier preenchida o campo Observação receberá um log informando a inconsistência.
  + Motivo de Improdutividade:\* Se o campo Improdutivo vier definido como "verdadeiro" e o Motivo de Improdutividade não vier preenchido o campo Observação receberá um log informando a inconsistência.  
    **Importante:**
* Com exceção do campo "Horas Apontadas", todos os outros poderão ser editados, obedecendo às regras em relação ao status do apontamento; - O campo "Motivo de Improdutividade" somente poderá ser editado se o apontamento for do tipo Improdutivo; - Caso o status do apontamento estiver como apropriado, não será possível realizar qualquer modificação no apontamento; - Caso  a tarefa não seja enviada ou encontrada, será considerado o código de barras para encontrar a mesma.

* **Parametrização de campos do funcionário no coletor móvel**

A parametrização dos campos proporciona uma melhor identificação de desvio de função ou os casos de substituição de funcionário por motivo de doença, licença e etc. É possível parametrizar no sistema dois campos do funcionário que serão exibidos pelo coletor móvel no momento do apontamento de mão de obra.   
Os campos do cadastro de funcionário disponíveis para parametrização de exibição no coletor móvel são:

1. Apelido;
2. CPF;
3. Função;
4. Situação;
5. Chapa.

**Observação:** **-** O campo "Apelido" virá parametrizado por default ao utilizar a funcionalidade pela primeira vez, ou seja, em uma base de dados nova o campo apelido já virá parametrizado e o parâmetro poderá ser alterado. - Podem ser parametrizados até dois campos do funcionário ao mesmo tempo (Informação extra 1 e Informação extra 2)  
Para parametrizar a exibição os campos do funcionário no coletor móvel deve ser acessado os parâmetros gerais de mobilidade: **- *Projeto\ Construção e Projetos\ Gerais\ Mobilidade***

* **Exclusão de Apontamentos no Coletor**

Essa funcionalidade permite que o apontamento de entrada possa ser excluído no coletor, antes de realizar o sincronismo com RM. A exclusão será realizada na tela de saída do apontamento, caso haja algum apontamento de entrada.  
Passo a Passo   
 1 - Acessar o TOTVS Obras e Projetos;  2 - Selecionar o Projeto;  3 - Acessar o Menu Cadastros | Mobilidade | Folha Tarefa;  4 - Selecionar Anexo | Apontamento de Mão de Obra, para verificar as informações dos apontamentos;  5 - Sistema deve retornar a visão contendo os Apontamentos de Mão de Obra "existentes".

 Processos

---
