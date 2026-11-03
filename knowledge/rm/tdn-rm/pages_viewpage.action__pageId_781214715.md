---
content_hash: 286c219fa78069fe95d978272de53d082fdd488ae958a1d9376fca8220da3834
fetched_at: '2026-06-29T00:11:38.137922+00:00'
page_id: '781214715'
product: rm
source: tdn-rm
title: Proposta - Solicitação Aprovação Proposta Reprovada
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=781214715
version: 2
---

API de Solicitação de Aprovação de Proposta Reprovada

| Título | **API de Solicitação de Aprovação de Proposta Reprovada** |
| --- | --- |
| Endpoint | [http://localhost:8051/api/imb/v1/sales/proposals/{Cod Coligada}\_{Número da Venda}/approva](http://localhost:8051/api/imb/v1/sales/proposals/20_1914/approval?note=Solicitar)l |
| Verbo | Post |
| Parameters | .   | Key | Value | | --- | --- | | note | Informe a mensagem de observação do corretor para o supervisor | | url | Informe o endereço da web para realizar a aprovação da proposta | |
| Descrição | Api para solicitar aprovação de proposta de venda quando a mesma foi reprovada pela validação.  Ao solicitar a aprovação da proposta o sistema enviára um e-mail para o supervisor do corretor solicitadando a sua aprovação, desde que o parâmetro "Permite Forçar Proposta" esteja marcado.  Para o envio do e-mail os campos dos parâmetros do TCGI → Portal do Imóvel→ Porposta de Venda devem ser preenchidos  Baixe  **aqui** o modelo do corpo do e-mail |
| Parâmetros  do TCGI |  |

Modelo Json Solicitação Geração ComissãoBodytrueModelo Json Solicitação Geração ComissãoRESPONSEtrue
