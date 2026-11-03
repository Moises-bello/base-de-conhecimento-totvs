---
content_hash: 88ee3f249e33cc89fe0db70cc6bf03b44d23773cd24e82164ace93ddb4d540f1
fetched_at: '2026-06-29T00:09:02.526111+00:00'
page_id: '379318636'
product: rm
source: tdn-rm
title: 3245012 DEDUINTEGRACOES-2733 DT Cadastrar Produto - Integracao Protheus
type: documentation
url: https://tdn.totvs.com/display/LRM/3245012+DEDUINTEGRACOES-2733+DT+Cadastrar+Produto+-+Integracao+Protheus
version: 1
---

# CADASTRAR PRODUTO - INTEGRAÇÃO PROTHEUS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | *****Educacional***** |
| **Módulo:** | *****Totvs Educacional***** |
| **Função:** | Cadastro de Produto - Integração Protheus |
| **Situação/Requisito:** | O protheus envia um produto através da integração. Caso o RM esteja parametrizado para utilizar o conceito de registro global para o produto ele tenta realizar as réplicas e retornando uma exceção. |
| **Solução/Implementação:** | Ajustes na integração do produto. Caso esteja parametrizado para utilizar o conceito de registro global as réplicas não serão realizadas, já que o registro com coligada 0 será criado e utilizado pelas outras com esse conceito. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
