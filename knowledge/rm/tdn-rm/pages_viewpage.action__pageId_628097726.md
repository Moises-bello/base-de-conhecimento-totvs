---
content_hash: e950b427e66323aa28091912e3cc54d01867ad22352dfe303113eeb8ec42a00a
fetched_at: '2026-06-29T00:11:05.027898+00:00'
page_id: '628097726'
product: rm
source: tdn-rm
title: Retornar Solicitações de SobreAviso do funcionário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=628097726
version: 2
---

Este serviço retorna todas as solicitações de SobreAviso do funcionário.

GET - timesheet/oncall/{employeeId}

Como parâmetro do serviço é necessário informar a coligada do funcionário, chapa do funcionário, página de início, página de fim.

Exemplo:

<http://localhost/MeuRH/rm/api/rest/timesheet/oncall/1%7C00031?page=1&pageSize=50>

| Parâmetro | Descrição do Parâmetro |
| --- | --- |
| employeedId | Coligada e chapa do Funcionário |
| page | Número da página que está sendo carregada |
| pageSize | Quantidade de registros da página requisitada |
