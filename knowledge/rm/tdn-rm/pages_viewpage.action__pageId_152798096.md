---
content_hash: 807c1553b7e6a5847bd8ac2fbc0a947ed265fb984e9cdda576a57b5f0eb9b116
fetched_at: '2026-06-29T00:05:56.518245+00:00'
page_id: '152798096'
product: rm
source: tdn-rm
title: O que validar no SEFIP quando utilizo tomadores de serviço?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=152798096
version: 1
---

| Produto | **RM** |
| --- | --- |
| **Sintoma** | **O que validar no SEFIP quando utilizo tomadores de serviço?** |
| Solução | Caso tenha algum problema no arquivo SEFIP gerado para funcionários que utilizam tomador de serviço, é importante sempre validar as informações abaixo:   * O tomador está devidamente cadastrado para o funcionário na aba Tomadores de serviço (Delphi) ou Rateio Tomadores (.Net)? * O tomador cadastrado no funcionário deve ser diferente do tomador informado em Opções -> Parâmetros -> RM Labore -> aba Param. Cálculo * Foi feita a distribuição dos valores para o funcionário/tomador? Verifique se a mesma foi levada para o tomador correto em Movimento -> Folha de Pagamento -> SEFIP - Distribuição -> Editar (Delphi) ou Encargos -> SEFIP -> Editar distribuição SEFIP (.Net) * Dentro do cadastro dos eventos que estão no envelope do funcionário, na primeira aba, o parâmetro Segue rateio de tomadores está marcado? O mesmo deve estar marcado para todos os eventos que o funcionário que possui tomador recebe |
