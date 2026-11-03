---
content_hash: 5a66fd18fe04e70276ef9dfd2118cc3aba09d6e8eec4c1b51c659c8125ee0ac1
fetched_at: '2026-06-29T00:11:38.141721+00:00'
page_id: '781214771'
product: rm
source: tdn-rm
title: Proposta - Aprovar Proposta Forçada
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=781214771
version: 2
---

API Aprovar Proposta Forçada

| Título | **API Aprovar Proposta Forçada** |
| --- | --- |
| Endpoint | <http://localhost:8051/api/imb/v1/sales/proposals/{Cod> Coligada}\_{Número da Venda}/forceapproval |
| Verbo | Post. |
| Parameters | | Key | Value | | --- | --- | | note | Informe a mensagem de observação do Supervisor para o Corretor | | userld | Informe Id do Superior vinculado ao Corretor da Proposta | |
| Descrição | Api para forçar a aprovação de uma Proposta reprovada, caso seja aprovada pelo Superior informado no cadastro dos parametros do Corretor.  Lembrando que o parâmetro no **PI** da Proposta ( **Reprovada** ) tem que estar marcada o parâmetro - **Permite forçar proposta.**  E-mail será enviado para Superior cadastrado configurado no cadastro do Corretor no Portal de Imóveis.  Uma proposta que foi reprovada , o Corretor envia um e-mail para seu Supervisor , conforme API : **API de Solicitação de Aprovação de Proposta Reprovada**citada  no exemplo acima , essa API força que uma proposta Reprovda possa se tornar APROVADA , fazendo que o e-mail possa ser enviado alterando a proposta de Reprovada para  Aprovada.  Baixe TCGIRELPI0002 - Corpo de E-mail para Forçar Aprovação de Proposta.TotvsReport[**aqui**](https://drive.google.com/drive/folders/1Kr00Gb95kIt5QCwHsPVvJv_x4f6Cmzzf) |
| Parâmetros  do TCGI |  |

Modelo Json Solicitação Geração ComissãoBodytrueModelo Json Solicitação Geração ComissãoRESPONSEtrue
