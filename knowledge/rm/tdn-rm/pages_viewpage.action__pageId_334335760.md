---
content_hash: 6f2439446fe12da6a0891a7b879d443272be15f17f6fe39aa6429d7f1da917e7
fetched_at: '2026-06-29T00:08:50.748957+00:00'
page_id: '334335760'
product: rm
source: tdn-rm
title: ER FINANCEIRO01-4595 Integração TOTVS e-commerce
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=334335760
version: 119
---

> | **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
> | --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | TOTVS Gestão Financeira |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** |  | **IRM/EPIC1** |  |
| **Requisito/Story/Issue1** | <http://jiraproducao.totvs.com.br/browse/FINANCEIRO01-4595> | **Subtarefa1** |  |
| **País** | (x) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| Outros | Rede : [Manual de integração API RESTFul e-Rede](https://www.userede.com.br/desenvolvedores/images/uploads/manual_integracao_api_rest.pdf)  getnet: [Manual de integração e-commerce getnet](https://www.auttar.com.br/download/e-commerce/?wpdmdl=457)  maxiPago: [Manual de integração e-commerce maxiPago](http://developers.maxipago.com/wp-content/uploads/2017/10/maxiPago_Guia_de_Afiliacoes.pdf) | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Integrar as soluções TOTVS com a solução de pagamentos online disponíveis no mercado. (e-Rede, getnet, maxiPago)

Para que a integração seja independente do produto, e seja utilizada por qualquer solução da TOTVS, será criada uma nova solução, denominada "TOTVS e-commerce" no qual irá ter a web-page para digitação dos dados sensíveis do cartão e um web-service para fazer a comunicação com os serviços da adquirente.

A solução TOTVS e-commerce deverá ter um instalador próprio.

## Definição da Regra de Negócio

*Criação da web-page para digitação dos dados do cartão:*

* *Dados de entrada:*
  + *Adquirente (e-Rede ou GetNet ou maxiPago)*
  + *Numero de Filiação (PV)*
  + *Token/Chave Acesso*
  + *URL e-Rede (Homologação ou Produção)*
  + *URL de retorno a pagina do estabelecimento*
  + *Código do Pedido do Estabelecimento*
  + *Valor (Exemplo R$ 10,00 = 1000 | R$ 0,50 = 50)*
  + *Numero máximo de parcelas*
  + *Descrição do Serviço*
* *Dados para digitação:*
  + *Numero do Cartão*
  + *Nome do portador impresso no cartão*
  + *Mês vencimento do cartão*
  + *Ano vencimento do cartão*
  + *Código de Segurança do cartão*
* *Validações*
  + *Deverá ser feita a validação, através de javascript de qual bandeira o cartão pertence*
* *Ação*
  + *Ao finalizar o pagamento será chamado do webservice o serviço de criação de transação*
* *Dados de Retorno:*
  + **Após chamada do serviço de criação de transação, c*aso parâmetro de entrada "URL de retorno a pagina do estabelecimento" esteja preenchido será feita chamada dessa URL, passando os seguintes parâmetros na linha de comando: (ex: http://totvs.com.br/corporerm/URLRetorno?sucesso=false&codigoretorno=101&mensagemretorno&=Não Autorizado&codigopedidoestabelecimento=0000135&TID=834500036348405380&NSU=66320641&numautorizacao=186376&valor=10289&numparcelas=3)*
    - *Sucesso - true/false*
    - codigoretorno - Preenchido caso tenha ocorrido erro - sucesso = false
    - mensagemretorno - Preenchido caso tenha ocorrido erro - sucesso = false
    - codigopedidoestabelecimento - Código do Pedido do Estabelecimento
    - TID - Numero identificar único da transação
    - ***NSU - Numero sequencial retornado pela Rede***
    - numautorizacao ****-****Numero de autorização da transação retornado pelo emissor do cartão
    - valor - Valor total da transação (Exemplo R$ 10,00 = 1000 | R$ 0,50 = 50)
    - numparcelas - Numero de Parcela da Transação
    - bandeira (Vide tópico abaixo "Identificação *da Bandeira do cartão")*
  + Caso parâmetro de entrada "URL de retorno a pagina do estabelecimento" não esteja preenchida, será chamada a web-page padrão de transação concluída ou não concluída conforme especificado mais abaixo
* *Chamada serviço e-Rede*
  + *Deverá ser montado o JSON de acordo com o [manual de integração API RESTFul e-Rede](https://www.userede.com.br/desenvolvedores/images/uploads/manual_integracao_api_rest.pdf)*
  + *Captura deverá ser automática*
* *Chamada serviço getnet*

Criação da web-page padrão de transação concluída ou não concluída:

* Dados de entrada
  + Código do Retorno (00 = Sucesso)
  + ***Mensagem de Retorno da Transação***
  + ***Descrição do Serviço***
  + *TID - Numero identificador único da transação*
  + NSU - Numero sequencial retornado pela Rede
  + ***Numero de autorização da transação retornado pelo emissor do cartão***
  + ***Valor total da transação *(Exemplo R$ 10,00 = 1000 | R$ 0,50 = 50)****

Criação do webservice para integração com adquirente:

* Serviço de Criação da Transação
  + Dados de Entrada
    - *Adquirente (e-Rede ou GetNet ou maxiPago)*
    - **Numero de Filiação (PV)**
    - **Token / Chave Acesso**
    - *URL (Homologação ou Produção)*
    - Tipo de Transação (Crédito/Débito)
    - Código do Pedido do Estabelecimento
    - *Valor (Exemplo R$ 10,00 = 1000 | R$ 0,50 = 50)*
    - Numero de Parcelas
    - *Nome do portador impresso no cartão*
    - *Numero do Cartão*
    - **Mês vencimento do cartão**
    - ***Ano vencimento do cartão***
    - *Código de Segurança do cartão*
  + *Chamada serviço e-Rede*
    - *Deverá ser montado o JSON de acordo com o [manual de integração API RESTFul e-Rede](https://www.userede.com.br/desenvolvedores/images/uploads/manual_integracao_api_rest.pdf)*
    - *Captura deverá ser automática*
  + *Chamada serviço getnet*
    - *Deverá ser montado o XML de acordo com o [Manual de integração e-commerce getnet](https://www.auttar.com.br/download/e-commerce/?wpdmdl=457)*
    - *Se tipo de transação igual a crédito*
      * *Para crédito chamar o serviço efetuarcredito*
    - *Se tipo de transação igual a débito*
      * *Verificar se o emissor do cartão suporta autenticação. Chamar o serviço verificarInscricacaoMPI*
      * *Se bandeira\emissor do cartão suporta autenticação:*
        + *Direcionar usuário para url de retorno do banco emissor do cartão*
        + *Se autenticação ocorrer com sucesso*
          - **chamar o serviço efetuarDebito (Vide abaixo diagrama de sequencia "Efetuar pagamento cartão débito getnet")**
      * *Se *bandeira\emissor*não suporta autenticação*
        + *Avisar usuário*
        + *Retornar para pagina de digitação de dados do cartão*
  + *Chamada serviço maxiPago*
    - *Deverá ser montado o XML do serviço "Venda Direta" de acordo com o [Manual de integração e-commerce maxiPago](http://developers.maxipago.com/wp-content/uploads/2017/10/maxiPago_Guia_de_Afiliacoes.pdf)*
  + ***Dados de Retorno***
    - ***Código do Retorno***
    - ***Mensagem de Retorno da Transação***
    - Código do Pedido do Estabelecimento
    - TID - Numero identificar único da transação
    - ***NSU - Numero sequencial retornado pela Rede***
    - ***Numero de autorização da transação retornado pelo emissor do cartão***
    - ***Data da transação no formato YYYY-MM-DDthh:mm:ss.sTZD***
    - ***Valor total da transação *(Exemplo R$ 10,00 = 1000 | R$ 0,50 = 50)****
* Serviço de consulta transação
  + Dados de entrada
    - *Adquirente (e-Rede/GetNet)*
    - **Numero de Filiação (PV)**
    - **Token / Chave Acesso**
    - Código do Pedido do Estabelecimento ou;
    - *TID - Numero identificador único da transação*
  + *Chamada serviço e-Rede*
    - Caso código do Pedido do Estabelecimento preenchido chamar *GET: [https://api.userede.com.br/erede/v1/transactions?reference=[código\_pedido]](https://api.userede.com.br/erede/v1/transactions?reference=[código_reference)*
    - Caso TID preenchido chamar GET: [https://api.userede.com.br/erede/v1/transactions?reference=[TID]](https://api.userede.com.br/erede/v1/transactions?reference=[c%C3%B3digo_reference)
    - *Detalhes no [manual de integração API RESTFul e-Rede](https://www.userede.com.br/desenvolvedores/images/uploads/manual_integracao_api_rest.pdf)*
  + Chamada serviço getnet
    - Chamar serviço consultarDocumento conforme descrito no  *[Manual de integração e-commerce getnet](https://www.auttar.com.br/download/e-commerce/?wpdmdl=457)*
  + Chamada serviço maxiPago
    - chamar servico consulta "<https://testapi.maxipago.net/ReportsAPI/servlet/ReportsAPI>"
  + Dados de Saida
    - Código do retorno da transação
    - Mensagem de retorno da transação
    - Numero de filiação (PV)
    - Status (Approved, Denied, Canceled, Pending
    - Numero do Pedido gerado pelo estabelcimento
    - *TID - Numero identificador único da transação*
    - NSU - numero sequencial retornado pela Rede
    - *Código de Autorização  da transação retornado pelo emissor do cartão*
    - *Método de pagamento utilizado na transação (Credit/Debit)*
    - *Valor total transação *(Exemplo R$ 10,00 = 1000 | R$ 0,50 = 50)**
    - *Numero de Parcelas*
    - ***Data da transação de cancelamento no formato YYYY-MM-DDthh:mm:ss.sTZD***
    - *Código de Retorno da solicitação de cancelamento gerado pela Rede*
    - *Status da solicitação de cancelamento (Done, Denied, Processing)*
    - *Valor do cancelamento*
* Serviço de solicitação de cancelamento de transação
  + Dados de Entrada
    - *TID - Numero identificador único da transação*
    - Valor ****total da transação *(Exemplo R$ 10,00 = 1000 | R$ 0,50 = 50)*****
  + *Chamada serviço e-Rede*
    - *Deverá ser montado o JSON de acordo com o [manual de integração API RESTFul e-Rede](https://www.userede.com.br/desenvolvedores/images/uploads/manual_integracao_api_rest.pdf)*
  + Chamada serviço getnet
    - chamar o serviço efetuarCancelamento  conforme descrito no  *[Manual de integração e-commerce getnet](https://www.auttar.com.br/download/e-commerce/?wpdmdl=457)*
  + *Chamada serviço maxiPago*
    - Se data de cancelamento igual mesmo dia da transação
      * Chamar serviço Cancelamento (Void) *de acordo com o [Manual de integração e-commerce maxiPago](http://developers.maxipago.com/wp-content/uploads/2017/10/maxiPago_Guia_de_Afiliacoes.pdf)*
    - Se data de cancelamento diferente dia da transação
      * Chamar serviço Estorno (Refund) *de acordo com o [Manual de integração e-commerce maxiPago](http://developers.maxipago.com/wp-content/uploads/2017/10/maxiPago_Guia_de_Afiliacoes.pdf)*
  + Dados de Retorno
    - Código de retorno da transação de cancelamento
    - Mensagem de retorno da transação de cancelamento
    - Código de retorno da solicitação de cancelamento gerado pela rede
    - *TID - Número identificado único de transação*
    - *NSU - Numero sequencial retornado pela rede*
    - ****Data da transação de cancelamento no formato YYYY-MM-DDthh:mm:ss.sTZD****
    - *Código identificador da transação de solicitação de cancelamento*

Identificação da Bandeira do cartão

* ELO
  + Começa com: 636368, 438935, 504175, 451416, 509048, 509067, 509049, 509069, 509050, 509074, 509068, 509040, 509045, 509051, 509046, 509066, 509047, 509042, 509052, 509043, 509064, 509040, 36297, 5067 ,4576 ,4011
* Discover
  + Começa com: 6011, 622, 64, 65
* Diners
  + Começa com: 301, 305, 36, 38
* AMEX
  + Começa com: 34, 37
* AURA
  + Começa com: 50
* JCB
  + Começa com: 35
* Hypercard
  + Começa com: 38, 60
* Visa
  + Começa com: 4
* MasterCard
  + Começa com 5

## Protótipo de Tela

\*Solicitar ajuda do Design Lucas para criação das telas

**Protótipo tela para informar dados de pagamento de cartão de crédito/débito**

**Protótipo tela padrão de pagamento concluído**

**Protótipo tela padrão de pagamento não concluído**

## Fluxo do Processo

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
