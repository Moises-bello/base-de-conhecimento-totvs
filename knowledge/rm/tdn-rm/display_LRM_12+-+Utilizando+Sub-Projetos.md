---
content_hash: 72501169ce79e0966da202a51a5eb8b21785153f5a626b768590aa1f509a3448
fetched_at: '2026-06-29T00:12:01.634526+00:00'
page_id: '896390284'
product: rm
source: tdn-rm
title: 12 - Utilizando Sub-Projetos
type: documentation
url: https://tdn.totvs.com/display/LRM/12+-+Utilizando+Sub-Projetos
version: 4
---

Um Projeto de Testes também é uma Atividade. Desta forma, podemos colocar um Projeto dentro de outro projeto de teste.  
O uso de Sub-Projetos é um facilitador para agruparmos projetos de uma mesma jornada, onde a ordem de execução é importante e principalmente quando há dependência entre estes projetos.

* Exemplo: Tenho um projeto de Jornada de internação de paciente (Projeto Pai) e dentro dele tenho todos os projetos relacionados aos cadastro e processos que fazem parte da jornada de internação de paciente (Projetos filhos).

Os recursos dos projetos “filhos” são compartilhados com o projeto “pai”.  
Você pode também criar um Projeto de Teste Sistêmico e inserir o projeto de montagem de ambiente e todos os projetos de teste no mesmo, desta forma, quando for testar um patch ou release, executará somente um projeto.

[← Anterior](https://tdn.totvs.com/pages/viewpage.action?pageId=896390218) |
