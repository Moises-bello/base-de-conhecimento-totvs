---
content_hash: 81c5f23458a82de6fa84e3f47e8db076728f11c9eb474db305b9f6b51cda2ef4
fetched_at: '2026-06-29T00:10:43.101104+00:00'
page_id: '549512868'
product: rm
source: tdn-rm
title: Controle de Solicitação para Emissão de Nota Fiscal / Recibos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=549512868
version: 70
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Processo de Geração de pedido de Nota Fiscal / Recibos**
3. **Cancelar solicitação de pedido de nota fiscal**
4. **Anexos**
5. **Validações para múltiplas notas fiscais em Gastos Particulares**
6. **Geração de pedido de nota fiscal**
7. **Dados Fiscais**
8. **Tabelas Utilizadas**

## **01. Visão Geral**

false

1. Neste documento, onde se lê "BackOffice", entende-se por TOTVS Gestão de Estoque, Compras e Faturamento (antigo RM Nucleus), Datasul EMS5 ou Protheus.
2. No processo antigo era necessário realizar duas etapas distintas, primeiro gerar o pedido e depois solicitar a Nota Fiscal ao BackOffice. A partir da versão 12.1.29, o processo foi migrado para a nova MDI e estes 2 processos foram unificados, sendo necessário apenas solicitar a emissão da Nota Fiscal / Pedido ao BackOffice.

Através desta funcionalidade você poderá

No menu Tesouraria, através da tela de **Controle de Solicitação para Emissão de Nota Fiscal / Recibos** será possível gerenciar todas as solicitações já geradas ou canceladas para a emissão de **Nota Fiscal** para paciente que possuir **gastos particulares** ou **coparticipação.** 

Através da coluna Status, será possível identificar qual a situação da solicitação, sendo elas:

* **Aberto**: Solicitação criada, porém ainda não integrado com BackOffice, esse status só é utilizando para os registros criados na versão 28 ou inferior feitas pelo Delphi.
* **Gerado**: Solicitação criada e já integrada ao BackOffice.
* **Cancelado**: Solicitação cancelada.

O processo de solicitação ou cancelamento da Nota Fiscal com o BackOffice é realizados através da funcionalidade **Processos que serão explicados em detalhes mais adiante.** 

É possível controlar os os acessos que no cadastro de Perfis. todo o processo de solicitação ou cancelamento é feito em processos distintos. 

## **02. Geração de pedido de Nota Fiscal / Recibo**

Para iniciar um novo pedido vá em Processos > Geração de pedido de Nota Fiscal, essa rotina será responsável em realizar a solicitação da **Nota Fiscal**, informando todos os dados necessários para a emissão do documento junto ao **BackOffice**.

### **Etapa 1 - Seleção do Paciente**

Na primeira etapa do processo, o usuário deverá pesquisar o Paciente que deseja emitir nota fiscal de seus gastos particulares.

Em seguida selecione a Parcial que deseja gerar nota fiscal.

### **Importante!**

Para Atendimento de Convênio: O status da Parcial deverá estar como Liberada. Caso o paciente queira quitar seus gastos particulares antes da Alta, a equipe de Faturamento deverá gerar uma nova parcial, transferindo os gastos para ela e fazer o seu encerramento, com isso será possível realizar a solicitação da nota fiscal.

Para Atendimento Particular: o status da Parcial poderá estar Em Elaboração, e a geração da nota fiscal será para todos os itens particulares que ainda faltam nota fiscal.

---

### **Etapa 2 - Dados do pedido da Nota Fiscal**

Na segunda etapa pode ser alterada a **Data Processamento**, o sistema já sugere a data atual, caso a nota fiscal deva ter uma data futura, deverá ser alterado o valor para a data desejada.

Nessa mesma etapa, caso o paciente possua mais de um responsável financeiro, será possível marcar qual o responsável será utilizado para emissão da Nota Fiscal.

Abaixo detalhes sobre os campos e suas regras de negócio:

**Dados do Pedido:**

