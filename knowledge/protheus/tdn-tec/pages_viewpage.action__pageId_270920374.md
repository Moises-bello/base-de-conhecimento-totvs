---
content_hash: 59d366d62e310cce60e1dc23be089921c5610dec6e858db3a3b8e481aa9a95c4
fetched_at: '2026-07-02T19:24:23.168939+00:00'
page_id: '270920374'
product: protheus
source: tdn-tec
title: Correção - LogUserName falha em ambiente Linux
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270920374
version: 2
---

A função LogUserName não falha no ambiente do cliente com esta correção.

|  |  |
| --- | --- |
| Situação | LogUserName falha em ambiente Linux gerando falha de segmentação. |
| Ocorrência | A falha de segmentação ocorria porque a chamada a função da API do Linux getpwuid falhava e não era tratada. |
| Correção | Foi adicionado tratamento em caso de falha da getpwuid (foi trocada por getpwuid\_r também), e caso falhar tenta conseguir o nome de usuário pela getlogin\_r antes de desistir. Quando qualquer uma das funções falham, é exibido no console uma mensagem com o código de erro. |
| Informações adicionais | * Referente ao chamado: TVMDPE-TVRDO5 * Referente à ocorrência: ITEC-36 * Disponível em builds superiores a 7.00.131227A 2.3.11 |
