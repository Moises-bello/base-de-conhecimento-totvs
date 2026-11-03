---
content_hash: a9a261544610c612aefd6381b2e8248009fff5edcf1ca80d660845c4d3661395
fetched_at: '2026-06-29T00:11:45.936612+00:00'
page_id: '822226112'
product: rm
source: tdn-rm
title: Lançar Movimentação de Convênios
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=822226112
version: 6
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. ****Tela Processo de Lançamento em Folha da Movimentação de Convênio do Funcionário****
   1. **Principais Campos e Parâmetros**
4. **Tabelas utilizadas**

## **01. VISÃO GERAL**

A partir do momento que todos os convênios utilizados pelos funcionários tenham sido criados, parametrizados e calculados dentro da movimentação dos funcionários, passará a ser necessário fazer o lançamento das parcelas para o envelope de pagamento do funcionário.   

IMPORTANTE

* Caso dentro do envelope de pagamento já existia um registro com o evento parametrizado no convenio (tópico Parâmetros do Convênio), o sistema irá somar o valor já existente com o valor atual do evento que se encontra sendo lançado.

* Após a execução do processo, os campos Mês Lançamento, Ano Lançamento e Período do lançamento serão preenchidos automaticamente dentro dos Anexos | Parcelas do Movimento do Convênio. Caso queira lançar novamente o mesmo convênio  é obrigatório o cancelamento do movimento em Folha Mensal / Cancelamento marcando o parâmetro "Atualiza cadastro de convênios" para que esses campos de Mês Lançamento, Ano Lançamento e Período do lançamento fiquem em branco e o processo possa ser executado novamente para o mesmo convênio.

          Veja mais detalhes sobre o parâmetro "Atualiza cadastro de convênios" em [Cancelamento de movimento - FOP](https://tdn.totvs.com.br/display/public/LRM/Cancelamento+de+movimento+-+FOP?draft=true).

## **02. EXEMPLO DE UTILIZAÇÃO**

Existindo Movimento de Convênio para o funcionário - sendo que no exemplo o total foi - R$370,00

Lançando o movimento:

Será inserido Mês e Ano lançamento em cada movimento lançado:

Será lançado o evento de desconto no envelope de pagamento do funcionário:

## **03.** **TELA Processo de Lançamento em Folha da Movimentação de Convênio do Funcionário**

****Principais Campos e Parâmetros****

| Campo | Descrição |
| --- | --- |
| Quebra de Seção | Informar a quebra da seção |
| Seleção de funcionários | Deverá realizar a seleção dos funcionários que terão suas parcelas dos convênios lançadas. |
| Competência, Período e Data Pagamento | Serão preenchidos automaticamente |
| Lança movimento no próximo mês | Parâmetro para lançar as parcelas do próximo mês que não se encontram lançadas |
| Incluir competências anteriores não lançadas | Parâmetro para lançar todas as parcelas das competências anteriores que não se encontram lançadas |
| Incluir competências futuras não lançadas | Parâmetro para lançar todas as parcelas das competências futuras que não se encontram lançadas |
| Forma de exibição do log | Selecionar qual será a forma de exibição do log, sendo que será considerado o simples como default visando uma melhor performance do processo. |

## **04. TABELAS UTILIZADAS**

* PFMOVCONVENIO
* PFFINANC