| Campo | Descrição |
| --- | --- |
| Paciente | Campo informativo que exibe o código e nome do paciente. |
| Atendimento | Campo informativo que exibe o código do atendimento. |
| Tipo de Faturamento | Campo informativo que exibe o tipo de faturamento podendo ser Fatura, Nota Fiscal ou Sem Ônus. |
| Grupo do Convênio | Campo informativo que exibe o Grupo do Convênio. |
| Parcial | Campo informativo que exibe o código da parcial do atendimento. |
| Data Inicial | Campo informativo que exibe a data inicial da parcial. |
| Data Final | Campo informativo que exibe a data final da parcial. |
| Agrupa lançamentos | Permite agrupar todos os lançamentos em uma única discriminação. Estará habilitado somente para os casos em que o parâmetro "Utilizar sempre discriminação única na NF" nos Parâmetros Gerais do Faturamento estiver marcado e existir ao menos um produto vinculado a coligada. |
| Data Processamento | Permite informar a data de processamento que não poderá ser menor do que a data informada no campo Data Inicial. |
| Controle | Selecionar o tipo de gasto entre as opções Gastos de Convênio, Gastos Particulares e Todos os Gastos. Obrigatório informar uma das opções. |
| Responsável Financeiro | Selecionar o responsável financeiro do paciente. Campo de preenchimento obrigatório. |

**Controle:**

Atualmente o campo controle disponibiliza três opções para gerar a Nota Fiscal:

* Gastos de Convênio;
* Gastos Particulares;
* Todos os Gastos.

Para que o sistema identifique e permita o usuário a utilizar cada uma das opções, deve ser observada as regras para geração:

A primeira regra a ser considerada é referente a outras gerações de pedido de Nota Fiscal já efetuadas:

1. Caso já tenha uma geração de pedido de Nota Fiscal que foi efetuado com a opção ‘Todos os Gastos’, então todas opções estarão desabilitadas para pedidos de parciais futuras e somente a opção "Todos Gastos" estará selecionada.
2. Caso já tenha uma geração de pedido para "Gastos de Convênio" então:
   1. Se o campo "Grupo de Convênio" no cadastro de convênios estiver informado como PARTICULAR(999), então todas opções estarão desabilitadas e somente a opção "Todos Gastos" estará selecionada.
   2. Caso o campo "Grupo de Convênio" no cadastro de convênios estiver informado com um grupo NÃO PARTICULAR, então estará selecionado somente a opção ‘Gastos Particulares’ e as demais opções estarão desabilitadas.

Para os casos em que não existe nenhum pedido de geração de Nota Fiscal:

1. A primeira regra a ser considerada será o campo ‘Grupo de Convênio' no cadastro de convênios. Se estiver Informado como PARTICULAR(999), então o sistema seleciona somente a opção "Todos Gastos" e as demais opções estarão desabilitadas;
2. No caso do campo ‘Grupo de Convênio' no cadastro de convênios não seja PARTICULAR então:
   1. A opção ‘Gastos Convênio’ poderá ser selecionado e todas opções HABILITADAS quando o Tipo de Faturamento for igual a Nota Fiscal e nenhum outro pedido de geração de Nota Fiscal tenha sido realizado;
   2. A opção ‘Gastos Particulares’ estará selecionada e todas opções desabilitadas quando o campo ‘Tipo de Faturamento’ no convênio for diferente de Nota Fiscal.

### **Etapa 3 - Selecionar o Responsável Financeiro**

Após selecionar o responsável financeiro do paciente e avançar no processo, o sistema tenta buscar no cadastro de Cliente/Fornecedor um registro já existente com o seu documento (CPF/CNPJ).

Quando o responsável financeiro selecionado é brasileiro:

Caso o parâmetro **CNPJ Único / CPF Único desligado** do Módulo Gestão Financeira, ou seja, permite a duplicidade de cadastro de fornecedores com o mesmo CPF ou CNPJ

1. Caso não seja encontrado, o sistema integra um novo cadastro de Cliente/Fornecedor com o responsável selecionado, neste caso essa etapa não será exibida, pois os dados anteriores serão utilizados para o cadastro.
2. Caso exista apenas um registro do responsável no cadastro de Cliente/Fornecedor, neste caso essa etapa não será exibida e os dados do Cliente/Fornecedor serão atualizados com os dados do responsável selecionado.
3. Caso o responsável esteja cadastrado com o mesmo CPF/CNPJ no Saúde e exista apenas um registro de  Cliente/Fornecedor o sistema deverá abrir a tela para o usuário selecionar o registro existente ou caso não selecione nenhum deverá cadastrar um novo.
4. Caso seja encontrado mais de um registro com o mesmo documento (CPF/CNPJ) e não exista duplicidade no Saúde, o sistema apresentará a lista destes registros para seleção obrigatória e vinculo no cadastro de Cliente/Fornecedor, pois não existe duplicidade no cadastro de responsável do Saúde.

