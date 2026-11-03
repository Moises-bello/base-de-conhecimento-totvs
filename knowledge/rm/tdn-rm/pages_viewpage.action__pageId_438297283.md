---
content_hash: 08576b1d4b55e82f7520db40eb6c57a5d31e14d66c154dfb01d405f92b471d54
fetched_at: '2026-06-29T00:09:52.332152+00:00'
page_id: '438297283'
product: rm
source: tdn-rm
title: Como_Fazer_Venda_Tratamento de Créditos TINxProtheus EAI2.0
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=438297283
version: 1
---

Este documento visa demonstrar como fazer o vínculo de lançamentos de créditos no RM e como isso reflete nos valores acessórios do PROTHEUS utilizando o EAI 2.0. Utilizaremos o processo de vínculo de lançamentos do Financeiro RM para atrelar parcelas de Notas de Crédito, Devoluções e Adiantamento.

Importante

Para utilizar este processo, toda a configuração prévia do ambiente TINxProtheus deve estar configurada.

### Preparação

Primeiramente devemos ter uma venda efetivada com os lançamentos financeiros gerados.

O processo de vincular lançamentos é um processo financeiro que adiciona créditos (lançamentos à pagar) à uma parcela de financiamento do TIN.

Para isso vamos abrir uma tela do Financeiro com um lançamento de exemplo e realizar o processo.

Vamos verificar também o titulo correspondente no Protheus, que neste caso será apenas para consulta dos dados que são enviados através do TIN.

**Observação:** Neste passo vamos vincular lançamentos com os seguintes tipos de documentos:

* 27 - Nota de Crédito
* 16 - Adiantamento
* 14 - Devoluções

### Realizando o processo

Para a nota de crédito e Devoluções é simples, temos que criar um lançamento financeiro e realizar o processo de vínculo, conforme imagens a seguir.

Lembrete

Importante lembrar de inserir o valor do lançamento na aba Valores e também o centro de custo e o rateio na aba "Dados Adicionais".

Outro ponto fundamental, é definir que o Cliente do lançamento, seja o mesmo do lançamento a receber.

Assim podemos no lançamento original "A receber, realizar o processo de vincular Lançamentos.

Aparecerá essa tela onde podemos escolher quais lançamentos iremos vincular e se iremos vincular o valor TOTAL ou PARCIAL do lançamento.

Todos os lançamentos vinculados podem ser acessados pelo anexo de Vínculos do Lançamento a receber.

Para o vínculo de **Adiantamento**, o processo terá um passo a mais. Primeiramente iremos criar um lançamento com o tipo de parcela adiantamento. Lembrando sempre de inserir o valor, o centro de custo e o rateio.

**Note que para este lançamento ele é criado como um lançamento a receber.**

O primeiro passo é realizar uma baixa deste lançamento, isto irá gerar um segundo lançamento automaticamente, este será um lançamento a pagar.

Com a baixa realizada, este lançamento do tipo Crédito de adiantamento é gerado automaticamente.

Assim é possível fazer o vínculo com o lançamento original.

Este vínculo será visível no anexo do lançamento como mostrado anteriormente e também no título do protheus. Basta entrar no protheus, no módulo financeiro e ir no menu Funções de conta a receber.

Para saber qual o título correspondente, basta verificar qual o de-para do lançamento no módulo de integrações no RM.

Os lançamentos vinculados podem ser consultados nos valores acessórios do titulo no protheus. Para isso basta seguir os passos abaixo:

Ao clicar no botão detalhe, podemos ver todos os componentes que fazem parte do título. Esses componentes são enviados diretamente do TIN. Aqui será possível ver também
