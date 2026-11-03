---
content_hash: 220aeef05ce99e65a2216bdc75117565adc2f9a110ebcd2e39d77cc50141f272
fetched_at: '2026-06-29T00:08:32.624785+00:00'
page_id: '273993534'
product: rm
source: tdn-rm
title: DT Registro Boleto Online Itaú
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=273993534
version: 130
---

# Registro Boleto Online Itaú

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção & Projetos* |
| **Módulo:** | **TOTVS Gestão Financeira** |
| **Requisito/S****tory/Issue:** | *FINANCEIRO01-24* |

## Descrição

Esta implementação tem como objetivo preparar o TOTVS Gestão Financeira para utilizar o serviço de registro online de cobrança registrada do Banco Itaú.

## Procedimento para Configuração

No TOTVS Gestão Financeira, menu *Movimentações Bancárias | Controle Bancário | Convênio,* devem ser feitas as configurações do convênio para o registro de boleto online:

* **Permite registro de boleto online:**Define se o convênio permite utilizar o registro de boleto online.
* **Ambiente**: Define o ambiente que será feito o registro do boleto no Banco.
* **Modelo de Registro Online:**Define o modelo do registro online: v1 ou v2. Caso o certificado digital No modelo v2 o ambiente de teste não irá salvar Código de barras e  IPTE, pois é apenas um ambiente para validação.
* **URL do serviço de registro do boleto**: Deve ser informada a URL do serviço de registro do boleto disponibilizada pelo Banco.
* **URL do sistema autorizador**: Deve ser informado a URL do sistema autorizador que retornará o token de acesso ao serviço de registro de cobrança.
* **Chave**: Parâmetro de acesso ao serviço de registro de boleto fornecido pelo Banco (campo disponível somente no modelo "v1")
* **Client Id**: Código de acesso ao sistema autorizador fornecido pelo Banco.
* **Client Secret**: Senha de acesso ao sistema autorizador fornecido pelo Banco.
* **Certificado digital:** Informe o certificado digital obtido pela empresa (campo disponível somente no modelo "v2")
* **Caminho do arquivo de chave privada:**Informe o caminho onde se encontra o arquivo pertinente a chave privada (campo disponível somente no modelo "v2"). Caso o certificado digital for do tipo PKCS #12 (arquivo .pfx) que já contempla a chave privada, não será necessário informar esse caminho.

**Atenção**:

* Deve ser informado o CNPJ do beneficiário/cedente na página Dados Adicionais.

