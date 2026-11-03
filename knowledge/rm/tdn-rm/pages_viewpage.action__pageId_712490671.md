---
content_hash: 8aaf96ee4e1df9fa7b96e0569f6ff1e4a63b43d8db4d5406f0b9a9ba4e75e785
fetched_at: '2026-06-29T00:11:25.558388+00:00'
page_id: '712490671'
product: rm
source: tdn-rm
title: Processador frequência diária
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=712490671
version: 16
---

Este processo é utilizado pela Instituição de Ensino para processar e validar os check-ins realizados pelos alunos, consolidando os resultados por meio da atribuição de presença ou ausência. A validação é feita com base na comparação das informações dos check-ins com os planos de aula previamente definidos para as turmas/disciplinas.

**Educacional  | Matrícula e Avaliação | Notas e Faltas | Mais... | Processador de frequência diária**

Permissão de acesso

Para acessar este processo, é necessário possuir permissão no perfil de usuário, especificamente no seguinte item:

Passo 1 - Dados iniciais

Este processo tem como objetivo realizar o controle de frequência diária de forma automatizada, com base nos check-ins registrados no banco de dados, realizados pelos alunos por diferentes meios. A partir dessas informações, o sistema atribui presença aos alunos que efetuarem check-in dentro do período de uma determinada aula e ausência àqueles que não o realizarem nesse intervalo, considerando os parâmetros definidos no processo, conforme detalhado a seguir.

Parametrizações necessárias

Para a correta execução do processo, é necessário realizar as seguintes parametrizações nas Turmas/Disciplinas:

**1) Etapa de Falta única no período**  
Deve existir **apenas uma única Etapa de Falta** para cada Turma/Disciplina a ser processada, cuja **Data de Início** e **Data de Término** estejam dentro do período correspondente à data de execução do Processador de Frequência Diária.

Essa configuração é necessária para que o sistema identifique corretamente qual etapa será utilizada no processamento automático da frequência.

> **Exemplo:**  
> Considerando uma execução em **17/05/2023**, não pode haver mais de uma etapa com período (Data de Início e Data de Término) que contemple essa data.
>
> Caso essa regra não seja atendida, será retornado o seguinte erro no log do processador:
>
> "Não foi possível recuperar uma única etapa de falta desta Turma/Disciplina cuja data de início e término esteja dentro do intervalo do dia 17/05/2023."

**2) Etapas sem período definido**  
Caso existam múltiplas Etapas de Falta sem preenchimento das datas de **Data de Início** e **Data de Término**, todas serão consideradas válidas para qualquer período de execução.

Isso fará com que o sistema entre no mesmo cenário descrito no item anterior, resultando em erro por ambiguidade de etapas.

**3) Período de digitação válido**  
As Etapas de Falta devem possuir um período de digitação válido, compatível com a data de execução do processo:

* Data de Início da Digitação
* Data Limite da Digitação

**4) Turmas/Disciplinas Gerenciais**  
Para Turmas/Disciplinas do tipo gerencial, o aluno realiza o check-in na turma gerenciadora.  
Nesse caso, o processador utilizará essas informações para processar as respectivas Turmas/Disciplinas gerenciadas.

Data de execução do processo

Este processo foi projetado para ser executado preferencialmente de forma **agendada**, com recorrência definida pela Instituição de Ensino, conforme suas necessidades operacionais.

Existem duas formas de execução do processamento:

### 1) Execução agendada (automática)

Opção: **“Executar o processador de frequência diária para a data e hora atual da execução do processo”**

Recomenda-se que a Instituição configure o agendamento automático, a fim de otimizar o processamento da frequência diária.

Nessa modalidade:

* O sistema considera todos os **planos de aula do dia da execução**;
* São processadas apenas as aulas cujo **horário de início seja menor ou igual ao horário da execução**.

> **Exemplo:**  
> Se o processo for executado às **09:00 do dia 05/09/2022**, serão processadas todas as aulas desse dia que tenham início até às 09:00.

