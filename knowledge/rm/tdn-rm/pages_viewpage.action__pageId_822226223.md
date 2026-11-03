---
content_hash: 3a7c9a42bf318753a6380f96650b186a45ed390baeb1849ff299e35f93e54f18
fetched_at: '2026-06-29T00:11:45.966609+00:00'
page_id: '822226223'
product: rm
source: tdn-rm
title: Cancelar Movimentação de Convênios
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=822226223
version: 4
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tela Cancelar Movimentação**
   1. **Principais Campos e Parâmetros**
4. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Este modulo executa o cancelamento das movimentações de convênio dos funcionários.

IMPORTANTE

Após a execução do processo de Lançar Movimentação de Convênios, os campos Mês Lançamento, Ano Lançamento e Período do lançamento serão preenchidos automaticamente dentro dos Anexos | Parcelas do Movimento do Convênio. Veja o preenchimento do campo no Exemplo de utilização do [Lançar Movimentação de Convênios](https://tdn.totvs.com/pages/viewpage.action?pageId=822226112).

Nesse caso é obrigatório o cancelamento do movimento em Folha Mensal / Cancelamento marcando o parâmetro "Atualiza cadastro de convênios" para que esses campos de Mês Lançamento, Ano Lançamento e Período do lançamento fiquem em branco e o processo de Cancelar Movimentação de Convênios possa cancelar o convênio conforme desejado.

Veja mais detalhes sobre o parâmetro "Atualiza cadastro de convênios" em [Cancelamento de movimento - FOP](https://tdn.totvs.com.br/display/public/LRM/Cancelamento+de+movimento+-+FOP?draft=true).

## **02. EXEMPLO DE UTILIZAÇÃO**

11Cancelar parcelas em aberto com algum lançamento (NF) em folha de pgto

Existe movimento com 10 parcelas, sendo que uma parcela já foi lançada para o envelope de pagamento:

Executado o processo marcando o parâmetro "Cancelar parcelas em aberto com algum lançamento (NF) em Folha de Pagto":

Foram canceladas as parcelas em aberto ficando apenas a parcela que já havia sido lançada:

Atenção

Caso não haja alguma parcela lançada será emitida mensagem e não cancelará o movimento:

2Cancelar parcelas em aberto sem algum lançamento (NF) em folha de pgto

Existe movimento com 10 parcelas, sendo que nenhuma parcela já foi lançada para o envelope de pagamento:

Executado o processo marcando o parâmetro "Cancelar parcelas em aberto sem algum lançamento (NF) em Folha de Pagto":

Foi cancelado todo o movimento:

Atenção

Caso haja alguma parcela lançada será emitida mensagem e não cancelará o movimento:

## **03.** **TELA Cancelar Movimentação**

****Principais Campos e Parâmetros****

| Campo | Descrição |
| --- | --- |
| Quebra de Seção | Selecionar os funcionários que terão suas movimentações canceladas |
| Seleção de funcionários | Selecionar funcionários |
| Nro. Nota Fiscal | Informar o número da nota fiscal |
| Forma de exibição do log | Exibição que se dará de forma Simples ou Detalhada |
| Data do movimento | Intervalo de datas (período) em que será levado em consideração para cancelamento |
| Tipo de movimento | Tipo de movimento que será considerado no processo que poderá ser somente os importados, os digitados e todos |
| Cancelar parcelas em aberto com algum lançamento (NF) em folha de pgto | Cancelamento das parcelas da movimentação de convênios, caso já exista alguma lançada. O processo irá apenas eliminar as parcelas ainda não lançadas, permanecendo assim as que já sofreram lançamento. |
| Cancelar parcelas em aberto sem algum lançamento (NF) em folha de pgto | Será feito o cancelamento apenas das movimentação que ainda não possuem nenhuma parcela lançada, cancelando assim todo o parcelamento, |
| Recalcular parcelas futuras | Realiza o recalculo das parcelas do convênio, ou seja efetuará um recalculo nos cálculos das parcelas das movimentações restantes, |

## **04. TABELAS UTILIZADAS**

* PFMOVCONVENIO
