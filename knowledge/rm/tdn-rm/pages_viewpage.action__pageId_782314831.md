---
content_hash: c0c7fa0c88c5d25155fcf29345b5500c029599fc25ff8fc610ae4ca8070c7480
fetched_at: '2026-06-29T00:11:38.249246+00:00'
page_id: '782314831'
product: rm
source: tdn-rm
title: API - PDC - Dados do Usuário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=782314831
version: 6
---

Esta API apresenta os dados do Usuário que está logando no Portal de Cliente PDC.

API de Dados do Usuário Logado no PDC

| Título | **API de Dados do Usuário Logado no PDC** |
| --- | --- |
| Endpoint | <http://localhost:8051/api/imb/v1/users/contextuserweb> |
| Verbo | Get. |
| Parameters | no parameters |
| Descrição | Esta API utiliza o verbo GET e em sua resposta apresenta as informações relativas ao usuário que está logando no Portal do Cliente - PDC |

Modelo Json Solicitação Geração ComissãoBODYtrueModelo Json Solicitação Geração ComissãoRESPONSEtrueParâmetros do Response

Parâmetros:

* Usuario: dados básicos do usuário logado no PDC
  + codusuario: Código de acesso do usuário
  + nome: Nome do usuário
  + email: Email deste usuário
* Empreendimentos:
  + company: Código da coligada do empreendimento
  + realEstate: Código do empreendimento em si
  + name: Nome do empreendimento
  + trandingName: Nome de fantasia do empreendimento
  + launchDate: Data de lançamento deste empreendimento
  + origincontracttype: Tipo do contrato, sendo:
    - 0 - Contrato de venda; ou
    - 1 - Contrato de aluguel.
  + contracts: Número dos contratos de venda e aluguel que o cliente possui neste empreendimento
