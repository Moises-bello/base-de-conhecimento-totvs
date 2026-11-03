---
content_hash: 87138705b6518a06a840dcab3463c05f0fa2238bade5565378bd3229a100b1d7
fetched_at: '2026-06-29T00:06:07.216895+00:00'
page_id: '201735957'
product: rm
source: tdn-rm
title: DT_Cadastro_Conta_Funcionario
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Cadastro_Conta_Funcionario
version: 11
---

# CADASTRO DE UMA CONTA PARA O FUNCIONÁRIO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Folha de Pagamento* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Funcionário* | *Cadastro de Funcionário* | |
| **Versão:** | *12.1.6* |

## Descrição

O Totvs Folha de Pagamento possibilita o cadastro de uma conta para o funcionário. Usualmente essa conta é a conta salário do funcionário. Como não é possível pagar estornos em conta salário, foi criada a conta bancária alternativa no cadastro de funcionários.  
Foi criado também um processo para incluir um Cliente/Fornecedor através do cadastro de um funcionário, copiando também os dados bancários do funcionário. Esse Cliente/Fornecedor será utilizado para geração dos lançamentos de estorno, e outros pagamentos para os funcionários.  
Foi adicionada uma mensagem de envio, para que os Clientes/Fornecedores RM, e seus dados bancários sejam enviados automaticamente para o Protheus, quando houver uma integração entre Folha de Pagamento e BackOffice Protheus

## Procedimento para Utilização

Para cadastro de funcionários, serão adicionados a tabela PFUNC como nos campos abaixo, que serão responsáveis por armazenar uma segunda conta.

 -PFUNC.CODAGENCIAPAGTO2

-PFUNC.CODBANCOPAGTO2

-PFUNC.CONTAPAGAMENTO2

-PFUNC.OPBANCARIA2

-PFUNC.TPCONTABANCARIA2

Na tela de cadastro os novos campos serão adicionados na seção “Banco Pagto/Financeiro”.

No histórico, serão adicionados a tabela PFHSTCPGTO conforme os campos abaixo:

 -PFUNC.TPCONTABANCARIA

- PFHSTCPGTO.PRINCIPAL (S = Conta Principal, N = Conta Alternativa)

 Nova chave primária:

 -CODCOLIGADA, CHAPA, DTMUDANCA, PRINCIPAL

Ao salvar o histórico, será verificado qual é o tipo de conta. Quando a alteração for na Conta Principal será gravado automaticamente o valor PRINCIPAL = 1, quando for a Conta Alternativa será gravado o valor PRINCIPAL = 2.

Na tela de cadastro do histórico será adicionado um RadioGroup para que possa ser selecionada a Classificação da Conta, no caso de inserção manual de histórico

 Ao solicitar o script para criação do campo TPCONTA, será criado também um script de UPDATE para atualizar o valor do novo campo para 1 (Conta Principal) para todos os registros existentes, visto que atualmente não existe Conta Alternativa.

Para a criação de cliente fornecedor, foi criado um processo para gerar um registro de Cliente/Fornecedor automaticamente através do cadastro de funcionário

 O Cliente/Fornecedor criado terá os mesmos dados que o funcionário.

A conta bancária a ser cadastrada nos dados bancários do CliFlor poderá ser escolhida entre as contas Principal e Alternativa do funcionário.

 O novo Cliente/Fornecedor será associado ao cadastro do funcionário automaticamente. Essa associação pode também ser feita manualmente através do campo **Fornecedor Lançamento Financeiro**, na seção Banco Pagto/Financeiro do cadastro de funcionário.  
  
 

Ao executar o novo processo existem 3 possibilidades:

1. Funcionário não possui Cliente/Fornecedor associado, e não existe cadastro de Cliente/Fornecedor com o seu CPF.

 No processo deverá ser informado um código para o cliente/fornecedor e escolhida uma conta bancária entre as contas bancárias alternativa e principal.  
  
 

Será inserido e associado ao usuário um registro de Cliente/Fornecedor (FCFO). Será inserido um registro de Dados Bancários (FDADOSPGTO).

 2. Funcionário não possui Cliente/Fornecedor associado, mas existem um ou mais registros de Cliente/Fornecedor com o seu CPF.

 Serão exibidos os registros de Cliente/Fornecedor encontrados, o usuário poderá escolher um deles para associar ao funcionário, ou escolher criar um novo.

Caso seja utilizado um Cliente/Fornecedor já existente, a próxima etapa exibirá o Cliente/Fornecedor, não precisando informar o código.  
  
  
 A conta bancária a ser cadastrada nos dados bancários do CliFlor poderá ser escolhida entre as contas Principal e Alternativa do funcionário.

Será inserido registro de Dados Bancários apenas (FDADOSPAGTO). O Cliente/Fornecedor será associado ao usuário, mas não sofrerá alterações.

3. Funcionário possui Cliente/Fornecedor associado.  
Será exibido o Cliente/Fornecedor que está associado, não precisando informar o código. A conta bancária a ser cadastrada nos dados bancários do CliFlor poderá ser escolhida entre as contas Principal e Alternativa do funcionário.

**Obs:** Quando incluindo um novo Cliente/Fornecedor será solicitado um código para o mesmo. Esse código obedece a uma máscara que pode ser definida nos Parâmetros Gerais do Totvs Gestão Financeira (**Contas a Pagar / Manutenção de Lançamentos / Lançamento**). Caso a máscara definida seja numérica, é possível marcar o parâmetro ‘Usar código sequencial’, caso marcado, o código será gerado automaticamente, não precisando informa-lo ao executar o processo.
