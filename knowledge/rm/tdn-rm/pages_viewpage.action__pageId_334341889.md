---
content_hash: ecba562527c573aad9608eb0d3eeb3bfb5b325c96f1ac5f39d2083194a315bbd
fetched_at: '2026-06-29T00:08:50.850140+00:00'
page_id: '334341889'
product: rm
source: tdn-rm
title: ER FINANCEIRO01-4595 Integração TOTVS Gestão Financeira com TOTVS e-commerce
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=334341889
version: 111
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | TOTVS Gestão Financeira / Portal Educacional |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** |  | **IRM/EPIC1** |  |
| **Requisito/Story/Issue1** | <http://jiraproducao.totvs.com.br/browse/FINANCEIRO01-4595> | **Subtarefa1** |  |
| **Chamado/Ticket2** |  | | |
| **País** | (x) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** |  | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Integrar o portal do Educacional e TOTVS gestão Financeira com a solução de pagamento on-line TOTVS e-commerce.

## Definição da Regra de Negócio

*Alteração Estrutura de Banco de Dados*

* Inserir na tabela FINTEGRACAOSTATUS o status abaixo
  + 12 - Pagamento em Cancelamento (Será utilizado quando for solicitado um cancelamento de transação, devido o cancelamento poder demorar alguns dias)
* Inserir os parâmetros abaixo na tabela FPARAM (Verificar a possibilidade de utilizar os mesmos campos do buypage da Cielo). Os parâmetros abaixo também devem permitir ser informados por filial.
  + Habilitar pagamento modelo TOTVS e-commerce  (Mais uma opção no ID 1104 da FPARAM)
  + URL ambiente TOTVS e-commerce  (Parâmetro novo)
  + Numero de Filiação  (CIELO buypage - Código de afiliação do Lojista - ID 1037 na FPARAM)
  + Token  (CIELO buypage  Chave de Acesso do Lojista - ID 1071 na FPARAM)
  + Ambiente Ativo   (CIELO buypage - Ambiente Ativo - ID 1087 na FPARAM)
  + URL Ambiente Teste (CIELO buypage URL Ambiente Teste - ID 1089 na FPARAM)
  + URL Ambiente Produção (CIELO buypage URL Ambiente Produção  - ID 1088 na FPARAM).

Alteração Parametrizador

* No parametrizador em 02.02 - Contas a Receber | 02.02.02 - Baixas | 02.02.02.03 Cartão de Crédito/Débito | Configurações gerais 1/2, criar a opções "e-rede" e "getnet" e parâmetro  "URL para o ambiente TOTVS e-commerce"

 

* No parametrizador em 02.02 - Contas a Receber | 02.02.02 - Baixas | 02.02.02.03 Cartão de Crédito/Débito | Configurações gerais 2/2, caso o parâmetro "Habilitar pagamento modelo TOTVS e-commerce" esteja marcado deverá ser apresentado os seguintes parâmetros: (Verificar a possibilidade de utilizar os mesmos campos do buypage da Cielo)  
  + Numero de Filiação = CIELO buypage - Código de afiliação do Lojista - ID 1037 na FPARAM
  + Token  = CIELO buypage -  Chave de Acesso do Lojista - ID 1071 na FPARAM
  + Ambiente Ativo  = CIELO buypage - Ambiente Ativo - ID 1087 na FPARAM
  + URL Ambiente Teste = CIELO buypage URL Ambiente Teste - ID 1089 na FPARAM
  + URL Ambiente Produção = CIELO buypage URL Ambiente Produção  - ID 1088 na FPARAM

*Efetuando pagamento com cartão e-Rede:*

