---
content_hash: 6b31ba921cdecd9b6cfc159cebf5788c083ef14eedef476eca8383b45e1d0137
fetched_at: '2026-06-29T00:11:05.029387+00:00'
page_id: '628098117'
product: rm
source: tdn-rm
title: Retornar Solicitações de SobreAviso do Time
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=628098117
version: 1
---

Este serviço retorna todas as solicitações de SobreAviso do time de um gestor.

GET - /team/oncall/{coordinatorId}

Como parâmetro do serviço é necessário informar a coligada do gestor, chapa do gestor, página de início, página de fim.

Exemplo:

<http://localhost/MeuRH32/rm/api/rest/team/oncall/1%7C00082?page=1&pageSize=200>
