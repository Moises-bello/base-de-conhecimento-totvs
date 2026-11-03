---
content_hash: ac9415714a7ef8b0e02bc91f774098b91baa89ef4eaf069c5f69ef43c913c226
fetched_at: '2026-06-29T00:11:44.221647+00:00'
page_id: '811262586'
product: rm
source: tdn-rm
title: DT - Transferência - Validar a data de pagamento das férias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=811262586
version: 9
---

## **01. DADOS GERAIS**

| Produto: | TOTVS - Folha de Pagamento |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Transferência de funcionários |
| País: | Brasil |
| Epic | [DRHCALCRM-4606](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-4606) |

## **02. SITUAÇÃO/REQUISITO**

Ao marcar uma férias para o próximo mês, com data de pagamento no mês corrente e efetuar a transferência do funcionário no mês subsequente, realizando o lançamento das férias no mês subsequente, estava sendo considerada a data de pagamento dos eventos de férias no mês subsequente, causando assim um erro  ao gerar a DIRF / Informe de de Rendimentos. pois como a data de pagamento dos eventos foi no mês anterior, deveria ser levado no mês da data de pagamento.

## **03. SOLUÇÃO**

Foi incluída uma validação na transferência do funcionário, verificando se o funcionário possui férias marcadas com a data de demissão por transferência, onde a data de pagamento das férias seja menor ou igual a data de transferência, Caso a data de pagamento atenda a condição, o usuário será impedido de efetuar a transferência e apresentada a mensagem  '**Há cadastro de férias com a situação 'Marcadas' e data de pagamento anterior a data de demissão.  Verifique a necessidade do lançamento das férias antes de realizar a transferência do funcionário.**'.  Neste caso, deverá ser realizado o processo de Lançamento de férias para o próximo mês para depois realizar a transferência do funcionário.

**Observação**

A rescisão por transferência somente será bloqueada e a mensagem exibida, quando houver férias marcadas, em que o início do gozo de férias seja posterior a data de demissão e a data de pagamento das férias seja até a data de demissão e o parâmetro **Permite transferência tipo 5 de funcionários afastados ou de férias**  existente em RH | Folha de Pagamento | Configurações | Parametrizador | Rescisão | Transferência estiver **desmarcado**.

## **04.** **EXEMPLO**

**1) Cadastrar as férias para o funcionário:**

**Dados:**

**Início das Férias:**

**Fim das Férias:**

**Data de Pagamento das Férias:**

**2) Em RM | RH | Folha de Pagamento |  Rescisão | Rescisão Individual:**

**Dados:**

**Tipo de Demissão: 5 - Transferência sem ônus p/ Cedente**

**Data de Demissão/Cálculo:**

**Data de Desligamento:**

**Data de Pagamento:**

**Data de Último Movimento:**

**3) Ao clicar em Salvar, será apresentada a mensagem:**

## **05.****ASSUNTOS RELACIONADOS**

* [Rescisão - RHU](https://tdn.totvs.com/pages/releaseview.action?pageId=452719347)
* [Rescisão Coletiva](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719318)
