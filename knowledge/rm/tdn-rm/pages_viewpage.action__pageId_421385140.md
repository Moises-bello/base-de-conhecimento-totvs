---
content_hash: 7493d0acef067e06ba97d9c862d104ccb052078a0881c3dfee09ded549e576d2
fetched_at: '2026-06-29T00:09:14.153900+00:00'
page_id: '421385140'
product: rm
source: tdn-rm
title: Alocação de Recursos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385140
version: 13
---

---

A funcionalidade alocação de recursos permite alocar recursos de insumos para tarefas que possuem associação com insumos ou composições, e que ainda possuem um cronograma previsto. Desse modo definindo quais funcionários ou bens estarão alocados em determinada tarefa em uma determinada data é possível prover um melhor planejamento da obra. Assim é possível saber onde podem ser ajustadas as tarefas para um melhor aproveitamento dos recursos disponíveis e quando não for possível se é necessário realizar novas contratações de funcionários, compra ou aluguel de bens.

Os insumos que podem ser alocados são aqueles que pertencem aos grupos DNIT:  
Grupo DNIT A - Equipamento;  
Grupo DNIT B - Mão-de-obra;   
Grupo DNIT F - Transporte.

**PRINCIPAIS RECURSOS DA FUNCIONALIDADE:**

Abaixo veremos uma explicação geral dos principais recursos da funcionalidade "Alocação de Recursos".

**GRID DA ALOCAÇÃO DE RECURSOS:**

Através do grid da alocação de recursos você pode realizar a maior parte das ações da alocação de recursos. Ele pode ser acessado de duas maneiras diferentes:  
Pela planilha de atividades: Clicar em uma célula da planilha de atividades (manter linha em foco) > "Anexos" > "Alocação de Recursos" > "Alocação de Recursos – Previsto e Alocado".  
Pelo menu opções: Clicar no item "Alocação de Recursos" > "Previsto e Alocado".

**CÁLCULO DA QUANTIDADE PREVISTA NA ALOCAÇÃO DE RECURSOS:**

Através do cálculo da alocação de recursos o sistema informa a quantidade de recursos necessária e o total de horas destes recursos por período do cronograma. O resultado desse cálculo fica visível nas coluna "Previsto" referente a cada insumo da tarefa no grid da alocação de recursos e serve como referência para a correta alocação dos recursos nos períodos.

Após o cálculo é importante arredondar a quantidade de recursos, pois o cálculo geralmente calcula valores não inteiros. Então para fazer o processo deve se seguir os seguintes passos:

Calcular alocação de recursos: Clicar com o botão direito dentro do grid da alocação de recursos para acessar o menu de contexto > "Calcular Alocação de Recursos" > "Sim".

Arredondar alocação de recursos: Clicar com o botão direito dentro do grid da alocação de recursos para acessar o menu de contexto > "Arredondar Alocação de Recursos" > "Sim".

**ALOCAÇÃO DE RECURSOS:**

**Observações:** 

A alocação de recursos permite definir horas diferenciadas para cada recurso, associado a um insumo;

Quando os valores de "Quantidade" e "Horas" forem apresentados de forma igual, inferior ou superior ao previsto para a alocação, os mesmos serão identificados nas cores preta, vermelha ou verde, respectivamente.  
Para alocar recursos é necessário seguir os seguintes passos:

Acessar o popup da alocação de recursos: Acessar o menu de contexto > "Associar Recursos"; ou duplo click em uma célula do grid da alocação de recursos, célula relativa à Insumo X Alocado.

Selecionar recursos no popup: Clicar em algum recurso no grid do lado esquerdo > ">" para associar um recurso ou ">>" para todos os recursos.

Definir horas de alocação: Clicar nas células quantidade do popup > inserir a quantidade de horas desejadas para cada recurso.

Executar o processo: Selecionar (ou não) o checkbox "Aplicar alocação atual em todos os períodos" > "Executar".

**LIMPAR ALOCAÇÃO DE RECURSOS:**

Através deste processo é possível limpar os valores de alocação prevista para uma tarefa. Para realizar o processo é necessário seguir os seguintes passos:

Limpar alocação de recursos: Acessar o menu de contexto > "Limpar Alocação de Recursos".

**CALENDÁRIO DE RECURSOS:**

Através do calendário de recursos é possível alterar as variáveis das quais é calculada a quantidade da equipe. Para isso é necessário seguir os seguintes passos:

Acessar calendário de recursos: Acessar menu de contexto > "Exibir Calendário de Recursos"; ou duplo click na célula do grid da alocação de recursos onde está a descrição do recurso.

