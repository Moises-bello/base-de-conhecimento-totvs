---
content_hash: b9126ea4d04fa23a98b8ff4ed8f1d7779e3ef26529badd0003392124e8985231
fetched_at: '2026-06-29T00:09:15.545285+00:00'
page_id: '421385408'
product: rm
source: tdn-rm
title: Importar Calendário de Atividades via Excel
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385408
version: 15
---

---

Nesta tela é possível que o usuário personalize informações referentes ao número de horas produtivas em uma determinada tarefa, esta opção esta disponível em Cadastros | Planilhas | Atividades | Funções Principais | Outros | Calendário de Atividade.

Para visualização correta do calendário é necessária a seleção da tarefa no momento da abertura do calendário de atividade.

Na tela do Calendário da Atividade temos as abas **Geral, Equipamento, Mão-de-Obra e Transporte** e para todas estão disponíveis os botões "Preencher valores default", "Calcular", "Copiar calendário para" e "Importar Calendário via Excel".

**1) Preencher valores default:**

Esse botão busca as informações básicas definidas no calendário do projeto, que são:

* Números de dias;
* Parâmetros do projeto;
* Número de horas por turno.

**2) Calcular:**

Esse botão fará o cálculo do número de horas produtivas da atividade período a período.

Os usuários ainda podem indicar o "número de dias parados", ou seja, mesmo que o período tenha um determinado "número de dias**"** pelo calendário padrão, alguns dias desse período não serão produtivos.

Pode-se determinar o "número de turnos para o período" e ainda um "fator de correção", que indicará o quanto será produtivo o número de dias que temos no calendário da atividade. Com estas informações será feito o cálculo do número de horas produtivas para o período.

O campo "Quantidade de Horas Produtivas" pode ser informado ou calculado através da fórmula de dias trabalháveis:

=((Número de dias - Número de dias parado) \* Número de horas do turno \* Número de turnos\*Fator de Correção / 100).

O campo "Número de horas do turno" pode ser definido pelo usuário.

**3) Copiar calendário para:**

Com esta opção é possível copiar o calendário da tarefa selecionada para outras tarefas.

**4) Importar Calendário via Excel:**

A importação de Calendário via Excel consiste em incluir informações referente ao número de horas produtivas em determinada tarefa de uma forma simplificada. Está localizada no menu de importações do projeto.

Para executar o Processo deve-se preencher os seguintes campos:

* **Arquivo:** Local onde o arquivo a ser importado se encontra;
* **Linha inicial:** Linha inicial do Excel que o processo irá utiliza para início da leitura dos dados, sendo que, não é um campo obrigatório e caso não haja o preenchimento o sistema utiliza como padrão a linha 1 (um).
* **Planilha:**Planilha onde será importado o calendário;
* **Código da Tarefa:** Coluna onde se encontra o código da Tarefa;
* **Código do Campo:** Coluna onde se encontra o código referente ao campo a ser importado, estes campos serão fixos de acordo com o calendário. Ex. A, B, C etc..;
  + **A -**Número de dias;
  + **B -**Número de dias parados;
  + **C -**Número de horas do turno;
  + **D -**Número de Turnos;
  + **E -**Fator de Correção (%);
  + **F -**Qtde. Horas Produtivas;
* **Início dos Lançamentos:** Coluna onde se encontra os dados dos Lançamentos a serem importados;
* **Período:** Coluna onde se encontra os dados dos Períodos que irão ser importados os dados, sendo que, não é um campo obrigatório e caso não haja o preenchimento o sistema utiliza como padrão a coluna 1 (um).
* **Destino dos dados importados:**Destino do calendário importado;
* **Sobrepor Calendário Existente:**Sobrepor o calendário já existente no projeto para as tarefas.
* **Utilizar Calendário Default:**Utilizar calendário default
* **Calcular Calendário:**Calcula o calendário, este processo pode substituir lançamentos da Quantidade de Horas Produtivas pois o mesmo é um campo calculados

O Excel a ser importado deve seguir o seguinte padrão:

* Deve conter uma coluna para as tarefas das quais será importado os lançamentos;
* Uma coluna informando o Código do Campo que será importado os lançamentos sendo que sua descrição não se faz obrigatória;
* Período a ser informado;
* Preenchimento dos lançamentos;

* Caso já exista no calendário lançamento no período que será importado o mesmo será substituído;
* Caso o usuário deseja limpar um campo no calendário, basta deixar o mesmo em branco no Excel;
* O Número de dias parados não pode ser maior que o Número de Dias;
* Caso não for informado Fator Correção (%) e a Qtde. Horas Produtivas estiver informada no excel, o valor do fator será calculado automaticamente. Se o fator estiver informado o valor que será importado será o valor informado no excel.

**Preenchimento do calendário default**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Número de dias | Número de dias parado | Número de horas do turno | Número de turnos | Fator de Correção (%) | Quantidade Horas Produtivas |
| O número de dias do calendário adotado para o projeto, considerando a parametrização definida no projeto (Trabalho aos sábados, Trabalho aos Domingos e Trabalho aos Feriados). Se não existir um calendário para o projeto, o sistema considerará os períodos do cronograma, considerando a mesma parametrização. | Em branco. | Jornada de trabalho definida nos parâmetros do projeto. Se não existir essa parametrização valor será 0(zero). | 1(um). | Em branco. | Em branco. |

Ainda temos a "Atualização Múltipla" que possibilita atualizar os valores das atividades que estiverem selecionadas, estes valores podem ser definidos pelo usuário.

**Atenção:**  
Utilize o filtro por período para que os defaults e a atualização múltipla sejam aplicados apenas para os períodos filtrados. Tomando este atitude, apenas os períodos selecionados serão atualizados.  
Utilize a atualização múltipla para preencher o campo selecionado, para vários períodos, com valor informado.

**Observação:**  
Na Alocação de Recursos em Opções | Alocação de Recursos, ao aplicar o calendário de tarefas, será considerado o Grupo DNIT do recurso associado à tarefa, ou seja, se o recurso estiver associado aos Grupos DNIT Equipamento, Mão de Obra ou Transporte, os respectivos calendários serão aplicados.   
Caso o calendário referente ao Grupo DNIT associado ao recurso não esteja preenchido, será aplicado o calendário Geral.
