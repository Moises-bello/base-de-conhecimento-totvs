---
content_hash: 90bc16120625c9969bccdefc8826071c7c9aeac990ca97af3f1925818413c5f6
fetched_at: '2026-06-29T00:11:20.527308+00:00'
page_id: '686474666'
product: rm
source: tdn-rm
title: Erro de CRC Inválido
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=686474666
version: 3
---

## 

## Ocorrência

Ocorre erro CRC INVÁLIDO na aplicação RM.

## Ambiente:

Framework - Framework (Linha RM) - Banco de Dados - Todas as versões

## Solução:

Para que este erro não aconteça, não deverá ser dado nenhum comando DML na base de dados, pois algumas tabelas possuem um controle interno que é gerado automaticamente pelo sistema, então quando há a intervenção humana nestas tabelas, este controle entra em um conflito interno e não é recalculado, resultando nestes erros de CRC.

Por isto não recomendamos o manuseio DML diretamente no banco de dados.

Quando este erro acontece, é preciso efetuar o Recalculo de Controle das tabelas Globais, onde isto é feito junto a equipe de consultoria de Banco de Dados e procedimento faturado. Se foram efetuadas alterações manuais pelo banco, deve ser recalculado o controle, e para isso será recomendada a nossa equipe de consultoria.

Caso o CRC esteja inválido em um objeto gerencial, ele poderá ser excluído, exemplo: Cubo, Relatório, Planilha e Fórmula Visual.
