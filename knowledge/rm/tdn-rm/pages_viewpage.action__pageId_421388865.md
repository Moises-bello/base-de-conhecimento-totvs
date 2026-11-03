---
content_hash: 3dfd99615f000bafec515fcdc30d6110ad4cf99948e1f64bcb7af9d4b2869efc
fetched_at: '2026-06-29T00:09:19.404000+00:00'
page_id: '421388865'
product: rm
source: tdn-rm
title: Parametrização do pagamento com cartão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388865
version: 126
---

**Pagamento através do portal educacional** -O RM disponibiliza para recebimento de cartão os modelos da Cielo BuyPage, Cielo Checkout, Checkout IFrame GetNet, CyberSource, Adyen e eRede. A instituição que define se utilizará o pagamento por cartão via portal, podendo realizar o pagamento com cartão de crédito (à vista ou parcelado) ou cartão de débito. O boleto pago será baixado automaticamente no sistema.

No TOTVS Gestão Financeira é necessário parametrizar Conta Caixa e Meio de pagamento das bandeiras dos cartões que serão utilizados no processo, bem como os dados do lojista.

Observação: Para as bandeiras Visa e Mastercard está disponível pagamento com as funções Crédito e Débito, para as demais bandeiras está disponível pagamentos somente com a funções Crédito.

Estas parametrizações podem ser realizadas através do menu Ambiente | Parâmetros | TOTVS Gestão Financeira | Contas a Receber **|** Baixas **|** Cartão de Crédito/Débito.

Modelos E-commerceBuyPageBuyPage

**Para o Modelo BuyPage:**

* Informar os dados do Lojista (Código de Afiliação, Chave de Acesso e o Endereço de Acesso);

Para o modelo **BuyPage** o sistema disponibiliza somente as Bandeiras:

* Bandeira Visa: Permite ativar as funções crédito e débito.
* Bandeira Mastercard: Permite ativar a função crédito.
* O parcelamento no crédito ocorre pela opção "Parcelamento Loja".

O cancelamento de baixa para este modelo, será realizado pelo TOTVS Gestão Financeira na Visão de Lançamentos em Processos / Cancelar Transação de Cartão de Crédito/Débito.

**Observação**

Os campos " NSU " e " CODAUTORIZACAO ", serão responsáveis por armazenar as informações de "Cód. de autorização retornado pelo emissor do cartão" e "Num. seq. único retornado pela adquirente (NSU)". Além destes campos, estão presentes na visão de histórico de transação, os campos "Id. Boleto", "NSU Adquirente", "Cod. de autorização emissor cartão" e "NSU Sitef" que também poderão ser usado para efetuar filtros. Estes campos facilitam a identificação das transações junto a Cielo.

