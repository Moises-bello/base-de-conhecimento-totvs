---
content_hash: a231b97b14e66bfa29c486c29b587aca6a7c4a724389fddf826a147d93ba30ab
fetched_at: '2026-06-29T00:06:08.105548+00:00'
page_id: '201746090'
product: rm
source: tdn-rm
title: PCREQ-4692_DT_Conta_Corrente
type: documentation
url: https://tdn.totvs.com/display/LRM/PCREQ-4692_DT_Conta_Corrente
version: 7
---

# CONTA CORRENTE

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **TOTVS Folha de Pagamento** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Funcionário* | *Conta do Funcionário* | |
| **Versões/Release:** | *12.1.7* |

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Folha de Pagamento | **Módulo** | RHU |
| **Segmento Executor** |  | | |
| **Projeto1** | [FOP007](http://jira.totvs.com.br/browse/PDR_RH_FOP007/?selectedTab=com.atlassian.jira.jira-projects-plugin:summary-panel) | **IRM1** | PCREQ-4689 |
| **Requisito1** | [PCREQ-4692](http://jira.totvs.com.br/browse/PDR_RH_FOP007-518) | **Subtarefa1** | [PDR\_RH\_FOP007-518](http://jira.totvs.com.br/browse/PDR_RH_FOP007-518) |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.6 | **Réplica** |  |
| **País** | (x) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** |  | | |

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Funcionário | Alteração | Administração de Pessoal / Funcionário | - |

## Descrição

Atualmente o Totvs Folha de Pagamento possibilita o cadastro de uma conta para o funcionário, no cadastro de funcionários. Usualmente essa conta é a conta salário do funcionário. Como não é possível pagar estornos em conta salário, foi criada a conta bancária alternativa  no cadastro de funcionários.  
Foi criado também um processo para incluir um Cliente/Fornecedor através do cadastro de um funcionário, copiando também os dados bancários do funcionário. Esse Cliente/Fornecedor será utilizado para geração dos lançamentos de estorno, e outros pagamentos para os funcionários.  
Foi adicionada uma mensagem de envio, para que os Clientes/Fornecedores RM, e seus dados bancários sejam enviados automaticamente para o Protheus, quando houver uma integração entre Folha de Pagamento e BackOffice Protheus.  
Para utilizar o cadastro de Cliente/Fornecedor é necessário possuir uma licença do RM Saldus.

## Procedimento para Utilização

Foram adicionados a tabela PFUNC funcionários os campos abaixo, que serão responsáveis por armazenar uma segunda conta.

 -PFUNC.CODAGENCIAPAGTO2  
-PFUNC.CODBANCOPAGTO2  
-PFUNC.CONTAPAGAMENTO2  
-PFUNC.OPBANCARIA2  
-PFUNC.TPCONTABANCARIA2  
  
Na tela de cadastro os novos campos serão adicionados na seção “Banco Pagto/Financeiro

Foram adicionados a tabela PFHSTCPGTO os campos abaixo:  
- PFHSTCPGTO.TPCONTABANCARIA  
- PFHSTCPGTO.PRINCIPAL (S = Conta Principal, N = Conta Alternativa)  
  
Nova chave primária:  
-CODCOLIGADA, CHAPA, DTMUDANCA, PRINCIPAL  
  
Ao salvar o histórico, será verificado qual é o tipo de conta. Quando a alteração for na Conta Principal será gravado automaticamente o valor PRINCIPAL = 1, quando for a Conta Alternativa será gravado o valor PRINCIPAL = 2.  
Na tela de cadastro do histórico será adicionado um RadioGroup para que possa ser selecionada a Classificação da Conta, no caso de inserção manual de histórico.

O campo principal PRINCIPAL, do histórico de conta bancária será preenchido com o valor ‘S’, para todos os registros de histórico existentes.  
Foi criado um processo para gerar um registro de Cliente/Fornecedor automaticamente através do cadastro de funcionário

Cliente/Fornecedor criado terá os mesmos dados que o funcionário  
  
    
A conta bancária a ser cadastrada nos dados bancários do CliFlor poderá ser escolhida entre as contas Principal e Alternativa, do funcionário   
  
  
  
O novo Cliente/Fornecedor será associado ao cadastro do funcionário automaticamente. Essa associação pode também ser feita manualmente através do campo ‘Fornecedor Lançamento Financeiro’, na seção Banco Pagto/Financeiro do cadastro de funcionário  
  
  
  
Ao executar o novo processo existem 3 possibilidades:

 Funcionário não possui Cliente/Fornecedor associado, e não existe cadastro de Cliente/Fornecedor com o seu CPF.

   1.  No processo deverá ser informado um código para o cliente/fornecedor e escolhida uma conta bancária entre as contas bancárias alternativa e principal.

   
  Será inserido e associado ao usuário um registro de Cliente/Fornecedor (FCFO). Será inserido um registro de Dados Bancários (FDADOSPGTO).  
   
  2. Funcionário não possui Cliente/Fornecedor associado, mas existem um ou mais registros de Cliente/Fornecedor com o seu CPF.  
  Serão exibidos os registros de Cliente/Fornecedor encontrados, o usuário poderá escolher um deles para associar ao funcionário, ou escolher criar um novo    
  
  
Caso seja utilizado um Cliente/Fornecedor já existente, a próxima etapa exibirá o Cliente/Fornecedor, não precisando informar o código.  
  
   
A conta bancária a ser cadastrada nos dados bancários do CliFlor poderá ser escolhida entre as contas Principal e Alternativa do funcionário.  
Será inserido registro de Dados Bancários apenas (FDADOSPAGTO). O Cliente/Fornecedor será associado ao usuário, mas não sofrerá alterações.  
    
 3. Funcionário possui Cliente/Fornecedor associado.  
 Será exibido o Cliente/Fornecedor que está associado, não precisando informar o código. A conta bancária a ser cadastrada nos dados bancários do CliFlor poderá ser escolhida entre as contas Principal e Alternativa do funcionário.

**Obs:** Quando incluindo um novo Cliente/Fornecedor será solicitado um código para o mesmo. Esse código obedece a uma máscara que pode ser definida nos Parâmetros Gerais do Totvs Gestão Financeira **(Contas a Pagar / Manutenção de Lançamentos / Lançamento)**. Caso a máscara definida seja numérica, é possível marcar o parâmetro ‘Usar código sequencial’, caso marcado, o código será gerado automaticamente, não precisando informa-lo ao executar o processo.

É possível consultar, editar, incluir ou excluir um Cliente/Fornecedor através do menu **Administração de Pessoal / Cadastros / Cliente e Fornecedor.**  
Para que esse cadastro seja exibido, é necessário uma licença do RM Saldus, e o parâmetro **Folha de Pagamento / Folha Normal / Tomador de Serviços / Usar tomador de serviços** deve estar habilitado.  
Após configurada a integração “TOTVS Folha pagto RM x Backoffice Protheus”, a mensagem CUSTOMERVENDOR será enviada automaticamente para o Protheus ao criar, alterar ou excluir um Cliente/Fornecedor, ou Dados Bancários do Cliente/Fornecedor, seja no novo processo criado, ou no cadastro de Cliente/Fornecedor.  
A mensagem será enviada 2 vezes. Primeiramente ao salvar ou alterar o Cliente/Fornecedor, serão enviados os dados do mesmo. Após salvar o Cliente/Fornecedor são cadastradas as contas bancárias, ao salvar cada conta, será enviada novamente a mensagem, porém somente com os dados de identificação do Cliente/Fornecedor e com os dados bancários.

Após configurada a integração “TOTVS Folha pagto RM x Backoffice Protheus”, a mensagem CUSTOMERVENDOR será enviada automaticamente para o Protheus ao criar, alterar ou excluir um Cliente/Fornecedor, ou Dados Bancários do Cliente/Fornecedor, seja no novo processo criado, ou no cadastro de Cliente/Fornecedor.  
A mensagem será enviada 2 vezes. Primeiramente ao salvar ou alterar o Cliente/Fornecedor, serão enviados os dados do mesmo. Após salvar o Cliente/Fornecedor são cadastradas as contas bancárias, ao salvar cada conta, será enviada novamente a mensagem, porém somente com os dados de identificação do Cliente/Fornecedor e com os dados bancários.

Foi criado o parâmetro RH\_CODCLASSIFICPAIS.  
O valor desse parâmetro deve ser o código da tabela de classificação de país. No exemplo abaixo, deveríamos configurar o valor 4 para esse parâmetro.

    
  
A tabela de classificação de país permite configurar um código diferente para os países. No exemplo abaixo, o código do Brasil na tabela “Integração Protheus” é 150, diferente do código 1, que é o código principal da tabela.  
  
   
  
  
Ao enviar a mensagem será enviado o código de país referente a tabela parametrizada (RH\_CODCLASSIFICPAIS). De acordo com os exemplos acima, seria enviado o código 150, referente a tabela “Integração Protheus”.

No cadastro de conta bancária do Folha de Pagamento não existe separação entre o dígito das agências e das contas. Logo, os campos referentes ao dígito da agência e conta nos dados bancários dos registros de Cliente/Fornecedor criados através do novo processo, ficarão em branco.  
A mensagem CUSTOMEVENDOR, atualmente na versão 2.004 não envia todos os campos existente nos dados bancários de cliente/fornecedor do RM.   
  
   
  
Entre os campos que podem ser vistos na imagem acima não são enviados:  
  
-Descrição  
-Tipo do Doc  
-Câmara Comp.:  
-Favorecido  
-CNPJ/CPF do Favorecido

Uma mensagem pode ser mapeada em mais de uma integração. Ao enviar a mensagem, são verificadas todas as integrações ativas que tem aquela mensagem mapeada, e a mensagem será enviada para cada integração.  
Atualmente a integração ‘TOTVS Educacional x BackOffie Protheus’ também possui a mensagem ‘CUSTOMERVENDOR’ mapeada, caso a integração do Educacional e a integração do Folha de Pagamento com o Protheus estiverem ativas, a mensagem ‘CUSTOMERVENDOR’  será enviada duas vezes e em versões diferentes.  
Foi enviado um e-mail para o Erlon para conversar sobre o assunto, para evoluir o conector.

É possível alterar os campos da conta corrente alternativa no processo de **alteração de dados globais / alterações cadastrais / alteração campos do funcionário.**

As informações relativas a conta corrente alternativa não poderão ser importadas juntamente com as demais informações do funcionário.

No portal não haverá cadastro ou alteração da conta corrente alternativa.

## Release Notes

|  |  |
| --- | --- |
| **Módulo** | Encargos – Fop Folha de pagamento |
| **Função** | Criação de campos para possibilitar o cadastro de mais uma conta para o funcionário. |
| **Situação/Requisito** | Necessidade de cadastrar mais de uma conta por funcionário. |
| **Solução/Implementação** | Foram inseridos novos campos na tela de cadastro de funcionário. |
| **Conversores de Parâmetros:** |  |
