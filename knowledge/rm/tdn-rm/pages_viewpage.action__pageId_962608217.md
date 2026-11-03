---
content_hash: 91b5653726b0dc959cda3d4379c5608868ca867cd64f5cd56d368258d1e655c8
fetched_at: '2026-06-29T00:12:13.967282+00:00'
page_id: '962608217'
product: rm
source: tdn-rm
title: TOTVS Gestão Hospitalar > Atendimento > Alta > Alta
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=962608217
version: 19
---

## **ÍNDICE**

1. **Visão Geral**
2. **Acesso ao processo**
3. **Operações**
   1. **Realizar alta do paciente**
   2. **Cancelar alta**
   3. **Editar dados da alta**
4. **Validações e mensagens**
5. **Impressão de formulários**
6. **Parâmetros e** **Fluxos alternativos**
sumarioVisão Geral

Processo de realização de alta de pacientes internados no RM Saúde, incluindo os caminhos de acesso, etapas do fluxo e alertas possíveis.

Esse processo contempla apenas pacientes internados, ou seja, registro de atendimento com o tipo paciente igual a interno.

Acesso ao processo

Existem duas formas de acessar a funcionalidade de alta de pacientes:

1. **Menu Principal:**

   * Caminho: `Atendimento > Alta > Alta`
2. **Via Registro de Atendimento:**

   * Caminho: `Registro de Atendimento > Processos > Alta`
   * *Vantagem*: Nesta opção, ao abrir o formulário de alta, o sistema já carrega automaticamente o atendimento do paciente em questão.

  
OperaçõesOperaçõesRealizar alta do paciente

### 1. **Seleção do Atendimento**

* O usuário deve selecionar o atendimento correspondente ao paciente que será liberado.
* Selecionar a opção Realizar alta do paciente
* Em seguida, clicar no botão **Avançar**.

### 2. **Preenchimento de Dados da Alta**

* O sistema apresenta uma nova tela para preenchimento das informações necessárias à alta.
* Após preencher os dados solicitados, clicar novamente em **Avançar**.

  + Data/hora da alta
  + Motivo - Caso o motivo seja óbito deverão também serem informados a dta/hora do óbito e o destino
  + CID da internação - será pré-carregados com a informação já registrada
  + CID da alta
* Caso a alta seja da mãe, existe a opção do RN permanecer internado. Neste caso serão exibidos todos os RNs vinculados ao atendimento da mãe. Para ocorrer a alta os RNs, todos devem ser selecionados. Caso algum não seja selecionado, o mesmo não terá alta.  
  Para RN vinculados ao convênio SUS e que não tiveram alta juntamente com a mãe, deve-se atualizar os dados do RN e as informações do atendimento. Nesse momento é que a AIH do RN será criada.

### **2.1 Motivos de alta: óbito**

* Caso o campo **"Motivo Alta"** seja preenchido com a opção **"Óbito"**, o campo **"Número Declaração de Óbito"**será habilitado para que seja inserido o número de declaração de óbito, atrelando essa informação ao processo de alta e assim facilitando a busca dessa informação dentro do sistema.

Válido ressaltar que existe a opção de que as informações de óbito sejam compartilhada com os dados da guia TISS para **convênios PADRÃO TISS**

* Para isso, o seguinte parâmetro "Exigir Número de Declaração de Óbito e dados TISS na alta de pacientes de convênios com faturamento padrão TISS." deve ser marcado, ele se encontra em : Ambiente > Configuração > Parâmetros > Gestão Hospitalar > Registro e Controle > Alta.

* Caso o parâmetro esteja marcado, o convênio seja padrão TISS e o motivo da alta seja: **óbito**
  + O sistema habilita e exige o preenchimento do "Número da Declaração de Óbito".
  + O sistema habilita e exige o preenchimento do campo "Motivo de Alta (TISS)".
  + O avanço é bloqueado caso os campos estejam vazios.

* Caso o parâmetro esteja marcado, o convênio seja padrão TISS e o motivo da alta seja: **Cenário Outros Motivos que não sejam óbito**
  + O campo "Número da Declaração de Óbito" é limpo e desabilitado.
  + O campo "Motivo de Alta (TISS)" é habilitado.

 As regras para **Convênios NÃO TISS são diferentes.**

* Caso seja um Cenário Óbito
  + O campo "Número da Declaração de Óbito" é habilitado, porém seu preenchimento é opcional.
  + O campo "Motivo de Alta (TISS)" é limpo e desabilitado independentemente do motivo.

* Cenário Outros Motivo
  + O campo "Número da Declaração de Óbito" deve ser limpo e desabilitado.
  + O campo "Motivo de Alta (TISS)" não deve ser habilitado independentemente do motivo.

### **3.** **Execução da Alta**

* Na tela final, o usuário deve clicar em **Executar** para concluir o processo.

Cancelar alta

### 1. **Seleção do Atendimento**

* O usuário deve selecionar o atendimento correspondente ao paciente que possui alta.
* Selecionar a opção Cancelar alta
* Em seguida, clicar no botão **Avançar**.

### 2. **Confirmação do cancelamento**

* É exibida uma nova tela com os dados do atendimento

### 3. **Finalizar cancelamento**

* Na tela final, o usuário deve clicar em **Executar** para concluir o processo.

Editar dados da alta

### 1. **Seleção do Atendimento**

* O usuário deve selecionar o atendimento correspondente ao paciente que será liberado.
* Selecionar a opção Editar dados da alta
* Em seguida, clicar no botão **Avançar**.

### 2. **Editar Dados da Alta**

* O sistema apresenta uma nova tela para alteração das informações necessárias à alta.
* Após preencher os dados solicitados, clicar novamente em **Avançar**.

  + Data/hora da alta
  + Motivo - Caso o motivo seja óbito deverão também serem informados a dta/hora do óbito e o destino
  + CID da internação - será pré-carregados com a informação já registrada
  + CID da alta

3. **Finalizar edição**

* Na tela final, o usuário deve clicar em **Executar** para concluir o processo.
Validações e mensagens

Após a execução, o sistema pode retornar um dos seguintes resultados:

* **Mensagem de sucesso ou alertas**, confirmando a conclusão do processo.
* **Mensagens de erro**, caso existam pendências ou inconsistências que impeçam a finalização da alta.

Impressão de formulários

### 1. **Impressão de formulários**

* Ao finalizar o processo de alta, o botão Imprimir formulários é habilitado e caso estejam configurados o RM realiza a impressão

Parâmetros e Fluxos alternativos

### 1. Permite dar Alta ao Paciente com Requisições de estoque pendentes de processamento

* Esse parâmetro, quando habilitado, permite dar alta ao paciente mesmo que seu atendimento possua requisições não processadas.
  + Posteriormente essas requisições podem ser processadas, caso atendam as regras de faturamento e farmácia ou podem ser suspensas
* Esse parâmetro pode ser configurado em Ambiente > Parâmetros > Gestão Hospitalar > Cuidados do paciente > Configuração

### 2. Utilizar workflow de processo de alta

* Caso o parâmetro **Utiliza workflow de processo de alta**esteja habilitado o RM utiliza o fluxo de processo de alta
* [Documentação do fluxo de processo de alta](https://tdn.totvs.com/pages/viewpage.action?pageId=962613044)
