---
content_hash: 874c9be65be18eb8edb79f6fa3146589c6e1079fc637bb029939017dd7d9864f
fetched_at: '2026-06-29T00:12:14.112803+00:00'
page_id: '965456997'
product: rm
source: tdn-rm
title: Registro online Banrisul
type: documentation
url: https://tdn.totvs.com/display/LRM/Registro+online+Banrisul
version: 1
---

# Conteúdo:

Conteúdo:

# 1. Registro online

Esta implementação tem como objetivo preparar o TOTVS Gestão Financeira para utilizar o serviço de registro online de cobrança registrada do banco Banrisul.

# 2. Procedimento para configuração

Através do cadastro do Convênio, localizado no menu 'Movimentações Bancárias', é necessário habilitar a opção "Permite registro de boleto online" e definir os parâmetros de acordo com os dados fornecidos pelo banco Banrisul.

Cards2Modelo de Registro Online v1

* **Permite registro de boleto online:**Define se o convênio permite utilizar o registro de boleto online.
* **Integração com os serviços da AutBank:**Define que o banco utiliza o padrão da AutBank para o registro online de boletos.
* **Ambiente**: Define o ambiente que será feito o registro do boleto no banco.
* **URL do serviço de registro de cobrança**: Deve ser informada a URL do serviço de registro do boleto disponibilizada pelo banco.
* **URL de homologação do serviço de registro de cobrança**: Deve ser informada a URL de homologação do serviço de registro do boleto disponibilizada pelo banco.
* **Certificado digita**l: Informe o certificado digital obtido pela empresa.

Conforme detalhado no item 3 deste documento, é possível enviar os dados de forma flexível para o banco ao registrar online os boletos. O cadastro do layout do registro online do Banrisul deve ser feito conforme o manual de cobrança online do banco, onde contempla a descrição de cada campo. Exemplos:

Outros exemplos de campos:

* titulo.nosso\_numero
* titulo.seu\_numero
* titulo.data\_vencimento
* titulo.valor\_nominal
* titulo.especie
* titulo.data\_emissao
* titulo.valor\_iof
* titulo.beneficiario.codigo
* titulo.pagador.aceite
* titulo.instrucoes.juros.codigo
* titulo.instrucoes.juros.data
* titulo.instrucoes.juros.taxa
* titulo.instrucoes.juros.valor
* titulo.instrucoes.multa.codigo
* titulo.instrucoes.multa.data
* titulo.instrucoes.multa.valor
* titulo.instrucoes.multa.taxa
* titulo.instrucoes.desconto.codigo
* titulo.instrucoes.desconto.data
* titulo.instrucoes.desconto.valor
* titulo.instrucoes.desconto.taxa
* titulo.instrucoes.protesto.codigo
* titulo.instrucoes.protesto.prazo
* titulo.instrucoes.baixa.codigo
* titulo.instrucoes.baixa.prazo
* titulo.pag\_parcial.autoriza
* titulo.pag\_parcial.codigo
* titulo.pag\_parcial.quantidade
* titulo.pag\_parcial.tipo
* titulo.pag\_parcial.valor\_min
* titulo.pag\_parcial.valor\_max
* titulo.pag\_parcial.percentual\_min
* titulo.pag\_parcial.percentual\_max
* titulo.mensagem[1 a 9].linha
* titulo.mensagem[1 a 9].texto

# 3. Customização de dados no registro online

Pode ser utilizado o [Cadastro de Layout do Registro Online](https://tdn.totvs.com/display/LRM/Layout+Registro+Online), para enviar dados de forma flexível para o registro online dos boletos para o banco. Para isso deve ser feito o [Cadastro de associação de fórmulas e campos do registro online](https://tdn.totvs.com/pages/viewpage.action?pageId=421388759) de acordo com o manual de cobrança online do Banrisul.

**IMPORTANTE**:

* Para os campos de valores ou percentual deve seguir o formato de acordo com o manual disponibilizado pelo banco. Ao definir um valor fixo ou formula deve ser retornado um string com o separador decimal '.' (ponto). Exemplo:   
  2.49 (com duas casas decimais )  
  2018-03-30 (data no formato AAAA-MM-DD)
* O campo Data da Multa será calculado a partir da Data de Vencimento do boleto acrescido do parâmetro *Dias de Atraso* configurado na etapa Valor Líquido do Lançamento Financeiro.
* No registro do boleto será gravado no campo Json/XML o valor completo da requisição, além do conteúdo do Json/XML, também incluídos os dados da requisição SOAP. Os mesmos são necessários no processo de validação da rotina junto ao banco.
