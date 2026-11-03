---
content_hash: 381022b83425f4c39854c5ebc88a4dfeec68505748ebf5b472bc831ec3f00119
fetched_at: '2026-06-29T00:10:36.980970+00:00'
page_id: '533729625'
product: rm
source: tdn-rm
title: Regras de geração XML Santa Casa - Faturamento Unimed Curitiba
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=533729625
version: 8
---

## 

## **EXEMPLO 01:****Atendimento Externo - Autorização online (Webservice)**

Dado que: o convênio atue com autorização online

Quando: for solicitada a autorização

Então: deverá ser gerada uma guia de solicitação de SPSADT

E: o convênio a partir do recebimento da solicitação consiga analisar e autorizar

E a partir disso autorizar em uma guia de SPSADT

Então para esses casos deverá ser incluída uma guia de: **SOLICITAÇÃO DE SP/SADT e SPSADT.**

E quando o convênio atuar somente com **autorização manual**

Então a guia de solicitação de SPSADT não será obrigatória

E SOMENTE OBRIGATÓRIA A **GUIA DE SPSADT**

## **EXEMPLO 02:****Atendimento Externos - Autorização Manual**

Dado que: o convênio atue com solicitação de autorização manual

Quando: informado o tipo de guia

Então: somente a guia do tipo **SPSADT** será obrigatória

## **EXEMPLO 03:****Atendimento Externos - Datas da guia de Solicitação de SP/SADT e guia SP/SADT**

Dado que: foi inserida uma guia de **Solicitação de SPSADT**

Quando: for informada a data da guia no sistema

Então: poderá ser diferente do período da parcial

E: quando for a guia de **SPSADT**

Então: deverá ser sempre dentro do período da parcial

## **EXEMPLO 04:****Atendimento Externo Guias Diferentes**

Dado que: foi necessário incluir mais de uma guia com autorizações diferentes

Quando: necessário separar os lançamentos por guia

Então: será necessário realizar o vínculo de cada item com sua devida guia

E: desta forma na geração do xml seja possível a distribuição dos lançamentos

com suas devidas guias

## **EXEMPLO 05:****Atendimento Internação - Geração XML para Honorários/SADT Exames de imagem /Resumo**

Dado que: será necessário gerar os xmls separados para a Unimed Curitiba

Quando: for realizado a geração do xml

Então: será necessário que a configuração na aba eletrônico TISS II, esteja como:

Faturamento para convênios

E na geração do xml esteja marcado a opção gerar xml para terceiros

**Configurações e processos necessários:**

1. Nas condições contratuais, estar selecionado o **Faturamento para Médicos** no campo **Informações Especificas**.

2. No cadastro do Prestador > Credenciamento, o médico deverá estar configurado como **Indireto**.

3. No processo de geração de Fatura / Remessa, o campo **Gerar XML para terceiros** deve estar marcado.

## **EXEMPLO 06:****Atendimento Internação - Geração XML para Honorários/SADT Exames de imagem e Exames de laboratório/Resumo**

Dado que: a conta possui lançamento de exames de laboratório

Quando:for gerado o xml

Então: não poderá ser exibida a tag equipe

**Configurações necessárias:**

Para que a tag não seja exibida, será necessário parametrizar nas condições contratuais a faixa de exames de laboratório.

## **EXEMPLO 07:****Atendimento Internação - Geração XML para Honorários Fora da Conta/SADT Exames de Imagem e Exames de Laboratório/Resumo**

Dado que: o prestador não for credenciado e precisa ser gerado o xml com os dados do Hospital

Quando: for realizada a configuração, deverá ser informado que o prestador é fora da conta

Então: ao gerar o xml, a tag será preenchida com os código do Hospital na Operadora.

## **EXEMPLO 08:****Atendimento Externo - Geração XML para credenciamento indireto SADT**

**Dado** que foi lançado na conta um exame, e o profissional é credenciado indireto  
   
**Quando** for gerado o xml para a Unimed Curitiba  
   
**Então**  deverá ser exibido o código de credenciamento do Hospital na operadora

Faturamento para convênios

E na geração do xml esteja marcado a opção gerar xml para terceiros

**Configurações e processos necessários:**

1. Nas condições contratuais, estar selecionado **Unimed Curitiba**  no campo **Informações Especificas**.

2. No cadastro do Prestador > Credenciamento, o médico deverá estar configurado como **Indireto**.

3. No processo de geração de Fatura / Remessa, o campo **Gerar XML para terceiros** deve estar marcado.
