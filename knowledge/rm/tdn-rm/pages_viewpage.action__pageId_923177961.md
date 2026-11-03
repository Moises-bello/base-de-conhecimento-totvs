---
content_hash: a729d6a262220e0907494e0ecb9b6c75f68382aa0413809021f2a20287bec142
fetched_at: '2026-06-29T00:12:07.300695+00:00'
page_id: '923177961'
product: rm
source: tdn-rm
title: Registro online Itaú
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=923177961
version: 13
---

# Conteúdo:

Conteúdo:

# 1. Registro online

Esta implementação tem como objetivo preparar o TOTVS Gestão Financeira para utilizar o serviço de registro online de cobrança registrada do banco Itaú.

# 2. Procedimento para configuração

Através do cadastro do Convênio, localizado no menu 'Movimentações Bancárias', é necessário habilitar a opção "Permite registro de boleto online" e definir os parâmetros de acordo com os dados fornecidos pelo banco Itaú. O TOTVS Gestão Financeira disponibiliza dois modelos de registro:

Cards2Modelo de Registro Online v1

* **Permite registro de boleto online:**Define se o convênio permite utilizar o registro de boleto online.
* **Ambiente**: Define o ambiente que será feito o registro do boleto no Banco.
* **Modelo de Registro Online:**Define o modelo do registro online: v1 ou v2.
* **URL do serviço de registro de cobrança**: Deve ser informada a URL do serviço de registro do boleto disponibilizada pelo banco.
* **URL do sistema autorizador**: Deve ser informado a URL do sistema autorizador que retornará o token de acesso ao serviço de registro de cobrança.
* **Chave**: Parâmetro de acesso ao serviço de registro de boleto fornecido pelo banco.
* **Client Id**: Código de acesso ao sistema autorizador fornecido pelo banco.
* **Client Secret**: Senha de acesso ao sistema autorizador fornecido pelo banco.