* + Ao solicitar um pagamento parametrizado para utilizar a solução TOTVS e-commerce, será necessário primeiramente solicitar a criação da transação na FINTEGRACAOCARTAO com o status de "-2 Sistema acessado"
    - Criar um novo método na Classe FinCartaoRedeMod
    - Método: InsereTransacaoRede
    - Gravar o CODCOLIGADA, IDBOLETO, IDENTIFICADORORIGEM e CODAFILIACAO
    - Gravar o campo IDMODELO como "4" - e-rede ou 5- getnet (Cria essa opção no enumerado FinModeloTransacaoEnum)
    - O método deverá retornar o campo "IDTRANSACAO" para que seja utilizado como código do Pedido do Estabelecimento
  + Chamar a página de pagamento online da solução TOTVS e-commerce que foi configurada no novo parâmetro "URL para o ambiente TOTVS e-commerce" passando os seguintes parâmetros: vide: 
    - *Adquirente (e-Rede/GetNet)*
    - *Numero de Filiação (PV)*
    - *Token*
    - *URL (Homologação ou Produção)*
    - *URL de retorno a pagina do estabelecimento*
    - *Código do Pedido do Estabelecimento (IDTRANSACAO gerado na FINTEGRACAOCARTAO)*
    - *Valor (Exemplo R$ 10,00 = 1000 | R$ 0,50 = 50)*
    - *Numero máximo de parcelas*
    - *Descrição do Serviço*
  + Na chamado da pagina de pagamento online da solução TOTVS e-commerce, será necessário passar a "URL de retorno do estabelecimento", que será responsável em chamar o serviço de baixa e apresentar para o usuário se a transação foi concluída ou não com sucesso. Essa página, que deverá ser criada, irá receber os seguintes parâmetros na URL:
    - *Sucesso - true/false*
    - codigoretorno - Preenchido caso tenha ocorrido erro - sucesso = false
    - mensagemretorno - Preenchido caso tenha ocorrido erro - sucesso = false
    - codigopedidoestabelecimento - Código do Pedido do Estabelecimento
    - TID - Numero identificar único da transação
    - NSU - Numero sequencial retornado pela Rede
    - codutorizacao****-****Numero de autorização da transação retornado pelo emissor do cartão
    - valor - Valor total da transação (Exemplo R$ 10,00 = 1000 | R$ 0,50 = 50)
    - numparcelas - Numero de Parcela da Transação
    - bandeira
  + Criação da pagina de retorno "URL de retorno do estabelecimento".
    - Criar a pagina na estrutura: \Corpore.Net\Source\Fin-Financeiro\RM.Fin.Lan\TOTVSecommerce
    - Nome: FinLanCartaoRetornoTOTVSecommerce.aspx
    - Se parâmetro "sucesso" igual a "true":
      * Chamar o serviço de baixa para o TOTVS e-commerce
        + Se a baixa for concluída com sucesso 
          - Apresentar para usuário pagina que a transação foi concluída com sucesso.
        + Se a baixa não for concluída, 
          - Apresentar para usuário que a transação com cartão foi concluída com sucesso mas a baixa do boleto não foi efetuada devido a erro.
    - Se parâmetro "sucesso" igual a false:
      * Chamar serviço para modificar na "FINTEGRACAOCARTAO" o STATUS para "-1 Falha no Pagamento com Cartão" e gerar o registro na tabela "FINTEGRACAOHISTORICO"
      * Apresentado para o usuário página que a transação não foi concluída
  + Criação do serviço de baixa para o TOTVS e-commerce
    - Irá receber os seguintes parâmetros:
      * codigopedidoestabelecimento (É o campo "IDTRANSACAO" da tabela "FINTEGRACAOCARTAO", é por ele que será localizado o boleto a ser baixado)
      * TID (Será gravado no campo "IDPROCESSO" da tabela "FINTEGRACAOCARTAO")
      * NSU (Será gravado no campo "NSU" criado na "FINTEGRACAOCARTAO")
      * codautorizacao (Será gravado no campo "CODAUTORIZACAO" criado na "FINTEGRACAOCARTAO")
      * valor
      * bandeira
    - Deverá através do parâmetro  "codigopedidoestabelecimento" localizar o boleto
    - Apos localizado o boleto chamar serviço para colocar os lançamento do boleto como baixa pendente por cartão de crédito
    - Chamar o serviço de baixa do boleto
    - Se a baixa efetuar com sucesso 
      * Chamar serviço para atualizar o status da tabela "FINTEGRACAOCARTAO" com "6 Pagamento Concluído" e incluir o registro de historico na tabela "FINTEGRACAOHISTORICO
    - Se ocorrer algum erro na baixa
      * Chamar serviço para atualizar o status da tabela "FINTEGRACAOCARTAO" com "4 Pagamento Confirmado" e incluir o registro de histórico na tabela "FINTEGRACAOHISTORICO"
      * Retornar a mensagem erro.

