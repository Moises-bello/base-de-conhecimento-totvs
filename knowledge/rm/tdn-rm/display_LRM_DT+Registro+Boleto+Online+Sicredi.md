---
content_hash: e268b18e561cb3a303549566faca4b699626a2209c3d36253bcac6f17b63b06c
fetched_at: '2026-06-29T00:08:46.122264+00:00'
page_id: '315901508'
product: rm
source: tdn-rm
title: DT Registro Boleto Online Sicredi
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+Registro+Boleto+Online+Sicredi
version: 103
---

# REGISTRO ONLINE DE BOLETO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção & Projetos* |
| **Módulo:** | **TOTVS Gestão Financeira** |
| **Requisito/S****tory/Issue:** | *<http://jiraproducao.totvs.com.br/browse/FINANCEIRO01-1135>* |

## Descrição

Esta implementação tem como objetivo preparar o TOTVS Gestão Financeira para utilizar o serviço de registro online de cobrança registrada da Sicredi.

## Procedimento para Configuração

No TOTVS Gestão Financeira, menu *Movimentações Bancárias | Controle Bancário | Convênio,* devem ser feitas as configurações do convênio para o registro de boleto online:

* **Permite registro de boleto online*:*** Define se o convênio permite utilizar o registro de boleto online.
* **Ambiente**: Define o ambiente que será feito o registro do boleto no Banco. (campo disponível somente no modelo "v2")
* **Modelo de Registro Online:**Define o modelo do registro online: v1 ou v2
* **URL do serviço de registro de cobrança**: Deve ser informada a URL do serviço de registro de cobrança disponibilizada pelo banco. Exemplo:
  + <https://api-parceiro.sicredi.com.br/cobranca/boleto/v1>
* **URL do sistema autenticação**: Deve ser informado a URL do sistema de autenticação conforme manual disponibilizado pelo banco. Exemplo:
  + <https://api-parceiro.sicredi.com.br/auth/openapi/token>
* **URL do serviço de registro de cobrança - Homologação**: Deve ser informada a URL do serviço de registro de cobrança - Homologação conforme manual disponibilizado pelo banco. (campo disponível somente no modelo "v2") Exemplo:
  + <https://api-parceiro.sicredi.com.br/sb/cobranca/boleto/v1>
* **URL do sistema autenticação - Homologação**: Deve ser informado a URL do sistema de autenticação - Homologação conforme manual disponibilizado pelo banco. (campo disponível somente no modelo "v2") Exemplo:
  + <https://api-parceiro.sicredi.com.br/sb/auth/openapi/token>
* **Usuário**: Deve ser informado o usuário disponibilizado pelo banco. (campo disponível somente no modelo "v2")
* **Senha**: Deve ser informada a senha disponibilizada pelo banco. (campo disponível somente no modelo "v2")
* **Chave de API (x-api-key)**: Deve ser informado a chave API disponibilizado pelo banco. (campo disponível somente no modelo "v2")
* **Chave de API (x-api-key) - Homologação**: Deve ser informado a chave API de homologação disponibilizado pelo banco. (campo disponível somente no modelo "v2")

Pode ser utilizado o , para enviar dados de forma flexível para o registro online dos boletos para o banco. Para isso deve ser feito o  no cadastro do convênio utilizado para o registro online.

O cadastro do layout do registro online do Sicredi deve ser feita de acordo com o manual de cobrança online do banco, da seguinte maneira:

* Exemplos:  
  informativo

mensagem

multa

Juros

tipoDesconto

valordesconto1

dataDesconto1

valorDesconto2

dataDesconto2

valorDesconto3

dataDesconto3

pagador.tipoPessoa

pagador.nome

pagador.endereco

**Importante:** Para o campo espécie do boleto deve ser informado os seguintes valores definidos conforme o manual do banco:

A - DUPLICATA MERCANTILINDICACAO  
B - DUPLICATA RURAL  
C - NOTA PROMISSORIA  
D - NOTA PROMISSORIA RURAL  
E - NOTA SEGUROS  
G - RECIBO  
H - LETRA CAMBIO  
I - NOTA DEBITO  
J - DUPLICATA SERVICO INDICACAO  
K - OUTROS  
O - BOLETO PROPOSTA  
P - CARTAO CREDITO

**Observação: Apesar da v2 do Sicredi possuir um serviço que permite o cancelamento do registro online e alteração da data de vencimento do boleto, a funcionalidade ainda não está disponível no TOTVS Gestão Financeira e será implementada futuramente.**

divs