Caso o parâmetro **CNPJ Único / CPF Único ligado** do Módulo Gestão Financeira, ou seja, não permite a duplicidade de cadastro de fornecedores com o mesmo CPF ou CNPJ

1. Caso não seja encontrado, o sistema integra um novo cadastro de Cliente/Fornecedor com o responsável selecionado, neste caso essa etapa não será exibida, pois os dados anteriores serão utilizados para o cadastro.
2. Caso seja encontrado mais de um registro com o mesmo documento (CPF/CNPJ), o sistema apresentará a lista destes registros para seleção obrigatória e vinculo no cadastro de Cliente/Fornecedor.

Caso seja identificada duplicidade de responsável no módulo Saúde, o sistema permitirá cadastrar um novo CFO no BackOffice, caso contrário, a seleção será obrigatória, no caso em que a tela é aberta com mais de um Cliente/Fornecedor listado do BackOffice.

Quando o responsável financeiro selecionado é estrangeiro:

1. Caso possua documento (CPF/CNPJ) informado, o sistema tenta buscar no cadastro de Cliente/Fornecedor um registro já existente com esse documento.
2. Caso possua documento (CPF/CNPJ) informado e for encontrado mais de um registro, o sistema então apresentará a lista destes registros para seleção opcional. Se nenhum registro for selecionado, o vinculo é feito com o responsável financeiro.
3. Caso não possua documento (CPF/CNPJ) informado, o sistema então exibirá todos os registros de Cliente/Fornecedor que são estrangeiros e estão ativos. A seleção é opcional e caso não seja selecionado nenhum, o vinculo é feito com o responsável financeiro.

---

### **Etapa 4 - Dados do pedido da Nota Fiscal**

Nesta etapa deverá ser preenchidos os dados referente a integração do BackOffice, sendo os seguintes campos:

**Campo - Movimento**

Informar qual o Movimento que onde será feita a contabilização da solicitação da Nota Fiscal, nos parâmetros do Saúde com o Backoffice RM, é possível ter um valor padrão que será sempre carregado pelo processo. É possível também exibir a tela do Movimento gerado, assim que o mesmo for criado com a solicitação da nota fiscal. Basta marcar o parâmetro "Exibe tela de movimentação do Nucleus após a integração"

Caso deseje, o campo pode ser alterado conforme necessidade.

**Campo - Condição de Pagamento**

Caso esteja parametrizado a condição de pagamento default, no tipo de movimento, o sistema já preencherá este campo. Caso contrário, é necessário selecionar a condição de pagamento negociada.

**Campo - Natureza Financeira**

Esse campo só é habilitado quando o BackOffice a ser integrado for o EMS5 ou Protheus.

**Campo - Valor Desconto**

Esta opção é habilitada quando o parâmetro em *Opções | Parâmetros | Parâmetros Gerais | Faturamento | Permitir informar desconto sobre o valor total no momento de integrar lançamentos no "Controle de Solicitação p/emissão de NF/Recibo"*está habilitado. 

Ao preencher o valor de desconto, o processo irá ratear o valor pelos itens da nota, calculando percentual de desconto sobre o valor total e aplicando a cada item.

### Processamento dos dados

O processo irá realizar solicitação da Nota Fiscal junto ao BackOffice, além disso algumas etapas são realizadas, seguem detalhes:

**Controle de documentos SAME**

O processo gera em sua execução um documento para controle no SAME, para verificação do documento gerado, pode-se visualizar na aba *Faturamento → Outros → Controle de Documentos.*

**Agrupamento de Gastos**

**O agrupamento dos gastos pode ser realizado de três maneiras:**

##### **Opção 1 - Agrupamento de todos os lançamentos em uma única descrição:**

Esta opção é habilitada quando o parâmetro em *Opções | Parâmetros | Parâmetros Gerais | Faturamento / Utilizar sempre discriminação única na NF*  estiver selecionado e se houver algum produto parametrizado para utilização na descrição única em *Opções | Parâmetros | Integração RM Nucleos | Aba geral / Pedido NF/Recibo Paciente.*