Efetuando cancelamento transação TOTVS e-commerce

* + A solicitação de cancelamento deverá ser efetuada pelo processo "Cancelar Transação" que ficará localizado no menu processo do "Histórico de Transações"
  + Somente transações com Status "4 Pagamento Confirmado" e "6 Pagamento Concluído" poderão ser canceladas.
  + Chamar o serviço de cancelamento de transação do webservice TOTVS e-commerce passando como parâmetro:
    - IDPROCESSO (tid)
    - VALOR
  + Se serviço de cancelamento o parametro de retorno "Código de retorno da transação de cancelamento" estiver vazio significa que o cancelamento foi efetuado com sucesso então:
    - Chamar serviço para atualizar o status da tabela "FINTEGRACAOCARTAO" com "12 Em Cancelamento" e incluir o registro de histórico na tabela "FINTEGRACAOHISTORICO" com os seguintes parâmetros que o serviço retornou:
    - * Código de retorno da solicitação de cancelamento gerado pela rede
      * Data da transação de cancelamento
      * Código identificador da transação de solicitação de cancelamento
    - Se a solicitação de cancelamento estiver ocorrendo na mesma data da transação então o processamento irá ocorrer no mesmo dia então:
      * Chamar serviço de consulta de transação do webservice TOTVS e-commerce passando o seguinte parâmetro
        + IDPROCESSO
      * Se o parâmetro de retorno "Status da solicitação de cancelamento" retornar "SUCESSO" significa que o cancelamento já foi processado então:
        + Chamar serviço de cancelamento de baixa
        + Se cancelamento de baixa concluída com sucesso
          - Chamar serviço para atualizar o status da tabela "FINTEGRACAOCARTAO" com "7 Pagamento Cancelado" e incluir o registro de histórico na tabela "FINTEGRACAOHISTORICO"
        + Se cancelamento de baixa não concluída
          - Apresentar mensagem de erro no LOG
    - Se a solicitação de cancelamento estiver ocorrendo em uma data diferente da transação então o cancelamento só irá ocorrer em D+1, com isso o cancelamento de baixa será efetuado pelo processo de ajuste de transação

Ajuste de Transação

* + Será utilizado o serviço de Ajuste de transação que já existe hoje no menu "Movimentação Bancaria | Cartão de Crédito/Débito"
  + Serão selecionados todos os registro da tabela "FINTEGRACAOCARTAO" que estão com status "-2 Sistema Acessado", "4 - Pagamento Confirmado" e "12 Em Cancelamento" e que o campo IDMODELO igual "4 - e-rede o u 5 - getnet"
  + Para cada registro será chamado o serviço de consulta de transação do webservice TOTVS e-commerce passando como parâmetro o IDTRANSACAO (Código do Pedido do Estabelecimento)
    - Caso não seja encontrado encontrada a Transação
      * Chamar serviço para atualizar o status da tabela "FINTEGRACAOCARTAO" com "11 Pagamento Expirado" e incluir o registro de histórico na tabela "FINTEGRACAOHISTORICO"
    - Para registro com status igual "-2 Sistema Acessado" e "4 - Pagamento Confirmado" e parâmetro STATUS da consulta igual "Approved" (
      * Fazer a chamada Serviço de baixa para o TOTVS e-commerce" detalhada acima no tópico "Criação do serviço de baixa para o TOTVS e-commerce"
    - Para registro com status igual "12 Em Cancelamento" e parâmetro "Status da solicitação de cancelamento" da consulta igual a "SUCESSO" (Cancelamento efetivado)
      * Chamar serviço de cancelamento de baixa
      * Se cancelamento de baixa concluída com sucesso
        + Chamar serviço para atualizar o status da tabela "FINTEGRACAOCARTAO" com "7 Pagamento Cancelado" e incluir o registro de histórico na tabela "FINTEGRACAOHISTORICO"
    - Toda ação deverá ser registrada em LOG para ser apresentada ao usuário no final do processo

## Fluxo do Processo

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
