---
content_hash: 1cc74195374dcd8f822abf9cac30af5bb382d2c6c4352a8c2a6b389addfc76bc
fetched_at: '2026-06-29T00:06:16.513863+00:00'
page_id: '212899053'
product: rm
source: tdn-rm
title: ER_PCREQ-8625_Checkout_Cielo
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-8625_Checkout_Cielo
version: 143
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | Portal Educacional e Processo Seletivo |
| **Segmento Executor** | Educacional | | |
| **Projeto** | R\_EDU\_CTB005 | **IRM** | PCREQ-8624 |
| **Requisito** | PCREQ-8625 | **Subtarefa** | PDR\_EDU\_CTB003-594 |
| **Release de Entrega Planejada** | 12.1.12 | **Réplica** |  |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** |  | | |

## Objetivo

Implementar o novo modelo de integração de pagamento com cartão CHECKOUT CIELO, no portal Educacional e Processo Seletivo.

## Definição da Regra de Negócio

**1 - Parametrização (Etapa 02.02.02.03 - Cartão de Crédito/Débito)**

**1.1 - Configurações Gerais Cartão de Crédito/Débito**

* Configurações Gerais 1/2:   
  Como a solução BuyPage da Cielo não foi descontinuada, será criado um parâmetro "Modelo E-commerce" para informar qual a modelo de integração com a Cielo será utilizada, com as seguintes opções: 1 - BuyPage e 2 - Checkout
* Configurações Gerais 2/2:  
  Se a opção BuyPage marcada serão exibidos os campos "Codigo de Afiliação do Lojista", "Ambiente Ativo", "Chave Acesso do Lojista", "URL Ambiente Teste" e "URL Ambiente Produção".  
  Se a opção Checkout marcada serão exibidos os campos: "MerchantId" que é o identificador do cliente junto a Cielo, e "URL de Post" onde será enviado um post para Cielo utilizando a API Rest, para iniciar a transação do pagamento com cartão de crédito/débito.

**1.2 - Configurações Cartão de Crédito/Débito**

* Bandeira 1/3:  
  Configurações de crédito/débito para a bandeira Visa, com campos de Conta Caixa e Meio de Pagamento. Se opção BuyPage marcada será exibido o campo "Ativar Bandeira Visa", "Numero de Parcelas" e "Ativar Função Débito".
* Bandeira 2/3:  
  Configurações de crédito/débito para a bandeira Master, com campos de Conta Caixa e Meio de Pagamento. Se opção BuyPage marcada será exibido o campo "Ativar Bandeira Master" "Número de Parcelas" e somente a opção crédito.
* Bandeira 3/3:  
  Configurações de crédito para outras bandeiras, com campos de Conta Caixa e Meio de Pagamento. Somente visível se opção Checkout marcada.

**2 - Envio do Post para Cielo**

Será utilizada a integração com Carrinho de Compras utilizando API Rest para envio do post. A URL de Post que deverá ser utilizada é `https://cieloecommerce.cielo.com.br/api/public/v1/orders`.

Para a integração serão utilizados os parâmetros abaixo:

#### REQUISIÇÃO

#### Header Http

| CAMPO | TIPO | OBRIGATÓRIO | TAMANHO | DESCRIÇÃO |
| --- | --- | --- | --- | --- |
| MerchantId | Guid | Sim | 36 | Identificador único da loja.**Formato:**00000000-0000-0000-0000-000000000000 |
| Content-type | Alfanumérico | Sim | n/a | Tipo do conteúdo da mensagem a ser enviada. **Utilizar:**“application/json” |

#### Body