##### **Opção 2 - Agrupamento dos lançamentos por Grupo de Gastos:**

O agrupamento dos gastos por grupo de gastos é realizado quando o parâmetro em *Cadastros | Faturamento | Grupos de Gasto / Agrupa Nota Fiscal* estiver marcado e a parametrização do item *"Agrupamento de todos lançamentos em uma única descrição"* desmarcada*.*

##### **Opção 3 - Agrupamento dos lançamentos por Codificação:**

Para essa parametrização ser executada é necessário que os parâmetros dos itens *"Agrupamento de todos lançamentos em uma única descrição"* e "*Agrupamento dos lançamentos por Grupo de Gastos*" estejam desmarcados.

* Grupo de gastos: Honorários, Diárias,Diagnose e Terapia, Taxas e Serviços

O agrupamento dos gastos por codificação é realizado quando o convênio referente ao pedido possuir produtos associados em *Cadastros | Faturamento | Condições Contratuais com Convênios / Padrão de Faturamento e Codificação*

* Materiais e Medicamos

Para utilizar faixa de codificação para Materiais e medicamentos na emissão de NF, deverá ser configurado o parâmetro   "Utilizar faixa de codificação para produto na emissão de NF"

* Gestão hospitalar > parâmetros gerais > faturamento > Emissão Nota fiscal 2/2.

* **Funcionamento:**

  + **Ativado:** O sistema aplica a **lógica de faixas de codificação**, flexibilizando a emissão.
  + **Desativado (Padrão):** O sistema mantém a **validação rigorosa** baseada no cadastro individual de cada produto.

O agrupamento dos gastos por codificação é realizado quando o convênio referente ao pedido possuir produtos associados em *Cadastros | Faturamento | Condições Contratuais com Convênios / Padrão de Faturamento e Codificação/Outras Codificações*

## **03. Cancelar solicitação de pedido de nota fiscal**

Esse processo irá realizar o cancelamento do pedido de nota fiscal. Ao finalizar o processo o sistema passa o status da solicitação para "Cancelado".

Para execução desse processo somente um registro por vez deve ser selecionado. Além disso, o código do pedido deve ser diferente de nulo e a nota fiscal não pode já ter sido cancelada. É necessário informar um motivo para o cancelamento:

Caso o pedido esteja com o status "Gerado" (Integrado com BackOffice RM), no processo de Cancelamento do Pedido existirá duas opções de ação no movimento do BackOffice.

Sendo essas de Cancelamento ou Exclusão do Pedido de NF do BackOffice, que fará com que o movimento seja cancelado ou excluído, respectivamente:

## **04. Anexos**

**Outras Ações / Ações relacionadas**

| Ação | Descrição |
| --- | --- |
| Movimento | Este anexo exibe movimentos financeiros referente ao pedido selecionado, ou seja, integração do RMSaude com o  Backoffice RM.  Para que os movimentos possam ser exibidos nesse Anexo, o pedido deve estar com status = **G** e na grid da visão com o **Ref. TOTVS BackOffice** preenchido, caso contrário de ser feito o processo de Gerar Movimentos para que as informações sejam exibidas. |

### **4.1 Movimentos**

Este anexo irá exibir os movimentos lançados para o backoffice. No caso abaixo, de acordo com o que estava parametrizado, ele se encontra em no BackOffice > Gestão de Estoque, Compras e Faturamento > Vendas > Pedido de Venda

## 

### **4.2 Imprimir Movimentos**

### 

É necessário algumas permissões para o usuário ter acesso a esse processo. Para alterar essas permissões siga estes passos:

Acesse o anexo "Permissões por tipo de movimento" do usuário desejado.

Habilite a permissão "Imprimir" do movimento NF/Recebimento Particular (2.2.21).

Como este processo é integrado ao BackOffice, também é necessário conferir as suas permissões de usuário.

Com essas permissões o usuário consegue fazer a impressão.

## **05.****Validações para múltiplas notas fiscais em Gastos Particulares**

Quando o convênio do paciente for diferente de SUS e de Particular, é possível gerar várias notas fiscais, somente para o grupo “Gastos Particulares”, sem ter executado o processo de “Encerramento da Parcial”.