Para a função Débito, no momento são aceitas somente as bandeiras Visa e Master com cartões emitidos pelos bancos validados pela Cielo: Bradesco, Banco do Brasil, Santander e HSBC. Novos bancos certificados podem ser verificados no site [www.cielo.com.br](http://www.cielo.com.br/).

Para função de crédito com parcelamento, caso exista diferença de centavos entre o total da transação e o somatório das parcelas, o valor será somado à primeira parcela.

A digitação e validação dos dados do cartão ocorre no ambiente das operadoras sem interferência do RM.

CheckoutCheckout

**Para o Modelo Checkout:**

* **Merchantld:** Identificador do lojista na Cielo
* **URL de Post:** URL de integração com Cielo, *<https://cieloecommerce.cielo.com.br/api/public/v1/orders>*.

* A configuração para definir o número máximo de parcelas para o modelo Checkout, será definida no Backoffice que a Cielo disponibilizará para o lojista.
* O cancelamento de baixa neste modelo, deve ser realizado pelo Backoffice da Cielo.
* Os pagamentos com cartão de crédito com status Autorizado, serão automaticamente marcados como Baixa Pendente no RM e serão baixados somente quando o pagamento for capturado.
* Ao mudar o status de pagamento com status "Pago" para "Cancelado" ou "ChargeBack" no BackOffice da Cielo, será automaticamente cancelada a baixa do boleto referente ao pagamento no RM.
* Ao mudar o status de pagamento com status "Autorizado" para "Cancelado" no BackOffice da Cielo, será automaticamente liberada a Baixa Pendente do lançamento referente ao pagamento no RM.

**Observações:**

* Quando o cliente estiver utilizando o modelo Checkout da Cielo, na tela 'Confirmar Dados Cadastrais', quando o usuário clicar no botão 'Avançar', o mesmo será redirecionado para a página de pagamento segura da Cielo.

* Para a função Débito, no momento são aceitas somente as bandeiras Visa e Master com cartões emitidos pelos bancos validados pela Cielo: Bradesco, Banco do Brasil, Santander e HSBC. Novos bancos certificados podem ser verificados no site [www.cielo.com.br](http://www.cielo.com.br/).

* A digitação e validação dos dados do cartão ocorre no ambiente das operadoras sem interferência do RM.

* Quando o modelo de pagamento for usado para transações no Portal do Processo Seletivo, no ambiente do cliente na Cielo, não ser feita a configuração da página de retorno de confirmação para o usuário quando o serviço não for num ambiente autenticado. Vale ressaltar que essa configuração não é obrigatória e não afeta a realização do pagamento.
* Para parcelamento no cartão de crédito, caso exista diferença de centavos entre o total da transação e o somatório das parcelas, o valor será somado à primeira parcela.
GetNetGetnet

**O modelo IFrame Getnet está disponível somente no novo Portal Educacional.**

Em Configurações E-commerce, ao selecionar o Modelo E-Commerce IFrame Getnet, o sistema disponibiliza os campos onde serão informados os dados de parametrização para comunicação com a Getnet.

* Informar os dados do Lojista (Código de acesso, URL de Checkout, URL de autenticação, URL de cancelamento, Client ID, Client Secret, Nº máximo de parcelas).

Para utilizar os serviços da Getnet é necessário que tenha configurado nos parâmetros do sistema as URLs de **Homologação** ou de **Produção**:

HOMOLOGAÇÃO  
URL de Checkout:  
<https://checkout-homologacao.getnet.com.br/loader.js>  
URL de Autenticação:  
<https://api-homologacao.getnet.com.br/auth/oauth/v2/token>  
URL de Cancelamento:  
<https://api-homologacao.getnet.com.br/v1/payments/cancel/request>

PRODUÇÃO  
URL ckeckout:  
<https://checkout.getnet.com.br/loader.js>  
URL autenticação:  
<https://api.getnet.com.br/auth/oauth/v2/token>  
URL cancelamento:  
<https://api.getnet.com.br/v1/payments/cancel/request>

Bandeira

Como a Getnet não retorna qual foi a bandeira do cartão utilizado no pagamento, no RM é necessário apenas informar a *Conta Caixa* e o *Meio de Pagamento* para *Outras Bandeiras.*

Pagamento

Quando realizado a transação com o IFrame Getnet (pagamento) pelo \*Portal do EDU, o processo de pagamento será direcionado para página da Getnet para que os dados do cartão para pagamento e outras informações de obrigatoriedade da operadora sejam informados. Ao final da transação será exibido a página de retorno do status do pagamento, Transação Efetuada ou Transação não Efetuada, integrando este pagamento ao RM, efetuando automaticamente a baixa do lançamento\boleto no sistema.

É necessário entrar em contato com a Getnet para configurar a página de "CallBack" para retorno da confirmação do pagamento na plataforma, com a seguinte URL: **https://[caminho do Corpore.Net]/Source/Fin-Financeiro/RM.Fin.Lan/Getnet/FinLanCartaoCallback.aspx**.Também deve ser configurado os arquivos de "host" conforme orientação em <https://tdn.totvs.com/display/public/LRM/Configurando+DefaultDB>.

**Observações**

* As informações inseridas na página da Getnet são de responsabilidade o usuário e os dados inseridos são de responsabilidade da Getnet, pois todo processo de pagamento é realizado pela Getnet e não pelo RM. Neste cenário, o RM somente recebe as informações do pagamento enviado pela Getnet.
* O modelo Getnet só está disponível no novo portal educacional.

Cancelamento do pagamento realizado via cartão pela Getnet

O processo para solicitar o cancelamento da transação é executado pela visão de Histórico de Transações em *Processos | Solicitar cancelamento de transação.*Este processo só terá efeito em transações realizadas com a solução IFrameGetnet.

**Observações:**

* Para  execução deste processo será preciso habilitar a permissão de acesso no perfil do usuário.
* Para cancelamentos solicitados no mesmo dia, o 'Ajuste de transações' irá executar o processo de cancelamento do pagamento. Caso a solicitação de cancelamento não for realizada no mesmo dia do Pagamento, o cancelamento será efetivado contando o dia do pedido de cancelamento + 1 dia(D+1) para processamento pela Getnet.

Ajuste de Transações

Para a Getnet esse processo somente ajusta transações com status *Cancelamento Pendente,* e tem como objetivo verificar se a solicitação de cancelamento enviada a Getnet foi processada e efetuar o cancelamento da baixa do boleto e irá alterar o status da transação do RM para *Pagamento Cancelado*.

O processo é executado em *Movimentações Bancárias| Ajuste de Transações* ou pela visão de Histórico de Transações em *Processos | Ajustar transação*.

CyberSourceCyberSource

Para visualizar as parametrizações desse modelo, selecione no combo-box **Modelo E-Commerce** a opção **CyberSource**.

Após a seleção, os campos para configuração do CyberSource serão exibidas.

**Informações CyberSource:**

* **Ambiente Ativo:** Indica qual ambiente será utilizado na comunicação com a CyberSource. Sempre informar o ambiente de "***Produção***".
* **Merchant Id:**Identificador do comerciante fornecido pela CyberSource.
* **Key Id:**Identificador relacionado a Shared Secrect Key, criado ao gerar a Shared Secrect Key através do portal do cliente CyberSource.
* **Shared Secrect Key:**Chave compartilhada gerada através do portal do cliente CyberSource.
* **Nº máximo de parcelas:**Define o número máximo de parcelas no pagamento com cartão.

**URL Autorizada CyberSource:**

* Para garantir a continuidade das transações de cartão de crédito, o Administrador do Sistema deve cadastrar as URLs da sua instituição que estão autorizadas ao processo de recebimento via cartão pela sua instituição. Essa medida atende aos novos protocolos de segurança da CyberSource que serão adotados em breve.

É necessário que o cadastro das informações de bandeira sejam preenchidas, informando a conta caixa e meio de pagamento a ser utilizado.

**OBSERVAÇÕES**

* Neste modelo, quando integrado com Rede, o cancelamento de alguma transação deve sempre ser feito via módulo Financeiro e não no ambiente da Rede.
* Operação de débito não disponível para este modelo.

Tipo de Adquirente

A partir da versões abaixo e com o parâmetro interno CyberSourceHabilitaTokenPorBandeira habilitado, será disponibilizado o combobox de Tipo de Adquirente.

Versões dos patches:

* 12.1.2302.264
* 12.1.2306.226
* 12.1.2310.166
* 12.1.2402.106

O Tipo de Adquirente foi implementado pois, será necessário envio de algumas informação para a tokenização por bandeira de cada adquirente.

eRedeAutenticação OAuth 2.0

A REDE comunicou a **descontinuação do modelo de autenticação Basic Auth a partir de 05/01/2026**, passando a adotar **exclusivamente o modelo OAuth 2.0**.

Para a correta adequação do sistema, será necessário:

* Solicitar à REDE a **URL de Autenticação OAuth 2.0**;
* Atualizar a **URL de transações para a versão v2**, também fornecida pela REDE.

⚠️ **ATENÇÃO**  
A configuração da **URL de Autenticação OAuth 2.0 exige obrigatoriamente a utilização da URL de transações na versão v2**.  
Caso a URL de transações permaneça em versão anterior, o **processo de recebimento por cartão no E-Commerce REDE não será executado com sucesso**, ocasionando falhas nas transações.

Para visualizar as parametrizações desse modelo, selecione no combo-box Modelo E-Commerce a opção **e-Rede**.

* **Nº máximo de parcelas:**Define o número máximo de parcelas no pagamento com cartão de crédito.
* **URL:** URL do processo de transação do recebimento com cartão da e-Rede.
* **URL de Autenticação:** URL para a obtenção do token de acesso (protocolo OAuth 2.0) - *só deve ser preenchido se estiver sendo utilizada a v2 da URL de transações.*
* **Client Id (Número de afiliação):** Identificação (PV) do ambiente da e-Rede, que com o protocolo OAuth 2.0 passa a ter o nome de Client Id.
* **Client Secret (Token):** Token de acesso do ambiente da e-Rede, que com o protocolo OAuth 2.0 passa a ter o nome Client Secret.

As URLs dos ambientes de teste e produção da Rede na v1, são as seguintes:

* Teste: <https://api.userede.com.br/desenvolvedores/v1/transactions>
* Produção: <https://api.userede.com.br/erede/v1/transactions>
* Mais informações no manual da e.Rede: <https://www.userede.com.br/desenvolvedores/pt/produto/e-Rede#documentacao>

As URLs do ambiente de teste da Rede na v2, são as seguintes:

* URL Serviço: <https://api.userede.com.br/desenvolvedores/v2/transactions>
* Gerar Token (Ambiente Teste): <https://rl7-sandbox-api.useredecloud.com.br/oauth2/token>
* Mais informações no manual da e.Rede: <https://developer.userede.com.br/e-rede>

É necessário que o cadastro das informações de bandeira sejam preenchidas, informando a conta caixa e meio de pagamento a ser utilizado.

Configuração por FilialConfiguração por Filial

**Pagamento/Baixa com cartão por filial**

Esta funcionalidade tem como objetivo permitir a parametrização para pagamento/baixa com cartão de crédito/débito por Filial.

Para utilizar esta opção é necessário configurar nos parâmetros do sistema definindo a filial e o modelo de pagamento que será utilizado em *Parâmetros | Contas a Receber | Baixas | Cartão de Crédito/Débito - Configurações por Filial*.

Ao iniciar o pagamento com cartão pelo portal, o sistema verifica se existe parametrização por filial definida, se afirmativo, usará a mesma para pagamento distinguindo o modelo de pagamento informado para filial, do contrário usará o modelo parametrizado para coligada.

**Observações:**

As configurações se cadastradas para a Filial, prevalecerá sobre as configurações da coligada.

**Configurações Gerais**

* **Usuário da Baixa:**Usuário a ser utilizado na baixa dos boletos pagos com cartão pelo e-commerce. Caso não seja informado, será utilizado o usuário autenticado no RM.

**Pagamento através do portal educacional**

Acessar o Portal do Educacional para realizar o processo de pagamento via cartão de crédito.

 Informações Complementares

* [DT Pagamento via Cartão modelo Checkout](http://tdn.totvs.com/display/LRM/DT_Checkout_Cielo)
* DT Pagamento via Cartão modelo Checkout IFrame Getnet - 12.1.24
* - [12.1.24](http://tdn.totvs.com/display/LRM/DT+Parametros+Checkou+IFrame+Getnet)
* [DT Captura do pagamento de cartão Crédito/Debito Checkout Cielo](http://tdn.totvs.com/pages/viewpage.action?pageId=269449364)
