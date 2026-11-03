---
content_hash: 59dfe6e0d035946308be71af0319c81f3e4ce59d9454ba93b1bbeb04ac240904
fetched_at: '2026-06-29T00:10:16.463828+00:00'
page_id: '469451501'
product: rm
source: tdn-rm
title: Contabilidade - Venda
type: documentation
url: https://tdn.totvs.com/display/LRM/Contabilidade+-+Venda
version: 4
---

Eliminação

**Coligada contra partida da Eliminação.**

Agora será possível o preenchimento dos novos campos presentes nas partidas do lançamento contábil e também do evento contábil que estão relacionadas a eliminação de valores em operações intercompany. Assim as origens que utilizam o evento contábil devem preencher tais campos nas partidas antes de enviar para o serviço de inclusão de lançamentos do módulo contábil.

A classe de lançamentos do evento contábil também já contempla.  Assim o serviço que executa o Evento Contábil já está preparado para retornar esses campos preenchidos.  As origens apenas têm que preencher a informação retornada pelo serviço do evento contábil nas partidas que são criadas para serem enviadas a módulo contábil.

Abaixo um exemplo:

Contrato de Venda criado no TCGI

Número do Contrato : 151

Em contabilidade do contrato : Inserir os eventos contábeis - Neste exemplo inserido o evento 1011 = Evento de Venda que encontra-se configurado.

Editando o evento contábil e em seguida, clicar em Itens Evento.

Editar as contas de Crédito e Débito.

Em eliminação : Informar outra coligada e a Conta contra partida da Eliminação.

Os dois itens do evento editados e inseridos os dados para Eliminação.

Contabilizando a Venda.

Verificando se foi realizado o preenchimento dos novos campos presentes nas partidas do lançamento contábil e também do evento contábil que estão relacionadas a eliminação de valores em operações.
