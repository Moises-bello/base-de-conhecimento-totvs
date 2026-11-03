---
content_hash: 513986338c519f7183834638dbfb1efa51837cb52d6f003ddaba7ec17caeaa0a
fetched_at: '2026-06-29T00:11:31.352492+00:00'
page_id: '737546308'
product: rm
source: tdn-rm
title: Integração TOTVS RM X Benefício Flexíveis Swile
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=737546308
version: 54
---

**CONTEÚDO**

1. **Versões**
2. **Visão Geral**
3. **Solução**
4. **Exemplo de utilização**
   1. **Integração de Funcionários**
   2. **Integração de Pedidos**
   3. **Integração de Funcionários e Pedidos**
5. **Demais informações**

## 01. **VERSÕES**

false

**A partir das versões:**

* **12.1.2302.253**
* **12.1.2306.206**
* **12.1.2310.139**

## **02. VISÃO GERAL**

Novo processo que permitirá com que as empresas que utilizam o processo de Controle de Benefícios do módulo TOTVS Gestão de Pessoas (Linha RM) enviem os valores dos benefícios calculados para uma carteira de benefícios da Swile, para serem utilizados pelos seus colaboradores através de um cartão de credito de benefícios disponibilizado pela Swile, com a possibilidade de utilização do saldo de forma flexível, dentro das opções contratadas pela Empresa x Swile

## **03.** **SOLUÇÃO**

Foi criada a configuração para ativar a integração com a Swile e informar os dados: Id Work Group, Usuário, Senha e URL Base

Criada uma tabela auxiliar para vincular os códigos de Benefícios do RM com os códigos de Benefícios da Swile

Criado um processo para enviar os dados necessários através da API interna do sistema:

* Os dados dos funcionários (nome, CPF, telefone, e-mail, sexo, data de nascimento, situação).
* Os dados do pedido informados na Tela de Pedidos de Benefícios (CPF do funcionário, CNPJ da coligada, Código do benefício Swile associado e valor do benefício).

Após realizada a ativação da integração e a configuração dos Benéficos RM x Swile, o usuário deverá utilizar o processo de **Integração Benefício com Swile** para enviar os Dados do funcionário e o Pedidos de Benefícios.

## **04. EXEMPLO DE UTILIZAÇÃO**

Para fazer o envio de dados de funcionários e pedidos para a Swile é necessário marcar o parâmetro '**Ativar Integração com Swile**', em **Totvs Gestão de Pessoas | Configurações | Parâmetros | Configurações | Integração com Terceiros e APIs | APIs | Integração API Swile**. Após marcar o parâmetro, serão habilitados os campos para preenchimento, conforme o exemplo abaixo:

Considerando em **Totvs Gestão de Pessoas | Valorização | Controle de Benefícios | Benefícios e Remuneração Variável**, os benefícios abaixo que serão fornecidos para os funcionários:

Em **Totvs Gestão de Pessoas | Valorização | Controle de Benefícios | Tabelas Auxiliares | De/Para Benefícios Terceiro**, vincular o **Benefício RM** ao **Benefício Swile**.

Para executar o processo de envio de funcionários e benefícios para a Swile, deverá ir em **Totvs Gestão de Pessoas | Valorização | Controle de Benefícios | Processos | Integração Benefício com Swile,** clicar em **Avançar** e será apresentada a tela abaixo:

Detalhes Importantes

Para avançar no processo, é necessário que seja selecionado ao menos 1 das duas opções ou **Envio de Funcionários** ou **Envio dos Pedidos de Beneficios.** Caso não selecione uma das duas opções, será exibida a seguinte mensagem de alerta:  
  
  
  
Com a flag ativa para Enviar Pedidos de Benefícios, é necessário atentar-se às seguintes regras:  
  
1. A **Data de Crédito deve ser no mínimo posterior a dois dias da Data de Hoje**.Isso serve para termos uma maior flexibilidade no pagamento do boleto e não atrase a data de crédito, tendo em vista que geralmente os bancos tendem a compensar o pagamento em até 1 dia.Caso selecione uma data menor ou igual a dois dias da data de Hoje e tente avançar, será exibida a seguinte mensagem:2. A **Data de Pagamento do Boleto deve anteceder no minimo dois dias da Data de Crédito**, pensando também nos prazos de pagamento e compensação do mesmo. Caso cadastremos uma data diferente desta regra, será exibida a mensagem de alerta, não permitindo o avanço no processo.

