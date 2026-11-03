---
content_hash: 059f38eaf3fe7e66c6820cfd9e5093500ede77629de613b17220fce22425ef83
fetched_at: '2026-06-29T00:09:37.470545+00:00'
page_id: '425459616'
product: rm
source: tdn-rm
title: Backoffice RM x Protheus SigaMNT - Cadastro de Cliente / Fornecedor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459616
version: 2
---

**Backoffice** **RM x Protheus SigaMNT - Cadastro de Cliente / Fornecedor**

---

As inclusões, alterações e exclusões de Cliente/Fornecedor são feitos através do Backoffice RM, que identifica o evento em sua entidade e envia uma mensagem ao Protheus SigaMNT . Através da sincronia de dados o Protheus pode utlizar os Cliente / Fornecedor enviados, em seus processos de Manutenção de Ativos.   
    
 Passo 1 – Acessar  Linha / Gestao de Estoque, Compras e Faturamento / Cadastros / Financeiros  / Cliente – Fornecedor.

Passo 2 – Incluir um novo Cliente / Fornecedor.

Passo 3 – Preencher os campos  conforme desejado  e Salvar.

O sistema também permite cadastrar um fornecedor , selecionando a classificação como Fornecedor.  
    
 **Os dados sincronizados pela mensagem única são :**  
    
 **Aba Identificação:**

* Ativo
* Categoria
* Cliente/Fornecedor
* CPF / CNPJ
* Global
* Inscrição Estadual
* Inscrição municipal
* Nome
* Nome Fantasia
* Tipo de Cliente/Fornecedor

**Aba Dados Adicionais:**

* Limite de crédito

**Aba Endereço / Principal:**

* Bairro
* Cep
* Cód.Municipio /Descricao da Cidade
* complemento
* Email
* Estado / Descrição do Estado
* Fax
* Numero
* Pais / Descrição do Pais
* Rua
* Telefone

**Aba Endereço / Pagamento:**

* Bairro
* Caixa Postal
* CEP
* Cód.Municipio /Descricao da Cidade
* Complemento
* Estado / Descrição do Estado
* Numero
* Pais / Descrição do Pais
* Rua

**Anexos / Condições de Pagamento Default para Cliente  | Fornecedor:**

* Condição de Pagamento Compra

  Passo 4- Acessar:Sistema Protheus , módulo SigaMNT Passo 5– Efetuar uma pesquisa de funcionalidade   :   Clientes Passo 6- Acessar: Compras / Atualizações  / Cadastros  / Clientes ou Faturamento / Atualizações / Cadastros / Clientes  . Passo 7– O sistema Protheus  exibe o cliente cadastrado  . Para visualizar os campos do cadastro preenchidos  ,clicar em Visualizar.   Os campos  abaixo  foram preenchidos através da integração Linha RM x Protheus SigaMNT e estão liberados apenas para visualização ou utilização em processos.

* Bairro Entr.
* Bloqueado
* Bairro Cob
* Codigo
* Complemento
* Cd Municipio
* CEP
* CNPJ/CPF
* Caixa Postal
* Cep Entr
* Cd Mun Entre
* Contato
* Cep de Cobr.
* Dt.Aber/Nasc
* Endereco
* E-Mail
* End. Cobranca
* End. Entrega
* Fisica/Jurid
* FAX
* Home-Page
* Insc. Estad.
* Ins. MunicipLoja
* Municipio
* Mun. entr
* Mun.Cob
* Nome
* N Fantasia
* SUFRAMA
* Telefone
* Tipo
* Uf de Cobr.
* Uf Entr

**Observações:**

1.  O Cliente / Fornecedor pode ser considerado como Federal, Estadual ou municipal , de acordo com as seleções abaixo informadas :

* + **Federal** : Informado o CPF / CNPJ e o País.
  + **Estadual** : Informado o CPF / CNPJ e o Estado
  + **Municipal** : Informada a Cidade e a Inscrição Municipal

2. O cadastro de Cliente / Fornecedor , feito utilizando a integração Backoffice RM x Protheus SigaMNT não envia através da mensagem única os campos dos Anexos Informações Bancárias e Contato do Cli / For.

3.  Lista de Contatos: Mesmo sendo enviados na mensagem, os dados de contatos não são inseridos no Protheus.

4.   Dados Bancários: Mesmo sendo enviados na mensagem, os dados bancários não são inseridos no Protheus.

5.   Condições de pagamento: Os dados de condições de pagamento não são contemplados na versão 1.000 da mensagem.

6.   A mensagem de resposta do PROTHEUS não está enviando o ReturnContent contendo os campos chaves. Desta maneira o De-Para RM ficará com dados já excluídos, inutilmente.

7.   Uma vez que o Cliente e Fornecedor são tratados na mesma mensagem (CustomerVendor), é responsabilidade do destinatário ao processar a mensagem garantir a consistência dos dados na origem e no destino da melhor forma possível.Ou seja, se o destino implementa uma única tabela, terá que manipular apenas um registro e se implementa mais de uma tabela, terá que manipular quantos registros forem necessários.

8.   Mesmo que a empresa não utilize Cliente/Fornecedor global no RM, deve-se compartilhar a tabela referente no Protheus por empresa.

9.   No Protheus o código do cliente fornecedor deverá ser autoincremento.

Os dados informados na aba Endereço / Principal podem ser replicados para as sub-abas, Pagamento e Entrega, através dos ícones de copiar.

O módulo SigaMNT não possui um menu para visualização dos cadastros de cliente, sendo possível acessá-lo somente através da pesquisa.

O campo Condição de Pagamento Compra, informado através do anexos, só será liberado após salvar o cadastro de Cliente / Fornecedor.Para que ele seja enviado através da mensagem única é necessário atualizar o cadastro de Cliente / Fornecedor após inserir o registro de condição de pagamento default para Cliente / Fornecedor.

---

Para mais detalhes sobre o cadastro , acese o Boletim Técnico.

**Recursos Adicionais**

TDN - Boletim Técnico : [Cliente/Fornecedor](http://tdn.totvs.com/download/attachments/76251248/CONNECTOR_BT_CADASTRAR+CLIENTE+OU+FORNECEDOR_BR_CON000158.pdf?version=1&modificationDate=1380044679000)
