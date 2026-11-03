---
content_hash: 5c676358d3aafded95ff087bfee4b704239676e567db3172aa9d0d72523e8486
fetched_at: '2026-06-29T00:11:55.560983+00:00'
page_id: '862118968'
product: rm
source: tdn-rm
title: Lançamento na conta com a data do aprazamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=862118968
version: 2
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**

SumárioVisão Geral

## **01. VISÃO GERAL**

Desde a versão 12.1.19, ao marcar o parâmetro de estoque “Lançamento na conta com a data do aprazamento”, localizado em:

A partir da 12.1.2406 = **Ambiente / Parâmetros / Gestão Hospitalar**

Após isso, vá para **Estoque / Estoque 5/5**

Em versões anteriores, o menu é: “Parâmetro Geral/Estoque II.

Somente através do Painel de Dispensação, caso tenha mapa de dispensação, após processar a requisição, o sistema irá lançar o item na conta do paciente com a data do aprazamento 05/08/2024, ou seja, na Parcial que contenha a data do aprazamento (poderá ser parcial 1, 2 ou a que estiver compreendida).

Com este parâmetro marcado, também ao encerrar a parcial na conta do paciente, caso o movimento de estoque esteja com status “E” (Pendente), será apenas emitido mensagem de alerta e concluído o encerramento da parcial com sucesso.

Vide informações sobre como procede este parâmetro em  <https://tdn.totvs.com/x/2oz-Fg>

Exemplo de Utilização.

## **02. EXEMPLO DE UTILIZAÇÃO**

* Permitir lançar o item da requisição na conta do paciente, com a data do aprazamento ao invés da data da requisição.

* Permitir o faturista encerrar a parcial na conta do paciente, mesmo que exista movimentação do estoque com status pendente. Caso não marque este parâmetro, a parcial não será encerrada enquanto não processar a requisição.
