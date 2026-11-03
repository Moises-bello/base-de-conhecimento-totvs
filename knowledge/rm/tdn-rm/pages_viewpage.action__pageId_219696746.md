---
content_hash: 1720008324337f834c625a880b34e0d3ed771bd844b3015c07afcf91b29caa8e
fetched_at: '2026-06-29T00:06:19.365562+00:00'
page_id: '219696746'
product: rm
source: tdn-rm
title: ER_PCREQ-8605_Eliminação_Resíduos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=219696746
version: 126
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Obras e Projetos | **Módulo** | Geração de Pedidos |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | R\_C&P\_TOP008 | **IRM1** | PCREQ-1546 |
| **Requisito1** | PCREQ-8605 | **Subtarefa1** | PDR\_CP\_TOP008-301 |
| **Chamado2** | Não se aplica. | | |
| **Release de Entrega Planejada** | 12.1.8 | **Réplica** | 12.1.7 |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *Informações de como configurar e utilizar a integração estão em: <http://tdn.totvs.com.br/pages/releaseview.action?pageId=152802572>* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

O objetivo e atender a necessidade de realizar uma nova solicitação com os itens não atendidos no TOP1 .

A eliminação de resíduos é a forma de liberar as quantidades não atendidas de um pedido. No processo de integração entre o TOP e o PROTHEUS, serve para ajustar as quantidades atendidas de forma a liberar para o usuário do TOP a possibilidade de realizar um novo pedido no limite da quantidade não atendida e de acordo com a necessidade do produto no projeto.

***1*** *TOP é a sigla de TOTVS Obras e Projetos que será utilizada neste documento para definir o módulo RM.*

## Definição da Regra de Negócio

## Sistemas Envolvidos

Este processo envolve o TOP e o modulo de compras do BackOffice PROTHEUS.

Visa refletir no TOP as quantidades solicitadas que não são atendidas e consequentemente eliminadas no processo de Eliminar Resíduos do modulo de Compras.

## Integração

O usuário gera uma solicitação no TOP e submete ao Compras do PROTHEUS, para que proceda com a liberação ou com a aquisição dos mesmos. Em alguns casos não há possibilidade de realizar o atendimento do total solicitado, nestas situações, o usuário no modulo de Compras poderá usufrui do processo de Eliminar Resíduos para finalizar a demanda.

A partir desta demanda o sistema de Compras passará a refletir no TOP as quantidades não atendidas e por consequência permitirá ao usuário criar uma nova solicitação.

* Premissas  
   A integração TOTVS Obras e Projetos x BackOffice Protheus deve está configurada no RM e no BackOffice PROTHEUS.
* Arquitetura (Tecnologia)   
   Será utilizada a arquitetura de comunicação por Mensagem Única. São trafegados XMLs estruturados e padronizados pela TOTVS.

## Escopo

As solicitações e pedidos são gerados no TOP através das funcionalidades ”Geração de Pedidos”. Quando associado a um contrato, será enviado um “Pedido de Compra” e quando não associado será enviada uma “Solicitação de Compra”.

Ao executar o processo “Eliminar Resíduos” do modulo de compras do PROTHEUS e a quantidade atendida for diferente do solicitado, a mesma será enviada para ajuste no TOP.  É enviada uma alteração referente ao movimento gerado no TOP, com exceção da eliminação realizada em um pedido que foi criado através de uma solicitação. Neste caso, o Protheus enviará a quantidade atendida e a referência do item da solicitação original. Para demais situações sempre será enviada a quantidade atendida.

Os seguintes cenários serão contemplados conforme descrito:

* O TOP gera uma solicitação e a eliminação de resíduos no PROTHEUS ocorre nesta solcitação. No Compras, ao eliminar o resíduo na solicitação será enviada a quantidade atendida para o TOP, que por sua vez, ajusta a quantidade estornada de acordo com a quantidade atendida. Caso ocorra uma exclusão do pedido no PROTHEUS após a eliminação de resíduos, é enviado uma mensagem com a referência da solicitação, o TOP recebe a mensagem e ajusta a quantidade estornada. Caso tenha ocorrido a criação de um novo pedido, será retornado um erro para o PROTHEUS informando que a realização do estorno irá superar a necessidade e, neste caso o PROTHEUS aborta a exclusão do pedido.
* O TOP gera um pedido e a eliminação de resíduos no PROTHEUS ocorre no pedido. No Compras, será bloqueado a utilização de eliminação de resíduos para pedidos associados a contratos.
* O TOP gera uma solicitação. No Compras é gerado um pedido com base nesta solicitação e a eliminação ocorre no pedido criado.  Após a geração da nota fiscal poderá executar a eliminação de resíduos no pedido e caso a quantidade comprada seja inferior a quantidade do pedido, será enviada a quantidade atendida para o TOP através de um pedido, informando qual o item da solicitação está sendo ajustado. O TOP verifica a existência da solicitação, ajusta a quantidade estornada de acordo com a quantidade atendida. O Pedido enviado será gravado como histórico com um tipo de movimento especifico criado pela integração. Caso ocorra uma exclusão da nota fiscal no PROTHEUS após a eliminação de resíduos, é enviado uma mensagem com a referência do pedido e da solicitação originada pelo TOP. O TOP recebe a mensagem e ajusta na solicitação a quantidade estornada e elimina o pedido de histórico gerado pela eliminação de resíduos. Caso tenha ocorrido uma nova solicitação e o total solicitado supere a necessidade do projeto, será retornado um erro para o PROTHEUS informando que a realização do estorno irá superar a necessidade e, neste caso o PROTHEUS aborta a exclusão da nota fiscal. Não ocorrendo o erro, a quantidade estornada da solicitação será ajustada e o pedido histórico será excluído.

