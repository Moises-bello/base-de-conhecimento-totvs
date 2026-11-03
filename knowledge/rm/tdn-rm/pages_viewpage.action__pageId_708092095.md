---
content_hash: 207a7ee0e636de5596247daca75774255a3aa3d49c3b5965981164985f4bf329
fetched_at: '2026-06-29T00:11:25.348423+00:00'
page_id: '708092095'
product: rm
source: tdn-rm
title: Férias Compulsórias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=708092095
version: 16
---

## **CONTEÚDO**

1. **Versões**
2. **Visão Geral**
3. **Exemplo de utilização**
4. **Tela Marcar Férias Compulsórias**
5. **Tela Parâmetros Coligada**
6. **Tela fracionamento de jobs e agendamento de processo**
7. **Tabelas utilizadas**

## **01.****VERSÕES**

false

**A partir do Release:**

* 12.1.2209 e Superiores

## **02.** **VISÃO GERAL**

Processo que permite marcar férias compulsórias para os funcionários que estejam com férias em dobro à vencer, considerando a data de execução do processo e a quantidade de dias informados para execução do processo.

Para a marcação das férias será necessário informar os parâmetros no módulo. Essa parametrização poderá ser global ou nos parâmetros da coligada.

A opção de usar Parâmetros específicos por coligada estará disponível após avançar a tela de Parâmetros. Dentro dos parâmetros por coligada é que será possível informar a seleção de funcionários para os quais deseja marcar as férias e outras informações específicas da coligada, podendo inclusive gerar para mais de uma coligada ao mesmo tempo.

A nova funcionalidade conta com o recurso de Agendamento de Processos e/ou Fracionamento de Jobs.

**Observações:**

01 - Ao realizar o processo de marcação das férias compulsórias será verificado se o funcionário possui férias a data fim do período aquisitivo em aberto, igual ou anterior a data de execução do processo - 1 ano +  a quantidade de dias informada no parâmetro '**Qtde dias a partir da execução do processo**'.

02 - Será verificado se a data de limite de início de gozo de férias, Data do aviso de férias e a data de pagamento está dentro da data de execução do processo e a data de execução do processo + a quantidade de dias vencidos para evitar a marcação de férias em dobro.

03 - Será verificado se as datas de aviso das férias e de pagamento de férias estão de acordo com a legislação vigente, ou seja, se é possível 'Marcar as Férias Compulsórias', respeitando a data de aviso de férias (30 (trinta) dias antes do início das férias) e pagamento das férias 02 (dois) úteis antes do início das férias.

04 - Através do novo processo será possível a aprovação de férias sugeridas aos funcionários que estejam com o status 'Aguardando aprovação do Gestor' e 'Aguardando aprovação do DP' e que atendam as regras de marcação de férias compulsórias, marcando o parâmetro '**Aprovar Férias'**.

05 - O usuário poderá solicitar o pagamento de 1ª parcela de 13º Salário para o funcionário marcando o parâmetro '**1ª parcela de 13º Salário'** na execução do processo.

06 - Para os funcionários que tenham informado '**Código de Grupo de Quiosque**' serão considerados também as regras específicas de marcação de férias do Grupo de Acesso ao RM Portal.

07 - Para utilização do recurso de Agendamento de Processos e/ou Fracionamento de Jobs deverão ser efetuadas as configurações necessárias no sistema.

08 - Após execução do processo, será cadastradas as férias na tela de Cadastro individual de férias para os funcionários que atendam TODAS as regras para a marcação de férias compulsórias, devendo o usuário de acordo com a sua necessidade efetuar os demais procedimentos para cálculo/lançamento e finalização de férias.

## **03. UTILIZAÇÃO**

Na primeira tela foi parametrizado da seguinte forma:

**Data de Execução do Processo:**

**Qtde dias a partir da execução do processo: 40**

Na tela por coligada foi parametrizado da seguinte forma:

Veja os dados cadastrados na tela de cadastro de férias:

**Observação:** As férias '**Marcadas**' ou '**Aprovadas**' pelo processo, apresentarão o campo '**Férias Compulsória**' marcada.

## **04. TELA Marcar Férias Compulsórias**

**Funcionamento dos parâmetros da Tela:**

**Quebra de seção e seleção de funcionários**: sendo que a seleção de funcionários para funcionários específicos somente será possível pelos parâmetros da coligada.

**Qtde de dias a partir da execução do processo:** Quantidade de dias para ser considerado como data final a ser calculada de acordo com a data de processamento.

**Exemplo:**

Data de processamento:

Quantidade de dias informado no parâmetro **Qtde de dias a partir da execução do processo**: 30

Data calculada para ser considerado como data final do processamento:

**Observação:**

