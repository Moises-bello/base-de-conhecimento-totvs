---
content_hash: 327894ee0a5e8f9029bac870546605089c260f09e4e0ce7ef0680a0ca76819ea
fetched_at: '2026-06-29T00:09:52.335706+00:00'
page_id: '438297332'
product: rm
source: tdn-rm
title: 4157937 FINANCEIRO01-9504 Atualização do campo Status da Remessa do boleto
  quando recusado pelo banco
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=438297332
version: 1
---

# Atualização do Status da Remessa do boleto quando recusado pelo banco no Registro Online

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | BackOffice |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Atualizar o Status da Remessa para recusado quando o boleto for recusado pelo banco. |
| **Situação/Requisito:** | Cliente entrou em contato informando que no caso do processo de registros online os títulos não forem registrados por algum erro o status da remessa continua como "Não Remetido", sendo que o titulo foi recusado pelo banco. Cliente deseja que quando o título for recusado o sistema altere o Status remessa para "Recusado" e não deixe como "Não Remetido". |
| **Solução/Implementação:** | Quando o boleto for recusado pelo banco no processo de registro online será apresentado a mensagem "Recusado" no status da remessa no boleto. O status da remessa será atualizado quando realizado o registro online corretamente ou a remessa ou a baixa manual, na inclusão do boleto registrando online ou no processo de registro online na visão de boleto. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
| **Pacote:** | N/A |
