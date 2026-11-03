---
content_hash: 8a9134d6703cd771b6124bf010a847f5d9ded1581f8de027cf08cd034b49e459
fetched_at: '2026-06-29T00:08:26.515357+00:00'
page_id: '271182206'
product: rm
source: tdn-rm
title: DT Apontamento de faltas no Educacional integrado com o Chronus
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+Apontamento+de+faltas+no+Educacional+integrado+com+o+Chronus
version: 122
---

# 

---

# **Apontamento de Faltas**

|  |  |  |  |
| --- | --- | --- | --- |
| **Linha de Produto:** | RM | | |
| **Segmento Executor:** | C&P, Educacional | | |
| **Módulo:** | TOTVS Automação de Ponto, TOTVS Educacional | | |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Gerar plano de aula | Gerar plano de aula | | Apontamento de Falta | Apontamento de Falta | | Importar Horário Professor | Importar Horário Professor | | Recalculo | Recalculo | | Lançar para Folha de Pagamento | Lançar para Folha de Pagamento | | "Lançar" Grupo de eventos | "Lançar" Grupo de eventos | | Lançamento por Centro de Custo | Lançamento por Centro de Custo | | | |
| **Requisito (ISSUE):** | RHFOP001-653 | | |
| **País:** | (X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

---

### **Contexto de negócio**

      A implementação foi realizada com o intuito de facilitar a tratativa de ponto por parte das entidades de ensino, pelo produto de Automação do Ponto, onde poderá ser optado pela ausência das marcações/batidas de ponto ou pela existência das mesmas para cálculo das Ocorrências/Eventos. Além disso, passará a existir a possibilidade de realizar o apontamento de faltas por meio do Educacional para os professores que fazem o uso do livro de ponto ao invés da marcação de batidas por meio do REP.

# **Sistemas Envolvidos**

* + - * **Totvs RM Educacional:**O módulo Educacional da linha RM é responsável pela criação da escala de trabalho dos professores (Horários/Plano de Aula) e do controle de presença/faltas dos professores que não realizam a marcação de batidas, posteriormente será feito o envio dessas informações para o produto de Automação do Ponto.
      * **Totvs RM Automação de Ponto:** O sistema de Automação do Ponto tratará o ponto dos professores de acordo com o plano de aula importado, considerando-o como horário planejado e gerando assim, as ocorrências/eventos a serem pagos ou descontados.  
        O Totvs Automação de ponto irá se basear para realizar o cálculo de acordo com o seguinte cenário:

* + - * + Para os professores que não realizam as marcações/batidas (assinam o livro de ponto) será considerado o Apontamento de Faltas feitos no Educacional.
        + Para os professores que realizam as marcações/batidas coletadas do relógio de ponto, o cálculo será feito automaticamente pelo produto considerando estas marcações.
      * **Totvs RM Folha de Pagamento:** O Totvs Folha de Pagamento é o produto responsável por receber as horas calculadas dos os eventos pelo Automação do Ponto, gerando assim valores a serem lançados para o envelope de pagamento do Professor.

### 

---

### **Contexto Professores que não batem ponto (Assinam o livro de ponto)**

# **Fluxo da integração**

### 

### 

### 

### 

### 

### 

### 

### 

### 

### 

### 

# **Detalhamento da integração (Cadastros/Processos)**

##### Educacional

###### Parâmetro “Desconsidera Ponto” no Educacional

Para os professores que não batem ponto, ou seja, assinam o livro de ponto, deve-se fazer a marcação do campo “Desconsidera Ponto” no momento da vinculação do mesmo na Turma/Disciplina.

Obs.: Se o parâmetro for marcado na vinculação do professor na turma/disciplina, todos os horários cadastrados para o professor serão considerados como "Desconsidera Ponto", mesmo sem a marcação do parâmetro dentro do horário.

Caminho: Educacional |Currículo e Oferta | Turmas/Disciplinas | Anexos | Professores

Caso seja necessário desconsiderar o ponto do professor em apenas algum horário/dia em específico, o parâmetro também poderá ser marcada dentro da vinculação do Professor no horário.

Caminho: Educacional |Currículo e Oferta | Turmas/Disciplinas | Anexos | Horários | Anexos | Professor do Horário

###### Criação do plano de aula do Professor.

      A criação do Plano de Aula é essencial para a integração. O processo irá criar toda a “grade de horário” em que o Professor terá que lecionar suas disciplinas, contendo o horário de início e fim de suas aulas, a rotina irá levar em consideração os horários criados e vinculados à turma/disciplina.

Obs.: Apenas com o Plano de Aula montado, será possível avançar nas etapas do fluxo.

##### 

##### Executar o apontamento dos dias de falta.

O apontamento das faltas é o processo que permite o Totvs Automação de ponto trabalhar sem a existência de batidas, neste menu são listados todos os dias em que o Professor selecionado possui horário, possibilitando assim a marcação da “Falta” de forma sintetizada.

Obs.: Este processo deverá trabalhar em conjunto com o parâmetro “Desconsidera Ponto”

Caminho: Educacional | Integrações | Recursos Humanos | Apontamento de Faltas

Também é possível realizar este apontamento manualmente dia a dia, acessando o menu Turmas/Disciplinas | Anexos | Plano de aula, edite o registro do dia em que houve a falta do professor e faça a marcação do campo “Falta” na aba “Faltas/Reposição”.

##### 

##### 

##### 

##### 

##### 

##### 

##### 

##### 

##### 

##### 

##### 

##### 

##### 

##### **Automação do Ponto**

      O módulo de Automação do Ponto irá realizar o cálculo das ocorrências para o professor de acordo com as informações importadas, ou seja, será levado em consideração “Plano de Aula” e o “Apontamento de falta” executado dentro do produto Educacional.

Obs.: Caso o funcionário trabalhe no horário noturno, o Chronus também irá efetuar o cálculo de Adicional Noturno.

###### Importação do horário do professor considerando o plano de aula.

      Para trazermos as informações criadas no Educacional para o Chronus, será necessário executar o processo “Importar Horário do Professor”. A partir da execução desse processo, será montado o horário do professor de acordo com o “Plano de Aula”, além de buscar também os “Apontamentos de Faltas”.

  Após a importação do horário do professor, poderá acessar o horário planejado do funcionário/professor através do caminho Automação do Ponto | Funcionários | Anexos | Movimento do Ponto | Espelho | Visualizar Horário, conforme print abaixo.

##### 

##### 

##### 

##### 

##### 

##### 

##### 

##### 

##### Cálculo considerando Faltas/Trabalho e Geração das Ocorrências.

Ao executar o processo de “Recalculo” do espelho, o sistema irá calcular as ocorrências de acordo com as faltas apontadas no Educacional, gerando assim os eventos de desconto (Falta) e a pagar (Adicional Noturno), caso o professor trabalhe em horário noturno.

Ocorrências de Faltas geradas de acordo com os dias apontados no Educacional.

Ocorrências de Adicional Noturno gerados entre o intervalo pré-definido.

Eventos de Falta e Adicional Noturno gerados para envio ao Folha de Pagamento

Nos casos em que os professores que tiveram **atrasos** para as Aulas, não será mais necessário fazer este controle pelo Livro de Ponto, basta inserir o par de batidas referente ao horário em que ocorreu o atraso, para que o Chronus gere as Ocorrências e Evento para desconto.

      De acordo com o exemplo acima, vemos que as batidas devem ser inseridas considerando o atraso do Professor, ou seja, caso o mesmo tenha se atrasado apenas 5 minutos, a batida deveria ser inclusa as 19:05.

Obs.: Para que seja lançado **as horas aulas trabalhadas** do professor, deverá executar a rotina de Reprogramação Salarial que se encontra presente no menu do Folha de Pagamento (Folha Educacional | Agrupador “Processos” Reprogramação Salarial)

##### **Lançamento dos eventos calculadas para a Folha de Pagamento.**

Para que possamos enviar para a Folha de Pagamento os eventos calculados a serem pagos ou descontados do funcionário (Falta, Atraso e Ad. Noturno), será necessário executar o Processo “Lançar para Folha de Pagamento.

Caminho: Automação do Ponto| Movimento | Lançar para a Folha de Pagamento.

Obs.: O processo irá enviar ao Labore, para a tabela de “Movimentação Temporária”, apenas os eventos que se encontram calculados na aba “Movimento” dentro do espelho do Professor.

##### **Folha de Pagamento**

##### Recebimento dos eventos enviados pelo modulo de Automação do Ponto.

Os eventos que foram calculados e enviados pelo Automação do Ponto serão armazenados (Tabela temporária PFMOVTEMP) até que sejam lançados ao Envelope.

Caminho: Folha de Pagamento | Folha Mensal | Consulta | Consulta Movimento da Integração

##### Lançamento dos eventos para o envelope do funcionário.

      Agora que os eventos já se encontram pendentes dentro do Folha de Pagamento, será necessário realizar o envio desses valores (Eventos a pagar/descontar) ao envelope dos professores. Para isso, deverá ser executado o processo de lançamento através do menu “Lançamentos | Grupos de Eventos”, onde serão buscados os eventos presentes na tabela temporária citada acima.

      No momento da execução do processo, deverá se atentar aos seguintes itens:

1)      Para que a rotina de lançamento ao envelope envie também o salário composto calculado pela “Reprogramação Salarial”, deverá marcar o campo “Lançar Salário Composto”.

