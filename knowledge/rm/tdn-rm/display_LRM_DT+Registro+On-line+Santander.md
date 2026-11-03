---
content_hash: 7597df0650f50b31e26c6148003b4ddd08f9e68dadca4426713fe6e42f6ce549
fetched_at: '2026-06-29T00:08:29.489560+00:00'
page_id: '272147537'
product: rm
source: tdn-rm
title: DT Registro On-line Santander
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+Registro+On-line+Santander
version: 118
---

# Serviço Registro On-line Santander

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | **Portal Educacional e Processo Seletivo** |
| **Requisito/S****tory/Issue:** | *EDUCTB002-630* |

## Descrição

Esta implementação tem como objetivo preparar o TOTVS Gestão Financeira para utilizar o serviço de registro online da carteira de cobrança registrada do Banco Santander.

## Procedimento para Configuração

No TOTVS Gestão Financeira, menu *Movimentações Bancárias | Controle Bancário | Convênio,* devem ser feitas as configurações do convênio para o registro de boleto online. Figura 1:

* **Permite registro de boleto online*:***Define se o convênio permite utilizar o registro de boleto online.
* **Ambiente**: Define o ambiente que será feito o registro do boleto no banco.
* **URL do serviço de registro do boleto**: Deve ser informada a URL do serviço de registro do boleto disponibilizada pelo banco. Para o banco Santander é a URL do serviço de cobrança. (<https://ymbcash.santander.com.br/ymbsrv/CobrancaV3EndpointService>)
* **URL do serviço do ticket de segurança**: Deve ser informada a URL do serviço do ticket de segurança disponibilizado pelo banco.  (<https://ymbdlb.santander.com.br/dl-ticket-services/TicketEndpointService>)
* **Cód. Estação**: Deve ser informado o código da estação do convênio gerada pelo banco.
* **Certificado digital**: Deve ser informado o certificado digital que foi cadastrado junto ao banco.

**Importante**: **Conforme manual disponibilizado pelo banco, o cliente deverá adquirir um certificado digital junto a uma empresa certificadora, e efetuar o cadastramento no ambiente de segurança do banco enviando o arquivo no formato ".CER" referente ao certificado adquirido. Requisitos: Certificado tipo Client de 2048 bits.**

divs
