---
content_hash: db390f313b3877b7f9a8fb08fdf2314d98b3e9c14a088ac4d1ff47e4171b516f
fetched_at: '2026-06-29T00:12:15.318158+00:00'
page_id: '976136570'
product: rm
source: tdn-rm
title: Registro online Banestes
type: documentation
url: https://tdn.totvs.com/display/LRM/Registro+online+Banestes
version: 6
---

# Conteúdo:

Conteúdo:

# 1. Registro online

Esta implementação tem como objetivo preparar o TOTVS Gestão Financeira para utilizar o serviço de registro online de cobrança registrada do banco Banestes (via webservice).

Disponível no release 12.1.2406 ou superior (recomendamos utilizar sempre o último patch).

[Baixe aqui o manual do banco Banestes.](https://www.banestes.com.br/downloads/arquivos/layout_web_service.pdf)

# 2. Procedimento para configuração

Através do cadastro do Convênio, localizado no menu 'Movimentações Bancárias', é necessário habilitar a opção "Permite registro de boleto online" e definir os parâmetros de acordo com os dados fornecidos pelo banco Banestes.

Cards2Modelo de Registro Online v1

* **Permite registro de boleto online:**Define se o convênio permite utilizar o registro de boleto online.
* **Integração com os serviços da AutBank:**Define que o banco utiliza o padrão da AutBank para o registro online de boletos.
* **Ambiente**: Define o ambiente que será feito o registro do boleto no banco.
* **URL do serviço de registro de cobrança**: Deve ser informada a URL do serviço de registro do boleto disponibilizada pelo banco. ([https://api.banestes.b.br/cobranca/v3/MetodosWebServerImp](https://api.banestes.b.br/cobranca/v2/MetodosWebServerImp))
* **URL de homologação do serviço de registro de cobrança**: Deve ser informada a URL de homologação do serviço de registro do boleto disponibilizada pelo banco. ([https://sandbox.banestes.b.br/cobranca/v3/MetodosWebServerImp](https://sandbox.banestes.b.br/cobranca/v2/MetodosWebServerImp))
* **Usuário:** Usuário fornecido pelo banco para autenticar a integração.
* **Senha:** Senha fornecida pelo banco para autenticar a integração.

Conforme detalhado no item 3 deste documento, é possível enviar os dados de forma flexível para o banco ao registrar online os boletos. O cadastro do layout do registro online do Banestes deve ser feito conforme o manual de cobrança online do banco, onde contempla a descrição de cada campo. Exemplos:

* titulo.CONTA\_CORRENTE
* titulo.IDENTIFICADOR\_RESPONSAVEL\_EMITIR\_BOLETO
* titulo.IDENTIFICADOR\_RESPONSAVEL\_DISTRIBUIR\_BOLETO
* titulo.PERCENTUAL\_MORA\_ATRASO
* titulo.PERCENTUAL\_MULTA\_ATRAS
* titulo.inscricaoPagador.NOME
* titulo.inscricaoSacadorAvalista.BAIRRO
* titulo.inscricaoSacadorAvalista.CEP
* titulo.PARCELAS\_ENTRADA.VALOR\_TITULO
* titulo.PARCELAS\_ENTRADA.VALOR\_ABATIMENTO
* titulo.PERCENTUAL\_MORA\_ATRASO
* titulo.PERCENTUAL\_MULTA\_ATRASO
* titulo.DATA\_LIMITE\_PAGAMENTO
* titulo.PARCELAS\_ENTRADA.DESCONTO1.CODIGO\_DESCONTO
* titulo.PARCELAS\_ENTRADA.DESCONTO1.VALOR\_DESCONTO
* titulo.PARCELAS\_ENTRADA.DESCONTO1.DATA\_DESCONTO
* titulo.PARCELAS\_ENTRADA.DESCONTO2.CODIGO\_DESCONTO
* titulo.PARCELAS\_ENTRADA.DESCONTO2.VALOR\_DESCONTO
* titulo.PARCELAS\_ENTRADA.DESCONTO2.DATA\_DESCONTO
* titulo.PARCELAS\_ENTRADA.DESCONTO3.CODIGO\_DESCONTO
* titulo.PARCELAS\_ENTRADA.DESCONTO3.VALOR\_DESCONTO
* titulo.PARCELAS\_ENTRADA.DESCONTO3.DATA\_DESCONTO
* titulo.BAIXA.CODIGO\_BAIXA
* titulo.BAIXA.DIAS\_BAIXA

# 3. Customização de dados no registro online

Pode ser utilizado o [Cadastro de Layout do Registro Online](https://tdn.totvs.com/display/LRM/Layout+Registro+Online), para enviar dados de forma flexível para o registro online dos boletos para o banco. Para isso deve ser feito o [Cadastro de associação de fórmulas e campos do registro online](https://tdn.totvs.com/pages/viewpage.action?pageId=421388759) conforme o manual de cobrança online do banco Banestes.

**IMPORTANTE**:

* Campo do tipo DATA deve ter o formato  AAAA-MM-DD. Ex: 2025-01-25
* Campo do tipo VALOR DECIMAL deve ser valor numérico com até 8 casas e 2 decimais separado por ponto. Ex: 678.12
* Será permitido definir até três descontos:

Primeiro desconto:

Campo: Código do primeiro desconto

TAG: titulo.PARCELAS\_ENTRADA.DESCONTO1.CODIGO\_DESCONTO

Valor: 1 (Valor fixo até a data informada)

Campo: Data do primeiro desconto

TAG: titulo.PARCELAS\_ENTRADA.DESCONTO1.DATA\_DESCONTO

Valor:

Ex: 2025-01-25 (AAAA-MM-DD)

Obs.: Caso não seja informado valor (Vazio) o desconto será desconsiderado e não será enviado

Campo: Valor do primeiro desconto

TAG: titulo.PARCELAS\_ENTRADA.DESCONTO1.VALOR\_DESCONTO

Valor:

Ex: 678.12 (Valor numérico com até 8 casas e 2 decimais separado por ponto)

Obs.: Caso não seja informado valor (Vazio) ou valor igual a zero, o desconto será desconsiderado e não será enviado

Segundo desconto:

Campo: Código do segundo desconto

TAG: titulo.PARCELAS\_ENTRADA.DESCONTO2.CODIGO\_DESCONTO

Valor: 1 (Valor fixo até a data informada)

Campo: Data do segundo desconto

TAG: titulo.PARCELAS\_ENTRADA.DESCONTO2.DATA\_DESCONTO

Valor:

Ex: 2025-01-25 (AAAA-MM-DD)

Obs.: Caso não seja informado valor (Vazio) o desconto será desconsiderado e não será enviado

Campo: Valor do segundo desconto

TAG: titulo.PARCELAS\_ENTRADA.DESCONTO2.VALOR\_DESCONTO

Valor:

Ex: 678.12 (Valor numérico com até 8 casas e 2 decimais separado por ponto)

Obs.: Caso não seja informado valor (Vazio) ou valor igual a zero, o desconto será desconsiderado e não será enviado

Terceiro desconto:

Campo: Código do terceiro desconto

TAG: titulo.PARCELAS\_ENTRADA.DESCONTO3.CODIGO\_DESCONTO

Valor: 1 (Valor fixo até a data informada)

Campo: Data do terceiro desconto

TAG: titulo.PARCELAS\_ENTRADA.DESCONTO3.DATA\_DESCONTO

Valor:

Ex: 2025-01-25 (AAAA-MM-DD)

Obs.: Caso não seja informado valor (Vazio) o desconto será desconsiderado e não será enviado

Campo: Valor do terceiro desconto

TAG: titulo.PARCELAS\_ENTRADA.DESCONTO3.VALOR\_DESCONTO

Valor:

Ex: 678.12 (Valor numérico com até 8 casas e 2 decimais separado por ponto)

Obs.: Caso não seja informado valor (Vazio) ou valor igual a zero, o desconto será desconsiderado e não será enviado

* Será possível definir quando o registro do título será cancelado (Baixa / Devolução)

Campo: Código da baixa

TAG: titulo.BAIXA.CODIGO\_BAIXA

Valor:

1 - Baixa/Devolução

2 - Não baixar / Não Devolver

Campo: Quantidade de dias para Baixa/Devolução

TAG: titulo.BAIXA.DIAS\_BAIXA

Valor:

Ex: 45

Se CODIGO\_BAIXA igual a 1 dias de baixa tem que ser maior ou igual a 1.  Quando Código para Baixa é 2 - Não baixar / Não Devolver , DIAS\_BAIXA deve ser 0

* Por padrão, o campo responsável por indicar o responsável por emitir o Boleto é 2 (Cliente). Caso o responsável seja o banco, é necessário enviar no campo "titulo.IDENTIFICADOR\_RESPONSAVEL\_EMITIR\_BOLETO" via associação de layout o valor 1, no qual representa o banco conforme o manual do banco.

* Por padrão, o campo responsável por indicar o responsável por distribuir o Boleto é 2 (Cliente). Caso o responsável seja o banco, é necessário enviar no campo "titulo.IDENTIFICADOR\_RESPONSAVEL\_DISTRIBUIR\_BOLETO" via associação de layout o valor 1, no qual representa o banco conforme o manual do banco.

* O banco espera como juros um percentual mensal, como o TOTVS Gestão financeira trabalha com juro valor fixo ou percentual diário, o que será enviado para o banco será o percentual de juros ao dia do boleto vezes trinta.  Caso queira enviar um valor diferente é possível utilizando a campo da associação de layout "titulo.PERCENTUAL\_MORA\_ATRASO". O formato deve ser 2 casas e 2 decimais separado por ponto. Ex: 1.00

* O banco espera como multa um percentual fixo, como o TOTVS Gestão financeira trabalha com multa valor fixo ou percentual diário, o que será enviado para o banco será o percentual de multa ao dia do boleto vezes trinta.  Caso queira enviar um valor diferente é possível utilizando a campo da associação de layout "titulo.PERCENTUAL\_MULTA\_ATRASO". O formato deve ser 2 casas e 2 decimais separado por ponto. Ex: 2.00

* O sacador/avalista não é obrigatório ser enviado, caso queira enviar é necessário cadastrar os campos abaixo na associação de layout registro online.
  + titulo.inscricaoSacadorAvalista.TIPO\_INSCRICAO
  + titulo.inscricaoSacadorAvalista.NUMERO\_INSCRICAO
  + titulo.inscricaoSacadorAvalista.NOME
  + titulo.inscricaoSacadorAvalista.LOGRADOURO
  + titulo.inscricaoSacadorAvalista.BAIRRO
  + titulo.inscricaoSacadorAvalista.CIDADE
  + titulo.inscricaoSacadorAvalista.UF
  + titulo.inscricaoSacadorAvalista.CEP

* A data do desconto por padrão é a data de vencimento, caso queira definir um outra data, é necessário cadastrar o campo "titulo.PARCELAS\_ENTRADA.DATA\_DESCONTO" e definir uma data no formato "yyyy-mm-dd"

* Caso queira definir uma data limite de pagamento do boleto, será necessário cadastra o campo "titulo.DATA\_LIMITE\_PAGAMENTO" e definir uma data no formato "AAAA-MM-DD"
