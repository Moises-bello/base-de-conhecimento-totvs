---
content_hash: 91f2b277c322647603ca677139919194102613d8a049f78777aad2209c92c2d4
fetched_at: '2026-06-29T00:09:22.568435+00:00'
page_id: '422546007'
product: rm
source: tdn-rm
title: Código da Conta Contábil (Bloco 1, C e D)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422546007
version: 14
---

A geração do Código da Conta Contábil "COD\_CTA"está disponível para os seguintes Registros:

* Bloco 1: 1510
* Bloco C: C170, C510 e C610
* Bloco D: D510 e D610

1. Será considerado a Conta Contábil informada no Item do Lançamento Fiscal  ***(A partir da versão 12.1.25)***
2. Será verificado se existe default contábil e que possua a classificação "SPED" no CFOP (Natureza de Operação) associado ao Lançamento Fiscal.
3. Será verificado se existe default contábil no Cadastro do Produto/Serviço e que possua a classificação "SPED" informada
4. Não existindo Default Contábil no CFOP ou no Produto que atenda as regras acimas, será utilizada a conta contábil informada no Cadastro – Produto - Dados Fiscais se informado.

***Importante!!!*** Contas cadastradas como Débito, serão para os lançamentos fiscais de entrada, e por sua vez, as contas cadastradas como Crédito serão para os lançamentos de saída. O campo Classificação da Conta, deve ser preenchido com "SPED"(em caixa alta).

Documentação Técnica

[Geração do campo COD\_CTA no Sped Fiscal](http://tdn.totvs.com/pages/viewpage.action?pageId=492709837)
