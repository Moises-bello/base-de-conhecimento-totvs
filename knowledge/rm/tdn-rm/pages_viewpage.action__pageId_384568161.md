---
content_hash: 5ed25d6c008437621145c0f3c35dbb7182b11ac989cb3143985ed471a021db6c
fetched_at: '2026-06-29T00:09:07.139909+00:00'
page_id: '384568161'
product: rm
source: tdn-rm
title: PORTALMOBILE01-4372 DT 2666043 Falta de permissão na edição de Plano de Aula
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=384568161
version: 1
---

# Falta de permissão para edição de Plano de Aula

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | TOTVS Educacional |
| **Módulo:** | Gestão Educacional |
| **Função:** | Edição de Plano de Aula |
| **Situação/Requisito:** | Ao realizar a visualização dos Planos de Aula no Diário de Classe através de um usuário de Professor no Corpore.NET, mesmo o usuário possuindo permissão para edição do Plano de Aula, não era exibido o botão para Editar o conteúdo do Plano de Aula. |
| **Solução/Implementação:** | O problema ocorria em casos onde o nome de usuário de acesso do professor continha um espaço no final do seu conteúdo. A identificação do professor no portal não ocorria da forma correta em casos nesta situação. Foi realizado um tratamento para retirar o espaço do código do professor no contexto do aluno, permitindo que as validações e verificações ocorram de forma unificada em todos os pontos. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
| **Pacote:** | N/A |