2)      Os eventos que foram enviados pelo Chronus (Automação do Ponto) serão considerados para lançamento apenas se o campo “Lançar eventos da integração com outros aplicativos” estiver marcado.

      Caso a folha esteja parametrizada para lançar por centro de custo deverá utilizar o módulo “Lançamento por centro de custo”

### 

---

### **Contexto Professores que registram de ponto**

# **Fluxo da integração**

# 

# 

# 

# 

# **Detalhamento da integração (Cadastros/Processos)**

#### **Educacional**

##### Criação do plano de aula do Professor.

      A criação do Plano de Aula é essencial para a integração, o processo irá criar toda a “grade de horário” em que o Professor terá que lecionar suas disciplinas, contendo o horário de início e fim de suas aulas. A rotina irá levar em consideração os horários criados e vinculados à turma/disciplina.

Obs.: Apenas com o Plano de Aula montado será possível avançar nas etapas do fluxo.

#### 

#### 

#### 

#### 

#### 

#### 

#### 

#### 

#### 

#### **Automação do Ponto**

O modulo de Automação do Ponto realizará o cálculo das ocorrências para o professor de acordo com as informações importadas, ou seja, será levado em consideração “Plano de Aula” x “Batidas/Marcações” realizadas.

##### Importação do horário do professor considerando o plano de aula.

      Para trazermos as informações criadas no Educacional para o Totvs Automação de ponto, será necessário executar o processo “Importar Horário do Professor”. A partir da execução desse processo, será montado o horário do professor conforme o “Plano de Aula.

      Após a importação do horário do professor, poderá acessar o horário planejado do funcionário/professor através do caminho Automação do Ponto | Funcionários | Anexos | Movimento do Ponto | Espelho | Visualizar Horário, conforme print abaixo.

