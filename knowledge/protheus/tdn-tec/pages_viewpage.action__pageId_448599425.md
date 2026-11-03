---
content_hash: d350282112ed67660ab4744173d7a0550833e85a3cc975e828e4a44ce73872d1
fetched_at: '2026-07-02T19:24:23.385343+00:00'
page_id: '448599425'
product: protheus
source: tdn-tec
title: Correção - Posição do Label quando criado em conjunto com outro campo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=448599425
version: 1
---

|  |  |
| --- | --- |
| Situação | Em algumas telas de cadastro do ERP Protheus, o Label deveria aparecer na linha superior que o tGet/tMultiGet porém está aparecendo na mesma linha, causando erro de posicionamento. |
| Ocorrência | Posição passada para o SmartClient não estava sendo respeitada |
| Correção | Estava faltando respeitar a posição passada pela mensagem de criação do componente tSay |
| Informações adicionais | * Referente ao chamado: PP-436 * Referente à ocorrência: ITEC-383 * Disponível em builds iguais ou superiores a 7.00.170117A - 17.3.0.5\_RC1 |
