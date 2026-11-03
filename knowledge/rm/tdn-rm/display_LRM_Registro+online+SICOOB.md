---
content_hash: aada4f59977ea5c7876f021958a98f7394290739ed405aaa5d8ea366754279eb
fetched_at: '2026-06-29T00:10:44.417152+00:00'
page_id: '552577668'
product: rm
source: tdn-rm
title: Registro online SICOOB
type: documentation
url: https://tdn.totvs.com/display/LRM/Registro+online+SICOOB
version: 35
---

# Conteúdo:

Conteúdo:

# 1. Registro online

Este recurso tem como objetivo preparar o TOTVS Gestão Financeira para utilizar o serviço de registro online da carteira de cobrança registrada do Banco SICOOB.

ProcedimentoConfiguracao

# 2. Procedimento para configuração

Através do cadastro do Convênio, localizado no menu 'Movimentações Bancárias', é necessário habilitar a opção "Permite registro de boleto online" e definir os parâmetros de acordo com os dados fornecidos pelo banco Sicoob. O TOTVS Gestão Financeira disponibiliza três modelos de registro:

Cards2Modelo de Registro Online v1

* **URL do serviço de registro do boleto**: Deve ser informada a URL do serviço de registro do boleto disponibilizada pelo Banco
* **URL do sistema autorizador**: Deve ser informada a URL do serviço de autorização disponibilizado pelo Banco
* **Client Id e****Client Secret**: Código do sistema de autorização fornecido pelo Banco
* **URL de Callback:** URL de Callback que deve ser informada na geração do código de autorização, onde o mesmo será exibido. ([http://[servidor]/Corpore.Net/Source/Fin-Financeiro/RM.Fin.Banco/SicoobCallback.aspx](http://localhost/Corpore.Net/Source/Fin-Financeiro/RM.Fin.Banco/SicoobCallback.aspx))
* **Código de autorização:**Código de acesso do sistema de autorização para criação de tokens. Deve ser gerada no portal do Banco.

**Importante**:

* O campo "Refresh token" está disponível apenas no modelo de registro online "v1". Ao ser gerado o código de autorização e informado no cadastro do convênio, deve ser obtido o refresh tokenclicando no botão. Esse refresh token será usado para obter o acess token necessário para registro do boleto no banco. Somente é preciso obter o refresh token uma vez
* O código de autorização expira em 5 minutos, ou seja, o mesmo deve ser utilizado nesse tempo para obter o refresh token

**Exemplo de geração do código de autorização.**

A URL para gerar o código de autorização tem o seguinte formato:

<https://api.sisbr.com.br/auth/oauth2/authorize?response_type=code&redirect_uri=[[callback_url]]&client_id=[[client_id]]&versaoHash=3&scope=[[escopos>]], onde

[[[callback\_url]]](https://api.sisbr.com.br/auth/oauth2/authorize?response_type=code&redirect_uri=[[callback_url]]&client_id=[[client_id]]&versaoHash=3&scope=[[escopos) = URL de callback informada no convênio

[[[client\_id]]](https://api.sisbr.com.br/auth/oauth2/authorize?response_type=code&redirect_uri=[[callback_url]]&client_id=[[client_id]]&versaoHash=3&scope=[[escopos) = client id informado no convênio

[[[escopos](https://api.sisbr.com.br/auth/oauth2/authorize?response_type=code&redirect_uri=[[callback_url]]&client_id=[[client_id]]&versaoHash=3&scope=[[escopos)]] = cobranca\_boletos\_incluir

3Modelo de Registro Online v2

                                                           

* **URL do serviço de registro do boleto**: Deve ser informada a URL do serviço de registro do boleto disponibilizada pelo Banco
* **URL do sistema autorizador**: Deve ser informada a URL do serviço de autorização disponibilizado pelo Banco
* **Client Id** : Código do sistema de autorização fornecido pelo Banco
* **Certificado digital:**Certificado digital cadastrado junto ao Banco para o registro de boleto online.

**Importante**:

* O Modelo de registro online "v2" está disponível a partir do patch 12.1.2302.**152**.
* Informações de como gerar o certificado é necessário verificar as instruções disponíveis na documentação da API. Dúvidas a respeito, recomendamos entrar em contato com o suporte do Banco.

<https://developers.sicoob.com.br/portal/documentacao?slugItem=apis-do-sicoob&slugSubItem=primeiros-passos>

<https://developers.sicoob.com.br/portal/documentacao?slugItem=seguranca&slugSubItem=certificado-digital>

**Notas:**

* Se no lançamento financeiro o campo 'Multa' for maior que 0 (zero), a tag *tipoMulta* será preenchida com o valor "1". Do contrário, se multa ao dia for maior que 0 (zero), a tag será preenchida com o valor "2". Por último, quando ambos 0 (zero), esta tag será preenchida com o valor "0"
* Para os dois primeiros casos a tag *dataMulta* será preenchida com a data de vencimento acrescida do campo "Dias atraso multa". No último caso, será preenchida com valor nulo.
* Códigos da Multa, segundo o Sicoob:

         '0' = Isento   
         '1' = Valor Fixo   
         '2' = Percentual

* Se no lançamento financeiro o valor de juros ao dia for maior que 0 (zero) e o tipo de juros ao dia como "Valor", a tag *tipoJurosMora* será gerada com o valor "1". Caso contrário, se o campo 'Juros' for maior que 0 (zero), a tag será preenchida com o valor "2". Por último, se ambos valores de juros for igual a 0 (zero) esta tag será preenchida com o valor "0"
* Para os dois primeiros casos a tag *dataJurosMora* será preenchida com a data de vencimento acrescida da carência de juros (campo do lançamento financeiro). No último caso, será preenchida com valor nulo.
* Código do Juros de Mora, segundo o SICOOB:

         '0' = Isento   
         '1' = Valor por Dia   
         '2' = Taxa Mensal 

Conforme detalhado no  deste documento, é possível customizar o dado a ser enviado no registro online. Abaixo, seguem alguns exemplos de cadastro de campo no layout do registro online:

**Campo da seção principal**:

* numeroContrato
* modalidade
* numeroContaCorrente
* especieDocumento
* dataEmissao
* nossoNumero
* seuNumero
* identificacaoBoletoEmpresa
* identificacaoEmissaoBoleto
* identificacaoDistribuicaoBoleto
* valor
* dataVencimento
* dataLimitePagamento
* valorAbatimento
* tipoDesconto
* dataPrimeiroDesconto
* valorPrimeiroDesconto
* dataSegundoDesconto
* valorSegundoDesconto
* dataTerceiroDesconto
* valorTerceiroDesconto
* tipoMulta
* dataMulta
* valorMulta
* tipoJurosMora
* dataJurosMora
* valorJurosMora
* numeroParcela
* aceite
* codigoNegativacao
* numeroDiasNegativacao
* codigoProtesto
* numeroDiasProtesto

**Campo da seção "pagador"**:

* pagador.numeroCpfCnpj
* pagador.nome
* pagador.endereco
* pagador.bairro
* pagador.cidade
* pagador.cep
* pagador.uf

**Campo da seção "beneficiarioFinal"**:

* beneficiarioFinal.numeroCpfCnpj
* beneficiarioFinal.nome

                                                               

**Campo da seção grupo de "mensagensInstrucao"**:

* tipoInstrucao
* mensagensInstrucao.mensagens1
* mensagensInstrucao.mensagens2
* mensagensInstrucao.mensagens3
* mensagensInstrucao.mensagens4
* mensagensInstrucao.mensagens5

4Modelo de Registro Online v3

                                                           

* **URL do serviço de registro do boleto**: Deve ser informada a URL do serviço de registro do boleto disponibilizada pelo Banco - <https://api.sicoob.com.br/cobranca-bancaria/v3>
* **URL do sistema autorizador**: Deve ser informada a URL do serviço de autorização disponibilizado pelo Banco - <https://auth.sicoob.com.br/auth/realms/cooperado/protocol/openid-connect/token>
* **Client Id** : Código do sistema de autorização fornecido pelo Banco
* **Certificado digital:**Certificado digital cadastrado junto ao Banco para o registro de boleto online.

**Importante**:

* O Modelo de registro online "v3" está disponível a partir das versões:
  + 12.1.2502.127
  + 12.1.2410.209
  + 12.1.2406.262
* Informações de como gerar o certificado é necessário verificar as instruções disponíveis na documentação da API. Dúvidas a respeito, recomendamos entrar em contato com o suporte do Banco.

<https://developers.sicoob.com.br/portal/documentacao?slugItem=apis-do-sicoob&slugSubItem=primeiros-passos>

<https://developers.sicoob.com.br/portal/documentacao?slugItem=seguranca&slugSubItem=certificado-digital>

**Notas:**

* Se no lançamento financeiro o campo 'Multa' for maior que 0 (zero), a tag *tipoMulta* será preenchida com o valor "1". Do contrário, se multa ao dia for maior que 0 (zero), a tag será preenchida com o valor "2". Por último, quando ambos 0 (zero), esta tag será preenchida com o valor "0"
* Para os dois primeiros casos a tag *dataMulta* será preenchida com a data de vencimento acrescida do campo "Dias atraso multa". No último caso, será preenchida com valor nulo.
* Códigos da Multa, segundo o Sicoob:

         '0' = Isento   
         '1' = Valor Fixo   
         '2' = Percentual

* Se no lançamento financeiro o valor de juros ao dia for maior que 0 (zero) e o tipo de juros ao dia como "Valor", a tag *tipoJurosMora* será gerada com o valor "1". Caso contrário, se o campo 'Juros' for maior que 0 (zero), a tag será preenchida com o valor "2". Por último, se ambos valores de juros for igual a 0 (zero) esta tag será preenchida com o valor "0"
* Para os dois primeiros casos a tag *dataJurosMora* será preenchida com a data de vencimento acrescida da carência de juros (campo do lançamento financeiro). No último caso, será preenchida com valor nulo.
* Código do Juros de Mora, segundo o SICOOB:

         '0' = Isento   
         '1' = Valor por Dia   
         '2' = Taxa Mensal 

* O formato dos campos de data deve ser: AAAA-MM-DD

Conforme detalhado no  deste documento, é possível customizar o dado a ser enviado no registro online. Abaixo, seguem alguns exemplos de cadastro de campo no layout do registro online:

**Campo da seção principal**:

* numeroCliente
* codigoModalidade
* numeroContaCorrente
* codigoEspecieDocumento
* dataEmissao
* nossoNumero
* seuNumero
* identificacaoBoletoEmpresa
* codigoBarras
* linhaDigitavel
* identificacaoEmissaoBoleto
* identificacaoDistribuicaoBoleto
* valor
* dataVencimento
* dataLimitePagamento
* valorAbatimento
* tipoDesconto
* dataPrimeiroDesconto
* valorPrimeiroDesconto
* dataSegundoDesconto
* valorSegundoDesconto
* dataTerceiroDesconto
* valorTerceiroDesconto
* tipoMulta
* dataMulta
* valorMulta
* tipoJurosMora
* dataJurosMora
* valorJurosMora
* numeroParcela
* aceite
* codigoNegativacao
* numeroDiasNegativacao
* codigoProtesto
* numeroDiasProtesto
* quantidadeDiasFloat

**Campo da seção "pagador"**:

* pagador.numeroCpfCnpj
* pagador.nome
* pagador.endereco
* pagador.bairro
* pagador.cidade
* pagador.cep
* pagador.uf
* pagador.email

**Campo da seção "beneficiarioFinal"**:

* beneficiarioFinal.numeroCpfCnpj
* beneficiarioFinal.nome

**Campo da seção grupo de "mensagensInstrucao"**:

* mensagensInstrucao1
* mensagensInstrucao2
* mensagensInstrucao3
* mensagensInstrucao4
* mensagensInstrucao5

# 3. Customização de dados no registro online

customizacaoDeDadosRegOnline  
Pode ser utilizado o [Cadastro de Layout do Registro Online](https://tdn.totvs.com/display/LRM/Layout+Registro+Online), para enviar dados de forma flexível para o registro online dos boletos para o banco. Para isso deve ser feito o [Cadastro de associação de fórmulas e campos do registro online](https://tdn.totvs.com/pages/viewpage.action?pageId=421388759) no cadastro do convênio.

O cadastro do layout do registro online do Sicoob deve ser realizado de acordo com o manual de cobrança online do banco. Ressaltamos que o layout da v1 é totalmente diferente da v2 e v3, então o cadastro de layout de registro online deve ser refeito na migração da v1 para v2 ou v3. Demonstramos alguns exemplos de campos nas guias referente a cada modelo de registro online ().