Conforme detalhado no [item 3](https://tdn.totvs.com/pages/viewpage.action?pageId=923177961#RegistroonlineIta%C3%BA-3.Customiza%C3%A7%C3%A3odedadosnoregistroonline) deste documento, é possível customizar o dado a ser enviado no registro online. Abaixo, seguem alguns exemplos de cadastro de campo no layout do registro online:

**Campo da seção principal**:

* tipo\_carteira\_titulo
* valor\_cobrado

**Campo da seção "juros"**:

* juros.tipo\_juros

**Campo da seção "sacador avalista"**:

* sacador\_avalista.cpf\_cnpj\_sacador\_avalista

**Campo da seção grupo de "desconto"**:

* grupo\_desconto1.data\_desconto
* grupo\_desconto1.tipo\_desconto

3Modelo de Registro Online v2

* **Permite registro de boleto online:**Define se o convênio permite utilizar o registro de boleto online.
* **Ambiente**: Define o ambiente que será feito o registro do boleto no Banco.
* **Modelo de Registro Online:**Define o modelo do registro online: v1 ou v2.
* **URL do serviço de registro de cobrança**: Deve ser informada a URL do serviço de registro do boleto disponibilizada pelo banco.
* **URL do sistema autorizador**: Deve ser informado a URL do sistema autorizador que retornará o token de acesso ao serviço de registro de cobrança.
* **Client Id**: Código de acesso ao sistema autorizador fornecido pelo banco.
* **Client Secret**: Senha de acesso ao sistema autorizador fornecido pelo banco.
* **Certificado digital:** Informe o certificado digital obtido pela empresa.
* **Caminho do arquivo de chave privada:**Informe o caminho onde se encontra o arquivo pertinente a chave privada. Caso o certificado digital for do tipo PKCS #12 (arquivo .pfx) que já contempla a chave privada, não será necessário informar esse caminho.

**IMPORTANTE**: Não é possível efetuar o cancelamento online do registro do boleto na mesma data que ocorreu o registro online. Nesse caso, o cancelamento deverá ser efetuado através do processo de cancelamento de remessa de boleto. Obs: Esta regra é do banco Itaú e não da aplicação.

Conforme detalhado no [item 3](https://tdn.totvs.com/pages/viewpage.action?pageId=923177961#RegistroonlineIta%C3%BA-3.Customiza%C3%A7%C3%A3odedadosnoregistroonline) deste documento, é possível customizar o dado a ser enviado no registro online. Abaixo, seguem alguns exemplos de cadastro de campo no layout do registro online:

**Campo da seção principal**:

* data.dado\_boleto.codigo\_carteira
* data.dado\_boleto.valor\_total\_titulo

**Campo da seção "juros"**:

* data.dado\_boleto.juros.codigo\_tipo\_juros

**Campo da seção "sacador avalista"**:

* data.dado\_boleto.sacador\_avalista.pessoa.nome\_pessoa
* data.dado\_boleto.sacador\_avalista.pessoa.nome\_fantasia
* data.dado\_boleto.sacador\_avalista.pessoa.tipo\_pessoa.numero\_cadastro\_pessoa\_fisica
* data.dado\_boleto.sacador\_avalista.pessoa.tipo\_pessoa.numero\_cadastro\_nacional\_pessoa\_juridica

**Campo da seção grupo de "desconto"**:

* data.dado\_boleto.desconto.codigo\_tipo\_desconto
* data.dado\_boleto.desconto.descontos1.quantidade\_dias\_desconto
* data.dado\_boleto.desconto.descontos1.valor\_desconto
* data.dado\_boleto.desconto.descontos1.percentual\_desconto
* data.dado\_boleto.desconto.descontos1.data\_desconto
* data.dado\_boleto.desconto.descontos2.quantidade\_dias\_desconto
* data.dado\_boleto.desconto.descontos2.valor\_desconto
* data.dado\_boleto.desconto.descontos2.percentual\_desconto
* data.dado\_boleto.desconto.descontos2.data\_desconto
* data.dado\_boleto.desconto.descontos3.quantidade\_dias\_desconto
* data.dado\_boleto.desconto.descontos3.valor\_desconto
* data.dado\_boleto.desconto.descontos3.percentual\_desconto
* data.dado\_boleto.desconto.descontos3.data\_desconto

**Campo da seção "beneficiário"**:

* data.beneficiario.id\_beneficiario

**Campo da seção "protesto"**:

* data.dado\_boleto.protesto.protesto
* data.dado\_boleto.protesto.codigo\_tipo\_protesto
* data.dado\_boleto.protesto.quantidade\_dias\_protesto

**Campo da seção "instrucao\_cobranca" (permitido até 3 instruções de cobrança)**:

* data.dado\_boleto.instrucao\_cobranca1.codigo\_instrucao\_cobranca
* data.dado\_boleto.instrucao\_cobranca1.quantidade\_dias\_apos\_vencimento
* data.dado\_boleto.instrucao\_cobranca1.dia\_util
* data.dado\_boleto.instrucao\_cobranca2.codigo\_instrucao\_cobranca
* data.dado\_boleto.instrucao\_cobranca2.quantidade\_dias\_apos\_vencimento
* data.dado\_boleto.instrucao\_cobranca2.dia\_util
* data.dado\_boleto.instrucao\_cobranca3.codigo\_instrucao\_cobranca
* data.dado\_boleto.instrucao\_cobranca3.quantidade\_dias\_apos\_vencimento
* data.dado\_boleto.instrucao\_cobranca3.dia\_util

**Campo da seção "dados\_individuais\_boleto"**:

* data.dado\_boleto.dados\_individuais\_boleto.data\_vencimento
* data.dado\_boleto.dados\_individuais\_boleto.valor\_titulo
* data.dado\_boleto.dados\_individuais\_boleto.texto\_uso\_beneficiario
* data.dado\_boleto.dados\_individuais\_boleto.texto\_seu\_numero

# 3. Customização de dados no registro online

Pode ser utilizado o [Cadastro de Layout do Registro Online](https://tdn.totvs.com/display/LRM/Layout+Registro+Online), para enviar dados de forma flexível para o registro online dos boletos para o banco. Para isso deve ser feito o [Cadastro de associação de fórmulas e campos do registro online](https://tdn.totvs.com/pages/viewpage.action?pageId=421388759) no cadastro do convênio.

O cadastro do layout do registro online do Itaú deve ser realizado de acordo com o manual de cobrança online do banco. Ressaltamos que o layout da v1 é totalmente diferente da v2, então o cadastro de layout de registro online deve ser refeito na migração da v1 para v2. Demonstramos alguns exemplos de campos nas guias referente a cada modelo de registro online ([item 2](https://tdn.totvs.com/pages/viewpage.action?pageId=923177961#RegistroonlineIta%C3%BA-2.Procedimentoparaconfigura%C3%A7%C3%A3o)).

**IMPORTANTE**:

* De acordo com o layout do banco pode ocorrer 5 (cinco) descontos, portanto o nome do campo deverá ser 'grupo\_desconto1.', 'grupo\_desconto2.' sucessivamente de acordo com número de vezes que ocorre. Seguir a mesma regra para o grupo de rateio e grupo de e-mail do pagador.
* O campo Data da Multa será calculado a partir da Data de Vencimento do boleto acrescido do parâmetro *Dias de Atraso* configurado na etapa Valor Líquido do Lançamento Financeiro.
