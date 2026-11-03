---
content_hash: 1eff7fcd0d8fddec0a7c5c2c0f46af6e0a77a3f2e9a2821faada53285032b9f2
fetched_at: '2026-06-29T00:08:26.562443+00:00'
page_id: '271183668'
product: rm
source: tdn-rm
title: DT Integração Educacional x Labore – Cálculo da Folha do Professor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271183668
version: 121
---

# 

---

# Integração Educacional x Labore – Cálculo da Folha do Professor

|  |  |  |  |
| --- | --- | --- | --- |
| **Linha de Produto:** | RM | | |
| **Segmento Executor:** | C&P, Educacional | | |
| **Módulo:** | TOTVS Folha de Pagamento, TOTVS Educacional | | |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Reprogramação Salarial | Reprogramação Salarial | | | |
| **Requisito (ISSUE):** | [RHFOP001-585](http://jiraproducao.totvs.com.br/browse/RHFOP001-585) | | |
| **País:** | (X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

---

# Reprogramação Salarial - Utilizando Tabela Salarial

### **Contexto de negócio**

      A implementação foi realizada com o intuito de aprimorar a rotina de “Reprogramação Salarial”, onde passará a existir a possibilidade de associação de Tabelas Salariais do RM Vitae as turmas/disciplinas por matriz aplicada, essa evolução visa atender ao mercado do ensino básico, onde as tabelas de valores da hora/aula são definidas pelos sindicatos dos professores, levando em consideração curso/série e titulação do professor.

# **Sistemas Envolvidos**

* + - **Totvs RM Educacional:**O modulo Educacional é responsável por retornar as informações que a rotina de reprogramação salarial necessita, uma dessas informações é o valor hora/aula que o professor deverá receber. Após a implementação, o modulo passará a disponibilizar a possibilidade de realizar a associação de tabelas salariais com valores de hora/aula predefinidos para as matrizes aplicadas.
    - **Totvs RM Folha de Pagamento:** O sistema Folha de pagamento disponibiliza a rotina Reprogramação Salarial que possui o intuito decalcular o salário dos professores, ao executar esse processo, o modulo Educacional é acionado para que dê o retorno da Quantidade de Aulas e Valor hora/aula (Tabela Salarial), após a “integração” entre os sistemas, será feito uma operação aritmética interna resultando no salário composto do professor.

### **Apresentação do fluxo da integração**

### **Detalhamento do Fluxo de trabalho**

# **Educacional**

##### Efetuar parametrização necessária para uso da tabela salarial

      Ciente do que foi dito anteriormente, para que o Educacional passe a fornecer valores de hora/aula conforme a tabela salarial, deverá acessar os parâmetros do módulo em questão e então fazer a marcação da flag “Utilizar valor da hora/aula: De acordo com a Tabela Salarial do professor”.

Caminho: Educacional | Configurações | Parâmetros | Integrações | Folha | Etapa 1 – Folha 2/2.

##### Vinculo do professor x Matriz Aplicada x Tabela Salarial

      Após executar a associação da tabela salarial à Matriz Aplicada do professor, os dados vinculados ficarão armazenados em tabelas do educacional para posterior recuperação da informação através do processo “Reprogramação salarial”, executado pelo Totvs Folha de Pagamento.

# **Folha de Pagamento**

##### Vinculação da tabela salarial à matriz aplicada.

      No modulo Folha de Pagamento foi disponibilizado a rotina “Associação de tabelas salariais aos professores” onde será listada as matrizes aplicadas e turmas livres disponíveis para associação.

      As Matrizes aplicadas dos professores serão listadas de acordo com o seguinte critério:

* + - * + Caso o professor lecione em turmas que possuem Matrizes aplicadas diferentes, será listado as Matrizes com possibilidade de associação de tabelas salariais ou níveis distintos.
        + Caso uma das turmas do professor siga o conceito de “Turma Livre”, onde não existe a vinculação de uma Matriz aplicada, a mesma passará a ser apresenta para possibilidade de associação da tabela salarial.

1. Como pode ser visto, foram listadas 5 Matrizes aplicadas diferentes para o mesmo professor pelo fato de que existe o seu vínculo a turmas/disciplinas com matrizes aplicadas distintas.
2. Nota-se também que a partir do momento em que é listada mais de uma Matriz Aplicada, será possível associar tabelas salariais diferentes.
3. A associação da tabela salarial é feita pelo menu selecionado (3), onde deverá ser selecionada à Matriz Aplicada, preencher os campos “Tabela Salarial”, “Nível” e “Faixa” e então clicar no botão “Associar”.

**Observação**: As informações que o usuário poderá visualizar são:

- Código da filial;  
- Nome da filial;  
- Código do nível de ensino;  
- Nome do nível de ensino;  
- Código do curso (somente para matriz aplicada);  
- Nome do curso (somente para matriz aplicada);  
- Código da habilitação (somente para matriz aplicada);  
- Nome da habilitação (somente para matriz aplicada);  
- Código da grade (somente para matriz aplicada);  
- Nome da grade (somente para matriz aplicada);  
- Código do turno;  
- Nome do turno;  
- Identificador da matriz aplicada (somente para matriz aplicada);  
- Código do professor;  
- Nome do professor;  
- Identificador da turma/disciplina (somente para turma livre);  
- Código da turma (somente para turma livre);  
- Nome da turma (somente para turma livre);  
- Código da disciplina (somente para turma livre);  
- Nome da disciplina (somente para turma livre);  
- Código da tabela;  
- Código do nível;  
- Código da faixa;

##### Executar a rotina de Reprogramação Salarial

      Para que seja calculado o salário composto do professor, deverá ser executado a rotina de Reprogramação Salarial.

      O processo irá realizar uma operação aritmética entre 3 itens, sendo eles:

* + - * + **Fator Mensal:** Valor predefino dentro dos parâmetros do Totvs Folha de Pagamento no caminho Folha de Pagamento | Integrações | Gestão Educacional | Etapa 1 – Configurações Gerais.
        + **Quantidade de Aulas:** Será retornado pelo Educacional de acordo com o plano de aula existente para o professor ou pelo preenchimento do campo “Quantidade de aulas semanais” no momento da vinculação do mesmo a turma/disciplina.
        + **Valor Hora/Aula:** O valor hora/aula é enviado pelo Educacional de acordo com o valor preenchido na vinculação do Professor com a Turma/Disciplina.

      A operação aritmética consiste na multiplicação da “Quantidade de Aulas” pelo “Fator Mensal” e em seguida será multiplicado o resultado pelo “Valor Hora/Aula”, onde resultará no salário do professor.

##### Lançar Salário Composto para Folha

      Agora que já temos o salário composto do professor calculado para a competência atual da folha, deverá ser feito o seu lançamento para o envelope do funcionário, o processo deve ser executado através do menu “Lançamentos | Grupos de Eventos”.

      Para que o processo de lançamento considere o salário composto calculado, será necessário fazer a marcação do campo “Lançar Salário composto”.

Caminho:  Folha de Pagamento | Folha Mensal | Lançamentos | Grupo de Eventos.

      Caso a folha esteja parametrizada para lançar por centro de custo deverá utilizar o módulo “Lançamento por centro de custo”

---

# Reprogramação Salarial - Quantidade de Aulas Semanais de acordo com o plano de aula

### **Contexto de negócio**

      A implementação foi realizada com o intuito de aprimorar a rotina de “Reprogramação Salarial”. Será possível efetuar o cálculo da folha para professor baseando-se na quantidade de aulas de acordo com o plano de aula gerado, ou seja, não será necessário o preenchimento manual de tal informação.

# **Sistemas Envolvidos**

* + - **Totvs RM Educacional:**O módulo Educacional é responsável por retornar as informações que a rotina de reprogramação salarial necessita. Uma dessas informações é a quantidade de aulas que o professor leciona por semana. Após a implementação, o módulo terá também a possibilidade de gerar a quantidade de aulas (plano de aula) automaticamente de acordo com os horários vinculados ao professor.
    - **Totvs RM Folha de Pagamento:**O sistema Folha de pagamento disponibiliza a rotina Reprogramação Salarial que possui o intuito decalcular a folha dos professores. Ao executar esse processo, o módulo Educacional é acionado para que dê o retorno da Quantidade de Aulas que atualmente pode ser originada pelo plano de aula ou pelo cadastro do professor da turma/disciplina. Após a “integração” entre os sistemas, será feito uma operação aritmética interna resultando no salário do professor.

### **Apresentação do fluxo da integração**

### 

### **Detalhamento do Fluxo de trabalho**

# **Educacional**

##### Parametrização necessária

      De acordo com o que já foi dito anteriormente, para que o Educacional passe a identificar automaticamente a quantidade de aulas do professor na semana, deverá acessar os parâmetros do modulo em questão e então fazer a marcação do parâmetro “Origem das aulas semanais: Do número de horários definidos no plano de aula”.

Caminho: Educacional | Configurações | Parâmetros | Integrações | Folha | Etapa – Folha 2/2.

##### Vinculo do professor x Matriz Aplicada x Horário.

      Nesta etapa deverá ser feito todo o processo desde o cadastro do professor até a vinculação do mesmo na turma/disciplina e aos horários em que terá que lecionar as aulas.

      Obs.: Os horários se encontram dentro da turma/disciplina.

      Após o término da configuração acima, será necessário gerar o “Plano de Aula” da turma/disciplina que posteriormente, será usado para cálculo de aulas semanais.

Com base nos horários busca-se o total de planos de aula gerados e divide esse valor pelo total de semanas.  
Obs.: Para calcular a quantidade de semanas, deverá considerar a diferença em dias da data de/até (período da Reprogramação) dividido por 7.

**Exemplo:**

Professor possui um total de planos de aula no valor de 88 aulas, dividindo pela quantidade de semanas (4), será encontrado o valor de 22 aulas por semana.

# **Folha de Pagamento**

##### Executar a rotina de Reprogramação Salarial

      Para que seja calculado o salário composto do professor, deverá ser executada a rotina de Reprogramação Salarial.

      O processo irá realizar uma operação aritmética entre 3 itens, sendo eles:

* + - * + - **Fator Mensal:**Valor predefino dentro dos parâmetros do Totvs Folha de pagamento no caminho Folha de Pagamento | Integrações | Gestão Educacional | Etapa 1 – Configurações Gerais.
          - **Quantidade de Aulas:** Será retornado pelo Educacional de acordo com o plano de aula existente para o professor.
          - **Valor Hora/Aula:**O valor hora/aula é enviado pelo Educacional de acordo com o valor preenchido na vinculação do Professor com a Turma/Disciplina.

      A operação aritmética consiste na multiplicação da “Quantidade de Aulas” pelo “Fator Mensal” e em seguida será multiplicado o resultado pelo “Valor Hora/Aula”, onde resultará no salário do professor.

##### Lançar Salário Composto para Folha

      Agora que já temos o salário composto do professor calculado para a competência atual da folha, deverá ser feito o seu lançamento para o envelope do funcionário através do menu “Lançamentos | Grupos de Eventos”. Para que o processo de lançamento considere o salário composto calculado, será necessário fazer a marcação do campo “Lançar Salário composto”.

Caminho:  Folha de Pagamento | Folha Mensal | Lançamentos | Grupo de Eventos.

Caso a folha esteja parametrizada para lançar por centro de custo deverá utilizar o módulo “Lançamento por centro de custo”

divs
