---
content_hash: c89dd05820a3101310fdfe47a6bf453192b409e6430eceb7a9a71406ccac4ebe
fetched_at: '2026-06-29T00:12:01.232631+00:00'
page_id: '889119928'
product: rm
source: tdn-rm
title: Consulta Saldo Online
type: documentation
url: https://tdn.totvs.com/display/LRM/Consulta+Saldo+Online
version: 3
---

## **01. VISÃO GERAL**

O recurso permite que o sistema se conecte, de forma automatizada, à API disponibilizada pelos bancos, realizando a consulta do saldo bancário em tempo real. O saldo obtido é então atualizado no sistema, garantindo que as informações financeiras estejam sempre atualizadas e refletindo os dados mais recentes das contas bancárias vinculadas.

Recurso disponibilizado a partir do release  12.1.2410

## **02. BANCOS DISPONIBILIZADOS**

* Banco do Brasil

## **03. CONFIGURAÇÃO**

A configuração para integração com a API do banco é efetuada na aba [Extrato Online](https://tdn.totvs.com/pages/viewpage.action?pageId=421388837#ContaCaixa-1809356232) do cadastro de conta caixa. 

## **04. EXECUÇÃO DO PROCESSO**

Ao executar o processo, não será necessário informar nenhum parâmetro, pois o processo irá percorrer todas as contas caixas que esteja com o extrato online habilitado, efetuar a consulta online no banco e atualizar o campo saldo bancário e data do saldo bancário da conta caixa.

Caso o ambiente esteja configurado para três camadas, será possível agendar o processo para que o saldo seja consultado por uma determinada recorrência.