Para esta demanda é utilizada exclusivamente a integração denominada como TOTVS Obras e Projetos X BACKOFFICE Protheus. Onde serão atualizadas as mensagens definidas para transacionar as solicitações, pedidos e movimentos de entrada.

Para melhor entendimento consulte o tópico Fluxo de Processo deste documento.

## Protheus

A integração por mensagem única deve estar ativa com o EAI devidamente configurado.

Os ADAPTERS necessários para integração devem estar configurados.

## RM

O TBC (TOTVS Businnes Connect) deve estar devidamente instalado e configurado.

As atividades do projeto no TOP devem estar devidamente programadas.

## Instalação/Atualização

As atualizações são disponibilizadas na área de download em: <https://suporte.totvs.com/portal/home>

## Protheus

Informações e instalação do WebService podem ser encontradas em: <http://tdn.totvs.com/display/tec/Web+Services+--+23597>

## RM

Informações sobre o gerenciamento e instalação do TBC podem ser encontradas em: <http://tdn.totvs.com/display/public/rm/TBC> e <http://tdn.totvs.com/pages/releaseview.action?pageId=82477609>. 

## Transações/Entidades/Mensagens únicas

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Método** | **ID** | **Descrição** | **Origem** | **Destino** | **XSD (versões podem variar)** |
| **Cadastros** | 01 | Solicitações (compras/armazém) | RM | Protheus | Request\_1\_010.xsd |
| 02 | Solicitações (compras/armazém) | Protheus | RM | Request\_1\_010.xsd |
| 03 | Pedidos Compra | RM | Protheus | Order\_1\_010.xsd |
| 04 | Pedidos Compra | Protheus | RM | Order\_1\_010.xsd |
| 05 | Nota fiscal | Protheus | RM | Invoice\_3\_006.xsd |
| **Processos** | 05 | Solicitação  (Eliminação de Resíduos) | Protheus | RM | Request\_1\_010.xsd |
| 06 | Pedidos  (Eliminação de Resíduos) | Protheus | RM | Order\_1\_010.xsd |
|  | 07 | Nota Fiscal  (Exclusão) | Protheus | RM | Invoice\_3\_006.xsd |

 

**Solicitações**

Identificador da Mensagem: REQUEST

Versão: 1.010

Módulo RM: TOTVS Obras e Projetos

Módulo Protheus: SIGACOM

Tipo de Envio: Síncrono

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Mensagem Padrão** | **PROTHEUS** | | **RM** | |
| Tabela | Campo | Tabela | Campo |
| **QUANTITYREACHED** |  |  | TITMMOV | QTDATENDIDA |

 

**Pedidos**

Identificador da Mensagem: ORDER

Versão: 3.004

Módulo RM: TOTVS Obras e Projetos

Módulo Protheus: SIGACOM

Tipo de Envio: Síncrono

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Mensagem Padrão** | **PROTHEUS** | | **RM** | |
| Tabela | Campo | Tabela | Campo |
| **QUANTITYREACHED** |  |  | TITMMOV | QTDATENDIDA |
| **REQUESTINTERNALID** |  |  | TITMMOV | REQUESTITEMINTERNALID |

 

**Nota Fiscal**

Identificador da Mensagem: INVOICE

Versão: 3.006

Módulo RM: TOTVS Obras e Projetos

Módulo Protheus: SIGACOM

Tipo de Envio: Síncrono

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Mensagem Padrão** | **PROTHEUS** | | **RM** | |
| Tabela | Campo | Tabela | Campo |
| **ORDERINTERNALID** |  |  | TITMMOV | ORDERITEMINTERNALID |
| **REQUESTINTERNALID** |  |  | TITMMOV | REQUESTITEMINTERNALID |

**Notas:**

Somente os campos adicionados nas respectivas versões foram mapeados neste documento. Para maiores detalhes relacionados a estas transações, consulte a documentação referente a integração em: <http://tdn.totvs.com/pages/releaseview.action?pageId=152802572>

**Limitações/Restrições**

A integração por mensagem única deve conter somente um mapeamento de cada entidade do lado RM para um mesmo web service de destino.

 

## Protótipo de Tela

Não se aplica.

## Fluxo do Processo

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
