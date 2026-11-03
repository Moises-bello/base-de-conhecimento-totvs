---
content_hash: 0cb6e8741c9b585be37b2942775b65eec23ce64203a4af234517e9884c53aee0
fetched_at: '2026-06-29T00:09:16.819663+00:00'
page_id: '421385566'
product: rm
source: tdn-rm
title: Rateio e Revaloração de Mão de Obra
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385566
version: 66
---

---

## Objetivo:

* Realizar o rateio da diferença de horas entre o total de apontamentos originados do coletor e o total de horas registradas na folha de ponto do funcionário no período;
* Realizar a revaloração das apropriações de acordo com o custo do funcionário e horas trabalhadas no período.

## Pré-condições:

* O projeto não pode ser um projeto global;
* O projeto deve estar parametrizado com integração no módulo Folha de Pagamento;

* O envelope de pagamento deve estar fechado para o período informado no processo;
* Para que os eventos e encargos do funcionário incidam no envelope como custo, eles devem estar com a opção "Incidir no custo do funcionário" marcados;

* Os encargos que forem incidir no pagamento da folha do funcionário devem estar com a opção "Incide no custo do funcionário" marcado;

**Atenção:** A configuração dos campos e parâmetros descritos nas pré-condições acima deve ser realizada em todas as coligadas e projetos nos quais são realizados apontamentos de mão-de-obra.

