---
content_hash: 296b59db993b606e22a536a5b55c874a242f0bc32adf20eceb6641cf8270f57d
fetched_at: '2026-06-29T00:05:51.563423+00:00'
page_id: '1051258110'
product: rm
source: tdn-rm
title: Permitir alterar item vindo de requisição ou pedido de exames
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1051258110
version: 7
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**

## **01. VISÃO GERAL**

Foi criado o parâmetro "**Permite alterar lançamento de matmed de requisição e SADT originado de pedido de exames**" para deixar o sistema mais flexível para a equipe do faturamento conseguir faturar as contas, sem ter que utilizar o módulo de Auditoria Interna e não depender da equipe da farmácia ou dos centros de diagnósticos. Cenário este em que o paciente já teve alta há mais dias e a mobilização de outra equipe pode atrasar o faturamento daquele atendimento.

## **02. EXEMPLO DE UTILIZAÇÃO**

Parametrização necessária

Importante

Somente na versão 12.1.2506, ao invés de editar o registro, deve-se selecionar o registro e executar o processo "Realizar Auditoria"

Para as versões superiores o funcionamento é da seguinte maneira:

Ao editar um item vindo de requisição, exibirá a página Auditoria

Ao editar um item sem requisição, não exibe a página Auditoria

O mesmo vale para exames de pedido

Para desfazer e retornar aos valores originais, deve editar o registro novamente e marcar o campo "Reverter auditoria" e no botão OK.  
Os valores serão retornados e os campos Tipo e Motivo serão apagados.

Use esse box para destacar informações relevantes e/ou de destaque.IMPORTANTE!