**Log de processamento:**  
Nesta opção, o log gerado é mais resumido, apresentando apenas:

* Total de alunos
* Total de presenças
* Total de ausências

Não é exibida a listagem detalhada de alunos por Turma/Disciplina.

### 2) Execução manual (reprocessamento)

Opção: **“Reprocessar para um dia específico”**

Essa modalidade é indicada quando há necessidade de recalcular a frequência para uma data específica, seja ela:

* Uma data anterior (retroativa), ou
* A data atual

Nessa execução:

* São consideradas **todas as aulas do dia selecionado**, até **23:59**;
* O processamento é refeito **mesmo que já tenha sido executado anteriormente**;
* Os dados existentes são **sobrescritos**, ou seja, a frequência será recalculada com base nas regras vigentes.

### Regra para reprocessamento de datas retroativas

Ao executar o processo para uma data anterior à atual, é necessário que exista **pelo menos uma Etapa de Falta válida na data da execução do processamento**.

> **Exemplo:**  
> Processamento para a data **11/04/2022**, sendo a data atual **09/09/2022**.
>
> Nesse cenário, deve existir uma Etapa de Falta cuja configuração atenda aos seguintes critérios:
>
> * Período de **Data de Início** e **Data de Término** compatível;
> * Período de **Data de Início da Digitação** e **Data Limite de Digitação** vigente na data em que o processo está sendo executado.

Essa validação é necessária para permitir a reavaliação da frequência, mesmo para períodos já encerrados.

Aulas geminadas

A parametrização de aulas geminadas define a forma como o sistema deve tratar **múltiplas aulas consecutivas da mesma disciplina no mesmo dia**, especialmente em relação à validação de check-in e atribuição de presença.

Essa configuração determina se será necessário um check-in por aula ou se um único check-in poderá ser considerado válido para todas as aulas do período.

**Opção:** *“Necessário um check-in em cada aula”*

Quando essa opção estiver habilitada, o Processador de Frequência Diária validará a presença do aluno **individualmente para cada aula geminada**. Ou seja, será necessário realizar um check-in em cada período de aula para que a presença seja atribuída corretamente.

> **Exemplo:**  
> Na Turma/Disciplina *Metodologia em Pesquisa*, existem duas aulas geminadas no mesmo dia:
>
> * Terça-feira: 07:00 às 07:50
> * Terça-feira: 07:50 às 08:40
>
> Se o aluno realizar apenas **um check-in às 07:10**, o resultado será:
>
> * Presença na aula das **07:00 às 07:50**
> * Ausência na aula das **07:50 às 08:40**
>
> Ou seja, a presença é contabilizada somente para a aula cujo período contém o horário do check-in.

**Opção:** *“Necessário apenas um check-in entre o período das aulas”*

Quando essa opção estiver habilitada, o Processador de Frequência Diária considerará a presença do aluno em **todas as aulas geminadas do dia** caso seja realizado **ao menos um check-in dentro do período de qualquer uma das aulas**.

Ou seja, ao efetuar um único check-in válido, o aluno receberá presença não apenas na aula correspondente ao horário do registro, mas também nas demais aulas geminadas da mesma disciplina naquele dia.

> **Exemplo:**  
> Considerando duas aulas geminadas:
>
> * 07:00 às 07:50
> * 07:50 às 08:40
>
> Se o aluno realizar um check-in às **07:10**, o resultado será:
>
> * Presença na aula das **07:00 às 07:50**
> * Presença na aula das **07:50 às 08:40**
>
> Isso ocorre porque o sistema identifica ao menos um check-in válido dentro do período total das aulas geminadas e replica a presença para as demais aulas do mesmo dia.

Limites para considerar presença do check-in

O processo permite configurar como os check-ins dos alunos serão considerados para atribuição de presença, com base nas seguintes opções:

**1) Utilizar todo o período da aula para coletar a presença**

