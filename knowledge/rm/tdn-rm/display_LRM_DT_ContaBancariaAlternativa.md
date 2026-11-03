---
content_hash: f62f938959115bd1ce19b593a5e0c56e27c9cb0f727731ea46322850380add2c
fetched_at: '2026-06-29T00:06:23.079460+00:00'
page_id: '223931761'
product: rm
source: tdn-rm
title: DT_ContaBancariaAlternativa
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_ContaBancariaAlternativa
version: 2
---

# CADASTRO FUNCIONÁRIO: CONTA BANCÁRIA ALTERNATIVA

## Características do Requisito

  

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **TOTVS Folha de Pagamento** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Cadastro de Funcionário* | *Inclusão de Cliente/Fornecedor* | |
| **Versões/Release:** | 12.1.10 |

## Descrição

O Totvs Folha de Pagamento possibilita o cadastro de uma conta bancária para o funcionário, sendo que esta se trata de uma conta salário, mas como não é possível o pagamento de reembolsos em conta salário foi criada a “Conta bancária alternativa” no cadastro de funcionários.

Também foi criado um processo para incluir um Cliente/Fornecedor através do cadastro de um funcionário, copiando os dados bancários do mesmo. Esse Cliente/Fornecedor será utilizado para geração dos lançamentos de reembolso, e outros pagamentos para os funcionários. Além disso, uma mensagem de envio foi adicionada para que os Clientes/Fornecedores RM e seus dados bancários sejam enviados automaticamente para o Protheus quando houver uma integração entre Folha de Pagamento e BackOffice Protheus.

## Procedimento para Utilização

**Cadastro de Contas Bancárias**No cadastro de Funcionários foram adicionados campos para possibilitar o cadastro de mais de uma conta bancária, que é chamada de “Conta Bancária Alternativa”.

No cadastro de “Histórico de Dados Bancários” foi adicionado um campo para informar se o histórico é referente a “Conta Principal” ou a “Conta Alternativa”. Para visualizar o novo campo em “Histórico de Dados Bancários” acesse **Funcionário / Banco Pgto Financeiro / Anexos / Histórico / Histórico de Dados Bancários.**

**Inclusão de Cliente/Fornecedor através de processo**

Foi criado o processo ‘Inclusão de Cliente/Fornecedor’ no cadastro de Funcionários.

Ao executar o novo processo existem 3 possibilidades, de acordo com os dados do funcionário.

1. Funcionário não possui Cliente/Fornecedor associado, e não existe cadastro de Cliente/Fornecedor com o seu CPF.

No processo deverá ser informado um código para o cliente/fornecedor e escolhida uma conta bancária entre “Alternativa” e “Principal”. Será inserido e associado ao usuário um registro de Cliente/Fornecedor (FCFO) e também um registro de Dados Bancários (FDADOSPGTO).

2. Funcionário não possui Cliente/Fornecedor associado, mas existem um ou mais registros de Cliente/Fornecedor com o seu CPF.  
Serão exibidos os registros de Cliente/Fornecedor encontrados, o usuário poderá escolher um deles para associar ao funcionário, ou escolher criar um novo.

2.1 Caso seja utilizado um Cliente/Fornecedor já existente, a próxima etapa exibirá o Cliente/Fornecedor, não precisando informar o código. A conta bancária a ser cadastrada nos dados bancários do CliFlor poderá ser escolhida entre as contas “Principal” e “Alternativa” do funcionário.  
Será inserido registro de Dados Bancários apenas (FDADOSPAGTO). O Cliente/Fornecedor será associado ao usuário, mas não sofrerá alterações.

2.2 Caso seja selecionada a opção “Criar um novo Cliente/Fornecedor”, deverá ser informado um código para o cliente/fornecedor e escolhida uma conta bancária entre “Alternativa” e “Principal”.  
Será inserido e associado ao usuário um registro de Cliente/Fornecedor (FCFO) e também um registro de Dados Bancários (FDADOSPGTO).

3. Funcionário possui Cliente/Fornecedor associado.  
Será exibido o Cliente/Fornecedor que está associado, não precisando informar o código. A conta bancária a ser cadastrada nos dados bancários do CliFlor poderá ser escolhida entre as contas “Principal” e “Alternativa” do funcionário.  
Será inserido e associado ao usuário um registro de Cliente/Fornecedor (FCFO) e também um registro de Dados Bancários (FDADOSPGTO).

A associação do Cliente/Fornecedor poderá ser feita a partir do campo “Fornecedor Lançamento Financeiro” que se encontra na tela de edição do funcionário em **Funcionário / Banco Pgto|Financeiro** como mostra a imagem abaixo:

**Integração Automática**

Deve ser configurada a integração “TOTVS Folha pagto RM x Backoffice Protheus” para que a mensagem CUSTOMERVENDOR seja enviada automaticamente, ao criar, alterar, ou excluir um Cliente/Fornecedor, ou Dados Bancários do Cliente/Fornecedor.

Para configurar a integração acesse **Integração / Ferramentas / Configurar,** preencha os campos obrigatórios “Usuário” e “Senha”, em seguida clique no botão “Testar Conexão” e avance. Na próxima tela, marque a integração “TOTVS Folha de Pgto RM x BackOffice Protheus” avance novamente e execute.

Após incluir a integração, edite a mesma e informe a URL do Webservice de integração. É importante que o webservice Protheus também esteja integrado e configurado.

**Novo Parâmetro de Integração**

Foi criado o parâmetro RH\_CODCLASSIFICPAIS onde o valor desse parâmetro deve ser o código da tabela de classificação de país. Pois a tabela Protheus é diferente da Tabela Rm, sendo assim é preciso configurar este parâmetro para que não ocorra nenhum problema ao executar a integração.  
No exemplo abaixo, “Integração Protheus” foi cadastrada com o código 4 portanto, devemos configurar o valor 4 para esse parâmetro. Para verificar o código do país na tabela acesse **BackOffice / Gestão Fiscal / Mais... / Endereços / Classificação de País.**

A tabela de classificação de país permite configurar um código diferente para os países. No exemplo abaixo, o código do Brasil na tabela “Integração Protheus” é 150, diferente do código 1, que é o código principal da tabela. **Backoffice / Gestão Fiscal / Mais... / Países / Anexo / Codificação de País**

Ao enviar a mensagem será enviado o código de país referente a tabela parametrizada (RH\_CODCLASSIFICPAIS). De acordo com os exemplos acima, seria enviado o código 150, referente a tabela “Integração Protheus”. E para configurar o valor do parâmetro RH\_CODCLASSIFICPAIS acesse **Integração / Mensagem Única / Integrações** / **Anexos / Parâmetros de Integração.**

## Informações Adicionais

Quando incluindo um novo Cliente/Fornecedor, através do cadastro ou através do processo “Inclusão de Cliente/Fornecedor”, será solicitado um código para o mesmo. Esse código obedece a uma máscara que pode ser definida nos Parâmetros Gerais do Totvs Gestão Financeira (**Ambiente / Parâmetros / TOTVS Gestão Financeira).**

Dentro do parametrizador acesse **Contas a Pagar/Receber / Manutenção de Lançamentos / Lançamentos,** caso a máscara definida seja numérica, é possível marcar o parâmetro “Usar código sequencial”, caso marcado, o código será gerado automaticamente, não precisando informa-lo ao executar o processo.
