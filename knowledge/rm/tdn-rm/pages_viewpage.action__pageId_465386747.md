---
content_hash: 9a1033a1a123284958f69b8bff80e512bfe3fa259c5baca29b107fce8d5eab3f
fetched_at: '2026-06-29T00:10:15.931584+00:00'
page_id: '465386747'
product: rm
source: tdn-rm
title: Múltiplos Vínculos que necessitam de Recálculo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=465386747
version: 20
---

## 

## **ÍNDICE**

1. **Visão Geral**
2. **Exemplo de utilização**

## **01. VISÃO GERAL**

Este relatório permite consultar os funcionários com múltiplos vínculos que possuem movimentação no mês e necessitam de recalculo.

## **02. EXEMPLO DE UTILIZAÇÃO**

Foi criado em Folha Mensal/ Consulta o menu de consulta de pendencias de recalculo dos múltiplos vínculos 

Este relatório deve ser utilizado somente quando os parâmetros no parametrizador "[Calcula IRRF/INSS de múltiplos vínculos sem chapa centralizadora](http://tdn.totvs.com.br/pages/viewpage.action?pageId=452719263)" e "[Calcula INSS conforme eSocial](http://tdn.totvs.com.br/pages/viewpage.action?pageId=452719263)" estiverem MARCADOS

Exemplo:

 Coligada 1 :  Chapa :11111-  Lançamento de folha com Eventos de base de INSS outro emprego complementar e INSS outro emprego .

 Coligada 2 : Chapa :12121212- Lançamento  de folha

 Após o lançamento da movimentação da coligada 2 o sistema irá gerar uma pendencia de recalculo da coligada  1.

 Para o correto envio de S-1200 para eSocial  dos funcionários múltiplos vínculos, è necessário recalcular a coligada 1 fazendo assim que o calculo de INSS seja calculado corretamente.

**Para Liberação do Menu de "Múltiplos Vínculos que necessitam de recalculo" deverá executar o Script Oracle(ESOCIALFOP01-8798.ORA.ZIP) ou SQL server (ESOCIALFOP01-8798.SQL.ZIP) de acordo com seu banco de dados. Maiores informações acessar o link abaixo: http://tdn.totvs.com/display/LRM/Executor+de+Scripts+RM IMPORTANTE!**

## **03. TABELAS UTILIZADAS**

* PFPRECISARECALCULOMV
