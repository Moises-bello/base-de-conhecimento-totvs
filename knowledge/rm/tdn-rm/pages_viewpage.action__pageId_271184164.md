---
content_hash: bc357b6fffa79a43ebc73f70211eeb664c79e675e2be77613f2c275c1fb6f38a
fetched_at: '2026-06-29T00:08:26.592848+00:00'
page_id: '271184164'
product: rm
source: tdn-rm
title: DT Rateio Contábil da folha do professor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271184164
version: 119
---

# 

---

# Rateio Contábil da folha do professor pelas entidades Item contábil e Classe de valor

|  |  |  |  |
| --- | --- | --- | --- |
| **Linha de Produto:** | RM | | |
| **Segmento Executor:** | C&P, Educacional | | |
| **Módulo:** | TOTVS Educacional, TOTVS Automação de Ponto, TOTVS Folha de Pagamento, TOTVS Protheus. | | |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Gerar plano de aula | Gerar plano de aula | | Importar horário professor | Importar horário professor | | Lançar para Folha de Pagamento | Lançar para Folha de Pagamento | | Agrupamento Salarial | Agrupamento Salarial | | Associação de Eventos | Associação de Eventos | | Reprogramação Salarial | Reprogramação Salarial | | "Lançar" Grupo de eventos | "Lançar" Grupo de eventos | | Geração dos Lançamentos (Contabilização) | Geração dos Lançamentos (Contabilização) | | Geração dos Lançamentos (Financeiro) | Geração dos Lançamentos (Financeiro) | | | |
| **Requisito (ISSUE):** | [RHFOP001-589](http://jiraproducao.totvs.com.br/browse/RHFOP001-589) e [RHFOP001-652](http://jiraproducao.totvs.com.br/browse/RHFOP001-652) | | |
| **País:** | (X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

---

### **Contexto de negócio**

      A implementação foi realizada com o intuito de aprimorar o rateio contábil das aulas dos professores originadas do Educacional. Os rateios contábeis em versões anteriores eram rateados até o nível de Centro de custo.  A partir da versão 12.1.15 o rateio será realizado também pelas entidades “Item Contábil” e “Classe de Valor”.

# **Sistemas Envolvidos**

* + - **Totvs RM Educacional:**Após a implementação realizada, o módulo Educacional passará a permitir que seja parametrizado o rateio contábil das aulas dos professores também por Item Contábil e Classe de valor.
    - **Totvs RM Automação do Ponto:** O produto Automação do Ponto terá como objetivo realizar o cálculo de todos os eventos a serem pagos e/ou descontados do funcionário/professor, porém esses eventos passarão a ser calculados por rateio contábil, de acordo com a configuração feita dentro do Educacional. No momento da importação do horário do professor, será preechida a tabela AINTERVALOPLANEJADOFUNRATEIO.
    - **Totvs RM Folha de Pagamento:** O sistema Folha de Pagamento irá receber os eventos calculados pelo Automação do Ponto e gerados pela “Reprogramação Salarial”, ambos rateados, realizando assim o pagamento dos valores a pagar e descontar com Rateio Contábil, além de enviar para o Protheus os Lançamentos Financeiros e Contabilização também com Rateio Contábil.
    - **Totvs Protheus :**O sistema Protheus  irá receber os lançamentos contábeis gerados pela Folha RM,  rateados por centro de custo, Item contábil e classe de valor.

### **Apresentação do fluxo da integração**

### **Detalhamento do Fluxo de trabalho**

# **Educacional**

##### Parametrizar o rateio contábil

Para que o Educacional repasse as informações das aulas lecionadas pelo professor rateadas, será necessário realizar as seguintes parametrização:

Dentro dos parâmetros do Educacional (Configurações | Parâmetros), acesse a etapa Integrações | Protheus e marque os campos “Financeiro” e “Contabilidade” que se encontram no quadrante “Módulos Integrados”.

Caminho: Educacional | Configurações | Parâmetros | Integrações | Protheus

Ainda nos parâmetros do Educacional, deverá se atentar aos seguintes itens:

1. Será necessário predefinir de qual cadastro será buscado o Centro de Custo, Item Contábil e Classe de Valor.
2. Parâmetros necessários para que o pagamento dos professores executados pela rotina de “Reprogramação Salarial” seja rateado por centro de Custo, Classe de Valor e Item Contábil.

##### Cadastrar as informações de acordo com a nova parametrização

Após as parametrizações feitas acima, passará a ser necessário preencher os campos Centro de Custo, Item Contábil e Classe de Valor de acordo com o que foi selecionado.

Apresentação dos campos no cadastro das Turmas:

A apresentação dos campos no cadastro da Matriz Aplicada se encontrará em lugares diferentes, sendo eles:

Centro de custo:

Item Contábil e Classe de Valor:

##### Criação do plano de aula do professor

      A criação do Plano de Aula é essencial para a integração, o processo irá criar toda a “grade de horário” em que o Professor terá que lecionar suas disciplinas, contendo o horário de início e fim de suas aulas, a rotina irá levar em consideração os horários criados e vinculados a turma/disciplina.

Obs.: Apenas com o Plano de Aula montado, será possível avançar nas etapas do fluxo.

# Automação do Ponto

##### Importação do horário do professor considerando Rateio Contábil

Para trazermos as informações criadas no Educacional para o Totvs Automação de Ponto, será necessário executar o processo “Importar Horário do Professor”, a partir da execução desse processo, será montado o horário do professor de acordo com o “Plano de Aula”.

Após a importação do horário do professor, poderá acessar o horário planejado do funcionário/professor através do caminho Automação do Ponto | Funcionários | Anexos | Movimento do Ponto | Espelho | Visualizar Horário, conforme print abaixo.

Obs.: A execução do processo de importação do horário do professor irá popular a tabela AINTERVALOPLANEJADOFUNRATEIO

##### Calcular o espelho ponto do professor de acordo com a parametrização, para geração das ocorrências/eventos rateados

      Ao executar o processo de “Recalculo” do espelho, o sistema poderá levar em consideração para o cálculo das ocorrências/eventos as seguintes informações:

* + - * + - Para os professores que **utilizam o Livro de Ponto**, será considerado as faltas apontadas no Educacional, gerando assim os eventos de desconto (Falta) e a pagar (Adicional Noturno), caso o professor trabalhe em horário noturno.

* + - * + - Para os professores que **utilizam o REP (Ponto Eletrônico)**, será levado em consideração as batidas/marcações realizadas no REP x Horário Planejado (Plano de Aula), gerando assim as ocorrências/eventos que se encontram parametrizados no Sindicato do funcionário/professor.

      Obs.: Caso seja configurado dentro do sindicato o evento do tipo “Horas trabalhadas”, fique ciente de que o Totvs Automação de Ponto não irá fazer a separação dessas horas de acordo com a disciplina lecionada, ou seja, será pago todas as horas calculadas em cima de um único valor. Para pagar as horas trabalhadas separadas por disciplina, deverá seguir o fluxo passando pela rotina de “Reprogramação Salarial” do Totvs Folha de Pagamento.

      Além da criação das ocorrências, as mesmas passarão a ser separadas de acordo com o centro de custo, item contábil e classe de valor parametrizado no Educacional para o horário em que foi lecionado a aula. Para entendermos o que foi dito anteriormente, foi feito a vinculação de um determinado professor a 2 turmas diferentes, onde cada uma possui “Centro de Custo”, “Item Contábil” e “Classe de Valor” distintos.

      O comportamento também será o mesmo para as ocorrências do tipo Adicional Noturno e atraso.

      Os eventos gerados também se encontrarão separados por CC, IC e CV de acordo com as ocorrências.

##### Lançamento dos eventos para a Folha de Pagamento

      Para que possamos enviar para a Folha de Pagamento os eventos calculados a serem pagos ou descontados do funcionário, será necessário executar o processo “Lançar para Folha de Pagamento.

Caminho: Automação do Ponto| Movimento | Lançar para a Folha de Pagamento.

Obs.: O processo irá enviar ao Totvs Folha de pagamento, para a tabela de “Movimentação Temporária”, apenas os eventos que se encontram calculados na aba “Movimento” dentro do espelho do Professor.

# Folha de Pagamento

##### Parametrizar o sistema para recebimento do rateio contábil

      Para que o módulo Folha de Pagamento consiga processar as informações que lhe serão enviadas, trabalhando assim com o rateio contábil dos valores, será necessário aplicar as parametrizações a seguir. Deverá ser feito a marcação do parâmetro “Utiliza Cálculo por Centro de Custo”, o mesmo se encontra dentro dos Parâmetros | Folha Normal | Etapa 1 – Cálculo.

      Na Etapa 11 | Contabilização, poderá ser marcado os parâmetros “Agrupa partidas contábeis por: ‘Item Contábil’ e ‘Classe de Valor’”.

      Marcando o parâmetro “Gerar rateio contábil com base na movimentação de ensino e movimento temporário”, o rateio dos eventos por centro de custo, item contábil e classe de valor será calculado verificando os parâmetros “Segue rateio movimento temporário” e “Segue rateio movimento ensino” presente no cadastro de eventos.

Obs: Este parâmetro ficará visível somente se a integração com outros BackOffices estiver ativa e se o Labore estiver integrado com o Educacional e/ou Totvs Automação de Ponto.

      Na Etapa 12 | Lancto Financeiro, poderá ser marcado os parâmetros “Gerar lançamentos rateados por: ‘Item Contábil’ e ‘Classe de Valor’”.

      Ainda no “Parametrizador” do Labore, terá que ser habilitado a integração com “Outros BackOffice” pelo caminho Parâmetros | Integrações | Outros BackOffice.

      Será necessário também realizar a parametrização dos eventos que serão considerados para o lançamento contábil e financeiro da folha de pagamento do professor, predefinindo assim de onde será buscado as informações (CC, CV, IC).

* Caso seja marcado o parâmetro “Segue rateio movimento temporário”, as informações serão buscadas da tabela PFMOVTEMP.

* Caso seja marcado o parâmetro “Segue rateio movimento de ensino”, as informações serão buscadas da tabela PFMOVENSINO.

* Caso não seja marcado nenhum parâmetro, o sistema buscará o centro de custo da tabela PFMOVCC. Para o item contábil e classe de valor, será buscado no cadastro do funcionário, aba Dados contábeis. Na ausência de preenchimento desses dados no funcionário, irá verificar no agrupamento contábil do evento, e por fim no cadastro de seção do funcionário.  
  Obs: Para a última opção, no caso do lançamento financeiro o sistema irá trazer somente o centro de custo.

* A possibilidade de vinculação do “Código do Rateio que o Evento Segue” foi adequado para que a rotina de Contabilização verifique dentro da ”Composição do Rateio” os eventos associados e de onde será buscado as informações (PFMOVTEMP, PFMOVENSINO ou PCMOVCC) para o rateio e lançamento do item contábil, classe de valor e centro de custo.

**Exemplo de utilização dos parâmetros pelo processo de Contabilização.**

* Quando marcado o parâmetro “segue rateio movimento temporário”

O evento editado irá buscar o Centro de Custo, Item Contábil e Classe de Valor do evento lançado na tabela PFMOVTEMP.

| Evento | Descrição | Hora | Valor |
| --- | --- | --- | --- |
| 0002 | Horas Aulas | 40,00 | 2000,00 |
| 0150 | Atividade extra classe | 10,00 | 250,00 |

Movimento temporário (PFMOVTEMP)

| Evento | Descrição | Hora | CC | IC | CV | Valor |
| --- | --- | --- | --- | --- | --- | --- |
| 0002 | Horas Aulas | 40,00 | 01.01 | 1 | 1 | 1500,00 |
| 0002 | Horas Aulas | 40,00 | 01.01 | 2 | 1 | 500,00 |
| 0150 | Atividade extra classe | 10,00 | 01.02 | 1 | 1 | 250,00 |
| Total | | | | | | 2250,00 |

Ao gerar o lançamento contábil do evento 0002 será selecionado somente as suas entidades contábeis (CC,I C, CV),  gerando assim 2 partidas contábeis rateadas conforme abaixo:

| Conta contábil | CC | IC | CV | Valor |
| --- | --- | --- | --- | --- |
| Salário a pagar | 01.01 | 1 | 1 | 1500,00 |
| Salário a pagar | 01.01 | 2 | 1 | 500,00 |
| Total | | | | 2000,00 |

* + - * + Quando informado um rateio que o evento segue

| Código do rateio | Eventos do rateio |
| --- | --- |
| 1 | | Evento | Descrição | | --- | --- | | 0002 | Horas Aulas | | 0150 | Atividade extra classe | |

Evento 1000 - DSR professor calculado por fórmula configurado para seguir o rateio de evento com código 1.

Valor pago no envelope =  375,00

Seguindo o exemplo da movimentação temporária acima, ao gerar o lançamento contábil do evento 1000 será selecionado as entidades contábeis (CC, IC, CV) dos eventos 0002 e 0150, realizando uma proporção de valor conforme o rateio.

| Evento | Descrição | CC | IC | CV | Calculo/Valor |
| --- | --- | --- | --- | --- | --- |
| 0002 | Horas Aulas | 01.01 | 1 | 1 | (375,00 / 2250,00) \* 1500,00 = 250,00 |
| 0002 | Horas Aulas | 01.01 | 2 | 1 | (375,00 / 2250,00) \* 500,00 = 83,33 |
| 0150 | Atividade extra classe | 01.02 | 1 | 1 | (375,00 / 2250,00) \* 250,00 = 41,67 |
| Total | | | | | 375,00 |

| Conta contábil | CC | IC | CV | Valor |
| --- | --- | --- | --- | --- |
| Salário a pagar | 01.01 | 1 | 1 | 250,00 |
| Salário a pagar | 01.01 | 2 | 1 | 83,33 |
| Salário a pagar | 01.02 | 1 | 1 | 41,67 |
| Total | | | | 375,00 |

Obs.: O cálculo acima também é valido para quando for utilizado "Segue rateio Movimento de Ensino" (PFMOVENSINO).

##### Associação de eventos as possíveis turmas

Além das configurações realizadas nos Parâmetros da Folha de Pagamento, deverá fazer a associação dos eventos abaixo.

* + - **Associação de evento Falta e Salário**

      Foi implementado no módulo Folha de Pagamento a possibilidade de realizar a vinculação de eventos do tipo Falta para a Disciplina, permitindo assim que cada disciplina gere evento de falta diferente para desconto no envelope de pagamento do funcionário/professor, o mesmo comportamento se aplica para eventos do tipo Salário.

* + - **Associação de evento Disciplinas/Atividade Extra**

      De acordo com o parâmetro “Utiliza agrupamento salarial por disciplina” que se encontra dentro dos Parâmetros do Labore, será apresentado o menu Disciplinas ou Atividade Extra (Grupo de Atividade).

Caminho: Configurações |Parâmetros |Integrações |Educacional | Etapa 1 - Configurações Gerais.

      Para que a rotina de Reprogramação Salarial faça a “criação” dos eventos do tipo “Trabalho” corretamente, deverá ser associado as disciplinas/atividade extras os eventos referentes a cada item existente na listagem.

* + - * + - Disciplinas

* + - * + - Associação de eventos Atividades extra

##### Reprogramação Salarial dos eventos tipo Salarial

      Para que seja gerado os valores a serem pagos referente as **horas aulas trabalhadas** pelo professor referente a cada **disciplina**, deverá executar a rotina de Reprogramação Salarial.

Obs.: Caso opte pelo cálculo das horas trabalhadas pelo RM Totvs Automação de Ponto, lembre-se de que as mesmas serão pagas em cima de um único valor, ou seja, não será pago sobre as horas os valores respectivos de cada disciplina.

O processo irá realizar uma operação aritmética entre 3 itens, sendo eles:

* + - * **Fator Mensal:** Valor predefino dentro dos parâmetros do Totvs Folha de Pagamento no caminho Folha de Pagamento | Integrações | Gestão Educacional | Etapa 1 – Configurações Gerais.
      * **Quantidade de Aulas:** Será retornado pelo Educacional de acordo com o plano de aula existente para o professor ou pelo preenchimento do campo “Quantidade de aulas semanais” no momento da vinculação do mesmo a turma/disciplina.
      * **Valor Hora/Aula:** O valor hora/aula é enviado pelo Educacional de acordo com o valor preenchido na vinculação do Professor com a Turma/Disciplina.

      A operação aritmética consiste na multiplicação da “Quantidade de Aulas” pelo “Fator Mensal” e em seguida será multiplicado o resultado pelo “Valor Hora/Aula”, onde resultará no salário do professor.

Obs.:  Os valores gerados pela “Reprogramação Salarial” serão armazenados na tabela “PFMOVENSINO”

##### Recebimento dos eventos enviados pelo Automação do Ponto

      Os eventos que foram calculados e enviados pelo Automação do Ponto serão armazenados (Tabela temporária PFMOVTEMP), separado por CC, IC e CV até que sejam lançados ao Envelope.

Caminho: Folha de Pagamento | Folha Mensal | Consulta | Consulta Movimento da Integração

##### Lançamento dos eventos recebidos pelo Automação do Ponto e calculados pela Reprogramação Salarial para o evenlope

      Agora que os eventos já se encontram pendentes dentro do Folha de Pagamento, será necessário realizar o envio desses valores (Eventos a pagar/descontar) ao envelope dos professores, para isso deverá ser executado o processo de Lançamento através do menu “Lançamentos | Grupos de Eventos”, onde será buscado os eventos presentes na tabela temporária citada acima.

      No momento da execução do processo, deverá se atentar aos seguintes itens:

1. Para que a rotina de lançamento ao envelope envie também o salário composto calculado pela “Reprogramação Salarial”, deverá marcar o campo “Lançar Salário Composto”.
2. Os eventos que foram enviados pelo Totvs Automação de Ponto (Automação do Ponto) serão considerados para lançamento apenas se o campo “Lançar eventos da integração com outros aplicativos” estiver marcado.

Caminho:  Folha de Pagamento | Folha Mensal | Lançamentos | Grupo de Eventos.

Caso a folha esteja parametrizada para lançar por centro de custo deverá utilizar o módulo “Lançamento por Centro de Custo"

Para o botão ficar habilitado, deve verificar a seguinte parametrização

O sistema deve estar integrado:

A opção 'Usa salário hora/jornada fixa' deve estar desmarcada

A opção 'Reprogramação salarial detalhada por centro de custo' deve estar marcada

##### Gerar/Enviar Contabilização com rateio contábil

      Para realizar a contabilização execute a rotina “Geração dos Lançamentos”, o processo irá buscar os eventos presentes no envelope do funcionário, verificando em cada um deles qual foi a parametrização aplicada, ou seja, de onde será buscado as informações (as tabelas a serem consideradas são: PFMOVTEMP, PFMOVENSINO ou PCMOVCC) para o rateio e lançamento do item contábil, classe de valor e centro de custo.

      Conforme pode ser visto, as informações presentes estão sendo separadas por CC, IC e CV. Para que essas informações sejam enviadas para o Protheus, deverá ser executado o processo “Integração financeira com outros BackOffices”

      **Atenção:** A Geração do lote contábil para envio a outros backoffices deverá ser executado por filial, ou seja, cada filial deverá ter um lote contábil. Não será possível gerar um lote para toda a empresa devido ao volume de partidas contábeis, comprometendo assim o desempenho da integração.

 

##### Gerar/Enviar Lançamento com rateio contábil

      Em Recursos Humanos | Folha de Pagamento| Encargos | Cadastros Financeiros | Parâmetros, edite ou cadastre um novo registro, faça a vinculação do ‘Rateio que o lançamento Segue’ para que o “Lançamento Financeiro” verifique dentro da ”Composição do Rateio” os eventos associados e de onde será buscado as informações (PFMOVTEMP, PFMOVENSINO ou PCMOVCC) para o rateio e lançamento do item contábil, classe de valor e centro de custo.

      Para efetivar o lançamento financeiro execute o processo “Geração dos Lançamentos”.

      Conforme pode ser visto, as informações presentes estão sendo separadas por CC, IC e CV. Para que essas informações sejam enviadas para o Protheus, deverá ser executado o processo “Integração financeira com outros Backoffices”.

      Obs.: O processo de lançamento financeiro ao TOTVS Protheus levará em consideração apenas o Centro de Custo.

divs