Ao realizar o processo o sistema irá verificar os funcionários que tenham férias em dobro à vencer dentro do período de 16/09/2022 á 16/10/2022.

**Aprovar  Férias**: Ao marcar esse parâmetro, o sistema irá verificar férias sugeridas para os funcionários que estejam com o status '**Aguardando aprovação do Gestor**' e '**Aguardando aprovação do DP**' e que atendam as regras de marcação de férias compulsórias passando-as para o status '**Marcadas**'.

**1ª parcela de 13º Salário**: Esse parâmetro será utilizado para pagamento de 1ª parcela de 13º Salário, junto com as férias marcadas para os funcionários que atendam as regras de marcação de férias compulsórias.

## **05. TELA Parâmetros Coligada**

**Funcionamento dos parâmetros que existem de forma global e por coligada:**

**Quebra de seção e seleção de funcionários**: sendo que a seleção de funcionários para funcionários específicos somente será possível pelos parâmetros da coligada.

**Qtde de dias a partir da execução do processo:** Quantidade de dias para ser considerado como data final a ser calculada de acordo com a data de processamento.

**Exemplo:**

Data de processamento:

Quantidade de dias informado no parâmetro **Qtde de dias a partir da execução do processo**: 30

Data calculada para ser considerado como data final do processamento:

**Observação:**

Ao realizar o processo o sistema irá verificar os funcionários que tenham férias em dobro à vencer dentro do período de 16/09/2022 á 16/10/2022.

**Aprovar  Férias**: Ao marcar esse parâmetro, o sistema irá verificar férias sugeridas para os funcionários que estejam com o status '**Aguardando aprovação do Gestor**' e '**Aguardando aprovação do DP**' e que atendam as regras de marcação de férias compulsórias passando-as para o status '**Marcadas**'.

**1ª parcela de 13º Salário**: Esse parâmetro será utilizado para pagamento de 1ª parcela de 13º Salário, junto com as férias marcadas para os funcionários que atendam as regras de marcação de férias compulsórias.

## **06. Tela para fracionamento de Jobs e agendamento do processo**

Para utilizar o fracionamento de jobs e agendamento de processos deverá ser criado:

1- Em **RM | RH | Folha de Pagamento | Ambiente | Segurança de Jobs Fracionáveis**:

2 - Definir um **Perfil** e **Classe de Job** para que a parametrização seja realizada com sucesso. Será necessário definir qual o perfil irá possuir autorização para executar o processo:

**Observação:** Deverá ser selecionada em **Classe de Job** a classe de processo ‘**FopMarcarFeriasCompulsóriasProcess**’.

3 - Em **RM | RH | Folha de Pagamento | Férias | Processos | Marcar Férias Compulsórias**, será apresentado a opção o quadro de “**Escalabilidade**”, onde será possível visualizar a quantidade de fracionamentos do processo e definir a periodicidade de execução do processo de acordo com a necessidade:

4 - Após realizar a parametrização e executar o processo de Marcar Férias Compulsórias, serão criados os Jobs em RM | RH | Folha de Pagamento | Ambiente | Gerenciamento de Jobs:

**Observação:** Neste módulo, serão apresentados os Jobs referentes a execução do processo.

**Exemplo: No quadro abaixo, o processo foi executado em 01 (um) Jobs.**

**Veja também outros fracionamentos em: [Agendamento com fracionamento de job](https://tdn.totvs.com/display/LRM/TOTVS+Folha+de+Pagamento+-+Fracionamento+de+Jobs)**

## **07. EXEMPLOS**

Considerando os funcionários abaixo com as data inicio e fim do período aquisitivo aberto e a data de limite para inicio de gozo de férias. Conforme as validações da legislação, onde deve considerar o período mínimo de aviso de férias de 30 dias antes do gozo, inicio da férias não podendo ser em dia de descanso ou feriado ou até dois dias antes destes e data de pagamento até dois dias uteis antes do início de gozo de férias, para estes funcionários, as férias devem ser marcadas nas datas:

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Chapa | Inicio Período Aquisito | Fim Período Aquisitivo | Limite de Inicio de Gozo | Início de Gozo de Férias | Data do Aviso | Data Pagamento |
| 00001 | 30/12/2020 | 29/12/2021 | 30/11/2022 | 30/11/2022 | 31/10/2022 | 28/11/2022 |
| 00002 | 31/12/2020 | 30/12/2021 | 01/12/2022 | 01/12/2022 | 01/11/2022 | 29/11/2022 |
| 00003 | 01/01/2021 | 31/12/2021 | 02/12/2022 | 30/11/2022 | 31/10/2022 | 28/11/2022 |
| 00004 | 05/01/2021 | 04/01/2022 | 06/12/2022 | 05/12/2022 | 05/11/2022 | 01/12/2022 |
| 00005 | 06/01/2021 | 05/01/2022 | 07/12/2022 | 05/12/2022 | 05/11/2022 | 01/12/2022 |
| 00006 | 07/01/2021 | 06/01/2022 | 08/12/2022 | 05/12/2022 | 05/11/2022 | 01/12/2022 |
| 00007 | 08/01/2021 | 07/01/2022 | 09/12/2022 | 05/12/2022 | 04/11/2022 | 01/12/2022 |

Executando o processo de marcar as férias compulsórias no dia 31/10/2022, com a quantidade de dias a partir da execução do processo = 67, será considerado todos os funcionário onde a data do fim do período aquisitivo é anterior data da execução - 1 ano + a quantidade de dias a parti da da execução (31/10/2022 - 365 + 67) ou seja funcionários com período aquisitivo aberto onde a data fim é igual ou anterior 06/01/2022. A data de referência será 06/01/2023, ou seja, irá marcar para funcionários onde a data limite de inicio de gozo de férias, data de aviso de gozo de férias e data de pagamento de férias está entre dia 31/10/2022 a 06/01/2023:

|  |  |
| --- | --- |
| Chapa | Resultado |
| 00001 | Marcou as férias conforme o esperado |
| 00002 | Marcou as férias, iniciando na 5ª Feira, pois o sabado para ele é trabalhado conforme a escala de horário do Automação de Ponto |
| 00003 | Marcou as férias conforme o esperado |
| 00004 | Marcou as férias conforme o esperado |
| 00005 | Marcou as férias conforme o esperado |
| 00006 | Marcou as férias conforme o esperado |
| 00007 | Não marcou, pois o fim do período aquisitivo é posterior a 06/01/22. O mesmo não retornou na listagem de Funcionários |

Executando o processo de marcar férias compulsórias no dia 01/02/2022 com a mesma quantidade de 67 dias, será considerado a data final do período aquisitivo em aberto até 07/01/2022. A data de referência será 07/01/2023 ou seja, irá marcar para funcionários onde a data limite de inicio de gozo de férias, data de aviso de gozo de férias e data de pagamento de férias está entre dia 01/11/2022 a 07/01/2023:

|  |  |
| --- | --- |
| Chapa | Resultado |
| 00001 | Não marcou, pois a data de aviso é anterior a data da execução |
| 00002 | Marcou as férias, iniciando na 5ª Feira, pois o sabado para ele é trabalhado conforme a escala de horário do Automação de Ponto |
| 00003 | Não marcou, pois a data de aviso é anterior a data da execução |
| 00004 | Marcou as férias conforme o esperado |
| 00005 | Marcou as férias conforme o esperado |
| 00006 | Marcou as férias conforme o esperado |
| 00007 | Marcou 05/12/2022 , pois dia 09/12 é Sexta-Feira e Sabado é dia descanso. Dia 07/12, Quarta-feira é um dia antes de feriado (08/12) conforme calendário da Seção e retrocedeu 2 dias antes do fériado |

Executando o processo de marcar férias compulsórias no dia 02/02/2022 com a mesma quantidade de 67 dias, será considerado a data final do período aquisitivo em aberto até 08/01/2022. A data de referência será 08/01/2023 ou seja, irá marcar para funcionários onde a data limite de inicio de gozo de férias, data de aviso de gozo de férias e data de pagamento de férias está entre dia 02/11/2022 a 08/01/2023:

|  |  |
| --- | --- |
| Chapa | Resultado |
| 00001 | Não marcou, pois a data de aviso é anterior a data da execução |
| 00002 | Não marcou, pois a data de aviso é anterior a data da execução |
| 00003 | Não marcou, pois a data de aviso é anterior a data da execução |
| 00004 | Marcou as férias conforme o esperado |
| 00005 | Marcou as férias conforme o esperado |
| 00006 | Marcou as férias conforme o esperado |
| 00007 | Marcou 05/12/2022 , pois dia 09/12 é Sexta-Feira e Sabado é dia descanso. Dia 07/12, Quarta-feira é um dia antes de feriado (08/12) conforme calendário da Seção e retrocedeu 2 dias antes do fériado |

Será apresentado logs, conforme abaixo:

Parametros:

Log quando as férias forem marcadas:

Log quando a data de aviso de férias é anterior a data da execução:

Quando o funcionário é elegível ao processo de marcação de férias compulsórias, mas já tem férias marcadas:

Funcionário com período aquisitivo aberto, porém as férias estão na situação pagas:

Funcionário com afastamento cadastrado sem data de retorno, com período aquisitivo em aberto:

**08. TABELAS UTILIZADAS**

* PFUFERIASPER
* PFUNC
* GSLCJOBPERFIL
* GJOBX
* GJOBXEXECUCAOVIEW
