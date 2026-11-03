---
content_hash: 70110cfb4ed608f12c7aafdeeb0e7cad869703a554066ee5be5d20a433671047
fetched_at: '2026-06-29T00:11:38.134167+00:00'
page_id: '781214682'
product: rm
source: tdn-rm
title: Proposta - Validação de Parametrização
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=781214682
version: 2
---

API - Validação de Parametrização

| Título | API - Validação de Parametrização |
| --- | --- |
| Endpoint | [http://localhost:8051/api/imb/v1/registrations/validate/pi/enterprises/](http://localhost:8051/api/imb/v1/registrations/validate/pi/enterprises/2057){Cod Empreendimento} |
| Verbo | GET |
| Parameters | Não tem Parãmetros. |
| Descrição | No preenchimento da proposta existem algumas validações ( parâmetro do financeiro sequência, corretor vinculado ao Cli/for, tabela de preço para unidade, modalidade de venda parametrizada) que ajudam o corretor a não continuar a proposta caso os mesmos já não estiverem já definidos. Essa API seria facilitadora para que o corretor não preencha cada campo para descobrir que falta parametrização padrão    Api geral - Valida todos Empreendimentos :  [http://localhost:8051/api/imb/v1/registrations/validate/pi](http://localhost:8051/api/imb/v1/registrations/validate/pi "Follow link")  Api por empreendimento : [http://localhost:8051/api/imb/v1/registrations/validate/pi/enterprise](http://localhost:8051/api/imb/v1/registrations/validate/pi/enterprises/1 "Follow link")s/2057 Neste exemplo passando pelo Empreendimento 2057    Neste exemplo da API , passou pelo empreendimento 2057 e o Response mostrando as parametrizações que precisam sem feitas. |
| Parãmetros TCGI | Não tem Parãmetros no TCGI. |

.

Modelo Json Solicitação Geração ComissãoBodytrueModelo Json Solicitação Geração ComissãoRESPONSEtrue