Alterar valores dos campos: Clicar nas células do calendário de recursos e alterar os valores para adequar à realidade de seu projeto.

Através do preenchimento dos valores defaults ,  a Qtde. Horas Necessárias é preenchida, onde esse valor é calculado utilizando as quantidades produtiva e improdutiva calculadas e existentes na curva ABC de insumos. Essas quantidades podem sofrer influências dos coeficientes produtivo e improdutivo do recurso do tipo equipamento pertencente à uma composição por produção, da produção horária da composição e do percentual de improdutividade definido no próprio insumo. Para que as horas totais do insumo sejam consideradas é necessário que o parâmetro de projeto\PERT/Alocação de Recursos "Desconsiderar improdutividade no calendário de recurso. (Quantidades Produtiva e Improdutiva da curva ABC))" seja marcado.

Abaixo dois exemplos de como o cálculo é feito:

* Composição por produção com equipamento:
  + Tarefa: 001.01.01 - Pavimentação: Quantidade: 100
    - Composição: CMP001 - Pavimento de concreto: ; Produção: 0,5
      * Recurso: ISM001 - Caminhão: Quantidade: 1; Improdutividade: 20%; Coef. Produtivo: 0,8; Coef. Improdutivo: 0,2
      * ABC: Qtde. Produtiva = ((1 x 0,8) x 100)  / 0,5 = 160; Qtde. Improdutiva = (((1 + (1 x (20 / 100))) x 0,2)  x 100) / 0,5 = 48
    - Cronograma Planejado: Período 1: 25%
  + Qtde. Horas Necessárias no Período 1:
    - Com o parâmetro marcado:
      * (160 + 48) x (25 / 100) = 52 horas
    - Sem o parâmetro marcado:
    * 160 x (25 / 100) = 40 horas

* Composição por produção com composição auxiliar CPU que contém equipamento:
  + Para composições por produção com composições auxiliares, é necessário que o recurso do tipo equipamento tenha as opções de Produtivo e Improdutivo marcados
  + Tarefa: 001.01.01 - Pavimentação: Quantidade: 100
    - Composição: CMP001 - Pavimento de concreto: Produção: 0,5
      * Recurso: CMP002 - Pavimento Auxiliar: Tipo: Equipamento; Coef. Produtivo: 0,7; Coef. Improdutivo: 0,3
        + Recurso: ISM001 - Caminhão: Quantidade: 1; Improdutividade: 20%; Flag Produtivo: Verdadeiro; Flag. Improdutivo: Verdadeiro
      * ABC: Qtde. Produtiva = ((1 x 0,7) x 100)  / 0,5 = 140; Qtde. Improdutiva = (((1 + (1 x (20 / 100))) x 0,3)  x 100) / 0,5 = 72
    - Cronograma Planejado: Período 1: 25%
  + Qtde. Horas Necessárias no Período 1:
    - Com o parâmetro marcado:
      * (140 + 72) x (25 / 100) = 53 horas
    - Sem o parâmetro marcado:
      * 140 x (25 / 100) = 35 horas

Calcular e arredondar quantidade da equipe: Clicar no botão "Calcular" > clicar no botão "Arredonda quantidade da equipe".

Salvar novos valores: Clicar no botão "Ok".

**CRONOGRAMA DE ALOCAÇÃO DE RECURSOS:**

Através do cronograma de alocação de recursos é possível visualizar as horas de alocação de cada recurso por período para a tarefa selecionada. Para isso é necessário seguir os seguintes passos:

Selecionar atividade: Clicar em uma célula da planilha de atividades (manter linha em foco).

Acessar o cronograma de alocação de recursos: Acessar o menu "Anexos" > "Alocação de Recursos" > "Cronograma de Alocação de Recursos (em horas)".

**REMOÇÃO DE RECURSOS ALOCADOS:**  
Através deste processo podemos remover rapidamente recursos associados a todas as tarefas. Para isso é necessário seguir os seguintes passos:

Acessar popup da remoção de recursos alocados: Planilha de atividades > "Processos" > "Alocação de Recursos" > "Remover Recursos Alocados".

Remover recursos alocados: Clicar no botão "Sim".

**REMOÇÃO DE RECURSOS NÃO UTILIZADOS:**

Através deste processo podemos remover rapidamente recursos associados a todas as tarefas onde o seu insumo correspondente não é mais necessário na tarefa, pois não está mais associado à tarefa ou à composição associada à tarefa. Para isso é necessário seguir os seguintes passos:

Acessar popup da remoção de recursos não utilizados: Planilha de atividades > "Processos" > "Alocação de Recursos" > "Remoção de Recursos Não Utilizados".

Remover recursos não utilizados: Clicar no botão "Executar".

**QUADRO DE PERMANÊNCIA:**

Através do quadro de permanência é possível visualizar o planejamento de alocação de mão-de-obra e equipamentos por período para cada insumo, deste modo obtém-se uma visão geral de recursos sub e super alocados, provendo uma melhor forma de planejamento. Para atualizar o quadro de permanência é necessário seguir os seguintes passos:

Acessar popup da exportação de recursos para o quadro de permanência no anexo de Alocação de Recursos ou Planilha de atividades > "Processos" > "Alocação de Recursos" > "Exportar Alocação para o Quadro de Permanência".

**Opções do processo:**

* Sobrescrever permanência existente pelos valores da alocação: Substitui todos os dados do Quadro pelos novos calculados
* Limpar permanência existente: Limpa todos os dados atuais do Quadro
* Calcular Alocação de Recursos
  + Agrupamento do Cálculo: São três opções para agrupamento do cálculo da alocação:
    - Insumo (Padrão): Considera toda a permanência calculada do insumo utilizada no projeto
    - Unidade de Serviço: Considera toda a permanência calculada do insumo utilizada no projeto porém agrupando por Unidade de Serviço associada à atividade
    - Local de Serviço: Considera toda a permanência calculada do insumo utilizada no projeto porém agrupando por Local de Serviço associado à atividade
  + Calendário Utilizado: Representa a partir de qual calendário os dados serão considerados para o cálculo
  + Limpar Alocação de Recursos: Limpa os dados calculados na Alocação de Recursos
  + Considerar Quantidade do Calendário quando preenchida: Somente disponível quando o Calendário Utilizado for o de Atividades. Permite não alterar a Quantidade de Horas Produtivas do Calendário de Atividades e consequentemente utiliza essa grandeza para o cálculo da alocação que será exportada para o quadro
  + Salvar Cálculo da Alocação: Somente disponível quando o Calendário Utilizado for o de Recursos. Salva os novos dados da Alocação de Recursos. Com essa opção desmarcada, a exportação será feita corretamente, porém a alocação não será salva
  + Calcular Projeto: Calcula o Projeto antes da exportação pois o cálculo da alocação utiliza dados dos insumos que estão associados às atividades

Exemplo de como funciona o Agrupamento do Cálculo:

* Insumo: X12345 - Ajudante

  | Atividade | Unidade de Serviço | Local de Serviço | Quantidade Período 1 | Quantidade Período 2 |
  | --- | --- | --- | --- | --- |
  | 001.01.01 - Escavação | 01 - Unidade Norte | 001 - Térreo | 10,00 | 5,00 |
  | 001.01.02 - Preparo | 01 - Unidade Norte | 002- Cobertura | 30,00 | 10,00 |
  | 001.01.03 - Assentamento |  |  | 25,00 | 15,00 |

  + Exibição no Quadro de Permanência:
    - Opção Insumo (Padrão) :

      | Insumo | Período 1 | Período 2 |
      | --- | --- | --- |
      | X12345 - Ajudante | 65,00 | 30,00 |
    - Opção Unidade de Serviço:

      | Insumo | Unidade de Serviço | Período 1 | Período 2 |
      | --- | --- | --- | --- |
      | X12345 - Ajudante |  | 25,00 | 15,00 |
      | X12345 - Ajudante | 01 - Unidade Norte | 40,00 | 15,00 |
    - Opção Local de Serviço:

      | Insumo | Unidade de Serviço | Local de Serviço | Período 1 | Período 2 |
      | --- | --- | --- | --- | --- |
      | X12345 - Ajudante |  |  | 25,00 | 15,00 |
      | X12345 - Ajudante | 01 - Unidade Norte | 001 - Térreo | 10,00 | 5,00 |
      | X12345 - Ajudante | 01 - Unidade Norte | 002- Cobertura | 30,00 | 10,00 |

Visualizar o quadro de permanência: Acessar o menu "Cadastros" > "Quadro de Permanência".

No quadro é possível visualizar os dados em diferentes formas, porém a disponibilidade vai depender da forma de agrupamento escolhida na exportação.

A edição dos valores somente será possível no nível máximo de detalhamento utilizado na exportação, respeitando o vínculo existente de Unidade ou Local de Serviços às atividades.

Veja Também

---
