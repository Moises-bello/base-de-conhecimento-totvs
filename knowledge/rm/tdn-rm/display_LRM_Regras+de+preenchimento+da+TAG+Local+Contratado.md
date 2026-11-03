---
content_hash: ac61d29e62d0524d90cc7409d6e3f89d5bb2978b245ec847ca1962fb4a8d5daf
fetched_at: '2026-06-29T00:10:57.009589+00:00'
page_id: '593976669'
product: rm
source: tdn-rm
title: Regras de preenchimento da TAG Local Contratado
type: documentation
url: https://tdn.totvs.com/display/LRM/Regras+de+preenchimento+da+TAG+Local+Contratado
version: 8
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **XML de Honorário Individual | Local Contratada**

****01. VISÃO GERAL****

O arquivo de XML de Honorário Individual é utilizado para o faturamento de médicos, hospitais e clínicas credenciados diretamente na operadora. Sendo assim, quando a cirurgia ou procedimento for executado em local externo, ou seja, não será executado no local da internação, é necessário informar o local de execução para o processo de faturamento, pois os honorários médicos são acordados por contratos hospitais/operadoras.

Para utilização do XML de honorário individual é necessário fazer algumas parametrizações no sistema, segue abaixo detalhamento:

1) O parâmetro "**Gerar XML de Terceiros em nome do prestador principal nos dados do contratado executante**" deve está marcado, acesse:

Cadastro >> Condições Contratuais >> Eletrônico III - TISS >> Gerar XML de Terceiros em nome do prestador principal nos dados do contratado executante

2) O Campo "**Informações Específicas"** deve está selecionado com a opção "**Faturamento para Médicos**", acesse:

Cadastro >> Condições Contratuais >> Eletrônico III - TISS >> Informações Específicas

3) O Parâmetro "**Informar Local de Execução Externa**" deve está marcado, acesse:

Opções >> Parâmetros Gerais >> Registro de Controle >> Página Dados do Atendimento >> Interno >> Informar Local de Execução Externa.

Na criação de um atendimento interno e onde a cirurgia ou procedimento não for executado no próprio local de internação, então, deve informar o campo  "**Informar Local de Execução Externa**" localizado na aba "**Dados do Atendimento**", com base no conteúdo desse campo a TAG "**Local Contrato**" do XML de Honorário Individual será alimentada com os dados do hospital / clínica que executou de fato serviço.

## **02. EXEMPLO DE UTILIZAÇÃO**

## **03. XML DE HONORÁRIO INDIVIDUAL GERADO | LOCAL CONTRATADO**

]]>