Pode ser utilizado o [Cadastro de Layout do Registro Online](http://tdn.totvs.com/pages/viewpage.action?pageId=311625508), para enviar dados de forma flexível para o registro online dos boletos para o banco. Para isso deve ser feito o [Cadastro de associação de fórmulas e campos do registro online](http://tdn.totvs.com/pages/viewpage.action?pageId=307835775) no cadastro do convênio.

O cadastro do layout do registro online do Itaú deve ser feita de acordo com o manual de cobrança online do banco, da seguinte maneira:

Obs.: O Layout da v1 é totalmente diferente da v2, então o cadastro de layout de registro on-line deve ser refeito na migração da v1 para v2. Veja abaixo alguns exemplos:

Exemplos para os campos da seção principal:

* v1
  + tipo\_carteira\_titulo
  + valor\_cobrado
* v2
  + data.dado\_boleto.codigo\_carteira
  + data.dado\_boleto.valor\_total\_titulo

Exemplo para os campos da seção "juros":

* v1
  + juros.tipo\_juros
* v2
  + data.dado\_boleto.juros.codigo\_tipo\_juros

Exemplos para os campos da seção "sacador avalista":

* v1
  + sacador\_avalista.cpf\_cnpj\_sacador\_avalista

* v2
  + data.dado\_boleto.sacador\_avalista.pessoa.nome\_pessoa
  + data.dado\_boleto.sacador\_avalista.pessoa.nome\_fantasia
  + data.dado\_boleto.sacador\_avalista.pessoa.tipo\_pessoa.numero\_cadastro\_pessoa\_fisica
  + data.dado\_boleto.sacador\_avalista.pessoa.tipo\_pessoa.numero\_cadastro\_nacional\_pessoa\_juridica

Exemplos para os campos da seção grupo de "desconto":

* v1
  + grupo\_desconto1.data\_desconto
  + grupo\_desconto1.tipo\_desconto

* v2
  + data.dado\_boleto.desconto.codigo\_tipo\_desconto
  + data.dado\_boleto.desconto.descontos1.quantidade\_dias\_desconto
  + data.dado\_boleto.desconto.descontos1.valor\_desconto
  + data.dado\_boleto.desconto.descontos1.percentual\_desconto
  + data.dado\_boleto.desconto.descontos2.quantidade\_dias\_desconto
  + data.dado\_boleto.desconto.descontos2.valor\_desconto
  + data.dado\_boleto.desconto.descontos2.percentual\_desconto
  + data.dado\_boleto.desconto.descontos3.quantidade\_dias\_desconto
  + data.dado\_boleto.desconto.descontos3.valor\_desconto
  + data.dado\_boleto.desconto.descontos3.percentual\_desconto

Exemplo para os campos da seção "beneficiário":

* v2
  + data.beneficiario.id\_beneficiario

Exemplos para os campos da seção "protesto":

* v2
  + data.dado\_boleto.protesto.protesto
  + data.dado\_boleto.protesto.codigo\_tipo\_protesto
  + data.dado\_boleto.protesto.quantidade\_dias\_protesto

Exemplos para os campos da seção "instrucao\_cobranca"

* v2 - Permitido até 3 instrução de cobrança
  + data.dado\_boleto.instrucao\_cobranca1.codigo\_instrucao\_cobranca
  + data.dado\_boleto.instrucao\_cobranca1.quantidade\_dias\_apos\_vencimento
  + data.dado\_boleto.instrucao\_cobranca1.dia\_util
  + data.dado\_boleto.instrucao\_cobranca2.codigo\_instrucao\_cobranca
  + data.dado\_boleto.instrucao\_cobranca2.quantidade\_dias\_apos\_vencimento
  + data.dado\_boleto.instrucao\_cobranca2.dia\_util
  + data.dado\_boleto.instrucao\_cobranca3.codigo\_instrucao\_cobranca
  + data.dado\_boleto.instrucao\_cobranca3.quantidade\_dias\_apos\_vencimento
  + data.dado\_boleto.instrucao\_cobranca1.dia\_util

Exemplos para os campos da seção "dados\_individuais\_boleto"

* v2
  + data.dado\_boleto.dados\_individuais\_boleto.data\_vencimento
  + data.dado\_boleto.dados\_individuais\_boleto.valor\_titulo
  + data.dado\_boleto.dados\_individuais\_boleto.texto\_uso\_beneficiario
  + data.dado\_boleto.dados\_individuais\_boleto.texto\_seu\_numero

**IMPORTANTE:**

* De acordo com o layout do banco pode ocorrer 5 (cinco) descontos, portanto o nome do campo deverá ser 'grupo\_desconto1.', 'grupo\_desconto2.' sucessivamente de acordo com número de vezes que ocorre. Seguir a mesma regra para o grupo de rateio e grupo de e-mail do pagador.
* O campo Data da Multa será calculado a partir da Data de Vencimento do boleto acrescido do parâmetro *Dias de Atraso* configurado na etapa Valor Líquido do Lançamento Financeiro.
* Ao utilizar o modelo 'v2' do registro online, não será possível efetuar o cancelamento online do registro do boleto na mesma data que ocorreu o registro online. Nesse caso, o cancelamento deverá ser efetuado através do processo de cancelamento de remessa de boleto. Obs: Esta regra é do Banco Itaú e não da aplicação.

divs
