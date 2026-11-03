---
content_hash: a3b753f658648f410482293e4300a41f38b77b7487afb3fd9130cf4e3e7acd95
fetched_at: '2026-07-02T19:24:18.594270+00:00'
page_id: '219120551'
product: protheus
source: tdn-tec
title: Correção - Tratamento de exceção para função reloadSAML
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=219120551
version: 1
---

Essa build contém uma correção nas chamadas de algumas funções AdvPL que tratam SAML.

|  |  |
| --- | --- |
| Situação | Ao chamar a função AdvPL reloadSAML, a mesma gerava uma exceção no AppServer. |
| Ocorrência | Caso houvesse algum problema com os arquivos de configuração do SAML e fosse chamada as funções AdvPL reloadSAML, setSAMLSvc ou getSAMLSvc, as mesmas davam uma exceção no Application Server, fechando a thread. |
| Correção | Foi colocado tratamento de exceção nas funções AdvPL reloadSAML, setSAMLSvc e getSAMLSvc. |
| Informações adicionais | * Referente ao chamado: TTTQVM * Referente à ocorrência: SSIM-230 * Disponível em builds superiores a 7.00.131227A com data de geração superior a 30/11/2015. |
