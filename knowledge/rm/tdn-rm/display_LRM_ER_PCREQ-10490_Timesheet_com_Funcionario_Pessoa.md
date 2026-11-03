---
content_hash: e7062507758fcb8aa249e0ae71419fd07e90779103eb14677db090fcd6de0d6a
fetched_at: '2026-06-29T00:06:30.368097+00:00'
page_id: '235320192'
product: rm
source: tdn-rm
title: ER_PCREQ-10490_Timesheet_com_Funcionario_Pessoa
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-10490_Timesheet_com_Funcionario_Pessoa
version: 16
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Obras e Projetos | **Módulo** | Timesheet |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | R\_C&P\_TOP011 | **IRM1** | PCREQ-7444 |
| **Requisito1** | PCREQ-10490 | **Subtarefa1** | PDR\_CP\_TOP011-58 |
| **Chamado2** | Não se aplica. | | |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | |  |  | | --- | --- | | **Pré-requisitos para melhor entendimento da especificação** | | | **Entidade** | **Link para o Wikihelp** | | Timesheet | <http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.Timesheet.aspx> | | Tarefas de Timesheet | <http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.TarefaDeTimesheet.aspx> | | Contratos de Timesheet | <http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.ContratosTimesheet.aspx> | | | |

### Objetivo

Possibilitar que Contratos de Insumo que utilizam Timesheet, tenham o seus tipos definidos como "A Receber", onde o valor contratado dos objetos, isto é, funcionários ou terceiros, poderão ser diferentes para o tipo a pagar e para o tipo a receber.

### Definição da Regra de Negócio

Para contratos de insumo que utilizam timesheet, é necessário que o mesmo funcionário/terceiro tenha valores diferentes em diferentes tipos, sendo a pagar ou a receber, sendo assim, será necessário alterar algumas funcionalidades do módulo de contratos para que o mesmo possibilite esse novo conceito. O exemplo abaixo demonstra a necessidade da implementação:

Ex.: Uma **Empresa A** é contratada por uma **Empresa B** (contrato 001/2016, à receber), onde os funcionários/terceiros são as pessoas envolvidas. Um **Funcionário X**é contratado pela **Empresa B**(contrato 002/2016, à pagar).

No contrato 002/2016 entre o **Funcionário X** e a **Empresa B**, o valor da hora é de **R$ 50,00**, porém o valor repassado para **Empresa A** através do contrato 001/2016 é de **R$ 100,00** a hora.

**1. **Cadastro de Contratos****

* + Ao cadastrar um contrato e definir sua finalidade como **Contrato de Insumo**e que utiliza **Timesheet**, deverá ser possível utilizar o tipo "**A** **Receber**" (Protótipo 01). Desmarcando a opção Timesheet, o contrato passa a ser "**A Pagar**" antes de ser salvo;
  + O ícone  representará o contrato como Contrato de Insumo (a receber).

**2. **Consumo de Objetos de **Contrato de Insumos com Timesheet******

* + O consumo de objetos desse tipo de contrato é realizado a partir do processo de "Atualizar consumo pela Apropriação", porém a exclusão desse consumo não é possível de ser realizada, portanto o processo de consumo de objetos deverá ser alterado para permitir essa exclusão;
  + A atualização do consumo através da apropriação, para os tipos de períodos acontece da seguinte maneira:
    - Período Principal: Consome as apropriações que estão com a data da apropriação dentro do intervalo do período selecionado;
    - Período Complementar: Consome as apropriações que estão com a data da apropriação dentro do intervalo do período selecionado, porém que não foram consumidas pelo período principal;
    - Período de Estorno: Consome as apropriações que foram consumidas pelo período principal, pois, por se tratar de estorno, apenas esses consumos poderão ser estornados.

**3. Vínculo de C****ontratos******

* + Com a possibilidade de se definir contratos de insumos que utilizam timesheet como a receber, o vínculo de contratos poderá ser utilizado para o mesma finalidade do contrato quando sendo de timesheet (Protótipo 02), e o exemplo citado anteriormente se encaixaria perfeitamente nesse conceito. Ao vincular o contrato 001/2016 ao contrato 002/2016 o TOP somente permitirá a liberação do período do contrato à pagar se o período do contrato à receber estiver liberado, isto é, consequentemente o **Funcionário X** somente receberá seu pagamento, se a **Empresa A** pagar a **Empresa B**.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Contratos | [Alteração] | [Controle -> Contrato -> Contratos] | - |

## Protótipo de Tela

**Protótipo 01**

**Protótipo 02**

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