##### 

##### 

##### 

##### 

##### 

##### 

##### 

##### 

##### Calcular o espelho considerando as batidas presentes e geração das ocorrências.

      Ao executar o processo de “Recálculo” do espelho, o sistema irá criar as ocorrências de acordo com as batidas/marcações realizadas no relógio ponto (REP), gerando assim os eventos conforme configuração do sindicado.Alguns exemplos de eventos seriam trabalho, extra, falta e atraso.

##### 

##### 

##### 

##### 

##### 

##### 

##### 

##### Lançamento dos eventos calculadas para a Folha de Pagamento.

       Para que possamos enviar para a Folha de Pagamento os eventos calculados a serem pagos ou descontados do funcionário (Trabalho, Extra, Falta, Atraso e Ad. Noturno), será necessário executar o processo “Lançar para Folha de Pagamento.

Caminho: Automação do Ponto| Movimento | Lançar para a Folha de Pagamento.

Obs.: O processo enviará para a tabela de movimentação temporária do  Totvs Folha de pagamento apenas os eventos que se encontram calculados na aba “Movimento” dentro do espelho do Professor.

#### **Folha de Pagamento**

##### Recebimento dos eventos enviados pelo módulo de Automação do Ponto.

Os eventos que foram calculados e enviados pelo Automação do Ponto serão armazenados (tabela temporária PFMOVTEMP) até que sejam lançados ao Envelope.

Caminho: Folha de Pagamento | Folha Mensal | Consulta | Consulta Movimento da Integração

##### Lançamento dos eventos para o envelope do funcionário.

      Agora que os eventos já se encontram pendentes dentro do Folha de Pagamento, será necessário realizar o envio desses valores (Eventos a pagar/descontar) ao envelope dos professores. Deverá ser executado o processo de lançamento através do menu “Lançamentos | Grupos de Eventos”, onde será buscado os eventos presentes na tabela temporária citada acima.

      Para que o processo de lançamento dos eventos considere os eventos que encontram-se na tabela temporária, deverá ser executado o processo marcando o parâmetro “Lançar eventos da integração com outros aplicativos”.

Caso a folha esteja parametrizada para lançar por centro de custo deverá utilizar o módulo “Lançamento por centro de custo”

divs
