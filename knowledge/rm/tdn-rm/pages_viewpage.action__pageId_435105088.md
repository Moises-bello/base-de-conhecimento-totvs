---
content_hash: aaefba722c4c2773af6d17a8001ba616c5326432057268b3e2968375d4cfebc2
fetched_at: '2026-06-29T00:09:47.856098+00:00'
page_id: '435105088'
product: rm
source: tdn-rm
title: Dados Complementares (TCGI)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105088
version: 8
---

**Dados Complementares (TCGI)**   
Nesta opção de menu serão inseridos os Dados Complementares do Cliente, que são utilizados apenas para o contexto do TCGI.

Através do cadastro é possível controlar:

##### **Aba Identificação** Ao cadastrar ou editar os Dados Complementares do Cliente, abrirá a janela de edição, na pasta Identificação, onde iremos cadastrar os seguintes campos:

**Coligada**: Este campo já estará preenchido automaticamente com a coligada corrente.  
**Cliente/Fornecedor**: Este campo já estará preenchido com o código do cliente selecionada na tela de visão de clientes.  
**Profissão**: Informe a profissão do cliente, o sistema apresentará na lista de opções as profissões já previamente cadastradas através do Menu Cadastro | Tabelas Adicionais | Profissões.  
**Estado Civil**: O Está civil será carregado automaticamente de acordo com o preenchido no cadastro do cliente/fornecedor na aba **Identificação**.

Atenção!

O campo "Estado Civil" dos dados complementares do TCGI, passa a ser herdado diretamente da aba Identificação do cadastro do Cliente Pessoa Física:

.  
- Para que seja carregado corretamente nos dados complementares do TCGI.  
     1 - No cadastro de estado civil do TCGI deverá ser informado para qual estado civil do financeiro está vinculado.  
     2 - Para vincular o estado civil do Financeiro com o do TCGI vá em: Venda | Gerais (Cadastros) | Estado Civil  
     3 - Preencha o campo "Código do Vinculo com a Tabela Estado Civil Global - Utilizar o Valor do Campo CODCLIENTE"  
[Saiba mais sobre estado civil!](https://tdn.totvs.com/display/public/LRM/Estado+Civil)

**Naturalidade**: Informe a Naturalidade do cliente, o sistema apresentará na lista de opções as Naturalidades já previamente cadastradas no sistema.  
**Nacionalidade**: Informe a Nacionalidade do cliente, o sistema apresentará na lista de opções as Nacionalidades já previamente cadastradas no sistema.  
**Sexo**: Informe o sexo do cliente, o sistema apresentará 2 opções (masculino / feminino) para marcar a opção desejada.  
**Data Nascimento**: É preenchida automaticamente conforme o cadastro do cliente/fornecedor.  
**Nome do Pai**: Informe o nome do Pai do cliente.  
**Nome da Mãe**: Informe o nome da Mãe do cliente.  
**Paga Aluguel**: Informe se o cliente paga aluguel, o sistema apresentará 2 opções (sim / não) para marcar a opção desejada.   
**Casa Própria**: Informe se o cliente tem Casa Própria, o sistema apresentará 2 opções (sim / não) para marcar a opção desejada.

##### **Aba Ocupação Profissional** Ao cadastrar ou editar os Dados Complementares do Cliente nesta aba, informe os seguintes campos: **Nome Empresa**: Nome da empresa em que o cliente trabalha; **Endereço**: Nome da rua, Avenida, praça, etc, da empresa; **Número**: Número do endereço da empresa; **Complemento**: Complemento do endereço da empresa; **Bairro**: Bairro da empresa; **Cidade**: Cidade da empresa; **UF**: Estado da empresa, o sistema apresentará uma lista com todos os estados já previamente cadastrados; **CEP**: CEP da empresa; **Telefone Comercial**: Telefone comercial da empresa; **Ramal**: Ramal do cliente na empresa; **Fax**: Fax do Cliente na empresa; **Data Admissão**: Data de Admissão do cliente na empresa; **Cargo**: Cargo do Cliente na empresa; **Renda Familiar**: Renda Familiar do cliente;

**Tipo de Integração:**Na nova versão do ***Módulo de Comissão 2.0*** foi liberado o cadastro do tipo de integração de comissão para o pagamento do cliente/fornecedor. Se o tipo escolhido for TOTVS Folha de Pagamento, o sistema habilita a opção de cadastro de chapa do funcionário. Na nova versão do módulo de Comissão, ao gerar a comissão, o sistema verificará o tipo de integração do Cliente/For e buscará a chapa que está preenchida e utilizará na comissão.

##### **Aba Referências**

Ao cadastrar ou editar os Dados Complementares do Cliente nesta aba, informe os seguintes campos:  
**Referências Bancárias**: Banco: Informe o código de um banco para referência; Agência: Informe a agência do banco de referência; Telefone: Informe o telefone do contato; Contato: Informe o nome de um contato no banco;  
**Referências Comerciais**: Empresa: Informe o nome de uma empresa ou loja para referências comerciais; Contato: Informe o nome de um contato na empresa; Telefone: Informe o telefone do contato;  
**Referências Particulares**: Nome: Informe o nome de um contato pessoal para referências; Telefone: Informe o telefone do contato;  
   
Observações: O anexo de Dados complementares do TIN também será copiado quando utilizar o processo de cópia de Cliente/Fornecedores entre coligadas.

##### **Aba Comissão/Responsável**

Ao cadastrar ou editar os Dados Complementares do Cliente nesta aba, informe os seguintes campos:

**Tipo de Integração Receberá a Comissão por:** Selecione o **Tipo de Integração**, pela qual este Cliente irá receber o pagamento da Comissão

* TOTVS Gestão de Estoque, Compras e Faturamento;
* TOTVS Folha de Pagamento;
* TOTVS Gestão Financeira; ou
* Sem Integração.

**Pagar Comissão para Imobiliária da Proposta:** selecione se a Comissão a ser paga para este Cliente deverá ser paga diretamente para ele ou para a Imobiliário (que fará o repasse deste valor por meios próprios).

**Representante Legal:** Preencha informações abaixo se este Cliente é um Representante Legal:

**Tipo****Responsável:** Informe a forma de atuação da representação Legal deste Cliente:

* Procurador; ou
* Administrador.

**Código Responsável:** Selecione o cadastro de **Cliente Pessoa Física** deste Representante Legal.