| CAMPO | TIPO | OBRIGATÓRIO | TAMANHO | DESCRIÇÃO |
| --- | --- | --- | --- | --- |
| OrderNumber | Alfanumérico | Opcional | 0..64 | Número do pedido da loja. |
| SoftDescriptor | Alfanumérico | Opcional | 0..13 | Texto para ser exibido na fatura do portador, após o nome do estabelecimento comercial. |
| Cart |  | Sim | n/a | Informações sobre o carrinho de compras. |
| Cart.Items |  | Sim | n/a | Lista de items do carrinho de compras (deve conter no mínimo 1 item) |
| Cart.Items.[].Name | [A](http://developercielo.github.io/Checkout-Cielo/#payment)lfanumerico | Sim | 1...128 | Nome do item no carrinho. |
| Cart.Items.[].UnitPrice | [N](http://developercielo.github.io/Checkout-Cielo/#customer)umerico | Sim | 1...18 | Preço unitário do item no carrinho *(**em centavos.*\* Ex: R$ 1,00 = 100)\*. |
| Cart.items.[].Quantity | Numérico | Sim | 1..9 | Quantidade do item no carrinho. |
| Cart.Items.[].Type | Alfanumérico | Sim | n/a | "Service" |
| Shipping |  | Sim | n/a | Informações sobre a entrega do pedido |
| Shipping.Type | Alfanumérico | Sim | n/a | “WithoutShipping” |
| Customer |  | Condicional | n/a | Informações sobre dados pessoais do comprador |
| Customer.Identity | Numérico | Condicional | 0..14 | CPF ou CNPJ do comprador. |
| Customer.FullName | Alfanumérico | Condicional | 0..288 | Nome completo do comprador. |
| Customer.Email | Alfanumérico | Condicional | 0..64 | Email do comprador. |
| Customer.Phone. | Numérico | Condicional | 0..11 | Telefone do comprador |
| Options |  | Condicional | n/a | Informações sobre opções configuráveis do pedido. |
| Options.AntifraudEnabled | Boolean | Conditional | n/a | Habilitar ou não a análise de fraude para o pedido. |

**RESPOSTA**

### Em caso de sucesso

| CAMPO | TIPO | OBRIGATÓRIO | TAMANHO | DESCRIÇÃO |
| --- | --- | --- | --- | --- |
| Settings | [Settings](http://developercielo.github.io/Checkout-Cielo/#settings) | Sim | n/a | Informações da resposta sobre a criação do pedido. |
| CheckoutUrl | Alfanumérico | Sim | 1..128 | URL de checkout do pedido. **Formato:** `https://cieloecommerce.cielo.com.br/transacional/order/index?id={id}` |
| Profile | Alfanumérico | Sim | 1..16 | Perfil do lojista: fixo “CheckoutCielo”. |
| Version | Alfanuméric | Sim | 1 | Versão do serviço de criação de pedido *(versão: 1)*. |

## Em caso de erro

| CAMPO | TIPO | OBRIGATÓRIO | TAMANHO | DESCRIÇÃO |
| --- | --- | --- | --- | --- |
| Message | String | Sim | 1..254 | Mensagem descritiva do erro |

**3 - Portal Educacional e Processo Seletivo**

Quando o cliente estiver usando o modelo Checkout da Cielo, na tela 'Confirmar Dados Cadastrais', quando o usuário clicar no botão 'Avançar' o mesmo será redirecionado para a pagina de pagamento segura da Cielo.

**4 - Retorno, Notificação e Mudança de status**

4.1 - Será criada uma página de retorno na qual o usuário será redirecionado assim que pagamento for concluído no ambiente seguro da Cielo. Caso o cliente não configure a página de retorno no BackOffice da Cielo o usuário será redirecionado para uma página própria da Cielo.

4.2 - Será criada uma página, sem autenticação, que deve ser preparadas para receber os dados do POST de Notificação e Mudança de Status enviados pela Cielo no momento que a transação é finalizada ou ter seu status alterado. A página deverá exibir um código informando que recebeu a notificação e a processou com sucesso. **Código:**`<status>OK</status>`

Parâmetros do Post de Notificação

| **PARÂMETRO** | **DESCRIÇÃO** | **TIPO DO CAMPO** | **TAM MÍN** | **TAM MÁX** |
| --- | --- | --- | --- | --- |
| checkout\_cielo\_order\_number | Identificador único gerado pelo CHECKOUT CIELO | Alfanumérico | 1 | 32 |
| amount | Preço unitário do produto, em centavos (ex: R$ 1,00 = 100) | Numérico | 1 | 10 |
| order\_number | Número do pedido enviado pela loja | Alfanumérico | 1 | 32 |
| created\_date | Data da criação do pedido (dd/MM/yyyy HH:mm:ss) | Alfanumérico | 1 | 20 |
| customer\_name | Nome do consumidor. Se enviado, esse valor já vem preenchido na tela do CHECKOUT CIELO | Alfanumérico | 1 | 289 |
| customer\_identity | Identificação do consumidor (CPF ou CNPJ) Se enviado, esse valor já vem preenchido na tela do CHECKOUT CIELO | Alfanumérico | 1 | 14 |
| customer\_email | E-mail do consumidor. Se enviado, esse valor já vem preenchido na tela do CHECKOUT CIELO | Alfanumérico | 1 | 64 |
| customer\_phone | Telefone do consumidor. Se enviado, esse valor já vem preenchido na tela do CHECKOUT CIELO | Numérico | 1 | 11 |
| discount\_amount | Valor do desconto fornecido (enviado somente se houver desconto) | Numérico | 1 | 10 |
| shipping\_type | Modalidade de frete | Numérico | 1 | 1 |
| shipping\_name | Nome do frete | Alfanumérico | 1 | 128 |
| shipping\_price | Valor do serviço de frete, em centavos (ex: R$ 10,00 = 1000) | Numérico | 1 | 10 |
| shipping\_address\_zipcode | CEP do endereço de entrega | Numérico | 1 | 8 |
| shipping\_address\_district | Bairro do endereço de entrega | Texto | 1 | 64 |
| shipping\_address\_city | Cidade do endereço de entrega | Alfanumérico | 1 | 64 |
| shipping\_address\_state | Estado de endereço de entrega | Alfanumérico | 1 | 64 |
| shipping\_address\_line1 | Endereço de entrega | Alfanumérico | 1 | 256 |
| shipping\_address\_line2 | Complemento do endereço de entrega | Alfanumérico | 1 | 256 |
| shipping\_address\_number | Número do endereço de entrega | Numérico | 1 | 8 |
| payment\_method\_type | Cód. do tipo de meio de pagamento | Numérico | 1 | 1 |
| payment\_method\_brand | Bandeira (somente para transações com meio de pagamento cartão de crédito) | Numérico | 1 | 1 |
| payment\_method\_bank | Banco emissor (Para transações de Boleto e Débito Automático) | Numérico | 1 | 1 |
| payment\_maskedcredicard | Cartão Mascarado (Somente para transações com meio de pagamento cartão de crédito) | Alfanumérico | 1 | 20 |
| payment\_installments | Número de parcelas | Numérico | 1 | 1 |
| payment\_antifrauderesult | Status das transações de cartão de Crédito no Antifraude | Numérico | 1 | 1 |
| payment\_boletonumber | Numero do boleto gerado | String |  |  |
| payment\_boletoexpirationdate | Data de vencimento para transações realizadas com boleto bancário | Numérico | 1 | 10 |
| payment\_status | Status da transação | Numérico | 1 | 1 |
| tid | TID Cielo gerado no momento da autorização da transação | Alfanumérico | 1 | 32 |

Parâmetros do Post de Mudança de Staus

| **PARÂMETRO** | **DESCRIÇÃO** | **TIPO DO CAMPO** | **TAM MÍN** | **TAM MÁX** |
| --- | --- | --- | --- | --- |
| checkout\_cielo\_order\_number | Identificador único gerado pelo CHECKOUT CIELO. | Alfanumérico | 1 | 32 |
| amount | Preço unitário do produto, em centavos (ex: R$ 1,00 = 100) | Numérico | 1 | 10 |
| order\_number | Número do pedido enviado pela loja | Alfanumérico | 1 | 32 |
| payment\_status | Status da transação | Numérico | 1 | 1 |

Tabela 1 - Meio de Pagamento

| Valor | Descrição |
| --- | --- |
| 1 | Cartão de Crédito |
| 2 | Boleto Bancário |
| 3 | Débito Online |
| 4 | Cartão de Débito |

Tabela 2 - Bandeira

| Valor | Descrição |
| --- | --- |
| 1 | Visa |
| 2 | Mastercard |
| 3 | AmericanExpress |
| 4 | Diners |
| 5 | Elo |
| 6 | Aura |
| 7 | JCB |

 

Tabela 3 - Banco Emissor

| Valor | Descrição |
| --- | --- |
| 1 | Banco do Brasil |
| 2 | Bradesco |

Tabela 4 - Status AntiFraude

| Valor | Descrição |
| --- | --- |
| 1 | Baixo Risco |
| 2 | Alto Risco |
| 3 | Não Finalizado |
| 4 | Risco Moderado |

Tabela 5 - Status da transação

| VALOR | DESCRIÇÃO |
| --- | --- |
| 1 | Pendente (Para todos os meios de pagamento) |
| 2 | Pago (Para todos os meios de pagamento) |
| 3 | Negado (Somente para Cartão Crédito) |
| 4 | Expirado (Cartão de Credito e Boleto) |
| 5 | Cancelado (Para cartões de crédito) |
| 6 | Não Finalizado (Todos os meios de pagamento) |
| 7 | Autorizado (somente para Cartão de Crédito) |
| 8 | ChargeBack (Somente Cartão de Credito) |

Processos:

Após receber o post notificação e enviar o status "ok" o sistema deve armazenar na tabela de Integração do cartão (FINTEGRACAOCARTAO), com os seguintes valores:

* IDENTIFICADORORIGEM: "Coligada" + '|' + "Identificador do Boleto"
* IDPROCESSO: tid
* IDCHECKOUT: checkout\_cielo\_order\_numbe
* BANDEIRA: payment\_method\_brand
* DATAHORA: created\_date
* IDSTATUS: payment\_status
* CODAFILIACAO: merchantid
* MEIOPAGTO: payment\_method\_type
* NUMPARCELAS; payment\_installments
* CODCOLIGADA: código da coligada
* IDBOLETO: identificador do boleto
* IDMODELO: preencher com 2 (Checkout Cielo)

Os pagamentos com cartão de crédito com status Autorizado serão automaticamente marcados como Baixa Pendente no RM e serão baixado somente quando o pagamento for capturado.

Ao mudar o status de pagamento com status "Pago" para "Cancelado" ou "ChargeBack" no BackOffice da Cielo, será automaticamente cancelado a baixa do boleto referente ao pagamento no RM.

Ao mudar o status de pagamento com status "Autorizado" para "Cancelado" no BackOffice da Cielo, será automaticamente liberado a Baixa Pendente do lançamento referente ao pagamento no RM.

Toda mudança de status do pagamento na Cielo será também alterado o status na tabela Integração do cartão (FINTEGRACAOCARTAO) do RM.

**5 - Backoffice Checkout Cielo**

O cliente deve configurar a URL de Retorno, Notificação e Mudança de Status no BackOffice. A URL de Retorno é opcional.

URL de Retorno: .../Corpore.Net/Source/Fin-Financeiro/RM.Fin.Lan/FinLanCartaoRetornoCheckout.aspx

URL de Notificação : .../Corpore.Net/Source/Fin-Financeiro/RM.Fin.Lan/CheckoutCielo/FinLanCartaoNotificacao.aspx

URL de Mudança de Status: .../Corpore.Net/Source/Fin-Financeiro/RM.Fin.Lan/CheckoutCielo/FinLanCartaoMudancaStatus.aspx

## Fluxo do Processo

## Dicionário de Dados

**Arquivo ou Código do Script:** FS.2016.03\_01; FS.2016.03\_02; FS.2016.06\_02

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