### **a. INTEGRAÇÃO DE FUNCINÁRIOS**

Para executar o processo de envio de funcionários para a Swile, deverá marcar a opção **Enviar Funcionários**:

Após marcada a opção '**Enviar Funcionários**', informar o'**Tipo de Atualização Funcionário (Ignorar/Substituir)**', '**Enviar Email de Boas Vindas**' e '**Data do Email de Boas Vindas**', conforme desejado

Após executar o processo será apresentado o log com o retorno da integração realizada

Abaixo iremos exemplifica possíveis retornos que serão apresentados no **Logs de Aviso, Debug e Execução.**

| Validação | Descrição do erro ou aviso |
| --- | --- |
| Telefone menor que 10 dígitos | Coligada: X Chapa: xxxxx O Campo de Telefone 3326565 sem caracteres de formatação 3326565 deve ter de 11 ou 10 dígitos numérico. |
| Telefone não informado | O campo Telefone é de preenchimento Obrigatório. Funcionário não será integrado. |
| E-mail não informado | O campo Email é de preenchimento Obrigatório. Funcionário não será integrado. |
| E-mail inválido | Integração de Funcionário não realizada devido a Erro no envio dos Dados para Requisição.  3 - Dados inválidos: Nome do Colaborador (CPF Colaborador) com e-mail inválido (e-mail enviado). |
| E-mail já cadastrado para outro colaborador | Integração de Funcionário não realizada devido a Erro no envio dos Dados para Requisição.  2 - Colaborador: Nome do Colaborador (CPF Colaborador) com e-mail já cadastrado (e-mail já existente). |
| CPF já cadastrado | Integração de Funcionário não realizada devido a Erro no envio dos Dados para Requisição.  2 - Colaborador: Nome do Colaborador (CPF Colaborador) com CPF já cadastrado. |

### Observações

* Quando existe mais de um funcionário vinculado a mesma pessoa, a integração verifica o vínculo de contrato mais recente para enviar. Isto se deve ao fato da Swile validar a pessoa (dados pessoais) e não contrato de trabalho. Caso integrasse os dois vínculos, retornaria erro de duplicidade de Colaborador. Com isto não é necessário enviar novamente a pessoa através do processo de integração em caso de cadastro de novo vínculo.
* Quando um vínculo é demitido, é possível enviar a atualização do cadastro do funcionário para Swile através da integração marcando a opção 'substituir'. O Colaborador é inativado na Swile, porém a Swile **não** valida se o colaborador está ativo ou não para receber o pedido de benefício do Colaborador. Neste caso, é importante se atentar quando for enviar os pedidos se está com o filtro dos funcionários desejados.
* Uma vez que o Colaborador está inativo no portal da Swile, não é possível ativar novamente a mesma pessoa através da integração, pois a Swile não trata essa ativação através da API. Quando enviado o cadastro de um colaborador inativo na Swile, o parceiro tenta cadastrar novamente o Colaborador. Neste caso, é retornado erro de colaborador já existente. Para ativar o colaborador no portal da Swile o mesmo deve ser feito através o portal do parceiro.
* O envio de e-mail de boas-vindas é opcional.
* Não é feita a integração do cadastro do dependente para a Swile, somente do colaborador. Caso exista benefícios lançados para o dependente o mesmo será enviado como pedido, vinculando ao colaborador.

### **b. INTEGRAÇÃO DE PEDIDOS**

Para o envio de Pedidos de Benefícios para a Swile, deverá marcar a opção '**Enviar Pedidos de Benefícios**', e informar os parâmetros '**Data do Crédito**' e '**Data Limite**'.

Após o envio do **Pedido de Benefício Swile**, serão apresentados os **Logs de Execução (Debug e Execução),** com as informações do envio do pedido, conforme abaixo. Neste exemplo, temos o resumo do pedido com o **Total do Pedido, Total de Colaboradores, Total de Itens e Data do Crédito** e logo depois o corpo do Log trará os dados dos Benefícios por colaborador **CPF**, **Código do Benefício Swile**, **Valor** e **Total do Colaborador**.

Abaixo iremos exemplificar possíveis retornos da Swile que serão apresentados no **Logs de Aviso, Debug e Execução.**

