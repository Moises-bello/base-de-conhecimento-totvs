---
content_hash: 4ef8df56dfaba7f7efc9eecd624933a28e082bc331484af070865ae97c546510
fetched_at: '2026-06-29T00:08:49.402131+00:00'
page_id: '330827487'
product: rm
source: tdn-rm
title: RMSAU-2135 1959817 DT Ao tentar efetuar a emissão de resultados o status não
  alterava
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=330827487
version: 1
---

# Ao tentar efetuar a emissão de resultados o status não alterava

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Função:** | Controle de Pedido de Exames |
| **Situação/Requisito:** | Ao efetuar a emissão de exames pelo controle de pedido de exames o sistema não alterava o status do exame para emitido ficando como liberado e não mostrando nenhuma mensagem para o usuário. |
| **Solução/Implementação:** | Alterado o sistema para alterar o status do exame, se acontecer algum erro exibir uma mensagem informando o que ocorre. |