Após gerar a Nota Fiscal para o Gasto Particular, não será permitido nenhuma movimentação no item de débito que já teve uma Nota Fiscal Gerada Por Item de Débito.

Nos processos abaixo, os itens com nota fiscal não serão transferidos e nem alterados:

- Estorno de Lançamento de Gasto Particular ( <https://tdn.totvs.com/x/XXlVJQ> );

- Alteração de data final da parcial ( <https://tdn.totvs.com/x/5CBxJg> );

- Transferência de itens entre parciais;

- Transfere Itens selecionados para MatMed ( <https://tdn.totvs.com/x/5T1EK> )

- Mudança de Categoria do Paciente: ( <https://tdn.totvs.com/x/3xu-J> )  
Segue as mesmas validações já existente, ou seja,   
O atendimento não pode possuir parciais com NF já emitida.

Criado a coluna “Pedido NF Gerada” na grid de visão da Elaboração de Contas, em Grupo de Gasto Particular. Utilizada para identificar se o item de débito teve uma nota fiscal gerada por item de débito.

## **06. Geração de pedido de nota fiscal**

Para atendimentos particulares é possível emitir a nota fiscal diretamente da tela de Registro de Atendimentos, na guia Lançamento na conta.

Selecione um único registro da grid abaixo e execute o processo Geração de pedido de nota fiscal.

## 

Para atendimentos de convênios e que tenham gastos particulares (coparticipação), esses itens são transferidos para uma nova parcial e a nota fiscal emitida e a parcial fica com o status de faturada.

## **08.** **DADOS FISCAIS**

Por conta das novas regras tributárias, tornou-se necessário informar novos dados para a geração do **Pedido de Nota** e do **Movimento Financeiro**. Algumas dessas informações estão relacionadas ao **endereço do paciente**.

Como a integração entre o módulo **Saúde** e o **Movimento da Tesouraria** utiliza códigos diferentes para **País/Nacionalidade**, foi necessário criar uma configuração de relacionamento entre esses dados.

Dessa forma, para garantir o correto funcionamento da integração, é necessário realizar a configuração desses parâmetros.

Para isso, o usuário deve acessar o menu:

**Utilitários → Integração → Relacionamento** para cadastrar os códigos relacionados.

### Exemplos de configuração

#### Exemplo 1: Nacionalidade Brasileiro no SUS

No **SUS**, a nacionalidade **Brasileiro** possui o código **10** no sistema RM. Já no sistema BackOffice, o código correspondente é **1**.

Dessa forma, a configuração do relacionamento deve ser realizada da seguinte maneira:

**Identificador RM:** 10  
**Identificador Sistema:** 1  
**Descrição:** Brasileiro  
**Tipo Integração:** Nacionalidade SUS  
**Sistema Integrador:** Sistema BackOffice

---

#### Exemplo 2: Nacionalidade Brasileiro não SUS — padrão RM Saúde

Para a nacionalidade **Brasileiro** no padrão do **RM Saúde**, não é necessário realizar o relacionamento, pois os códigos utilizados são compatíveis entre os sistemas.

Nesse caso:

**Código Brasileiro padrão RM Saúde:** 1  
**Código Brasileiro no sistema BackOffice:** 1

Como os códigos são iguais, a integração ocorre corretamente sem necessidade de configuração adicional.

---

### Observação sobre nacionalidade no RM Saúde

O RM Saúde trabalha apenas com duas opções fixas de nacionalidade:

**Brasileiro = 1**  
**Estrangeiro = 2**

No caso de pacientes cadastrados como **Estrangeiro**, para que a integração seja realizada corretamente, é necessário configurar o vínculo de relacionamento com o código correspondente cadastrado no BackOffice.

A configuração deve ser feita da seguinte forma:

**Identificador RM:** 2  
**Identificador Sistema:** XXX  
**Descrição:** Estrangeiro  
**Tipo Integração:** Nacionalidade RM Saúde  
**Sistema Integrador:** BackOffice

Onde **XXX** deve ser substituído pelo código cadastrado no BackOffice referente à nacionalidade **Estrangeiro**.

## **07.****TABELAS UTILIZADAS**

* SZPEDIDOATEND = Identificação do Pedido de Atendimento
* SZPEDIDOATENDIT = Itens do Pedido de Atendimento
* SZATENDIMENTO = Atendimentos