Nesta configuração, o processador considera como válido qualquer check-in realizado **dentro do período da aula**.

> **Exemplo:**  
> Período da aula: **07:00 às 07:50**
>
> * Check-in às **07:01** → Presença atribuíd
> * Check-in às **06:59** → Não considerado (aluno receberá falta)

**2) Utilizar limites com tolerância para check-in**

Nesta opção, o processador considera a presença com base em **intervalos de tolerância configuráveis**, permitindo maior flexibilidade no registro dos check-ins.

Parâmetros disponíveis:

* Considerar check-in a partir de **X minutos antes do início da aula**
* Considerar check-in até **X minutos após o início da aula**
* Considerar check-in a partir de **X minutos antes do final da aula**
* Considerar check-in até **X minutos após o final da aula**

Essas configurações permitem definir uma janela de validação personalizada para os registros de presença.

**3) Liberar frequência das aulas automaticamente após o processamento dos dados**

A Instituição de Ensino pode optar por liberar automaticamente a frequência das aulas após o processamento.

**Regras importantes:**

1. Caso a liberação automática **não esteja habilitada**, a disponibilização da frequência deverá ser realizada pelos processos padrão (ex.: portais ou aplicação administrativa).
2. Se o parâmetro  
   **“Permitir a visualização das notas e faltas da etapa somente após a liberação do professor”**  
   estiver habilitado, a frequência **não ficará visível para os alunos**, mesmo após o processamento.

   Nesse caso, será necessário também marcar o parâmetro: **“Disponível para Alunos”** no cadastro da Etapa de Faltas.
Passo 2 - Filtro de Turma/Disciplina

O processo permite definir quais Turmas/Disciplinas serão consideradas na execução, por meio das seguintes opções:

**1) Realizar processamento para todas as Turmas/Disciplinas do contexto**

Ao selecionar esta opção, o processador executará o processamento para **todas as Turmas/Disciplinas disponíveis no contexto logado**, considerando o critério da **data de execução**.

Ou seja, serão processadas todas as Turmas/Disciplinas que possuam **planos de aula vinculados à data informada**, independentemente de seleção individual.

**2) Realizar processamento apenas para as Turmas/Disciplinas abaixo**

Ao selecionar esta opção, é possível **refinar quais Turmas/Disciplinas serão processadas**.

Para isso:

* Utilize a opção **“Filtro”**;
* O filtro disponível é o mesmo utilizado na visão de Turmas/Disciplinas;
* Após aplicar os critérios desejados, apenas as Turmas/Disciplinas filtradas serão consideradas no processamento.

Passo 3 - Ponto de referência para validação de check-in

Essa parametrização tem como objetivo definir a **localização de referência** da Instituição de Ensino (ou do local onde as aulas são realizadas), bem como a **distância máxima permitida** para que um check-in seja considerado válido para atribuição de presença.

A localização é definida a partir de um endereço, utilizando como base suas **coordenadas geográficas (latitude e longitude)**.

**Opção:** *“Considerar a presença apenas para check-ins dentro do raio da localização definida”*

Quando habilitada, essa opção faz com que o processador valide apenas os check-ins realizados **dentro de um raio configurado** a partir da localização informada.

Ou seja:

* Check-ins realizados **dentro do raio permitido** → considerados para presença
* Check-ins realizados **fora do raio permitido** → desconsiderados (aluno poderá receber falta)

Para informar as coordenadas, siga os passos indicados no respectivo guia de configuração.

As informações de **latitude** e **longitude** serão copiadas automaticamente para os campos:

* Latitude
* Longitude

O campo **“Distância em metros”** é utilizado para definir o raio de validação do check-in. Por padrão, ele já vem preenchido com o valor mínimo permitido, porém a Instituição de Ensino pode **reduzir ou aumentar essa distância** conforme sua necessidade operacional.

Essa configuração determina o alcance geográfico aceito para que o check-in seja considerado válido para fins de presença.
