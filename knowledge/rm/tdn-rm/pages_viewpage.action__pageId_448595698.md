---
content_hash: d79c50e9338e2713ba11cd3732ccd9939bbd1c360dcf9ef08cb52947f9256f43
fetched_at: '2026-06-29T00:09:55.605750+00:00'
page_id: '448595698'
product: rm
source: tdn-rm
title: DT Pacote de Serviços
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=448595698
version: 12
---

# PACOTE DE SERVIÇOS

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos.* |
| **Módulo:** | **Gestão de Obras e Projetos*.* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Folha Tarefa | Folha Tarefa | | Itens da Folha Tarefa | Itens da Folha Tarefa | |
| **Cadastros Iniciais:** | Projeto, Insumos, Funções, Equipe de Mobilidade, Tarefas |
| **Parâmetro(s):** | *Não se aplica.* |
| **Ponto de Entrada:** | *Não se aplica.* |
| **Tickets relacionados** | *Não se aplica.* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | [TOPORCAPLAN001-6000](http://jiraproducao.totvs.com.br/browse/TOPORCAPLAN001-6000) |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | **SQL Server e Oracle** |
| **Tabelas Utilizadas:** | *Não se aplica.* |
| **Sistema(s) Operacional(is):** | **Windows** |
| **Pacote:** | *Não se aplica.* |

## Descrição

Cadastro do Pacote de Serviço que tem como finalidade a definição de quais tarefas serão executadas por uma determinada equipe e qual o custo dessa equipe associada.

## Procedimento para Utilização

O cadastro do Pacote de Serviço é realizado no cadastro da Folha Tarefa, onde a mesma pode assumir dois tipos distintos, o tipo **"Padrão"**, que é o tipo já conhecido e utilizado no TOP Mobile, e o tipo **"Produtividade"**, que se refere ao pacote de serviços, e faz com que a Folha Tarefa assuma algumas características específicas:

* Ao selecionar o tipo da Folha Tarefa como Produtividade, além da Descrição e Tipo de Apontamento é necessário preencher a equipe do Pacote de Serviço;
* Não é necessário preencher a Periodicidade e Datas de Início e Fim, essas serão preenchidas automaticamente como **Personalizada**, **Data Inicial do Projeto** e **Data Final do Projeto** respectivamente;
* Anexos e Processos que não estão disponíveis para esse tipo de folha:
  + Programado X Alocado;e
  + Alocação de Mão de Obra;
  + Equipes Associadas à Folha Tarefa;
  + Recalcular Planejamento das Tarefas;
  + Alocar Mão de Obra na Folha Tarefa;
  + Copiar Folha Tarefa.
* **Itens da Folha Tarefa:**Para esse tipo de folha, a associação de Tarefas à mesma, deve obedecer algumas regras que não são consideradas no tipo de folha tarefa "Padrão":  
  + No lookup da tarefa é possível filtrar por Unidade de Serviço, Local de Serviço e/ou a Equipe no qual a Tarefa está associada;
  + As Tarefas que são exibidas são aquelas que ainda possuem saldo e que ainda não foram iniciadas, e uma tarefa considerada não iniciada deve ter as seguintes características:
    - Não ter sido apropriada;
    - Não ter realizado no cronograma;
    - Não ter medido no cronograma;
    - Não ter apontamento de folha tarefa;
    - Não estar em uma folha tarefa com status diferente de EM PROCESSAMENTO;
    - Não ter medição de contrato.
  + O valor de Mão Obra da Tarefa se refere aos valores dos insumos de Natureza "Mão de Obra", onde esses valores não tem a incidência de Leis Sociais.
  + É necessário definir o Valor Alocado para a Tarefa na Folha de Produtividade. Ao defini-lo o saldo disponível de Mão de Obra da tarefa em relação ao seu valor total de Mão de Obra da mesma é recalculado.
  + A Quantidade Planejada poderá ser independente do Valor Alocado.
  + Para que o Valor Alocado ou a Quantidade Planejada sejam calculados proporcional ao outro, deve-se limpar o campo que o mesmo será automaticamente recalculado.
  + Ao salvar o registro o Valor Alocado de todas as tarefas da folha são somados e distribuídos entre os membros da equipe associada à folha tarefa, onde o cálculo considera o peso definido no cadastro do membro, como por exemplo:
    - Total Alocado dos itens da folha = 500,00
    - Membros da equipe:
      * JOSÉ: Peso = 3
      * JOÃO: Peso = 1
      * MARIA: Peso = 1
    - Distribuição dos valores:
      * JOSÉ: 60% x 500,00 = 300,00
      * JOÃO: 20% x 500,00 = 100,00
      * MARIA: 20% x 500,00 = 100,00
  + No anexo "Distribuição de Valores da Equipe" em Folha Tarefa, são exibidos os membros da equipe com seus valores devidamente distribuídos:
  + **Validações:**
    - Processo de Drag and Drop não é permitido para esse tipo de folha;
    - O Valor Alocado não pode ser maior que o valor da tarefa ou o saldo;
    - O Valor Alocado não pode ser menor ou igual a zero.
* **Processo de Associar Tarefas (Itens) na Folha Tarefa:**Para esse tipo de folha,  o processo de associar de Tarefas à mesma, deve obedecer as mesmas regras do anexo e que também não são consideradas no tipo de folha tarefa "Padrão":
  + Na tela do processo, na opção de filtro, também é possível definir alguns filtros para a seleção da Tarefa desejada, a Unidade de Serviço, o Local de Serviço e/ou a Equipe no qual a Tarefa está associada;
  + As Tarefas que são exibidas são aquelas que ainda possuem saldo e que ainda não foram iniciadas, assim como no anexo;
  + O valor de Mão Obra da Tarefa se refere aos valores dos insumos de Natureza "Mão de Obra", onde esses valores não tem a incidência de Leis Sociais;
  + Também é necessário definir o Valor Alocado e a Quantidade Planejada para a Tarefa na Folha de Produtividade, basta editar o valor no grid da respectiva coluna;
  + Para que o Valor Alocado ou a Quantidade Planejada sejam calculados proporcional ao outro, deve-se limpar o campo que o mesmo será automaticamente recalculado;
  + Na página seguinte da tela, são apresentados os membros da equipe da folha com os valores alocados distribuídos entre os membros da equipe associada à folha tarefa, onde o cálculo também considera o peso definido no cadastro do membro;
  + A distribuição dos valores dos membros leva em consideração todas as tarefas associadas à folha, não somente as definidas na tela do processo.

Folhas Tarefas do tipo Produtividade, podem ser criadas a partir do processo de "Desmembrar Tarefas", onde para cada tarefa criada, uma nova folha também será criada com sua respectiva tarefa associada.