| Validação | Descrição do erro ou aviso |
| --- | --- |
| Código de Benefício Swile inválido | Integração de Pedido não realizada devido a Erro no envio dos Dados para Requisição.  3 - Dados inválidos: Processado com erros, favor visualizar os logs de processamento. |
| Data de Credito menor que o dia da geração | Integração de Pedido não realizada devido a Erro no envio dos Dados para Requisição.  3 - Dados inválidos: Data de crédito dd/mm/yyyy 00:00 inválida, data de liberação de carga deve ser pelo menos 0 dias úteis a frente para que haja tempo suficiente para compensação bancária do seu pagamento. |
| Colaborador não cadastrado no portal da Swile | Integração de Pedido não realizada devido a Erro no envio dos Dados para Requisição.  3 - Dados inválidos: Processado com erros, favor visualizar os logs de processamento. |

### Observações

* É necessário ter o funcionário cadastrado na Swile para poder realizar um pedido. Caso não exista, será necessário cadastrá-lo pelo Portal da Swile ou utilizando a integração de funcionários.
* A Swile valida a data de credito do pedido, devendo ser maior que o dia da geração do pedido.
* Quando vinculado mais de um benefício RM a um mesmo benefício da Swile, os valores lançados para o funcionário e/ou dependentes são acumulados no mesmo código de benefício da Swile e enviados via API.
* O processo de integração verifica data limite informado na tela do processo se está dentro da vigência benefícios lançados para o funcionário conforme ocorre no Lançamento de Benefícios de Funcionários para Folha de Pagamento.

**Exemplo:**

Competência: 01/2024

Data limite informada no processo: 31/01/2024

| Benefício RM | Data Início | Data Término | Comportamento na Integração |
| --- | --- | --- | --- |
| 00001 | 01/01/2024 | 30/01/2024 | Será integrado, pois está dentro da vigência |
| 00002 | 01/01/2024 | - | Será Integrado, pois a data início é anterior ao dia 31/01 e não tem data fim. Neste caso, esse benefício sempre entrará na integração se for lançado |
| 00003 | 01/02/2024 | 28/02/2024 | Não será integrado pois inicia após o dia 31/01 |
| 00004 | 01/12/2023 | 31/12/2023 | Não será integrado pois a data término é menor que a competência da base. |

* É possível fazer pedidos de benefícios específicos, informando o código de benefício RM no processo de integração.
* Não é feito a verificação de pedidos de benefícios duplicados, pois a Swile não faz esta verificação, podendo o usuário enviar quantos benefícios desejar. Neste caso deve ficar atento para não enviar o mesmo benefício de forma duplicada.
* Não é feito o cancelamento de pedido de benefício via API, mesmo se o pedido constar como pendente no portal da Swile. Esse controle é todo gerenciado através do portal pelo Usuário

### **c. INTEGRAÇÃO DE FUNCIONÁRIOS E PEDIDOS**

Para o envio de funcionários e Pedidos de Benefícios para a Swile, deverão ser marcadas as opções **'Enviar Funcionários'** e'**Enviar Pedidos de Benefícios**', informar os parâmetros '**'Tipo de Atualização Funcionário (Ignorar/Substituir)'**, **'Enviar Email de Boas Vindas'**, **'Data do Email de Boas Vindas'**, ''**Data do Crédito**' e '**Data Limite**'.

O processo irá enviar os funcionários e em seguida o pedido de benefícios:

## **05. DEMAIS INFORMAÇÕES**

**[Parametrizador - Integração Swile](https://tdn.totvs.com/pages/viewpage.action?pageId=758491903)**

**[De/Para benefícios Terceiros - Swile](https://tdn.totvs.com/pages/viewpage.action?pageId=758491988)**

**[Integração Benefícios com Swile](https://tdn.totvs.com/pages/viewpage.action?pageId=758491949)**

**[RHU - Controle de Benefícios](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035960374-TOTVS-RH-Linha-RM-RHU-Como-realizar-o-lan%C3%A7amento-de-benef%C3%ADcio-para-os-funcion%C3%A1rios-e-ou-dependentes-)**

**[RHU - Benefícios e Remuneração Variável](https://tdn.totvs.com/pages/viewpage.action?pageId=452719384)**
