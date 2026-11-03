---
content_hash: 14720aa0886a224227c864a06f6de8321f273c5628b702e1c1fe0de960e98ce5
fetched_at: '2026-06-29T00:10:52.433154+00:00'
page_id: '572510281'
product: rm
source: tdn-rm
title: Validações Guia de Consulta
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=572510281
version: 9
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

itensVisão Geral

## **01. VISÃO GERAL**

Caso existam Guias de Consulta para o atendimento, as seguintes validações serão executadas:

* Confere se o tipo de consulta do atendimento foi preenchido, caso não, retorna a mensagem de erro “Falta informar o tipo de consulta para este atendimento. Registre as informações necessárias de acordo com a guia informada.” Observação: Esta validação só ocorrerá se o tipo de atendimento for Consulta ou Exame ou Pronto Socorro.
* Confere se o tipo de consulta é compatível com a versão TISS, se não, retorna a mensagem de erro “Tipo de consulta incompatível com a versão XXX do padrão TISS - ANS. Registre as informações necessárias de acordo com a guia informada.” Observação: Esta validação só ocorrerá se o tipo de atendimento for Consulta ou Exame ou Pronto Socorro.
* Confere se o indicador de acidente foi preenchido, se não, retorna a mensagem de erro “Falta informar o 'Indicador de acidente'. Registre as informações necessárias de acordo com a guia informada."
* Confere se o indicador de acidente é compatível com a versão TISS, se não, retorna a mensagem de erro “Indicador de acidente esta incompatível com a versão XXXX do padrão TISS - ANS. Registre as informações necessárias de acordo com a guia informada.”
Exemplo de Utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

## **03. TABELAS UTILIZADAS**

* SZATENDIMENTO
* SZANSATEND
]]>