Para mais detalhes como lançar eventos e encargos no folha: Lançar [Eventos para folha](https://tdn.totvs.com/pages/viewpage.action?pageId=452719144) e [Encargos para Folha](https://tdn.totvs.com/display/LRM/Encargos+-+Folha+de+Pagamento)

## O Processo:

* O objetivo do processo é atualizar o preço de todas as apropriações geradas no período a partir do custo do funcionário. O processo consiste em realizar o rateio das horas calculadas que é a diferença entre as horas registradas na folha de ponto e as horas apropriadas para o funcionário. Após ser informado o mês/ano e avançar, o sistema realizará a simulação do rateio.

* Valida o mês e ano informado. Não poderá ser igual ou superior a mês e ano corrente. O período de processamento deve ser compatível com o período da folha de ponto;
* Serão processados todos os membros ativos que compõem a(s) equipe(s) do projeto e demais funcionários que não fazem parte da equipe, porém, possuem apropriações no período. Além disso, serão processados os terceiros que são funcionários em outra coligada e demais terceiros que não fazem parte da equipe, porém, possuem apropriações no período. Também será realizado o rateio de improdutividade para membros inativos mas que possuem apontamento de mão de obra no período. Não existe revaloração ou rateio de horas improdutivas para membro que se encontra inativo e que não possui apontamento no período;
* Quando não houver apropriações, as horas da folha de pagamento serão apropriadas na totalidade como produtivas. A apropriação da totalidade de horas da folha de ponto como produtivas, visa apropriar as horas dos funcionários que compõem as equipes administrativas e financeiras.
* Antes de realizar a inclusão das apropriações e a atualização do preço unitário com o valor do ticket médio, deverão ser excluídas todas as apropriações realizadas por este processo. Desta forma fica permitida a execução por mais de uma vez. Estas atualizações de apropriações são consideradas no projeto após o recálculo.
* Caso não existam horas a ratear, o sistema exibirá uma mensagem ao usuário informando que não existem horas para serem rateadas e orientar ao usuário que poderá mesmo assim realizar a revaloração. Com as informações do rateio simuladas, o usuário poderá avaliar o resultado e optar por executar ou não o processo.
* O Rateio para terceiros somente será considerado se o parâmetro da tela do processo, "Gerar Improdutividade de Terceiros" estiver marcado.

* As horas apropriadas serão obtidas na tabela de apropriações considerando, para cada membro, a soma da quantidade de apropriações realizadas dentro do período independente de coligada pois representa o que o funcionário/terceiro apontou via coletor. Serão considerados todos os projetos, ou seja, não haverá filtro, sendo que o contexto para os cálculos deste processo é o funcionário/terceiro.
* As horas registradas na folha de pagamento serão obtidas através de integração com o sistema de Gestão do Ponto, onde estará informada a quantidade de horas registradas no ponto no período.
* Após obter a diferença entre as horas do ponto e as horas apropriadas, será realizada a apropriação, somente se esta diferença for positiva. Nos casos em que o funcionário possuir apropriações para vários projetos no período, o sistema refará o cálculo das horas a apropriar, proporcional as horas apropriadas no projeto que está sendo processado. Após o cálculo deverá ser gerada a apropriação conforme descrito abaixo;
* A data de apropriação será a do último dia do período;
* O TOTVS Construção Obras e Projetos irá realizar a atualização do preço unitário de cada apropriação do respectivo membro, em que a data de apropriação esteja dentro do período de processamento. O preço utilizado será o valor do ticket médio, que é o resultado do valor pago no período, dividido pela a quantidade de horas registradas na folha de ponto do período;
* Caso o cálculo da Folha seja desfeito e a Folha seja calculada novamente no período, a revaloração deve ser executada novamente para atualizar as apropriações com os valores corretos.
* Caso o funcionário tenha horas de ponto e não possua horas apropriadas (não apontou em nenhuma tarefa), o processo adotará o seguinte comportamento seguindo a ordem abaixo:
  + Valida se o parâmetro "Tarefa para Rateio de Horas Improdutivas" ([Parâmetros do projeto](https://tdn.totvs.com/pages/viewpage.action?pageId=421385196)) está preenchido e se estiver o rateio de horas improdutivas e a revaloração de mão de obra serão geradas para essa tarefa;
  + Se o parâmetro "Tarefa para Rateio de Horas Improdutivas" não estiver preenchido, o sistema irá verificar a Alocação de Mão de obra informada para o funcionário no período e irá considerar as tarefas ali informadas na geração do rateio de horas improdutivas e revaloração de mão de obra;
  + Sem a utilização do parâmetro "Tarefa para Rateio de Horas Improdutivas" e sem a Alocação de mão de obra, o processo irá buscar as tarefas às quais está vinculado o insumo (função do funcionário) no período informado e irá gerar nessas tarefas o rateio de horas improdutivas e a revaloração de mão de obra.

**Observações:**

* Quando o parâmetro do projeto "Mobilidade/Ratear horas improdutivas para a tarefa" estiver marcado, o TOTVS Construção Obras e Projetos irá gerar a apropriação na tarefa definida no parâmetro de mão de obra.
* Quando o parâmetro não estiver marcado, o TOTVS Construção Obras e Projetos irá ratear entre as tarefas das apropriações do membro ativo dentro do projeto e no período informado.
* Quando o parâmetro não estiver marcado e houver necessidade de gerar apropriação para um membro que possui registro na folha de ponto, mas não possui nenhuma apropriação no período, o TOTVS Construção Obras e Projetos identificará a tarefa através da planilha de atividades, pesquisando pelo insumo do membro na equipe e o centro de custos retornado da folha de ponto através da seção do funcionário, pegando a primeira tarefa obedecendo à hierarquia do cadastro.
* Caso não seja possível identificar nenhuma tarefa pelas regras acima, o processo deverá gerar um LOG informando que não houve apropriação, explicando o motivo.

**Importante:**

Caso não exista tarefa default para improdutividade de mão de obra informada no parâmetro o sistema irá, após a tela da simulação do processo de Revaloração e Rateio de Improdutividade mostrar os funcionários que se encontram nessa situação e permitir que o usuário informe qual será a tarefa para a qual a improdutividade será lançada.

Na nova tela serão mostrados os funcionários que se enquadram nessa situação, sendo que essa nova tela somente irá aparecer se houverem funcionários nesta situação.

**Detalhamento de Cálculos:**

Importante

Segue abaixo um exemplo de como os calculos são realizados.

**Porem em cada empresa e projeto o exemplo demonstrado abaixo pode variar.**

****É importante que o Gerente do projeto em conjunto com o RH  verifiquem os encargos e proventos que deverão ser considerados ao buscar o custo do funcionário.****

* **Ticket Médio** = (Valor pago no período / Número de horas do ponto no período).
  + **Importante**: O Valor pago no período é calculado baseado nos eventos e encargos que foram considerados para a geração do envelope de pagamento do funcionário. O Número de horas do ponto no período representa as horas registradas na folha de ponto naquele período de apuração. Para que eventos e encargos sejam considerados nos cálculos, é necessário que estejam com a opção "Incide no custo do funcionário" marcada.

**Valor pago no período:**

O valor pago total é igual à soma do Valor Pago Eventos + Valor Pago Encargos: **3.551,30 + 3.384,40 = 6.935,70**

* + **Número de horas do ponto no período:**Esse número de horas consiste na soma das horas dos eventos no período de apuração e é definido de acordo com o tipo de grandeza definida no evento, Valor, Hora, Dia ou Referência, considerando as seguintes regras:
    - Se o evento é do tipo **Provento**:
      * Se o tipo da grandeza é **Dia**: A jornada mensal do funcionário é considerada e multiplicada pelo valor de referência do evento: (jornada / 30 dias fixos do mês) X referência
      * Se o tipo da grandeza é diferente de **Dia**: O campo Horas será considerado
    - Se o evento é do tipo **Desconto**: O cálculo é o mesmo citado acima, porém ao invés de somar ao total, o valor é subtraído;
    - Exemplo em números, considerando a jornada de PEDRO ÁLVARES CABRAL como 220 horas:
      * Para o evento 0001, temos: (220 / 30 ) X 30 = 220 horas
      * Para o evento 0034, temos: 3 horas
      * Para o evento 0003, temos: 0 horas
      * Para o evento 0004, temos: 0 horas
      * Para o evento 0019, temos: 1 hora
      * Então o **Número de horas do ponto no período**será: 220 + 3 + 0 + 0 - 1 = **222 horas**
  + Concluímos então que o valor do Ticket Médio será: **6.935,70 / 222 = 31,24**

* **Horas Improdutivas:** Número de horas do ponto no período - Número de horas apropriadas no período
  + Exemplo em números, considerando que o Número de horas apropriadas no período é igual a 180 horas, temos **222** - **180** = **42 horas** para serem apropriadas.
  + Exemplo de cálculo quando houver apropriações em mais de um projeto para o cenário acima:

    - Fórmula = **(A – B) / B \* C**, onde:

      * A: **Número de horas do ponto no período**
      * B: Total de horas produtivas apropriadas para o funcionário no período da Folha de Ponto em todos os projetos
      * C: Total de horas produtivas apropriadas para o funcionário no período da Folha de Ponto no projeto corrente
      * Em números:
        + A: **222 horas**
        + Projeto 1 (corrente): **90 horas** apropriações produtivas
        + Projeto 2: **50 horas** apropriações produtivas
        + Projeto 3: **40 horas** apropriações produtivas
        + Total dos Projetos: **180 horas**
        + Ao executar o processo de rateio no projeto 1, o resultado será:  
          - Memória de cálculo = (**222** - **180** ) / **180** \* **90** = **21 horas**
          - Projeto 1  
            * 90 horas apropriações produtivas
            * 21 horas apropriações improdutivas
          - Projeto 2  
            * 50 horas apropriações produtivas
            * 11,66 horas apropriações improdutivas
          - Projeto 3  
            * 40 horas apropriações produtivas
            * 9,33 horas apropriações improdutivas

* **Após execução do processo, será exibido um log com a memória de calculo para auxiliar na conferência dos valores, ele será exibido no seguinte formato:**

É possível abrir o log no editor, ou copiar e abrir em qualquer editor de sua preferência para uma melhor visualização, ao fazer isso, o log será apresentado da seguinte forma:

FUNCIONÁRIOS

Rateio de mão de obra improdutiva:

00035 - MILTON MACHADO DANTAS:

Função : 00030 - Ajudante  Armação  
Tipo membro : Funcionário  
Insumo : 02020202 - TINTA   
Preço unitário da apropriação : R$ 10,07  
Quantidade horas do ponto : 220  
Quantidade horas apropriadas : 194,0000   
Quantidade horas improdutivas rateadas : 26,0000  
   
Tarefas:

001.01.01.01 - Pintura de Paredes Internas   
Quantidade horas improdutivas rateadas na tarefa : 14,7423  
      
001.01.01.02 - Pintura de Fachadas Externas   
Quantidade horas improdutivas rateadas na tarefa : 5,3608  
      
001.01.01.03 - Impermeabilização de Superfícies  
Quantidade horas improdutivas rateadas na tarefa : 2,2784  
      
001.01.01.04 - Pintura de Estruturas Metálicas  
Quantidade horas improdutivas rateadas na tarefa : 3,6185

Apropriações de Funcionário revaloradas:

00035 - MILTON MACHADO DANTAS:

Insumo : 02020202 - TINTA   
Preço unitário revalorado : R$ 10,07

TERCEIROS

Rateio de mão de obra improdutiva:

001 - JOSÉ DA SILVA:

Função : 00001 - AUXILIAR  
Tipo membro : Terceiro  
Insumo : 01.01.001.002 - Auxiliar  
Preço unitário : R$ 15,61  
Quantidade horas do ponto : 220  
Quantidade horas apropriadas : 215,0000   
Quantidade horas improdutivas rateadas : 5,0000  
   
Tarefas:

002.01.01.01 - Transporte de material 1ª e 2ª categoria c/ Caminhão Basculante   
Quantidade horas improdutivas rateadas na tarefa : 3,1628  
      
002.01.01.02 - Esc., regul., assent. e reat. de tubo concreto para rede pluvial Ø600mm h=2,2m   
Quantidade horas improdutivas rateadas na tarefa : 0,0233  
      
002.01.01.03 - Esc., regul., assent. e reat. de tubo concreto para rede pluvial Ø400mm h=2m   
Quantidade horas improdutivas rateadas na tarefa : 1,5116  
      
002.01.01.04 - Transporte de material 1ª e 2ª categoria c/ Caminhão Basculante   
Quantidade horas improdutivas rateadas na tarefa : 0,3023

Apropriações de Terceiro revaloradas:

001 - JOSÉ DA SILVA:

Insumo : 01.01.001.002 - Auxiliar  
Preço unitário revalorado : R$ 15,61

* **Folha PROTHEUS**:
  + A integração com o PROTHEUS é realizada via EAI no padrão de mensagem única. Deve estar ativa no TOTVS Integração. A utilizada neste processo é a “TOTVS Folha Pagto X Mobilidade”, que permite as seguinte integrações:
    - Funcionários, através da mensagem “EMPLOYEE”;
    - Busca de Custos, através da mensagem “GETEMPLOYEECOST”;
    - Eventos/Verbas, através da mensagem “PAYROLLAMOUNT”;
    - Funções, através da mensagem “ROLE”.
  + A busca de parâmetros é realizada através de Webservice que está definido nos parâmetros gerais, vide o tópico parâmetros do módulo de mão de obra deste documento. Neste WebService é verificado o período de folha de ponto e a competência da folha de pagamento corrente para identificar se a folha está fechada ou não. Considera-se folha fechada, todas anteriores a corrente;
  + O TOP solicita ao PROTHEUS o custo do funcionário em um determinado período. Esta solicitação é feita através da matrícula do funcionário e de acordo com as eventos/verbas parametrizadas. Não havendo a parametrização dos eventos/verbas, é retornado o valor do custo unitário do funcionário considerando todos os eventos da folha de pagamento;
  + Para visualizar detalhes das mensagens trafegadas é necessário acessar sistema de integração através do RM.exe e utilizar a opção é “Integração \ Mensagem única \ Fila de mensagens únicas”.
* **Folha RM**:
  + As informações necessárias para este processo são obtidas através de serviços disponibilizados pelos sistemas TOTVS Automação de Ponto e TOTVS Folha de Pagamento;
  + Os eventos que compõe o custo do funcionário devem ter o campo “Incide no custo do funcionário” marcado;
  + Os encargos que compõe o custo do funcionário devem ter o campo “Incide no custo do funcionário” marcado.
* **Ponto Controlado por Terceiros**:
  + O sistema busca a informação do total de horas de ponto na tabela MHISTHORASTRABALHO. As informações desta tabela são gerenciadas pelo processo de integração. As informações devem ser enviadas ao TOP pelo WebService “WsConTerceiros” disponível via TOTVS Integração (WCF).

### **🔹 Importante**

Para que esse processo **considere funcionários/terceiros demitidos ou em férias**, é necessário que o usuário que irá executar o processo esteja com a permissão **“Considerar funcionários demitidos/férias na Apropriação de Mão de Obra”** liberada em seu perfil, conforme figura abaixo:
