---
article_id: 15822541881111
category: Férias
content_hash: 5a3f6bf6d8071f4512d6ccdc8165a15f1e76aacccdc74a9f4892d7bd4881c4c9
fetched_at: '2026-06-28T22:46:56.184165+00:00'
product: rm
section_id: 1500000861102
source: central-rm
title: RH - RM - FOP -  Parametrização para marcação de Férias Compulsórias
type: support-article
updated_at: '2024-06-12T14:10:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15822541881111-RH-RM-FOP-Parametriza%C3%A7%C3%A3o-para-marca%C3%A7%C3%A3o-de-F%C3%A9rias-Compuls%C3%B3rias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15822529564823) Tempo aproximado para leitura: **00:16:07 min****Dúvida**Como posso marcar férias compulsórias no meu sistema?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - **Versões e patches a partir**

* 12.1.2209 e Superiores

**Observações:**

1. Ao realizar o processo de marcação das férias compulsórias será verificado se o funcionário possui férias a data fim do período aquisitivo em aberto, igual ou anterior a data de execução do processo - 1 ano +  a quantidade de dias informada no parâmetro '**Qtde dias a partir da execução do processo**'.

2. Será verificado se a data de limite de início de gozo de férias, Data do aviso de férias e a data de pagamento está dentro da data de execução do processo e a data de execução do processo + a quantidade de dias vencidos para evitar a marcação de férias em dobro.

3. Será verificado se as datas de aviso das férias e de pagamento de férias estão de acordo com a legislação vigente, ou seja, se é possível 'Marcar as Férias Compulsórias', respeitando a data de aviso de férias (30 (trinta) dias antes do início das férias) e pagamento das férias 02 (dois) úteis antes do início das férias.

4. Através do novo processo será possível a aprovação de férias sugeridas aos funcionários que estejam com o status 'Aguardando aprovação do Gestor' e 'Aguardando aprovação do DP' e que atendam as regras de marcação de férias compulsórias, marcando o parâmetro '**Aprovar Férias'**.

5. O usuário poderá solicitar o pagamento de 1ª parcela de 13º Salário para o funcionário marcando o parâmetro '**1ª parcela de 13º Salário'**na execução do processo.

6. Para os funcionários que tenham informado '**Código de Grupo de Quiosque**' serão considerados também as regras específicas de marcação de férias do Grupo de Acesso ao RM Portal.

7. Para utilização do recurso de Agendamento de Processos e/ou Fracionamento de Jobs deverão ser efetuadas as configurações necessárias no sistema.

8. Após execução do processo, será cadastradas as férias na tela de Cadastro individual de férias para os funcionários que atendam TODAS as regras para a marcação de férias compulsórias, devendo o usuário de acordo com a sua necessidade efetuar os demais procedimentos para cálculo/lançamento e finalização de férias.

**Solução**1. Na primeira tela foi parametrizado da seguinte forma:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15820444324631)

**Data de Execução do Processo:  16/09/2022**

**Qtde dias a partir da execução do processo: 40**

2. Na tela por coligada foi parametrizado da seguinte forma:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15820526126231)

3. Veja os dados cadastrados na tela de cadastro de férias:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15820563166231)

**Observação:**As férias '**Marcadas**' ou '**Aprovadas**' pelo processo, apresentarão o campo '**Férias Compulsória**' marcada. 

4. Verifique a tela para marcar férias compulsórias:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15820570128407)

**Funcionalidade dos parâmetros apresentados na tela:**

**Quebra de seção e seleção de funcionários**: sendo que a seleção de funcionários para funcionários específicos somente será possível pelos parâmetros da coligada.

**Qtde de dias a partir da execução do processo:** Quantidade de dias para ser considerado como data final a ser calculada de acordo com a data de processamento.

**Exemplo:**

Data de processamento: 16/09/2022

Quantidade de dias informado no parâmetro **Qtde de dias a partir da execução do processo**: 30

Data calculada para ser considerado como data final do processamento: 16/10/2022 

**Observação:**

Ao realizar o processo o sistema irá verificar os funcionários que tenham férias em dobro à vencer dentro do período de 16/09/2022 á 16/10/2022.

**Aprovar  Férias**: Ao marcar esse parâmetro, o sistema irá verificar férias sugeridas para os funcionários que estejam com o status '**Aguardando aprovação do Gestor**' e '**Aguardando aprovação do DP**' e que atendam as regras de marcação de férias compulsórias passando-as para o status '**Marcadas**'.

**1ª parcela de 13º Salário**: Esse parâmetro será utilizado para pagamento de 1ª parcela de 13º Salário, junto com as férias marcadas para os funcionários que atendam as regras de marcação de férias compulsórias.

5. Verifique a tela dos Parâmetros da Coligada:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15820958683799)

**Funcionamento dos parâmetros que existem de forma global e por coligada:**

**Quebra de seção e seleção de funcionários**: sendo que a seleção de funcionários para funcionários específicos somente será possível pelos parâmetros da coligada.

**Qtde de dias a partir da execução do processo:** Quantidade de dias para ser considerado como data final a ser calculada de acordo com a data de processamento.

**Exemplo:**

Data de processamento: 16/09/2022

Quantidade de dias informado no parâmetro **Qtde de dias a partir da execução do processo**: 30

Data calculada para ser considerado como data final do processamento: 16/10/2022

**Observação:**

Ao realizar o processo o sistema irá verificar os funcionários que tenham férias em dobro à vencer dentro do período de 16/09/2022 á 16/10/2022.

**Aprovar  Férias**: Ao marcar esse parâmetro, o sistema irá verificar férias sugeridas para os funcionários que estejam com o status '**Aguardando aprovação do Gestor**' e '**Aguardando aprovação do DP**' e que atendam as regras de marcação de férias compulsórias passando-as para o status '**Marcadas**'.

**1ª parcela de 13º Salário**: Esse parâmetro será utilizado para pagamento de 1ª parcela de 13º Salário, junto com as férias marcadas para os funcionários que atendam as regras de marcação de férias compulsórias.

6. Tela para fracionamento de jobs e agendamento de processos

Para utilizar o fracionamento de jobs e agendamento de processos deverá ser criado:

7. Em**Ambiente | Segurança de Jobs Fracionáveis**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15822011130135)

8. Definir um **Perfil**e **Classe de Job** para que a parametrização seja realizada com sucesso. Será necessário definir qual o perfil irá possuir autorização para executar o processo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15822059408279)

**Observação:** Deverá ser selecionada em**Classe de Job** a classe de processo ‘**FopMarcarFeriasCompulsóriasProcess**’.

9. Em **Férias | Processos | Marcar Férias Compulsórias**, será apresentado a opção o quadro de “**Escalabilidade**”, onde será possível visualizar a quantidade de fracionamentos do processo e definir a periodicidade de execução do processo de acordo com a necessidade:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15822082837783)

10. Após realizar a parametrização e executar o processo de Marcar Férias Compulsórias, serão criados os Jobs em **Ambiente | Gerenciamento de Jobs**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15822148974103)

**Observação:** Neste módulo, serão apresentados os Jobs referentes a execução do processo.

**Exemplo: No quadro abaixo, o processo foi executado em 01 (um) Jobs:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15822146580247)

11. Exemplos:

Considerando os funcionários abaixo com as data inicio e fim do período aquisitivo aberto e a data de limite para inicio de gozo de férias. Conforme as validações da legislação, onde deve considerar o período mínimo de aviso de férias de 30 dias antes do gozo, inicio da férias não podendo ser em dia de descanso ou feriado ou até dois dias antes destes e data de pagamento até dois dias uteis antes do início de gozo de férias, para estes funcionários, as férias devem ser marcadas nas datas:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15833868395927)

Executando o processo de marcar as férias compulsórias no dia 31/10/2022, com a quantidade de dias a partir da execução do processo = 67, será considerado todos os funcionário onde a data do fim do período aquisitivo é anterior data da execução - 1 ano + a quantidade de dias a parti da da execução (31/10/2022 - 365 + 67) ou seja funcionários com período aquisitivo aberto onde a data fim é igual ou anterior 06/01/2022. A data de referência será 06/01/2023, ou seja, irá marcar para funcionários onde a data limite de inicio de gozo de férias, data de aviso de gozo de férias e data de pagamento de férias está entre dia 31/10/2022 a 06/01/2023:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15833863067543)

Executando o processo de marcar férias compulsórias no dia 01/02/2022 com a mesma quantidade de 67 dias, será considerado a data final do período aquisitivo em aberto até 07/01/2022. A data de referência será 07/01/2023 ou seja, irá marcar para funcionários onde a data limite de inicio de gozo de férias, data de aviso de gozo de férias e data de pagamento de férias está entre dia 01/11/2022 a 07/01/2023:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15833913558423)

Executando o processo de marcar férias compulsórias no dia 02/02/2022 com a mesma quantidade de 67 dias, será considerado a data final do período aquisitivo em aberto até 08/01/2022. A data de referência será 08/01/2023 ou seja, irá marcar para funcionários onde a data limite de inicio de gozo de férias, data de aviso de gozo de férias e data de pagamento de férias está entre dia 02/11/2022 a 08/01/2023:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15834002621847)

**Serão apresentados os logs, conforme abaixo:**

Parâmetros:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15822285372567)

Log quando as férias forem marcadas:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15822288074647)

Log quando a data de aviso de férias é anterior a data da execução:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15822305039511)

Quando o funcionário é elegível ao processo de marcação de férias compulsórias, mas já tem férias marcadas:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15822358035735)

Funcionário com período aquisitivo aberto, porém as férias estão na situação pagas:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15822391531415)

Funcionário com afastamento cadastrado sem data de retorno, com período aquisitivo em aberto:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15822346966039)

**Saiba Mais**

**[RH - RM - FOP - Férias: Lançamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007913092-RH-RM-FOP-F%C3%A9rias-Lan%C3%A7amento)**
