---
content_hash: 0c1a4320411e45d89930dc52cf166712b03b99f80f6d92d78f47999d5ab83531
fetched_at: '2026-07-02T19:24:28.726909+00:00'
page_id: '819046105'
product: protheus
source: tdn-tec
title: Melhoria - Encerramento da workspace durante mensagem de desconexão por inatividade
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=819046105
version: 1
---

Melhoria - Encerramento da workspace durante mensagem de desconexão por inatividade

|  |  |
| --- | --- |
| Situação | Quando o TOTVS Application Server desconecta um usuário por tempo de inatividade, a workspace (aba) de trabalho continua aberta exibindo as informações (como um formulário de cadastro, por exemplo) porém com a caixa de mensagem exibindo o alerta de desconexão e bloqueando qualquer interação no sistema até que o usuário confirme na caixa. |
| Ocorrência | A workspace/aba de trabalho deve ser fechada no momento da desconexão por inatividade para garantir segurança e privacidade dos dados. |
| Melhoria | O SmartClient recebeu uma melhoria para encerrar a workspace/aba no momento que exibir o alerta de desconexão por inatividade. |
| Informações adicionais | * Referente ao chamado: 18666707 * Referente à ocorrência: DTCLIENT01-4466 * Disponível a partir da build 7.00.210324P - 20.3.2.4 |
