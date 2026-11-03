---
content_hash: c2075cccc9550098246e80bb31e02c77a8eb112ec3a183130e047702f2da0eed
fetched_at: '2026-06-29T00:11:38.148733+00:00'
page_id: '781214896'
product: rm
source: tdn-rm
title: Proposta - Associar Pessoa na Proposta
type: documentation
url: https://tdn.totvs.com/display/LRM/Proposta+-+Associar+Pessoa+na+Proposta
version: 2
---

API - Associar Pessoa na Proposta

| Título | API - Associar Pessoa na Proposta |
| --- | --- |
| Endpoint | [http://localhost:8051/api/imb/v1/sales/proposals/](http://localhost:8051/api/imb/v1/sales/proposals/20_1914)[{Cod Coligada}\_{Número da Venda}](http://localhost:8051/api/imb/v1/sales/proposals/20_1914/approval?note=Solicitar) |
| Verbo | Put ou Post. |
| Parameters | Não tem Parãmetros. |
| Descrição | API para inserir a Pessoa cadastrada na API <http://localhost:8051/rmsrestdataserver/rest/ImbPVIClienteData> em uma proposta no TCGI.    No BODY , informo :  [ { "idcliente": 4, "clienteprincipal": 1, "pessoasadicionais": [{"idpessoa": 111,"tipopessoa": 8}, {"idpessoa": 112,"tipopessoa": 7}  ]    IDPESSOA cadastrada na API Pessoas Adicionais com seu TIPO.  Ao inserir uma Pessoa Adicional via API , retorna seu ID como mostra o cadastro da API acima. |
| Parãmetros TCGI | Não tem Parãmetros no TCGI. |

Modelo Json Solicitação Geração ComissãoBodytrueModelo Json Solicitação Geração ComissãoRESPONSEtrue
