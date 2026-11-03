---
content_hash: 880fe5f20cd8edd4e1e81486b23456a21928e5eee0ddf2ad98a086074dfa5e83
fetched_at: '2026-06-29T00:11:38.114235+00:00'
page_id: '781213960'
product: rm
source: tdn-rm
title: API - PARAMETROS
type: documentation
url: https://tdn.totvs.com/display/LRM/API+-+PARAMETROS
version: 4
---

Parâmetros

### Apis de Parâmetros

API: GET: <http://localhost:8051/api/imb/v1/parameters/getParameter?company=0&parameter=UTILIZACOMISSAOVERSAO2>

API para verificar se a comissão 2.0 está ativada..

Modelo Json Solicitação Geração ComissãoRESPONSEtrueParâmetros

Dados recebidos:

* company: Código da coliga. (0 para coligada global);
* name: Nome do parâmetro para verificação;
* value: Pode ser 1 ou 0. Se 1, está ativado e 0 está desativado.
