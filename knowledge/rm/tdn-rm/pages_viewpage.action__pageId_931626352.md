---
content_hash: aeeeebd2106ba30a30055c04a0234a0e8b1aad1befca548382c6a7cdecacdc0f
fetched_at: '2026-06-29T00:12:08.374668+00:00'
page_id: '931626352'
product: rm
source: tdn-rm
title: S-1210 - Devolução de plano de saúde
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=931626352
version: 11
---

## 

## **01. VISÃO GERAL**

Este documento tem como objetivo apresentar o passo a passo para realizar a devolução de plano de saúde, nos casos em que o valor de uma mensalidade ou desconto de coparticipação foi lançado incorretamente em uma competência anterior.

## **02. EXEMPLO DE UTILIZAÇÃO**

**1)** Acesse o menu Folha Mensal |  Lançamentos | Retificação da Folha de Pagamento, conforme print abaixo:

**2)** No nosso exemplo, estamos na competência 05/2024. No período 1, foi descontado o valor de R$100,00 de plano de saúde para o funcionário na competência 04/2024, porém o valor correto seria R$50,00.

Para iniciar o processo, selecione o funcionário e informe a competência e o período em que o desconto incorreto foi realizado.

**3)**Criação do evento de ajuste

Deverá criar um evento do tipo Provento, com:

* + Código de Cálculo (CC): *14 – Assistência Médica*
  + Rubrica: *9219 – Desconto de assistência médica ou odontológica*

O evento poderá utilizar fórmula customizada para retorno automático do valor já pago ou como alternativa, o valor poderá ser informado manualmente, conforme a estratégia adotada pela empresa para controle do ajuste.

**Tratamento do histórico de Assistência Médica**

Importante destacar que o processo de retificação não gera automaticamente o valor negativo no Histórico de Assistência Médica, que representa o ajuste necessário para geração dos encargos: Informe de Rendimentos, eSocial dentre outros.

Dessa forma, a inclusão do valor negativo deverá ser realizada por uma das seguintes formas:

* + Lançamento manual no Histórico de Assistência Médica; ou
  + Importação do Histórico de Assistência Médica, utilizando o processo específico de importação.

**4)** Após o lançamento da retificação, a competência 04/2024 passou a conter os seguintes envelopes:

* + **Envelope original (1):** com o desconto de **R$ 100,00** referente à assistência médica.

* + **Envelope de retificação (10000):** com o valor do **estorno da assistência médica**, corrigindo o desconto indevido.

**5)** No menu Administração de Folha de Pagamento | Funcionário | Anexos | Históricos | Histórico Assistência Saúde, ficará conforme abaixo:

**6)** Na competência 05/2024, foi lançado o valor líquido referente à devolução do desconto de assistência médica ao funcionário, efetuando a devolução na competência atual.

**7)**Na fila de eventos, foram gerados dois XMLs de retificação para a competência 04/2024, que deverão ser enviados para atualizar corretamente o desconto de assistência médica do funcionário.

* + **S-1200:** contendo o envelope 10000, com o evento de estorno da assistência médica.

## 

* + **S-1210:** com o detalhamento correto do plano de saúde, refletindo o valor ajustado após a retificação.
