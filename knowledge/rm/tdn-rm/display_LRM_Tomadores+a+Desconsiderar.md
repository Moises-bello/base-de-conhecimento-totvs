---
content_hash: eb40d9d49d42bdd45fbe40de87c4b7dfd2bb0b428a06fd78b7a84aaca523e934
fetched_at: '2026-06-29T00:10:07.978365+00:00'
page_id: '452719490'
product: rm
source: tdn-rm
title: Tomadores a Desconsiderar
type: documentation
url: https://tdn.totvs.com/display/LRM/Tomadores+a+Desconsiderar
version: 2
---

Através deste cadastro o usuário poderá incluir os tomadores que serão desconsiderados no evento S-1020 - Tabela de Lotações Tributárias e S-1005 - Tabela de Estabelecimento/Obras.  
    
 **Atenção:**

* Carga inicial S-1005: Ao executar a geração da carga inicial, caso exista algum Tomador de Serviço – Obra Própria informado nos tomadores a desconsiderar estas lotações não terão gatilhos gerados.
* Carga inicial S-1020: Ao executar a geração da carga inicial, caso exista alguma lotação tributária associada a um tomador informado nos tomadores a desconsiderar ou inativo (caso o parâmetro para desconsiderar inativos esteja marcado) estas lotações não terão gatilhos gerados.
* Gerar XML e Validação da base de dados: Caso já exista na fila de eventos algum registro de gatilho vinculado há alguma lotação que tenha tomador inativo ou relacionado nos tomadores a desconsiderar, ao realizar sua geração será apresentada a seguinte mensagem ao usuário: *A Lotação Tributária 'XXXX' está relacionada a um Tomador informado nos parâmetros do eSocial (Tomadores a Desconsiderar e/ou Registros Inativos a Desconsiderar) não podendo ser utilizada. Avalie a necessidade da utilização desta Lotação Tributária e ajuste a parametrização.*
