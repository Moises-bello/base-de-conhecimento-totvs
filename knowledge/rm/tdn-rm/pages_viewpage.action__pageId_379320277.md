---
content_hash: 1ff907c607aced20ffd3641b1848ebba0e259dc9a59a03992abc5daccff39224
fetched_at: '2026-06-29T00:09:02.554439+00:00'
page_id: '379320277'
product: rm
source: tdn-rm
title: 2647374 DSAUGHCOM-13 DT Ajuste erro número inválido - Soroterapia inclusão
  de etapas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=379320277
version: 2
---

# Ajuste erro número inválido - Soroterapia inclusão de etapas

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospital |
| **Função:** | Prontuário Eletrônico |
| **Situação/Requisito:** | Em soroterapia, ao confirmar um princípio ativo e concentração acontece a mensagem de erro '.0' não é um número válido. |
| **Solução/Implementação:** | Formatação do sequencial estruturado da tabela SZITEMPRESCRICAO que estava errado quando retornado pela função responsável por trazer o mesmo, estava como 01..00 e foi ajustado para retornar 01.00. |
| **Documento de Referência:** | [Ticket #2647374](https://totvssuporte.zendesk.com/agent/tickets/2647374 "Open ticket in Zendesk Support") |
