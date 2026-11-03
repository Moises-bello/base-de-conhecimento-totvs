---
content_hash: 47f2edf52218d58caf82e2caf169bcbafe9f9ba5ad36624638f5172bc793459d
fetched_at: '2026-06-29T00:11:18.223871+00:00'
page_id: '684327442'
product: rm
source: tdn-rm
title: Integração RM x Protheus
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=684327442
version: 2
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Versões da Integração**
3. **EAI 2.0**
4. **Adicionando Parâmetro de Integração**

## **01. VISÃO GERAL**

Esse documento visa esclarecer o comportamento da baixa quando o RM está integrado com o Protheus.

## **02. VERSÕES DA INTEGRAÇÃO**

* EAI 2.0

## **03. EAI 2.0**

1. **TOTVS Construção Gestão de Imóveis X BackOffice Protheus**

* + **Atualizar lançamentos que tiveram valores financeiros alterados no formulário da baixa**

Essa funcionalidade estará disponível a partir da 12.1.34.xxx ou superior.

Caso alguma informação de valor de juros, multa, capitalização, e valores opcionais, dos lançamentos que estiverem sendo baixados forem alterados pelo cliente no formulário de baixa, a partir dessa versão, antes de efetuar a baixa, os lançamentos alterados serão atualizados no RM e nesse momento uma mensagem de alteração do lançamento será enviado ao Protheus.

Para habilitar esse comportamento será necessário  criar um parâmetro de integração com o nome  “ATUALIZA\_LANCAMENTOS\_BAIXA” do tipo booleano.

 

OBS: Somente lançamentos a receber terão esse comportamento.

OBS: Caso a alteração do lançamento falhe a baixa não será realizada.

OBS: Para as integrações que estão utilizando o envio da mensagem após o commit, a alteração e a baixa devem pertencer ao mesmo id de grupo de mensagem.

## **04.  ADICIONANDO PARÂMETRO DE INTEGRAÇÃO**

Acessar o modulo de Integrações.

Acessar o menu EAI 2.0.

Clicar no botão "Parâmetros adapter".

Na visão de parâmetros do adapter, incluir um novo parâmetro.
