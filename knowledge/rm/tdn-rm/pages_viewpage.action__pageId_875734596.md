---
content_hash: e2dd8a6a3a23a93dcf844da2b3415e984c7ce771cefc28323f49b584d1b12571
fetched_at: '2026-06-29T00:11:59.669178+00:00'
page_id: '875734596'
product: rm
source: tdn-rm
title: Pagamento com Cartão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=875734596
version: 15
---

---

Possibilita ao usuário o pagamento do título com cartão, o usuário terá a opção de pagar com os cartões cadastrados na carteira, pagar com novo cartão que será gravado na carteira e pagar com cartão que não será gravado na carteira.

O sistema tem que estar habilitado para utilização do Meu eduCONNECT (Payments)

Se uma opção de pagamento estiver **MARCADA** em um dos serviços do boleto, a mesma estará disponível no extrato financeiro, as opções estão localizadas no [Cadastro de Serviços](https://tdn.totvs.com/pages/viewpage.action?pageId=425458880)

As opções disponíveis para pagamento dependerão se o pagamento com cartão está habilitado nas parametrizações gerais de Portal (8/18), da marcação dos respectivos campos no cadastro de serviços e da disponibilidade do pagamento com cartão de crédito na matriz aplicada.

**IMPORTANTE:**Pagamento por cartão de crédito só será permitido se o modelo de transação parametrizado no TOTVS Gestão Financeira for Cybersource ou Adyen.  
Após parametrização do modelo de transação, o serviço do host deverá ser reiniciado ou deverá ser aguardado um intervalo de 10 minutos entre a última execução do extrato financeiro que armazenou o cache de parâmetros. Dúvidas na parametrização do TOTVS Gestão Financeira, [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=421388865)

Pagamento com Cartão

No extrato financeiro, o usuário selecionará um boleto para ser pago e na tela de seleção de método de pagamento, o usuário selecionará a opção "**CARTÃO**" e avançará para o próximo passo.

O próximo passo é a visualização do resumo dos lançamentos do boleto. Para mais detalhes do resumo dos lançamentos clique [aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=848809594).

Após prosseguir com o pagamento, o usuário terá opção de pagar com cartão da carteira ou novo cartão.

Serão exibidos os cartões de acordo com a bandeira (Visa, Mastercard, American Express, Dinners, JCB, etc...).

Pagamento parcelado

O usuário poderá alterar o número de parcelas do pagamento clicando na quantidade de parcelas.

**Observação:** O número máximo de parcelas a ser mostrado dependerá do número máximo de parcelas de cartão de crédito parametrizado nos serviços contidos no boleto. Caso o número máximo de parcelas não tenha sido informado em nenhum serviço do boleto, será consultada a parametrização do número máximo de parcelas feito no financeiro. (Contas a receber → Baixas → Cartão de crédito/débito). Se ainda este não contiver um número máximo de parcelas parametrizado, será mostrada a opção com apenas uma parcela para o usuário.

Ao realizar o pagamento com cartão, existe três opções:

Cartão selecionado (carteira digital)

Poderá ser feito um pagamento com o cartão selecionado. Botão somente ficará habilitado se o cartão selecionado não for o cartão com o ícone de "+". Nesse caso, após clicar em "Pagar", o pagamento será feito imediatamente caso seja autorizado.

Deverá ser informado o código de segurança do cartão do usuário antes de se efetuar o pagamento.

O botão pagar somente estará habilitado se um cartão cadastrado na carteira do usuário tiver sido selecionado.

Inclusão de novo cartão na carteira

 Poderá ser incluído um cartão a partir do clique no cartão com um "+" no centro da imagem do cartão ou clicando no ícone abaixo do carrossel de imagens de cartões.

Após salvar o cartão o sistema volta para a tela de carteira digital.

Pagamento com outro cartão

Poderá ser feito um pagamento com um outro cartão sem ser cartão da carteira.

Nesse caso o usuário deverá preencher os dados do cartão e dados de endereço. Após estas informações, será mostrada uma tela com os dados do cartão e o valor a ser pago antes da confirmação do pagamento.

Cartão internacional

O comportamento de vários campos na tela de dados de endereço do cartão dependerá do país selecionado.  
Para países diferentes de Brasil, o campo CEP mudará para código postal e o campo CPF mudará para passaporte.  
Quando o país for Brasil, os campos CEP, CPF e telefone somente aceitarão números e suas respectivas máscaras serão considerada, se o país for diferente de Brasil, não haverá máscara para esses campos.  
  
Com relação à obrigatoriedade dos campos a serem informados, segue abaixo:

* Brasil: São obrigatórios os campos: (País, CEP Endereço, Número, Bairro, Cidade, Estado, CPF, Telefone e E-mail)
* Estados Unidos e Canadá: (País, Código postal, Endereço, Número, Cidade, Estado, Passaporte, Telefone, E-mail)
* Outros países não citados acima: (País, Endereço, Número, Cidade, Passaporte, Telefone e E-mail)

O comportamento dos campos obedecerá aos critérios citados acima tanto no pagamento com outro cartão quanto na inclusão de um cartão na carteira digital.

Dados do cartão não serão armazenados na base de dados para maior segurança dos usuários.IMPORTANTE!

## **TABELAS UTILIZADAS**

* FCARTEIRADIGITAL - Tabela de carteira digital
* GENDERECO - Contém os dados de endereço do cartão

]]>
